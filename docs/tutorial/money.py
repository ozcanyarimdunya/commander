from commander import Command
from commander import Commander


class CurrencyCommand(Command):
    name = "currency"
    description = "Currency command"

    def create(self):
        self.add_argument(
            "amount",
            help="Amount of money",
        )
        self.add_argument(
            "--currency",
            type=str,
            choices=["TRY", "USD"],
            help="Currency",
            default="TRY",
        )
        self.add_argument(
            "--verbose",
            default=False,
            action="store_true",
            help="Verbosity",
        )

    def handle(self, **arguments):
        amount = arguments.get("amount")
        currency = arguments.get("currency")
        verbose = arguments.get("verbose")

        self.cyan("You have {} {} money.".format(amount, currency))
        if verbose:
            self.red("You're luck!")


if __name__ == '__main__':
    commander = Commander(description="Commander", version="0.1.0")
    commander.register(CurrencyCommand)
    commander.run()
