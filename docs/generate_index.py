#!/usr/bin/python3
""" This script generates index.md from the md files listed in mkdocs.yml.

All of the pages listed in the nav section of mkdocs.yml are listed in index.md
with the exception of index.md. Links are included to the level 2 headings in
each file.
"""

def get_files(yml_file):
    """Get a list of markdown files from the nav section of a yml file.

    Args:
        yml_file: the yml file to search
    
    Returns:
        List of markdown files
    """

    with open(yml_file) as file_:
        config = file_.readlines()

    files = []
    started_nav = False
    for line in config:
        if started_nav == False:
            if line == 'nav:\n':
                started_nav = True
            continue
        
        line = line.strip()
        if len(line) == 0 or line[0] != '-':
            break
        
        components = line.split(':')
        if len(components) != 2:
            raise ValueError('Unexpected format: {}'.format(line))
        
        path = components[1].strip().strip('"\'')
        if path != 'index.md' and len(path) > 0:
            files.append(path)
    return files

def file_links(md_file):
    """Format links based on the headings in a markdown file.

    Args:
        md_file: the md file to search for headings
    
    Returns:
        List of formated lines to write
    """
    with open(md_file, encoding='utf-8') as file_:
        md_lines = file_.readlines()
    
    lines = []
    lines.append('#{}'.format(md_lines[0]))
    for line in md_lines:
        if line[:3] == '## ':
            heading = line[3:-1]
            tag = heading.lower().replace(' ', '_')
            lines.append('* [{}]({}#{})\n'.format(heading, md_file, tag))
    return lines

files = get_files('../mkdocs.yml')

with open('index.md', 'w') as index:
    index.write('# Index\n')
    for path in files:
        lines = file_links(path)
        index.writelines(lines)