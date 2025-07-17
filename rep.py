import os
import re

# Define the directory to search in (project root)
project_root = '/Users/konstantinputincev/CascadeProjects/independent-clone'

# Define the patterns to replace
replacements = {
    '../../politika.html': '../politika.html',
    '../../mir.html': '../mir.html',
    '../../sport.html': '../sport.html',
    '../../kultura.html': '../kultura.html',
    '../../tehnologii.html': '../tehnologii.html'
}

# Compile a regex pattern to find all the target patterns
pattern = re.compile('|'.join(re.escape(k) for k in replacements.keys()))

# Function to replace content in a file
def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace all occurrences of the patterns
        new_content = pattern.sub(lambda m: replacements[m.group(0)], content)
        
        # Only write if changes were made
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

# Walk through all files in the project directory
updated_files = 0
for root, dirs, files in os.walk(project_root):
    # Skip node_modules and other directories if needed
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            if update_file(filepath):
                print(f"Updated: {filepath}")
                updated_files += 1

print(f"\nUpdate complete! {updated_files} files were modified.")