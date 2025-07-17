import os
import re
from pathlib import Path

def update_links_in_file(file_path):
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
            url.startswith(('/', '../', 'data:', 'javascript:')) or 
            not any(url.endswith(ext) for ext in ['.html', '.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico', '.webp'])):
            return f'{attr}={quote}{url}{quote}'
            
        # Replace /index.html with ../pages/index.html
        if url == '/index.html':
            return f'{attr}={quote}../pages/index.html{quote}'
            
        # Handle other relative paths
        if not url.startswith(('../', '/')):
            # Make relative paths absolute from site root
            return f'{attr}={quote}../{url}{quote}'
            
        return match.group(0)  # Return unchanged if no replacement needed
    
    # Apply replacements
    updated_content = re.sub(pattern, replace_match, content)
    
    # Replace /index.html with ../pages/index.html in the entire content
    updated_content = updated_content.replace('href="/index.html"', 'href="../pages/index.html"')
    updated_content = updated_content.replace("href='/index.html'", "href='../pages/index.html'")
    
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
    for root, _, files in os.walk(pages_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    if update_links_in_file(file_path):
                        updated_files.append(file)
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")
    
    # Also process the root index.html if it exists
    root_index = script_dir / 'index.html'
    if root_index.exists():
        try:
            if update_links_in_file(root_index):
                updated_files.append('index.html')
        except Exception as e:
            print(f"Error processing {root_index}: {e}")
    
    # Print summary
    if updated_files:
        print("Updated links in the following files:")
        for file in updated_files:
            print(f"- {file}")
    else:
        print("No files needed updating.")

if __name__ == "__main__":
    main()
