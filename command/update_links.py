import re

def should_wrap(line):
    if '|' in line: # table
        return False
    if line[:4] == '    ' or line[0] == '\t': # code block
        return False
    if re.match(r'\d\.('    '|\t)', line) is not None: # numbered list
        return False
    if re.match('- ', line) is not None:  # bullet list
        return False

    return True

def wrap(line, limit):
    links = re.finditer(r'\[[\w\s]+\]\([\w/\.]+#[\w]+\)', line)

    for link in links:
        if link.start() < limit and link.end() > limit:
            limit = link.start()
            break
    
    split_point = line.rfind(' ', 0, limit)

    wrapped = line[:split_point]+'\n'
    remainder = line[split_point+1:-1]+' '
    return wrapped, remainder

with open('full_command-Copy.md') as file_:
    old_lines = file_.readlines()

new_lines = []
remainder = ''
for line in old_lines:
    if line == '\n':
        if len(remainder) != 0:
            new_lines.append('{}\n'.format(remainder))
            remainder = ''
        new_lines.append(line)
        continue
        

    line = line.replace('](syntax#', '](syntax.md#')
    line = remainder+line
    remainder = ''

    if should_wrap(line) and len(line) > 121:
        line, remainder = wrap(line, 120)
    new_lines.append(line)

with open('full_command.md', 'w') as file_:
    file_.writelines(new_lines)