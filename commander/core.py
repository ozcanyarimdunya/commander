import argparse
import sys

from commander import color


class CommandError(Exception):
    pass


class HelpFormatter(argparse.HelpFormatter):
    def start_section(self, heading):
        heading = color.bold(heading.upper())
        super(HelpFormatter, self).start_section(heading=heading)

    def add_usage(self, usage, actions, groups, prefix=None):
        super(HelpFormatter, self).add_usage(usage, actions, groups, prefix=color.bold("USAGE: "))

    def add_argument(self, action):
        if not hasattr(action, "subcommands"):
            super(HelpFormatter, self).add_argument(action)
            return

        subcommands = getattr(action, "subcommands", list())
        for command in subcommands:
            description = command.description or ""
            _action = argparse.Action(
                [color.cyan(command.name)],
                dest="",
                help=description,
            )
            super(HelpFormatter, self).add_argument(_action)


class Parser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        kwargs.update(formatter_class=kwargs.get("formatter_class", HelpFormatter))
        super(Parser, self).__init__(*args, **kwargs)


class Command(object):
    name = None
    description = None

    def __init__(self, *args, **kwargs):
        self._parser = Parser(*args, **kwargs)

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)

    def parse_args(self, args=None):
        self.create()
        return self.parser.parse_args(args)

    @property
    def parser(self):
        return self._parser

    @parser.setter
    def parser(self, value):
        raise ValueError("Cannot set parser!")

    @property
    def prog(self):
        return self.parser.prog

    @prog.setter
    def prog(self, value):
        self.parser.prog = value

    def create(self):
        raise NotImplementedError

    def handle(self, **arguments):
        raise NotImplementedError

    @staticmethod
    def write(text, style=None):
        if style:
            text = style(text)
        sys.stdout.write(text)
        sys.stdout.write("\n")

    black = staticmethod(lambda text: Command.write(text, style=color.black))
    red = staticmethod(lambda text: Command.write(text, style=color.red))
    green = staticmethod(lambda text: Command.write(text, style=color.green))
    yellow = staticmethod(lambda text: Command.write(text, style=color.yellow))
    blue = staticmethod(lambda text: Command.write(text, style=color.blue))
    magenta = staticmethod(lambda text: Command.write(text, style=color.magenta))
    cyan = staticmethod(lambda text: Command.write(text, style=color.cyan))
    white = staticmethod(lambda text: Command.write(text, style=color.white))
    bold = staticmethod(lambda text: Command.write(text, style=color.bold))
    faint = staticmethod(lambda text: Command.write(text, style=color.faint))
    italic = staticmethod(lambda text: Command.write(text, style=color.italic))
    underline = staticmethod(lambda text: Command.write(text, style=color.underline))
    blink = staticmethod(lambda text: Command.write(text, style=color.blink))
    blink2 = staticmethod(lambda text: Command.write(text, style=color.blink2))
    negative = staticmethod(lambda text: Command.write(text, style=color.negative))
    concealed = staticmethod(lambda text: Command.write(text, style=color.concealed))
    crossed = staticmethod(lambda text: Command.write(text, style=color.crossed))


class Commander(Command):
    def __init__(self, description="", version=""):
        if description and version:
            description = "{} {}".format(description, color.green(version))

        self._description = description
        self._version = version
        self._commands = []

        super(Commander, self).__init__(
            description=self._description,
            formatter_class=HelpFormatter
        )
        self.prog = color.underline(self.prog)

    def create(self):
        command_group = self.parser.add_argument_group("available commands")
        command_action = command_group.add_argument(
            "command",
            choices=[cmd.name for cmd in self._commands],
        )
        # note: used in HelpFormatter
        setattr(command_action, "subcommands", self._commands)

        self.add_argument(
            "-v",
            "--version",
            action="version",
            help="show program's version number and exit",
            version=self._version,
        )

    def register(self, command):
        if not command.name:
            command.name = command.__name__.replace("Command", "").lower()

        try:
            next(it for it in self._commands if it.name == command.name)
            raise CommandError("A command with name '{}' already exists.".format(command.name))
        except StopIteration:
            pass

        self._commands.append(command)

    def run(self, argv=None):
        argv = argv or sys.argv
        args = self.parse_args(argv[1:2])
        self.handle(argv, args.command)

    def handle(self, argv, command):
        command_class = next(cmd for cmd in self._commands if cmd.name == command)
        description = command_class.description
        prog = "{} {}".format(
            color.underline(self.prog),
            color.underline(command),
        )
        instance = command_class(prog=prog, description=description)
        arguments = instance.parse_args(argv[2:])
        instance.handle(**arguments.__dict__)
