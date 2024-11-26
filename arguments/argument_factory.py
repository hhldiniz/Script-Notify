from typing import Optional

from arguments.argument_interface import ArgumentInterface
from arguments.cli_argument_provider import CliArgumentProvider
from arguments.environment_argument_provider import EnvironmentArgumentProvider


class ArgumentFactory(ArgumentInterface):
    def __init__(self):
        self.__cli_argument_provider = CliArgumentProvider()
        self.__environment_argument_provider = EnvironmentArgumentProvider()

    @property
    def script_path(self) -> Optional[str]:
        return self.__cli_argument_provider.script_path or self.__environment_argument_provider.script_path

    @property
    def script(self) -> Optional[str]:
        return self.__cli_argument_provider.script or self.__environment_argument_provider.script

    @property
    def recipient(self) -> Optional[str]:
        return self.__cli_argument_provider.recipient or self.__environment_argument_provider.recipient

    @property
    def sender(self) -> Optional[str]:
        return self.__cli_argument_provider.sender or self.__environment_argument_provider.sender

    @property
    def password(self) -> Optional[str]:
        return self.__cli_argument_provider.password or self.__environment_argument_provider.password
