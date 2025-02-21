from generated_api.apis.products_api_base import BaseProductsApi

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from generated_api.models.product import Product

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)


class ProductsApiImpl(BaseProductsApi):
    
    async def get_products(
        self,
        category,
        limit,
    ) -> Product:
        """Obtiene una lista de productos con filtros opcionales por categoría y límite."""
        print(category)
        print(limit)
        return {"json": "json"}
    