import uvicorn

from fastapi import FastAPI
from generated_api.apis.products_api import router as product_api
from .impl.products_api_impl import ProductsApiImpl  # noqa: F401

app = FastAPI()

# Include the product API router
app.include_router(product_api)

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()