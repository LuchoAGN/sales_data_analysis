from fastapi import APIRouter, UploadFile, File
from app.services.data_processing import process_sales_data
from app.models.sales_data import SalesData
from typing import List

router = APIRouter()

@router.post("/upload", response_model=List[SalesData])
async def upload_sales_data(file: UploadFile = File(...)):
    analysis_results = process_sales_data(file)

    sales_data_list = [
        SalesData(
            date=row['date'],
            product_id=row.get('product_id'),
            product_name=row.get('product_name'),
            quantity_sold=row.get('quantity_sold', 0),
            sales=row['sales'],
            region=row.get('region')
        )
        for _, row in analysis_results.iterrows()
    ]
    return sales_data_list