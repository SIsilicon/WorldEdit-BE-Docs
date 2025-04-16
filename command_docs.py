import re, json, polib, sys
from warnings import warn

def printFlag(arg):
    return f'[-{arg["flag"]}]'

def printArg(arg):
    name = arg['name'] + ('...' if arg['type'].endswith('...') else '')
    if 'default' in arg:
        return f'[{name}]'
    else:
        return f'<{name}>'

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

command_prefix = "/wedit:"
commands_folder = '../WorldEdit/src/server/commands'
commands = {}

## Get location of commands
with open(commands_folder + '/command_list.ts') as file:
    line = file.readline()
    while line:
        match = re.match(r'import "\.(/.+).js";', line)
        if match:
            commands[commands_folder + match.group(1) + '.ts'] = {}
        line = file.readline()

## Get command data
for path in commands:
    with open(path) as file:
        line = file.readline()
        suffixJsonStr = None
        jsonStr = None
        while line:
            if re.match(r'const suffixArguments: commandArgList = \[', line):
                suffixJsonStr = re.sub(r'const suffixArguments: commandArgList = \[', "[", line).replace(";", "")
            elif re.match(r'const registerInformation: CommandInfo = {', line):
                jsonStr = '{\n'
            elif re.match(r'};', line):
                jsonStr += '}'
                break
            elif re.match(r'];', line):
                suffixJsonStr += ']'
            elif jsonStr or suffixJsonStr:
                line = re.sub(r'(default:\s*)(.*?)([,}])', r'\1 1\3', line)
                line = re.sub(r'(range:\s*)(\[.*?\])\s*([,}])', r'\1 1\3', line)
                line = re.sub(r'(\s+)(\S+?):(.+)', r'\1"\2":\3', line).replace("'", '"').split('//')[0]
                if jsonStr:
                    if suffixJsonStr:
                        line = re.sub(r'...suffixArguments', suffixJsonStr[1:-3], line)
                    jsonStr += line
                elif suffixJsonStr:
                    suffixJsonStr += line
            line = file.readline()

        jsonStr = re.sub(r'(\w+?)(?=: )', r'"\1"', jsonStr)
        jsonStr = re.sub(r',(\s*?)([}\]])', r'\1\2', jsonStr)
        jsonStr = re.sub(r',(\s*?)([}\]])', r'\1\2', jsonStr)
        try:
            commands[path] = json.loads(jsonStr)
        except Exception as e:
            print(e, '\n' + jsonStr, file=sys.stderr)
            exit(1)

texts_file = '../WorldEdit/texts/en_US.po'
texts = {
    'commands.help.description': 'Get a list of commands available and a quick description for each of them'
}

## Get texts
for entry in polib.pofile(texts_file):
    if entry.msgid != '':
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
            aliases += f'{command_prefix}{alias}, '
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
            print(f'WARNING: There is no text value for \033[93m{desc}\033[0m.')
        perm = f'`{perm}`' if perm else ''
        
        file.write(f'\t**{command_prefix}{name}{aliases}**\n\n')
        file.write(f'\t|**Description**|{texts.get(desc, desc)}|\n')
        file.write('\t|:--|:--|\n')
        file.write(f'\t|**Permission**|{perm}|\n')
        file.write(f'\t|**Usage**|`{command_prefix}{command["name"]}{args}`|\n')
        
        file.write('\n')
    
    for command in commands.values():
        printCommand(command)
        for sub in getSubCmds(command.get('usage', [])).values():
            printCommand(command, sub)
