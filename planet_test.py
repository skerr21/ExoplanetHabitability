import pandas as pd

def habitable_zone_boundaries(T_eff):
    """
    Calculate the habitable zone boundaries based on a star's effective temperature.
    Returns the inner and outer boundaries.
    """
    S_eff_sun = 1.0  # Solar constant for our Sun
    
    # Constants for Recent Venus and Early Mars
    a_in = 1.776
    a_out = 0.350
    b_in = 1.4335e-4
    b_out = 5.547e-5
    c_in = 2.12e-8
    c_out = 1.5265e-9
    d_in = -1.6e-11
    d_out = -2.874e-12
    e_in = -3.16e-15
    e_out = -5.011e-15
    
    # Calculate the effective stellar fluxes for inner and outer boundaries
    S_eff_in = S_eff_sun * (a_in + b_in*T_eff + c_in*T_eff**2 + d_in*T_eff**3 + e_in*T_eff**4)
    S_eff_out = S_eff_sun * (a_out + b_out*T_eff + c_out*T_eff**2 + d_out*T_eff**3 + e_out*T_eff**4)
    
    # Assuming the luminosity of the star is proportional to the cube of its radius
    # and using the st_rad column for star radius
    # L_star = (radius of star)^3, this is a simplification, a more detailed model would require more data
    L_star = df['st_rad']**3
    
    # Calculate the distances for inner and outer boundaries
    d_in = (L_star / S_eff_in)**0.5
    d_out = (L_star / S_eff_out)**0.5
    
    return d_in, d_out


def is_in_habitable_zone(row):
    return 'yes' if (row['Inner_Boundary'] <= row['pl_orbsmax']).all() and (row['pl_orbsmax'] <= row['Outer_Boundary']).all() else 'no'


# Read the CSV file into a DataFrame
file_path = "planets.csv"  # replace with the path to your CSV file
df = pd.read_csv(file_path)

# Ensure there are no leading or trailing spaces in column names
df.columns = df.columns.str.strip()

# Calculate the habitable zone boundaries for each star
df['Inner_Boundary'], df['Outer_Boundary'] = zip(*df['st_teff'].apply(habitable_zone_boundaries))

# Check if each planet is in the habitable zone
df['habitable_zone'] = df.apply(is_in_habitable_zone, axis=1)

# Save the updated DataFrame back to the CSV file (or to a new CSV file if you prefer)
df.to_csv(file_path, index=False)

# Read the CSV data
file_path = "planets.csv"  # replace with the path to your CSV file
df = pd.read_csv(file_path)
from io import StringIO
# df = pd.read_csv(StringIO(data))
print(df.columns)
# Apply the function to compute habitable zone boundaries
df['Inner_Boundary'], df['Outer_Boundary'] = zip(*df['st_teff'].apply(habitable_zone_boundaries))

# Save the updated DataFrame to a new CSV file
df.to_csv('updated_stars.csv', index=False)
