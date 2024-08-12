



def print_command_tree(command, indent=0):
    """ Recursively prints the command tree structure """
    print(' ' * indent + '- ' + command.name)
    for subcommand in getattr(command, 'commands', {}).values():
        print_command_tree(subcommand, indent + 4)