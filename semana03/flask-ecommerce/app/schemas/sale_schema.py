from pydantic import BaseModel, EmailStr

class CreateCustomerSchema(BaseModel):
    name: str
    last_name: str
    email: EmailStr
    address: str
    document_number: str

class CreateSaleDetailSchema(BaseModel):
    quantity: int
    price: float
    subtotal: float
    product_id: int

class CreateSaleSchema(BaseModel):
    total: float
    customer: CreateCustomerSchema
    details: list[CreateSaleDetailSchema]

class SaleSchema(BaseModel):
    pass