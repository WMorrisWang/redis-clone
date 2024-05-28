import pytest
from src.parser import RespParser
import math


class TestRespParser:

    @pytest.mark.parametrize(
        "inputString, expectedOutput",
        [
            (b"+OK\r\n", "OK"),
            (b"-Error message\r\n", Exception("Error message")),
            (b":10\r\n", 10),
            (b":+10\r\n", 10),
            (b":-10\r\n", -10),
            (b"$5\r\nhello\r\n", "hello"),
            (b"$0\r\n\r\n", ""),
            (b"*0\r\n", []),
            (b"*2\r\n$5\r\nhello\r\n$5\r\nworld\r\n", ["hello", "world"]),
            (b"*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$5\r\nhello\r\n", [1, 2, 3, 4, "hello"]),
            (
                b"*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n",
                [[1, 2, 3], ["hello", "world"]],
            ),
            (b"_\r\n", None),
            (b"#t\r\n", True),
            (b"#f\r\n", False),
            (b",-0.5e-4\r\n", -0.5e-4),
            (b",10\r\n", 10),
            (b",inf\r\n", math.inf),
            (b",-inf\r\n", -math.inf),
            (b",nan\r\n", math.nan),
            (b"%2\r\n+first\r\n:1\r\n+second\r\n:2\r\n", {"first": 1, "second": 2}),
            (b"~2\r\n:1\r\n:2\r\n", set([1, 2])),
        ],
    )
    def test_deserialize(self, inputString, expectedOutput):
        result = RespParser.deserialize(inputString)
        assert result == expectedOutput

    @pytest.mark.parametrize(
        "expectedOutput, inputString",
        [
            (b"+OK\r\n", "OK"),
            (b"-Error message\r\n", Exception("Error message")),
            (b":10\r\n", 10),
            (b":+10\r\n", 10),
            (b":-10\r\n", -10),
            (b"$5\r\nhello\r\n", "hello"),
            (b"$0\r\n\r\n", ""),
            (b"*0\r\n", []),
            (b"*2\r\n$5\r\nhello\r\n$5\r\nworld\r\n", ["hello", "world"]),
            (b"*5\r\n:1\r\n:2\r\n:3\r\n:4\r\n$5\r\nhello\r\n", [1, 2, 3, 4, "hello"]),
            (
                b"*2\r\n*3\r\n:1\r\n:2\r\n:3\r\n*2\r\n+Hello\r\n-World\r\n",
                [[1, 2, 3], ["hello", "world"]],
            ),
            (b"_\r\n", None),
            (b"#t\r\n", True),
            (b"#f\r\n", False),
            (b",-0.5e-4\r\n", -0.5e-4),
            (b",10\r\n", 10),
            (b",inf\r\n", math.inf),
            (b",-inf\r\n", -math.inf),
            (b",nan\r\n", math.nan),
            (b"%2\r\n+first\r\n:1\r\n+second\r\n:2\r\n", {"first": 1, "second": 2}),
            (b"~2\r\n:1\r\n:2\r\n", set([1, 2])),
        ],
    )
    def test_serialize(self, inputString, expectedOutput):
        result = RespParser.serialize(inputString)
        assert result == expectedOutput
