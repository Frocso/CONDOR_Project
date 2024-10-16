# CONDOR Project

This repository contains the code and data for the analysis of particle distributions in time and space as part of the CONDOR Observatory project.

## Overview

The main objective of this project is to process and analyze particle data from simulations. The analysis includes reading data from specified files, filtering outliers, and generating visualizations that illustrate the spatial and temporal distributions of particles.

## Directory Structure

```
CONDOR_Project/
│
├── dataextract.py  # Main Python script for data processing and visualization
├── datapreprocessing.ipynb  # Jupyter Notebook script for data processing and visualization. Contains more analysis like correlation matrices and other spacial distribution plots.
├── panamatranslate.ipynb # Jupyter Notebook script for CORSIKA .DAT Binary files translation and data visualization
├── output/         # Directory where output files will be saved
│   ├── output_particleid_14_angle_0_energy_1.0e+03/
│   │   ├── all_data_particleid_14_angle_0_energy_1.0e+03.csv
│   │   ├── binned_data_particleid_14_angle_0_energy_1.0e+03.csv
│   │   ├── 2D_particle_distribution_particleid_14_angle_0_energy_1.0e+03.png
│   │   ├── 3D_particle_distribution_particleid_14_angle_0_energy_1.0e+03.png
│   │   ├── particles_animation_2D_particleid_14_angle_0_energy_1.0e+03.gif
│   │   └── particles_animation_3D_particleid_14_angle_0_energy_1.0e+03.gif
│   └── ...         # Other configurations as needed
└── README.md       # This readme file
```

**output_particleid_X_angle_Y_energy_Z/**: Contains output files for each particle configuration where `X` is the particle ID, `Y` is the incidence angle, and `Z` is the incidence energy. Inside each folder, you'll find:

  - `all_data_particleid_X_angle_Y_energy_Z.csv`: A CSV file containing all processed particle data including coordinates and additional metadata.
  - `binned_data_particleid_X_angle_Y_energy_Z.csv`: A CSV file showing binned particle counts based on spatial and temporal bins.
  - `2D_particle_distribution_particleid_X_angle_Y_energy_Z.png`: A 2D heatmap representing the particle density across spatial bins.
  - `3D_particle_distribution_particleid_X_angle_Y_energy_Z.png`: A 3D scatter plot showing particle distribution in space and time.
  - `particles_animation_3D_particleid_X_angle_Y_energy_Z.gif`: A 3D animation illustrating how particles are distributed over time.
  - `particles_animation_2D_particleid_X_angle_Y_energy_Z.gif`: A 2D animation demonstrating the temporal distribution of particles.

## Plot Explanations

1. **2D Heatmap**: The 2D heatmap visualizes the density of particles in spatial bins (1m x 1m). Each cell in the heatmap corresponds to a specific spatial bin, and the color intensity represents the number of particles that fall within that bin. This provides a clear view of how particle density varies spatially.

2. **3D Particle Distribution**: The 3D scatter plot displays the distribution of particles across the x, y, and time bins. Each point represents a particle, and the color indicates the number of particles in that bin. This plot helps to visualize the particle dispersion in three-dimensional space over time.

3. **Animations**: Both the 2D and 3D animations show how particle distributions evolve over time. In the 2D animation, the scatter plot updates to show the current distribution of particles in the x-y plane for each time bin. The 3D animation allows for dynamic visualization of particle movement and concentration over time, enhancing the understanding of their behavior.

## Requirements

Make sure you have the following Python packages installed:

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `scikit-learn`

You can install these packages using pip:

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

_MISSING VALUES/FOLDERS (FOR CONDOR AREA LIMITED PLOTS) JUST MEANS THAT THERE ARE NO PARTICLES IN THE AREA FOR THAT CONFIGURATION._
