import json
from os import path
from typing import List, Optional
from pydantic import BaseModel, field_validator
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Variant(BaseModel):
    name: str
    variantCode: str
    available: bool
    price: int

    @field_validator("variantCode")
    def validate_variant_code(cls, v):
        if len(v) != 1:
            raise ValueError("Variant code must be one character long")


class Product(BaseModel):
    id: int
    title: str
    variants: Optional[List[Variant]]


currentDir = path.dirname(path.abspath(__file__))
dataPath = path.join(currentDir, "..", "data", "data.json")

with open(dataPath, "r") as f:
    data = json.load(f)
    products = [Product(**p) for p in data["results"]]
console.print(products)
