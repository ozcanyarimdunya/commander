import argparse
import sys

from commander import color


class CommandError(Exception):
    pass


class HelpFormatter(argparse.HelpFormatter):
    def start_section(self, heading):
        heading = color.bold(heading.upper())
        super().start_section(heading=heading)

    def add_usage(self, usage, actions, groups, prefix=None):
        super().add_usage(usage, actions, groups, prefix=color.bold("USAGE: "))

    def add_argument(self, action):
        if not hasattr(action, "subcommands"):
            super().add_argument(action)
            return

        subcommands = getattr(action, "subcommands", list())
        for command in subcommands:
            description = command.description or ""
            _action = argparse.Action(
                [color.cyan(command.name)],
                dest="",
                help=description,
            )
            super().add_argument(_action)


class Parser(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        kwargs.update(formatter_class=kwargs.get("formatter_class", HelpFormatter))
        super().__init__(*args, **kwargs)


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

    def info(self, text):
        self.write(text, style=self.cyan)

    def success(self, text):
        self.write(text, style=self.green)

    def warn(self, text):
        self.write(text, style=self.yellow)

    def danger(self, text):
        self.write(text, style=self.red)

    def comment(self, text):
        self.write(text, style=self.italic)

    black = color.black
    red = color.red
    green = color.green
    yellow = color.yellow
    blue = color.blue
    magenta = color.magenta
    cyan = color.cyan
    white = color.white
    bold = color.bold
    faint = color.faint
    italic = color.italic
    underline = color.underline
    blink = color.blink
    blink2 = color.blink2
    negative = color.negative
    concealed = color.concealed
    crossed = color.crossed


class Commander(Command):
    def __init__(self, description="", version=""):
        if description and version:
            description = "{} {}".format(description, color.green(version))

        self._description = description
        self._version = version
        self._commands = []

        super().__init__(
            description=self._description,
            formatter_class=HelpFormatter,
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
            raise CommandError(f"A command with name '{command.name}' already exists.")
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
