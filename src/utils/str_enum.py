from enum import Enum


class StrEnum(str, Enum):
    value: str

    def __str__(self) -> str:
        return self.value
