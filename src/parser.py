from enum import Enum


class RespType(Enum):
    SimpleStrings = "+"
    SimpleErrors = "-"
    Intergers = ":"
    BulkStrings = "$"
    Arrays = "*"
    Nulls = "_"
    Booleans = "#"
    Doubles = ","
    BigNumbers = "("
    BulkErrors = "!"
    VerbatimStrings = "="
    Maps = "%"
    Sets = "~"
    Pushes = ">"


class RespParser:
    @staticmethod
    def deserialize(inputString: bytes) -> object: ...

    def serialize(data) -> bytes: ...
