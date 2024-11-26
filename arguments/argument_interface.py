import abc
from typing import Optional


class ArgumentInterface(abc.ABC):
    @property
    @abc.abstractmethod
    def script_path(self) -> Optional[str]:
        pass

    @property
    @abc.abstractmethod
    def script(self) -> Optional[str]:
        pass

    @property
    @abc.abstractmethod
    def recipient(self) -> Optional[str]:
        pass

    @property
    @abc.abstractmethod
    def sender(self) -> Optional[str]:
        pass

    @property
    @abc.abstractmethod
    def password(self) -> Optional[str]:
        pass