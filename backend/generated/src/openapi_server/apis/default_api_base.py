# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from openapi_server.models.course_info import CourseInfo
from openapi_server.models.get_course_reviews200_response import GetCourseReviews200Response
from openapi_server.models.get_courses200_response import GetCourses200Response
from openapi_server.models.teacher import Teacher


class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    async def get_course(
        self,
        id: StrictInt,
    ) -> CourseInfo:
        ...


    async def get_course_reviews(
        self,
        id: StrictInt,
    ) -> GetCourseReviews200Response:
        ...


    async def get_courses(
        self,
        only_available: Optional[StrictBool],
        have_extern: Optional[StrictBool],
        high_simplicity: Optional[StrictBool],
        high_teacher_rating: Optional[StrictBool],
        text_query: Optional[StrictStr],
    ) -> GetCourses200Response:
        ...


    async def get_teachers(
        self,
        query: Optional[StrictStr],
    ) -> List[Teacher]:
        ...
