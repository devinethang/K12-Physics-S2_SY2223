#!/usr/bin/env python3
"""
Convert all markdown files in the directory to HTML
"""

import os
import markdown
from pathlib import Path

def convert_md_to_html(md_file_path):
    """Convert a single markdown file to HTML"""
    
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Fix links from .md to .html
    import re
    md_content = re.sub(r'\[([^\]]+)\]\(([^)]+)\.md\)', r'[\1](\2.html)', md_content)
    
    # Convert markdown to HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite', 'toc'])
    html_content = md.convert(md_content)
    
    # Create full HTML document
    html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{Path(md_file_path).stem}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .container {{
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 2em;
            margin-bottom: 1em;
        }}
        h1 {{
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            border-bottom: 2px solid #95a5a6;
            padding-bottom: 5px;
        }}
        code {{
            background-color: #f8f8f8;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background-color: #f8f8f8;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            border-left: 4px solid #3498db;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin-left: 0;
            font-style: italic;
            color: #555;
        }}
        ul, ol {{
            margin-left: 20px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        a {{
            color: #3498db;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        .toc {{
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        {html_content}
    </div>
</body>
</html>"""
    
    # Create HTML file path
    html_file_path = md_file_path.replace('.md', '.html')
    
    # Write HTML file
    with open(html_file_path, 'w', encoding='utf-8') as f:
        f.write(html_doc)
    
    return html_file_path

def main():
    """Main function to convert all markdown files"""
    
    # Get current directory
    current_dir = Path(__file__).parent
    
    # Find all markdown files
    md_files = list(current_dir.glob('*.md'))
    
    if not md_files:
        print("No markdown files found in the current directory.")
        return
    
    print(f"Found {len(md_files)} markdown files to convert:")
    
    converted_files = []
    for md_file in md_files:
        try:
            html_file = convert_md_to_html(str(md_file))
            converted_files.append(html_file)
            print(f"✓ Converted: {md_file.name} → {Path(html_file).name}")
        except Exception as e:
            print(f"✗ Error converting {md_file.name}: {str(e)}")
    
    print(f"\nConversion complete! {len(converted_files)} files converted to HTML.")
    print("\nGenerated HTML files:")
    for html_file in converted_files:
        print(f"  - {Path(html_file).name}")

if __name__ == "__main__":
    main()