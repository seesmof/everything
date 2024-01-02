from typing import List, Optional
from pydantic import BaseModel
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Variant(BaseModel):
    name: str
    variantCode: str
    available: bool
    price: int


class Product(BaseModel):
    id: int
    title: str
    variants: Optional[List[Variant]]


item = Product(
    id=51981,
    title="New T-Shirt",
    variants=[
        Variant(name="Small", variantCode="S", available=True, price=10),
        Variant(name="Medium", variantCode="M", available=True, price=20),
        Variant(name="Large", variantCode="L", available=False, price=30),
        Variant(name="Extra Large", variantCode="X", available=True, price=40),
    ],
)
console.print(item)
