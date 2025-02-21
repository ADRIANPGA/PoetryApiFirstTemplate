# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from generated_api.apis.products_api_base import BaseProductsApi
import recommender.impl

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

from generated_api.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from generated_api.models.product import Product


router = APIRouter()

ns_pkg = recommender.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/api/v0/products",
    responses={
        201: {"description": "Producto creado exitosamente"},
        400: {"description": "La solicitud no es válida"},
    },
    tags=["products"],
    summary="Crear un producto",
    response_model_by_alias=True,
)
async def create_product(
    product: Annotated[Product, Field(description="Datos del producto a crear")] = Body(None, description="Datos del producto a crear"),
) -> None:
    """Crea un nuevo producto en la base de datos."""
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().create_product(product)


@router.delete(
    "/api/v0/products/{asin}",
    responses={
        204: {"description": "Producto eliminado exitosamente"},
        404: {"description": "El recurso no se encuentra"},
    },
    tags=["products"],
    summary="Eliminar un producto",
    response_model_by_alias=True,
)
async def delete_product(
    asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")] = Path(..., description="Identificador único del producto (ASIN)"),
) -> None:
    """Elimina un producto de la base de datos."""
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().delete_product(asin)


@router.get(
    "/api/v0/products/{asin}",
    responses={
        200: {"model": Product, "description": "Producto encontrado"},
        404: {"description": "El recurso no se encuentra"},
    },
    tags=["products"],
    summary="Obtener un producto por ASIN",
    response_model_by_alias=True,
)
async def get_product_by_asin(
    asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")] = Path(..., description="Identificador único del producto (ASIN)"),
) -> Product:
    """Recupera un producto específico utilizando su ASIN."""
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().get_product_by_asin(asin)


@router.get(
    "/api/v0/products",
    responses={
        200: {"model": Product, "description": "Lista de productos obtenida exitosamente"},
        400: {"description": "La solicitud no es válida"},
    },
    tags=["products"],
    summary="Obtener productos",
    response_model_by_alias=True,
)
async def get_products(
    category: Annotated[Optional[StrictStr], Field(description="Filtrar por categoría")] = Query(None, description="Filtrar por categoría", alias="category"),
    limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Limitar el número de productos devueltos")] = Query(None, description="Limitar el número de productos devueltos", alias="limit", ge=1),
) -> Product:
    """Obtiene una lista de productos con filtros opcionales por categoría y límite."""
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().get_products(category, limit)


@router.put(
    "/api/v0/products/{asin}",
    responses={
        200: {"description": "Producto actualizado exitosamente"},
        400: {"description": "La solicitud no es válida"},
    },
    tags=["products"],
    summary="Actualizar un producto",
    response_model_by_alias=True,
)
async def update_product(
    asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")] = Path(..., description="Identificador único del producto (ASIN)"),
    product: Annotated[Product, Field(description="Datos actualizados del producto")] = Body(None, description="Datos actualizados del producto"),
) -> None:
    """Actualiza los datos de un producto existente."""
    if not BaseProductsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseProductsApi.subclasses[0]().update_product(asin, product)
