# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing import Any
from typing_extensions import Annotated
from generated_api.models.review import Review
from generated_api.models.review_list_response import ReviewListResponse


class BaseReviewsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseReviewsApi.subclasses = BaseReviewsApi.subclasses + (cls,)
    async def create_review(
        self,
        review: Annotated[Review, Field(description="Datos de la reseña a crear")],
    ) -> None:
        """Crea una nueva reseña para un producto."""
        ...


    async def delete_review(
        self,
        review_id: Annotated[StrictStr, Field(description="iD de la reseña a eliminar")],
    ) -> None:
        """Elimina una reseña de la base de datos."""
        ...


    async def get_reviews(
        self,
    ) -> ReviewListResponse:
        """Obtiene una lista de reseñas con filtros opcionales."""
        ...
