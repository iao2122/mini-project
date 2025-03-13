import argparse
import numpy as np
import pandas as pd

class MEEMS:
    def __init__(self, num_sites=10, num_species=15, num_samples_per_site=20):

        # Parameters
        self.num_sites = 10
        self.num_species = 15
        self.num_samples_per_site = 20  # Sample points per site

    def sim(self):
        # Generate site locations (lat, lon)
        latitudes = np.random.uniform(30, 50, self.num_sites)  # Example latitude range
        longitudes = np.random.uniform(-120, -80, self.num_sites)  # Example longitude range
        
        # Generate environmental variables (temperature, precipitation)
        temperature = np.random.uniform(5, 25, self.num_sites)  # Temperature in Celsius
        precipitation = np.random.uniform(500, 2000, self.num_sites)  # Precipitation in mm/year
        
        # Create species preferences
        species_prefs = {
            f"Species_{i+1}": {
                "temp_opt": np.random.uniform(10, 20),
                "precip_opt": np.random.uniform(800, 1500),
                "temp_tol": np.random.uniform(3, 7),
                "precip_tol": np.random.uniform(200, 500)
            }
            for i in range(self.num_species)
        }
        
        # Generate occurrences
        data = []
        for site_idx in range(self.num_sites):
            lat, lon = latitudes[site_idx], longitudes[site_idx]
            temp, precip = temperature[site_idx], precipitation[site_idx]
            
            for _ in range(self.num_samples_per_site):
                for species, prefs in species_prefs.items():
                    temp_suitability = np.exp(-((temp - prefs["temp_opt"]) ** 2) / (2 * prefs["temp_tol"] ** 2))
                    precip_suitability = np.exp(-((precip - prefs["precip_opt"]) ** 2) / (2 * prefs["precip_tol"] ** 2))
                    occurrence_prob = temp_suitability * precip_suitability  # Combined suitability
                    
                    presence = np.random.rand() < occurrence_prob  # Presence/absence based on probability
                    
                    if presence:
                        data.append([site_idx, lat, lon, temp, precip, species])
        
        # Convert to DataFrame
        df = pd.DataFrame(data, columns=["Site", "Latitude", "Longitude", "Temperature", "Precipitation", "Species"])
        
        return(df)

if __name__ == "__main__":
    m = MEEMS()
    df = m.sim()
    print(df.head())
