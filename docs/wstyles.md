# Printer and styles

List of printers

| Printers |
|----------|
| write    |
| info     |
| success  |
| warn     |
| danger   |
| comment  |

and list of styles

| Styles    |
|-----------|
| black     |
| red       |
| green     |
| yellow    |
| blue      |
| magenta   |
| cyan      |
| white     |
| bold      |
| faint     |
| italic    |
| underline |
| blink     |
| blink2    |
| negative  |
| concealed |
| crossed   |

You can use in `handle` method like below.

```python
self.printer(self.style(text))

```

Example:

```python
def handle(self, **arguments):
    self.success(f"Hello {self.red('red text')}, {self.green('green text')}.")
```
