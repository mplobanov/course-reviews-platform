from openapi_server.apis.default_api_base import BaseDefaultApi
from openapi_server.models.get_courses200_response import GetCourses200Response
from pydantic import StrictBool, StrictStr
from typing import Any, Optional


teacher_info = {"id": 1,
                "name": "Владимир Щелов",
                "average_grade": 4.6,
                }

course_info = {"id": 1,
               "name": "Arch1",
               "is_passed": True,
               "has_extern": False,
               "recredit_available": False,
               "teacher": teacher_info,
               "prerequisites": [{"id": 0, "name": "VCS"}],
               "marks": []
               }


class ApiImplementation(BaseDefaultApi):
    async def get_courses(
        self,
        only_available: Optional[StrictBool],
        have_extern: Optional[StrictBool],
        high_simplicity: Optional[StrictBool],
        high_teacher_rating: Optional[StrictBool],
        text_query: Optional[StrictStr],
    ) -> GetCourses200Response:
        return GetCourses200Response( courses = [course_info])
