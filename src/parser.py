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
    CRLF = "\r\n"

    @staticmethod
    def deserialize(data: bytes | list[str], offset: list[int]) -> object:
        if type(data) == bytes:
            data = data.decode()
            data = data.split(RespParser.CRLF)
        tokens = data
        if tokens[-1] == "":
            tokens.pop()
        match RespType(tokens[offset][0]):
            case RespType.SimpleStrings:
                result = tokens[offset[0]][1:]
                offset[0] += 1
                return result
            case RespType.SimpleErrors:
                result = tokens[offset[0]][1:]
                offset[0] += 1
                return BaseException(result)
            case RespType.Intergers:
                result = tokens[offset[0]][1:]
                offset[0] += 1
                return int(result)
            case RespType.BulkStrings:
                offset[0] += 2
                return tokens[offset[0]]
            case RespType.Arrays:
                currentOffset = [1]
                resultList = []
                while currentOffset[0] < len(tokens):
                    resultList.append(RespParser.deserialize(tokens, currentOffset))
                return resultList
            case RespType.Nulls:
                offset[0] += 1
                return None
            case RespType.Booleans:
                result = (
                    True
                    if tokens[offset[0]] == "#t" or tokens[offset[0]] == "#T"
                    else False
                )
                offset[0] += 1
                return result
            case RespType.Doubles:
                result = float(tokens[offset[0]][1:])
                offset[0] += 1
                return result

    def serialize(data) -> bytes: ...
