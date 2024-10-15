# CONDOR Project

## Overview

The CONDOR Project aims to analyze particle data generated from simulations, focusing on the distribution of particles in space and time. This repository contains a Python script that processes raw data files, performs data analysis, and generates visualizations, including 2D and 3D particle distributions, heatmaps, and animations.

## Directory Structure

```
CONDOR_Project/
│
├── your_script.py  # Main Python script for data processing and visualization
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

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Frocso/CONDOR_Project.git
   ```

2. Change the directory to the project folder:

   ```bash
   cd CONDOR_Project
   ```

3. Update the `directory` variable in the script with the path to your data files:

   ```python
   directory = r'C:\path\to\your\data\files'
   ```

4. Run the script:

   ```bash
   python your_script.py
   ```

## Output

After running the script, output files will be created in subdirectories corresponding to the particle ID, incidence angle, and energy level. The generated outputs include:

- **CSV files** containing particle data:
  - `all_data_particleid_{id}_angle_{angle}_energy_{energy}.csv`: All data from the processed file.
  - `binned_data_particleid_{id}_angle_{angle}_energy_{energy}.csv`: Binned particle data.

- **Figures**:
  - `2D_particle_distribution_particleid_{id}_angle_{angle}_energy_{energy}.png`: 2D heatmap of particle density.
  - `3D_particle_distribution_particleid_{id}_angle_{angle}_energy_{energy}.png`: 3D scatter plot of particle distribution.

- **Animations**:
  - `particles_animation_2D_particleid_{id}_angle_{angle}_energy_{energy}.gif`: 2D animation of particle distribution over time.
  - `particles_animation_3D_particleid_{id}_angle_{angle}_energy_{energy}.gif`: 3D animation of particle distribution over time.
