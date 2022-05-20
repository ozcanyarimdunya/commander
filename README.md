# Commander

> A very simple tool to create beautiful console application by using native argparse.

| Project       | Tabler                                       |
|---------------|----------------------------------------------|
| Author        | Özcan Yarımdünya                             |
| Documentation | https://ozcanyarimdunya.github.io/commander/ |
| Source code   | https://github.com/ozcanyarimdunya/commander |

`commander` is a library that you can create beautiful class based cli application by using `argparse`.

## Installation

Only `python3.7+` required, no extra dependencies.

```shell
pip install commander-py
```

## Usage

Basic usage, let's greet someone :)

Create a file named `myapp.py`.

Import required classes from `commander` library

```python
from commander import Application
from commander import Command
```

Define your first command.

1. `create` is the method where you define your cli arguments
2. `handle` is the method where you use entered arguments.

```python
class GreetCommand(Command):
    name = "greet"
    description = "Greet command"

    def create(self):
        """Create your cli arguments here"""

        self.add_argument("-n", "--name", help="Name of sample")

    def handle(self, **arguments):
        """Do things with your arguments here"""

        name = arguments["name"]
        print(f"Greetings {name} :)")

```

Create your commander application and register the command then run.

```python
if __name__ == '__main__':
    app = Application(name="myapp", description="My first commander application")
    app.register(GreetCommand)
    app.run()
```

**Now test your first application**

Simple usage.

```text
# Command
$ python myapp.py greet -n "John Doe"

# Output
Greetings John Doe :)
```

Subcommand `greet` subcommand also have its own help function.

```text
# Command
$ python myapp.py greet --help

# Output
USAGE: myapp greet [-h] [-n NAME]

Greeting command

OPTIONAL ARGUMENTS:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  Name of sample
```

The main application `myapp` has its own help function, you can see `greet` command in the _AVAILABLE COMMANDS_ section

```text
# Command
$ python myapp.py --help

# Output
USAGE: myapp [-h] {greet}

My first commander application

OPTIONAL ARGUMENTS:
  -h, --help       show this help message and exit

AVAILABLE COMMANDS:
  greet   Greeting command
```

## Test

This project using `pytest` and `pytest-cov`.

```shell
make test
```

## Documentation

**Live preview**

```shell
make serve-docs
```

**Building**

```shell
build-docs
```

## LICENSE

```text
MIT License

Copyright (c) 2022 yarimdunya.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```
