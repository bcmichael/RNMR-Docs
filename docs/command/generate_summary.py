#!/usr/bin/python3
""" This script generates command_summary.md from full_command.md.

The short description and categories listed with each with each command in
full_command.md provide the information needed to generate command_summary.md,
which is organized by category and provides links to the full descriptions as
well as displaying the short descriptions.
"""

def format_command(lines, categories, num):
    """Format a mardown line for a table entry for a command.

    Args:
        lines: list of 4 lines starting with the heading containing the command
        categories: dict containing formatted lines organized by category
        num: line number for error messages
    """

    if len(lines[0]) <= 4:
        raise ValueError('Invalid Heading at line {}'.format(num))
    else:
        command = lines[0][4:]

    if len(lines[1]) == 0:
        raise ValueError('No description for {} command at line {}'.format(command, num))
    else:
        description = lines[1]
    
    if len(lines[2]) != 0 or lines[3][:10] != 'Category: ':
        raise ValueError('Improper formatting for {} command at line {}'.format(command, num))

    if len(lines[3]) <= 10:
        raise ValueError('No category for {} command at line {}'.format(command, num))
    else:
        category = lines[3][10:]
    
    line = '[{}](full_command.md#{}) | {}\n'.format(command, command.lower(), description)
    if category in categories:
        categories[category].append(line)
    else:
        categories[category] = [line]

with open('full_command.md') as file_:
    lines = file_.readlines()

lines = [line.rstrip('\n') for line in lines]

categories = {}
for ind, line in enumerate(lines):
    if line[:4] == '### ':
        format_command(lines[ind:ind+4], categories, ind+1)

keys = list(categories.keys())
keys.sort()

with open('command_summary.md', 'w') as file_:
    file_.write('# Command Summary\n')
    for category in keys:
        file_.write('## {}\n'.format(category))
        file_.write('Command | Description\n')
        file_.write('------- | -----------\n')
        for command in categories[category]:
            file_.write(command)
        file_.write('\n')