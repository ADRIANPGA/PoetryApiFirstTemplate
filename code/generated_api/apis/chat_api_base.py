# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from generated_api.models.chat_query import ChatQuery
from generated_api.models.chat_response import ChatResponse


class BaseChatApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseChatApi.subclasses = BaseChatApi.subclasses + (cls,)
    async def chat_product_query(
        self,
        asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")],
        chat_query: Annotated[ChatQuery, Field(description="Consulta específica para el chatbot")],
    ) -> ChatResponse:
        """Consulta sobre un producto específico utilizando su ASIN."""
        ...


    async def chat_query(
        self,
        chat_query: Annotated[ChatQuery, Field(description="Consulta para el chatbot")],
    ) -> ChatResponse:
        """Permite interactuar con el chatbot para consultas generales."""
        ...
