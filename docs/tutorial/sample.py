#!/usr/bin/env python3
from commander import Command
from commander import Commander


class InstallCommand(Command):
    name = "install"
    description = "Install a package"

    def create(self):
        self.add_argument(
            "package",
            help="Package name",
        )
        self.add_argument(
            "--version",
            type=str,
            help="Package version",
            default="0.1.0",
        )

    def handle(self, **arguments):
        package = arguments.get("package")
        version = arguments.get("version")
        self.info(f"You have installed {package}=={version}.")


class UninstallCommand(Command):
    name = "uninstall"
    description = "Uninstall a package"

    def create(self):
        self.add_argument(
            "package",
            help="Package name",
        )

    def handle(self, **arguments):
        package = arguments.get("package")
        self.danger(f"You have uninstalled {package}.")


if __name__ == "__main__":
    commander = Commander(description="Package manager", version="2.0.0")
    commander.register(InstallCommand)
    commander.register(UninstallCommand)
    commander.run()
