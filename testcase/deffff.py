import json
import os
import random

import pytest
import yaml

from common.handle_test import Handle
from config import Conf
from utils.YamlUtil import YamlReader

option = [
    {
        "value": {
            "defaultStatus": "0",
            "code": "0",
            "detailedStatus": "0",
            "display": "从未感觉气短",
            "itemOptionRId": "481184742155358208",
            "optionId": "481151303221907456"
        }
    },
    {
        "value": {
            "defaultStatus": "0",
            "code": "1",
            "detailedStatus": "0",
            "display": "很少感觉气短",
            "itemOptionRId": "481184742159552512",
            "optionId": "481151303221907457"
        }
    },
    {
        "value": {
            "defaultStatus": "0",
            "code": "2",
            "detailedStatus": "0",
            "display": "有时感觉气短",
            "itemOptionRId": "481184742163746816",
            "optionId": "481151303226101760"
        }
    }
]
print(len(option))
print(random.randint(0, len(option)))

duziteng = {
    "key": "man", "a": "zhe", "hao": "kun"
}

for k, v in duziteng.items():
    print(k + v)
    print(list(range(1, 11)))

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in "ABC" for n in "123"])


d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + " = " + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])


