from openapi_server.apis.default_api_base import BaseDefaultApi
from openapi_server.models.get_courses200_response import GetCourses200Response
from openapi_server.models.course_info import CourseInfo
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from fastapi.responses import JSONResponse
from openapi_server.models.teacher import Teacher
from openapi_server.models.get_course_reviews200_response import GetCourseReviews200Response
import openapi_server.mock.mock_data as mock

from openapi_server.db.db import DB

class ApiImplementation(BaseDefaultApi):
    db_adapter = DB()
    async def get_courses(
        self,
        only_available: Optional[StrictBool],
        have_extern: Optional[StrictBool],
        high_simplicity: Optional[StrictBool],
        high_teacher_rating: Optional[StrictBool],
        text_query: Optional[StrictStr],
    ) -> GetCourses200Response:
        return GetCourses200Response(courses = self.db_adapter.getCourses())

    async def get_course(
        self,
        id: Annotated[StrictInt, Field(description="ID of the course")],
    ) -> CourseInfo:
        result = next(
            (item for item in mock.cources_info if item.get("id") == id), None)
        if result is None:
            return JSONResponse(status_code=404, content={"message": "Course not found"})
        return CourseInfo(**result)

    async def get_teachers(
        self,
        query: Annotated[Optional[StrictStr], Field(description="Search query for teachers")],
    ) -> List[Teacher]:
        return mock.teachers

    async def get_course_reviews(
        self,
        id: StrictInt,
    ) -> GetCourseReviews200Response:
        reviews = mock.courses_reviews.get(id)
        if reviews is None:
            return JSONResponse(status_code=404, content={"message": "Course not found"})
        return GetCourseReviews200Response(reviews = reviews)
