from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class SalesData(BaseModel):
    """
    Modelo que representa una entrada de datos de ventas.
    """
    date: datetime = Field(..., description="Fecha de la venta")
    product_id: Optional[int] = Field(None, description="ID del producto vendido")
    product_name: Optional[str] = Field(None, description="Nombre del producto vendido")
    quantity_sold: Optional[int] = Field(0, description="Cantidad de unidades vendidas")
    sales: float = Field(..., description="Cantidad total de la venta en términos monetarios")
    region: Optional[str] = Field(None, description="Región en la que se realizó la venta")

    class Config:
        json_schema_extra = {
            "example": {
                "date": "2024-08-25T12:34:56",
                "product_id": 123,
                "product_name": "Example Product",
                "quantity_sold": 10,
                "sales": 250.75,
                "region": "North America"
            }
        }