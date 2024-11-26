from typing import Optional

from arguments.argument_interface import ArgumentInterface
import argparse


class CliArgumentProvider(ArgumentInterface):
    def __init__(self):
        parser = argparse.ArgumentParser(description="Run a script and send an email.")

        parser.add_argument(
            "--script-path", "-p", required=False, help="Path to the script to be executed"
        )

        parser.add_argument("--script", "-sc", required=False, help="Bash code to run in place")

        parser.add_argument(
            "--recipient", "-r", required=False, help="Recipient email address"
        )

        parser.add_argument(
            "--sender", "-s", required=False, help="Sender email address"
        )

        parser.add_argument("--password", "-ps", required=False, help="Sender password")

        self.args = parser.parse_args()

    @property
    def script_path(self) -> Optional[str]:
        return self.args.script_path

    @property
    def script(self) -> Optional[str]:
        return self.args.script

    @property
    def recipient(self) -> Optional[str]:
        return self.args.recipient

    @property
    def sender(self) -> Optional[str]:
        return self.args.sender

    @property
    def password(self) -> Optional[str]:
        return self.args.password

