import os
import shutil

def organize_directory(directory):
    for filename in os.listdir(directory):
        # Skip directories
        if os.path.isdir(os.path.join(directory, filename)):
            continue

        # Split the filename into name and extension
        file_extension = filename.split('.')[-1] if '.' in filename else ''
        if file_extension:
            # Create a directory for the file extension if it doesn't exist
            destination_folder = os.path.join(directory, file_extension.lower())
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Move the file into its respective directory
            shutil.move(os.path.join(directory, filename), os.path.join(destination_folder, filename))

if __name__ == "__main__":
    current_folder_path = os.getcwd()
    organize_directory(current_folder_path)
