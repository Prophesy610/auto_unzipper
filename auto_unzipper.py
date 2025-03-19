import os
import zipfile

def unzip_all_files_in_folder():
    # Get the current working directory (the folder where the script is run)
    folder_path = os.getcwd()
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a zip file
        if filename.endswith('.zip'):
            file_path = os.path.join(folder_path, filename)
            extract_folder = os.path.join(folder_path, filename[:-4])  # Create folder to extract into
            
            # Create a directory to extract the contents
            if not os.path.exists(extract_folder):
                os.makedirs(extract_folder)
            
            # Unzip the file
            try:
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    print(f"Extracting {filename}...")
                    zip_ref.extractall(extract_folder)
                    print(f"Extracted to {extract_folder}")
                
                # Delete the zip file after extraction
                os.remove(file_path)
                print(f"Deleted {filename} after extraction.")
            
            except Exception as e:
                print(f"Error extracting {filename}: {e}")

if __name__ == "__main__":
    unzip_all_files_in_folder()
import os
import zipfile

def unzip_all_files_in_folder():
    # Get the current working directory (the folder where the script is run)
    folder_path = os.getcwd()
    
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is a zip file
        if filename.endswith('.zip'):
            file_path = os.path.join(folder_path, filename)
            extract_folder = os.path.join(folder_path, filename[:-4])  # Create folder to extract into
            
            # Create a directory to extract the contents
            if not os.path.exists(extract_folder):
                os.makedirs(extract_folder)
            
            # Unzip the file
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                print(f"Extracting {filename}...")
                zip_ref.extractall(extract_folder)
                print(f"Extracted to {extract_folder}")

if __name__ == "__main__":
    unzip_all_files_in_folder()
