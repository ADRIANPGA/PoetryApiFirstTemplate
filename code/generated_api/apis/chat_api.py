# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from generated_api.apis.chat_api_base import BaseChatApi
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
from typing_extensions import Annotated
from generated_api.models.chat_query import ChatQuery
from generated_api.models.chat_response import ChatResponse


router = APIRouter()

ns_pkg = recommender.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/api/v0/chat/product/{asin}",
    responses={
        200: {"model": ChatResponse, "description": "Respuesta del chatbot"},
    },
    tags=["chat"],
    summary="Hacer una consulta específica de un producto al chatbot",
    response_model_by_alias=True,
)
async def chat_product_query(
    asin: Annotated[StrictStr, Field(description="Identificador único del producto (ASIN)")] = Path(..., description="Identificador único del producto (ASIN)"),
    chat_query: Annotated[ChatQuery, Field(description="Consulta específica para el chatbot")] = Body(None, description="Consulta específica para el chatbot"),
) -> ChatResponse:
    """Consulta sobre un producto específico utilizando su ASIN."""
    if not BaseChatApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseChatApi.subclasses[0]().chat_product_query(asin, chat_query)


@router.post(
    "/api/v0/chat/query",
    responses={
        200: {"model": ChatResponse, "description": "Respuesta del chatbot"},
    },
    tags=["chat"],
    summary="Hacer una consulta general al chatbot",
    response_model_by_alias=True,
)
async def chat_query(
    chat_query: Annotated[ChatQuery, Field(description="Consulta para el chatbot")] = Body(None, description="Consulta para el chatbot"),
) -> ChatResponse:
    """Permite interactuar con el chatbot para consultas generales."""
    if not BaseChatApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseChatApi.subclasses[0]().chat_query(chat_query)
