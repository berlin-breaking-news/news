import os
from pathlib import Path

def update_file_paths(file_path):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Make replacements
    updated_content = content.replace('pages/js/', 'js/')
    updated_content = updated_content.replace('pages/css/', 'css/')
    
    # Write back to file if changes were made
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)
        return True
    return False

def main():
    # Get the directory of this script
    script_dir = Path(__file__).parent
    pages_dir = script_dir / 'pages'
    
    # Process all HTML files in the pages directory
    updated_files = []
    for file_path in pages_dir.glob('**/*.html'):
        try:
            relative_path = file_path.relative_to(script_dir)
            if update_file_paths(file_path):
                updated_files.append(str(relative_path))
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Print summary
    if updated_files:
        print("Updated asset paths in the following files:")
        for file in updated_files:
            print(f"- {file}")
    else:
        print("No files needed updating.")

if __name__ == "__main__":
    main()
