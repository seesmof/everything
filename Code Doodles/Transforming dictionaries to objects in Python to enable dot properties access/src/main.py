inputData = {"a": 1, "b": {"c": 2}, "d": ["hi", {"foo": "bar"}]}

from box import Box

data = Box(inputData)

print(data, data.a)

from easydict import EasyDict

data = EasyDict(inputData)

print(data, data.a)
