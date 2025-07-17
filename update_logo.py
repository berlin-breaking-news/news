import os
import re

# Define the directory to search in (project root)
project_root = '/Users/konstantinputincev/CascadeProjects/independent-clone'

# Define the pattern to search for and its replacement
old_logo = '''<p>&copy; 2025 Independent Clone. Все права защищены.</p>'''

new_logo = '''<p>&copy; 2025 Правда.ру. Все права защищены.</p>'''

# Compile a regex pattern that matches the old logo text
pattern = re.escape(old_logo)

# Function to replace content in a file
def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace all occurrences of the pattern
        new_content, count = re.subn(pattern, new_logo, content, flags=re.DOTALL)
        
        # Only write if changes were made
        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(new_content)
            return count
        return 0
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return 0

# Walk through all files in the project directory
updated_files = 0
total_replacements = 0

for root, dirs, files in os.walk(project_root):
    # Skip node_modules and other directories if needed
    if 'node_modules' in dirs:
        dirs.remove('node_modules')
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            replacements = update_file(filepath)
            if replacements > 0:
                print(f"Updated: {filepath} ({replacements} replacements)")
                updated_files += 1
                total_replacements += replacements

print(f"\nUpdate complete! {total_replacements} replacements made in {updated_files} files.")
