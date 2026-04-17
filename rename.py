import os

target_dir = r"C:\Users\manwh\OneDrive\Documents\Politics\USWorldNATO\usworld_images_package"
sizes = ["1600", "1024", "640"]

# 1. Finish the interrupted JPGs by forcing the overwrite
interrupted_bases = ["foreign-aid-donors", "migration-destination-countries"]
for base in interrupted_bases:
    for size in sizes:
        temp_file = os.path.join(target_dir, f"TEMP_{base}-{size}.jpg")
        final_file = os.path.join(target_dir, f"{base}-{size}.jpg")
        if os.path.exists(temp_file):
            os.replace(temp_file, final_file)
            print(f"Recovered and Finalized: {base}-{size}.jpg")

# 2. Process all the WebP files safely
rename_map = {
    "green-revolution-diffusion": "polio-cases-trends",
    "polio-cases-trends": "smallpox-cases",
    "smallpox-cases": "hiv-aids-deaths-share",
    "hiv-aids-deaths-share": "nuclear-warhead-stockpiles",
    "nuclear-warhead-stockpiles": "ozone-dobson-trends",
    "ozone-dobson-trends": "foreign-aid-donors",
    "montreal-protocol": "migration-destination-countries"
}

# Rename old webp to TEMP
for old_base, new_base in rename_map.items():
    for size in sizes:
        old_file = os.path.join(target_dir, f"{old_base}-{size}.webp")
        temp_file = os.path.join(target_dir, f"TEMP_{new_base}-{size}.webp")
        if os.path.exists(old_file):
            os.replace(old_file, temp_file)

# Rename TEMP webp to final, overwriting any garbage text images
for old_base, new_base in rename_map.items():
    for size in sizes:
        temp_file = os.path.join(target_dir, f"TEMP_{new_base}-{size}.webp")
        final_file = os.path.join(target_dir, f"{new_base}-{size}.webp")
        if os.path.exists(temp_file):
            os.replace(temp_file, final_file)
            print(f"Success: Finalized {new_base}-{size}.webp")