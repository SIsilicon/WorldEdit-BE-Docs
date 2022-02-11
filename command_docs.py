import re, json, polib
from warnings import warn

def printFlag(arg):
    return f'[-{arg["flag"]}]'

def printArg(arg):
    if 'default' in arg:
        return f'[{arg["name"]}]'
    else:
        return f'<{arg["name"]}>'

def getSubCmds(args):
    subs = {}
    for arg in args:
        if 'subName' in arg and not arg['subName'].startswith('_'):
            subs[arg['subName']] = arg
    return subs

def printUsage(args, sub=''):
    usage = []
    
    subs = getSubCmds(args)
    if subs and not sub:
        text = '<'
        for arg in subs.values():
            text += arg['subName'] + '|'
        usage.append(text[:-1] + '>')
    else:
        flagtext = ''
        sublist = []
        def processflagtext():
            nonlocal flagtext
            if flagtext:
                usage.append(flagtext + ']')
                flagtext = ''
        
        for arg in args:
            if 'subName' in arg:
                processflagtext()
                if arg['subName'] == sub:
                    print(sub)
                    usage.append(sub)
                    text = printUsage(arg.get('args', []))
                    if text:
                        usage.append(text[1:])
                    break
                elif arg['subName'].startswith('_'):
                    if arg['subName'] == '_x':
                        text = printUsage(arg.get('args', []))
                        if text:
                            usage.append(text[1:])
                        break
                    else:
                        sublist.append(printUsage(arg.get('args', []))[1:])
            elif 'flag' in arg:
                if not flagtext:
                    flagtext = '[-'
                flagtext += arg['flag']
                if 'name' in arg:
                    flagtext += ' ' + printArg(arg)
                    processflagtext()
            elif 'name' in arg:
                processflagtext()
                usage.append(printArg(arg))
        processflagtext()
        if sublist:
            usage.append('(' + '|'.join(sublist) + ')')
    
    return ' ' + ' '.join(usage) if usage else ''

commands_folder = '../WorldEdit/src/server/commands'
commands = {}

## Get location of commands
with open(commands_folder + '/import-commands.ts') as file:
    line = file.readline()
    while line:
        match = re.match(r"import '\.(/.+).js';", line)
        if match:
            commands[commands_folder + match.group(1) + '.ts'] = {}
        line = file.readline()

## Get command data
for path in commands:
    with open(path) as file:
        line = file.readline()
        jsonStr = None
        while line:
            if re.match(r"const registerInformation = {", line):
                jsonStr = '{\n'
            elif re.match(r"};", line):
                jsonStr += '}'
                break
            elif jsonStr:
                if re.match(r"\s+default:.+\n", line):
                    line = '\tdefault: 1' + (',\n' if line[:-1].endswith(',') else '\n')
                elif re.match(r"\s+range:.+\n", line):
                    line = '\trange: 1' + (',\n' if line[:-1].endswith(',') else '\n')
                line = re.sub(r"(\s+)(.+?):(.+)", r"\1'\2':\3", line)
                jsonStr += line.replace("'", '"')
            line = file.readline()
        commands[path] = json.loads(jsonStr)

texts_file = '../WorldEdit/texts/en_US.po'
texts = {
    'commands.help.description': 'Get a list of commands available and a quick description for each of them'
}

## Get texts
for entry in polib.pofile(texts_file):
    if entry.msgid != "":
        texts[entry.msgid] = entry.msgstr.replace('\\"', '"')

commandspage = 'docs/commands.md'
prevfile = ''
with open(commandspage, 'r') as file:
    for line in file.readlines():
        prevfile += line
        if line.startswith('<!--COMMANDAREA-->'):
            break

with open(commandspage, 'w') as file:
    file.write(prevfile)
    
    def printCommand(command, sub=None):
        file.write('!!! note ""\n\t\n')
        
        aliases = ''
        for alias in command.get('aliases', []):
            aliases += ' (or ' if not aliases else ''
            aliases += f';{alias}, '
        aliases = ')'.join(aliases.rsplit(', ', 1))
        
        if sub:
            name = f'{command["name"]} {sub["subName"]}'
            desc = command['description'] + '.' + sub['subName']
            perm = sub.get('permission', '')
            args = printUsage(command.get('usage', []), sub['subName'])
            aliases = ''
        else:
            name = command['name']
            desc = command['description']
            perm = command.get('permission', '')
            args = printUsage(command.get('usage', []))
        
        if not desc in texts:
            warn(f'there is no text value for \033[93m{desc}\033[0m.')
        perm = f'`{perm}`' if perm else ''
        
        file.write(f'\t**;{name}{aliases}**\n\n')
        file.write('\t|||\n\t|:--|:--|\n')
        file.write(f'\t|**Description**|{texts.get(desc, desc)}|\n')
        file.write(f'\t|**Permission**|{perm}|\n')
        file.write(f'\t|**Usage**|`;{command["name"]}{args}`|\n')
        
        file.write('\n')
    
    for command in commands.values():
        printCommand(command)
        for sub in getSubCmds(command.get('usage', [])).values():
            printCommand(command, sub)