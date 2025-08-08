import os
import datetime

# ✅ Define the folder where your target files are located
source_folder = "D:\\Users\\love\\projects\\Python work\\Projects\\Files"

# ✅ Change the current working directory to the source folder
os.chdir(source_folder)

# ✅ List all items (files and folders) in the source folder
items = os.listdir(source_folder)

# ✅ Get today's date in YYYY-MM-DD format
today = datetime.date.today().isoformat()

# ✅ Loop through each item in the folder
for item in items:
    # 🔍 Get the full path of the item
    full_path = os.path.join(source_folder, item)
    
    # ✅ Check if the item is a file
    if os.path.isfile(full_path):
        # 🧩 Split the file name and extension
        name, ext = os.path.splitext(item)
        
        # 🎯 Target only .txt files for renaming
        if item.endswith(".txt"):
            print("Current working directory:", os.getcwd())
            print("File Name:", name, ext)
            
            # 🆕 Create the new file name with today's date
            new_name = name + "_" + today + ext
            
            # 📍 Get the full path for the new file name
            new_full_path = os.path.join(source_folder, new_name)
            
            # 🔄 Rename the file using full paths
            os.rename(full_path, new_full_path)
            print(f"Renamed: {item} → {new_name}")
    
    # 📁 If the item is a directory, just print its name
    elif os.path.isdir(full_path):
        print("Directory Name:", item)
