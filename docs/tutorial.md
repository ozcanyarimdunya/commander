# Tutorial

Let's have cli that user can reverse, capitalize or randomize a word.

For example, if your entered **Football** string then;

1. `reverse` command will convert word to **llabtooF**
2. `capitalize` command will convert word to **FOOTBALL**
3. `randomize` command will convert word to **otblalof**

For the simplicity we will have cli prompt given below.

```shell
python app.py reverse --word "Football"

# or
python app.py capitalize --word "Football"

# or
python app.py randomize --word "Football"
```

Let's start!

First create a python file `app.py` and import commander classes.

```python
{!./docs/code/app.py[ln:1-4]!}
```

Now let's create our first command `reverse`.

```python
{!./docs/code/app.py[ln:7-17]!}
```

Here `{!./docs/code/app.py[ln:12]!}` we add `--word` argument, to get word from cli.

Here `{!./docs/code/app.py[ln:15]!}` we get value of `--word` argument.

Let's define rest of the commands.

```python
{!./docs/code/app.py[ln:20-44]!}
```

Here `{!./docs/code/app.py[ln:30]!}` we add `write` function with `style=self.red` to print a red text.

Here `{!./docs/code/app.py[ln:44]!}` we add `success` function to print a success text.

For more color and styles check [Printer and styles,](./wstyles.md)

Now let's create our main application and register commands.

```python
{!./docs/code/app.py[ln:47-52]!}
```

Let's test.

First let's directly run app.py, it should give and error and ask for a command.

```text
# command
python app.py

# output
USAGE: app [-h] {reverse,capitalize,randomize}
app: error: the following arguments are required: command
```

Let's have a try `--help` option

```text
# command
python app.py --help

# output
USAGE: app [-h] {reverse,capitalize,randomize}

Simple word operation

OPTIONAL ARGUMENTS:
  -h, --help            show this help message and exit

AVAILABLE COMMANDS:
  reverse      Reverse a word
  capitalize   Capitalize a word
  randomize    Randomize a word
```

Now it is more clear, see :)

Let's have a try `--help` option for `reverse` command.

```text
# command
python app.py reverse --help

# output
USAGE: app reverse [-h] [--word WORD]

Reverse a word

OPTIONAL ARGUMENTS:
  -h, --help   show this help message and exit
  --word WORD  Word to reverse
```

As expected !

Now let's try `--word` argument for `reverse` command!

```text
# command
python app.py reverse --word "Test"

# output
Reverse of Test is tseT.
```

And it worked!

Now test the others by yourself :)

Cheers.
