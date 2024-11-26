from typing import Optional

from arguments.argument_interface import ArgumentInterface
from environment import Environment


class EnvironmentArgumentProvider(ArgumentInterface):
    @property
    def sender(self) -> Optional[str]:
        return Environment.SENDER.value

    @property
    def script_path(self) -> Optional[str]:
        return Environment.SCRIPT_PATH.value

    @property
    def script(self) -> Optional[str]:
        return None

    @property
    def recipient(self) -> Optional[str]:
        return Environment.RECIPIENT.value

    @property
    def password(self) -> Optional[str]:
        return Environment.PASSWORD.value


