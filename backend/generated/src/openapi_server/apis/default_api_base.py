# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictBool, StrictStr
from typing import Any, Optional
from openapi_server.models.get_courses200_response import GetCourses200Response


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def get_courses(
        self,
        only_available: Optional[StrictBool],
        have_extern: Optional[StrictBool],
        high_simplicity: Optional[StrictBool],
        high_teacher_rating: Optional[StrictBool],
        text_query: Optional[StrictStr],
    ) -> GetCourses200Response:
        ...
