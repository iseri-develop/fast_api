from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    telephone: str
    my_products: List[Product]
    my_sales: List[Purchase]
    my_purchases: List[Purchase]
    

class Product(BaseModel):
    id: Optional[str] = None
    user: User
    name: str
    details: str
    price: float
    disponible: bool = False

class Purchase(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delivery: bool = False
    address: str
    observation: Optional[str] = "Sem obersavaçoes"