import random

from commander import Application
from commander import Command


class ReverseCommand(Command):
    name = "reverse"
    description = "Reverse a word"

    def create(self):
        self.add_argument("--word", help="Word to reverse")

    def handle(self, **arguments):
        word = arguments["word"]
        reverse = word[::-1]
        print(f"Reverse of {word} is {reverse}.")


class CapitalizeCommand(Command):
    name = "capitalize"
    description = "Capitalize a word"

    def create(self):
        self.add_argument("--word", help="Word to capitalize")

    def handle(self, **arguments):
        word = arguments["word"]
        capitalize = word.capitalize()
        self.write(f"Capitalized of '{word}' is {capitalize}.", style=self.red)


class RandomizeCommand(Command):
    name = "randomize"
    description = "Randomize a word"

    def create(self):
        self.add_argument("--word", help="Word to randomize")

    def handle(self, **arguments):
        word = arguments["word"]
        randomize = random.sample(word, len(word))
        randomize = "".join(randomize)
        self.success(f"Randomize of {word} is {randomize}.")


if __name__ == "__main__":
    app = Application(name="app", description="Simple word operation")
    app.register(ReverseCommand)
    app.register(CapitalizeCommand)
    app.register(RandomizeCommand)
    app.run()
