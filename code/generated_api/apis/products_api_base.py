# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any, Optional
from typing_extensions import Annotated
from generated_api.models.product import Product


class BaseProductsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseProductsApi.subclasses = BaseProductsApi.subclasses + (cls,)
    async def create_product(
        self,
        product: Annotated[Product, Field(description="Datos del producto a crear")],
    ) -> None:
        """Crea un nuevo producto en la base de datos."""
        ...


    async def delete_product(
        self,
        asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")],
    ) -> None:
        """Elimina un producto de la base de datos."""
        ...


    async def get_product_by_asin(
        self,
        asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")],
    ) -> Product:
        """Recupera un producto específico utilizando su ASIN."""
        ...


    async def get_products(
        self,
        category: Annotated[Optional[StrictStr], Field(description="Filtrar por categoría")],
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Limitar el número de productos devueltos")],
    ) -> Product:
        """Obtiene una lista de productos con filtros opcionales por categoría y límite."""
        ...


    async def update_product(
        self,
        asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")],
        product: Annotated[Product, Field(description="Datos actualizados del producto")],
    ) -> None:
        """Actualiza los datos de un producto existente."""
        ...
