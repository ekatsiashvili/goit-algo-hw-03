import os
import shutil
import argparse

def copy_files(source_dir, destination_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_path = os.path.join(root, file)
            extension = os.path.splitext(file)[1]
            destination_path = os.path.join(destination_dir, extension[1:], file)
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            shutil.copy(source_path, destination_path)

def main():
    parser = argparse.ArgumentParser(description="Recursive copy and sort files by extension.")
    parser.add_argument("source_dir", help="Source directory path")
    parser.add_argument("destination_dir", nargs="?", default="dist", help="Destination directory path (default: dist)")
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    try:
        copy_files(source_dir, destination_dir)
        print("Files copied and sorted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    # For testing with the provided file paths
    source_dir = r"C:\Projects\Tier_1\Algo\3"
    destination_dir = r"C:\Projects\Tier_1\Algo\3\dist"

    main()
    
    #example to run  python task1.py C:\Projects\Tier_1\Algo\3 C:\Projects\Tier_1\Algo\3\dist