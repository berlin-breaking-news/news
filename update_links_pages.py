import os
import re
from pathlib import Path

def update_links_in_file(file_path, relative_to):
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Pattern to match href and src attributes
    pattern = r'(href|src)=["\']([^"\']+?)["\']'
    
    def replace_match(match):
        attr = match.group(1)  # href or src
        url = match.group(2)   # the URL
        quote = match.group(0)[len(attr) + 1]  # get the quote character used
        
        # Skip external URLs, anchors, and already absolute paths
        if (url.startswith(('http://', 'https://', '//', 'mailto:', 'tel:', '#')) or 
            url.startswith(('http', 'data:', 'javascript:')) or 
            not any(url.endswith(ext) for ext in ['.html', '.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp'])):
            return f'{attr}={quote}{url}{quote}'
            
        # Handle root-relative paths (starting with /)
        if url.startswith('/'):
            return f'{attr}={quote}.{url}{quote}'
            
        # Handle parent directory references
        if url.startswith('../'):
            return f'{attr}={quote}{url}{quote}'
            
        # Handle same-directory references
        return f'{attr}={quote}../pages/{url}{quote}'
    
    # Apply replacements
    updated_content = re.sub(pattern, replace_match, content)
    
    # Special case for index.html links
    updated_content = updated_content.replace('href="index.html"', 'href="../pages/index.html"')
    updated_content = updated_content.replace("href='index.html'", "href='../pages/index.html'")
    
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
            if update_links_in_file(file_path, relative_path):
                updated_files.append(str(relative_path))
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
    
    # Print summary
    if updated_files:
        print("Updated links in the following files:")
        for file in updated_files:
            print(f"- {file}")
    else:
        print("No files needed updating.")

if __name__ == "__main__":
    main()
