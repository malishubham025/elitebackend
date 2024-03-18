import os

def sort_files_and_get_paths(folder_path):
    """
    Sort files in a folder based on custom sorting function and return their paths.

    Args:
    - folder_path (str): Path to the folder containing the files.

    Returns:
    - list: Array of file paths sorted based on custom sorting function.
    """
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Custom sorting function
    def custom_sort(file_name):
        # Split the file name into base and extension
        base, ext = os.path.splitext(file_name)
        # Split the base part into prefix and numeric part
        prefix, numeric = base.split('-') if '-' in base else (base, '')
        # Convert numeric part to integer for sorting
        return prefix, int(numeric or 0), ext

    # Sort the files based on custom sorting function
    sorted_files = sorted(files, key=custom_sort)

    # Create an array to store file paths
    file_paths = []

    # Display the sorted file names and store their paths
    for file_name in sorted_files:
        if not file_name.startswith('.ipynb_checkpoints'):  # Skip .ipynb_checkpoints file
            file_path = os.path.join(folder_path, file_name)
            file_paths.append(file_path)
            print(file_name)

    # Display the array of file paths
    print("File paths:", file_paths)
    
    return file_paths

# # Example usage:
# folder_path = "/content/screenshot"
# file_paths = sort_files_and_get_paths(folder_path)
