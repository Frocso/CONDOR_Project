import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D
import gc  # Para la liberación de memoria

# Directorio de archivos
directory = r'C:\Users\Froxo\OneDrive\Escritorio\Corsika\Non_Binary_output_files_MC_Condor_DAT_1_Shower'

# Filtrar archivos que contienen '1.0E+03' en el nombre
files = [f for f in os.listdir(directory) if '1.0E+03' in f]

for file in files:
    file_path = os.path.join(directory, file)
    
    # Suponiendo que el archivo es un CSV (ajusta si es necesario)
    print(f"Processing {file_path}")

    column_names = ['x', 'y', 'z', 't', 'px', 'py', 'pz', 'energy']
    
    # Leer el archivo (ajusta el formato si no es CSV)
    particles_df = pd.read_csv(file_path, delimiter=" ", names=column_names, header=None)

    # Obtener el nombre del archivo para etiquetas
    import re
    match = re.search(r'particle_(\d+)_energy_(\S+)_angle_(\d+)_run_(\d+)', file)
    if match:
        particle_id = int(match.group(1))
        incidence_energy = float(match.group(2))
        incidence_angle = int(match.group(3))
    else:
        raise ValueError("Nombre de archivo no tiene el formato esperado")

    # Crear un directorio para cada configuración de salida
    output_dir = f"output_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}"
    os.makedirs(output_dir, exist_ok=True)

    # Agregar columnas de etiquetas
    particles_df['particle_id'] = particle_id
    particles_df['incidence_energy'] = incidence_energy
    particles_df['incidence_angle'] = incidence_angle

    # Reordenar las columnas
    new_column_order = ['x', 'y', 't', 'energy', 'particle_id', 'incidence_energy', 'incidence_angle']
    particles_df = particles_df[new_column_order]

    # Manejo de outliers 
    Q1 = particles_df.quantile(0.1)
    Q3 = particles_df.quantile(0.9)
    IQR = Q3 - Q1
    particles_df = particles_df[~((particles_df < (Q1 - 1.5 * IQR)) | (particles_df > (Q3 + 1.5 * IQR))).any(axis=1)].reset_index(drop=True)

    particles_df['t'] = particles_df['t'] - particles_df['t'].min()

    # Exportar el DataFrame all_data a CSV
    particles_df.to_csv(os.path.join(output_dir, f"all_data_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}.csv"), index=False)

    # Crear los bins
    particles_df['x_bin'] = np.floor(particles_df['x']).astype(int)
    particles_df['y_bin'] = np.floor(particles_df['y']).astype(int)
    time_bin_size = 1  # 1 nanosegundo
    particles_df['t_bin'] = np.floor(particles_df['t'] / time_bin_size).astype(int)

    # Agrupar por 'x_bin', 'y_bin', 't_bin' para contar partículas
    binned_particles = particles_df.groupby(['x_bin', 'y_bin', 't_bin']).size().reset_index(name='particle_count')

    # Exportar binned_particles a CSV
    binned_particles.to_csv(os.path.join(output_dir, f"binned_data_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}.csv"), index=False)    

    # Graficar el heatmap
    heatmap_data = binned_particles.pivot_table(index='y_bin', columns='x_bin', values='particle_count', fill_value=0)
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, cmap='mako', cbar_kws={'label': 'Particle Count'})
    plt.title('Particle Density Heatmap in Spatial Bins (1x1 meter)')
    plt.xlabel('X Bin (1m)')
    plt.ylabel('Y Bin (1m)')
    plt.savefig(os.path.join(output_dir, f"2D_particle_distribution_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}.png"))
    plt.close()  # Cerrar la figura después de guardarla

    # Filtrar partículas válidas
    filtered_particles = binned_particles[binned_particles['particle_count'] >= 0]  

    # Graficar en 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(filtered_particles['x_bin'], filtered_particles['y_bin'], filtered_particles['t_bin'], 
                         c=filtered_particles['particle_count'], cmap='viridis', marker='o')
    ax.set_xlabel('X Bin')
    ax.set_ylabel('Y Bin')
    ax.set_zlabel('Time Bin')
    cbar = plt.colorbar(scatter, ax=ax, label='Particle Count')
    plt.title('3D Particle Distribution in Time and Space')
    plt.savefig(os.path.join(output_dir, f"3D_particle_distribution_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}.png"), dpi=300)
    plt.close()

    # Crear animación 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(filtered_particles['x_bin'], filtered_particles['y_bin'], filtered_particles['t_bin'], 
                         c=filtered_particles['particle_count'], cmap='viridis', marker='o')
    ax.set_xlabel('X Bin')
    ax.set_ylabel('Y Bin')
    ax.set_zlabel('Time Bin')
    cbar = plt.colorbar(scatter, ax=ax, label='Particle Count')

    def update_3d(frame):
        current_bin_data = filtered_particles[filtered_particles['t_bin'] == frame]
        scatter._offsets3d = (current_bin_data['x_bin'], current_bin_data['y_bin'], current_bin_data['t_bin'])
        scatter.set_array(current_bin_data['particle_count'])
        ax.set_title(f'3D Particle Distribution - Time: {frame} [ns]')
    
    anim = FuncAnimation(fig, update_3d, frames=sorted(filtered_particles['t_bin'].unique()), interval=200, repeat=False)
    anim.save(os.path.join(output_dir, f"particles_animation_3D_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}.gif"))
    plt.close()

    # Crear animación 2D
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter([], [], c=[], cmap='viridis', vmin=filtered_particles['particle_count'].min(), 
                         vmax=filtered_particles['particle_count'].max())
    ax.set_xlabel('X Bin')
    ax.set_ylabel('Y Bin')
    plt.title('Particle Distribution Over Time')
    plt.grid(alpha=0.5)
    cbar = plt.colorbar(scatter, ax=ax, label='Particle Count')
    ax.set_xlim(filtered_particles['x_bin'].min(), filtered_particles['x_bin'].max())
    ax.set_ylim(filtered_particles['y_bin'].min(), filtered_particles['y_bin'].max())

    def update_2d(frame):
        current_bin_data = filtered_particles[filtered_particles['t_bin'] == frame]
        scatter.set_offsets(np.c_[current_bin_data['x_bin'], current_bin_data['y_bin']])
        scatter.set_array(current_bin_data['particle_count'])
        ax.set_title(f'2D Particle Distribution - Time: {frame} [ns]')
    
    anim = FuncAnimation(fig, update_2d, frames=sorted(filtered_particles['t_bin'].unique()), interval=200, repeat=False)
    anim.save(os.path.join(output_dir, f'particles_animation_2D_particleid_{particle_id}_angle_{incidence_angle}_energy_{incidence_energy:.1e}.gif'))
    plt.close()

    # Liberar memoria después de cada archivo procesado
    del particles_df, binned_particles, filtered_particles
    gc.collect()
