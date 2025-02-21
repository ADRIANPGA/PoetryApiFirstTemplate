# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from generated_api.apis.reviews_api_base import BaseReviewsApi
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
from typing import Any
from typing_extensions import Annotated
from generated_api.models.review import Review
from generated_api.models.review_list_response import ReviewListResponse


router = APIRouter()

ns_pkg = recommender.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/api/v0/reviews",
    responses={
        201: {"description": "Reseña creada exitosamente"},
    },
    tags=["reviews"],
    summary="Crear una reseña",
    response_model_by_alias=True,
)
async def create_review(
    review: Annotated[Review, Field(description="Datos de la reseña a crear")] = Body(None, description="Datos de la reseña a crear"),
) -> None:
    """Crea una nueva reseña para un producto."""
    if not BaseReviewsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReviewsApi.subclasses[0]().create_review(review)


@router.delete(
    "/api/v0/reviews/{review_id}",
    responses={
        204: {"description": "Reseña eliminada exitosamente"},
        404: {"description": "El recurso no se encuentra"},
    },
    tags=["reviews"],
    summary="Eliminar una reseña",
    response_model_by_alias=True,
)
async def delete_review(
    review_id: Annotated[StrictStr, Field(description="iD de la reseña a eliminar")] = Path(..., description="iD de la reseña a eliminar"),
) -> None:
    """Elimina una reseña de la base de datos."""
    if not BaseReviewsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReviewsApi.subclasses[0]().delete_review(review_id)


@router.get(
    "/api/v0/reviews",
    responses={
        200: {"model": ReviewListResponse, "description": "Lista de reseñas obtenida exitosamente"},
    },
    tags=["reviews"],
    summary="Obtener reseñas",
    response_model_by_alias=True,
)
async def get_reviews(
) -> ReviewListResponse:
    """Obtiene una lista de reseñas con filtros opcionales."""
    if not BaseReviewsApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseReviewsApi.subclasses[0]().get_reviews()
