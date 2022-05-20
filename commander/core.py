import argparse
import sys

from commander import color


class ApplicationError(Exception):
    pass


class CommandError(argparse.ArgumentError):
    pass


class CommandTypeError(argparse.ArgumentTypeError):
    pass


class HelpFormatter(argparse.HelpFormatter):
    def __init__(self, *args, **kwargs):
        kwargs.update(max_help_position=32, width=120)
        super().__init__(*args, **kwargs)

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
            description = command.description
            _action = argparse.Action(
                [color.cyan(command.name)],
                dest="",
                help=description,
            )
            super().add_argument(_action)


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

    def create(self):
        raise NotImplementedError

    def handle(self, **arguments):
        raise NotImplementedError

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


class Application(Command):
    def __init__(self, name=None, description=None):
        self._description = description
        self._commands = []

        super().__init__(description=self._description, formatter_class=HelpFormatter)
        self.prog = color.underline(name or self.prog)

    def create(self):
        command_group = self.parser.add_argument_group("available commands")
        command_action = command_group.add_argument(
            "command",
            choices=[cmd.name for cmd in self._commands],
        )
        # note: used in HelpFormatter
        setattr(command_action, "subcommands", self._commands)

    def handle(self, argv, command):
        command_class = next(cmd for cmd in self._commands if cmd.name == command)
        description = command_class.description
        prog = f"{self.prog} {color.underline(command)}"
        instance = command_class(prog=prog, description=description)
        arguments = instance.parse_args(argv[2:])
        instance.handle(**arguments.__dict__)

    def register(self, command):
        if command.name is None:
            command.name = command.__name__.replace("Command", "").lower()

        found = next((it for it in self._commands if it.name == command.name), None)
        if found:
            raise ApplicationError(f"A command with name '{command.name}' already exists.")

        self._commands.append(command)

    def run(self, argv=None):
        argv = argv or sys.argv
        args = self.parse_args(argv[1:2])
        self.handle(argv, args.command)
