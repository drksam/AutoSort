import shutil
import argparse
from pathlib import Path

def copy_folder_structure(source_dir, dest_dir):
    """
    Recursively copies the folder structure from source_dir to dest_dir,
    without copying any files.
    
    Args:
        source_dir (str or Path): Path to the source directory
        dest_dir (str or Path): Path to the destination directory
    """
    # Convert to Path objects if they aren't already
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    
    # Ensure the source directory exists
    if not source_path.exists():
        raise FileNotFoundError(f"Source directory '{source_dir}' not found.")
    
    # Create the destination directory if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)
    
    # Iterate through all items in the source directory
    for item in source_path.glob("**/*"):
        if item.is_dir():
            # Calculate the relative path from source_dir
            rel_path = item.relative_to(source_path)
            
            # Create the directory in the destination
            target_dir = dest_path / rel_path
            target_dir.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {target_dir}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Copy folder structure without files.')
    parser.add_argument('source', help='Source directory path')
    parser.add_argument('destination', help='Destination directory path')
    args = parser.parse_args()
    
    try:
        copy_folder_structure(args.source, args.destination)
        print("\nFolder structure copied successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
