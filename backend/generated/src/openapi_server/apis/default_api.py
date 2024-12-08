# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import endpoints

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

from openapi_server.models.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from typing_extensions import Annotated
from openapi_server.models.course_info import CourseInfo
from openapi_server.models.get_course_reviews200_response import GetCourseReviews200Response
from openapi_server.models.get_courses200_response import GetCourses200Response
from openapi_server.models.teacher import Teacher


router = APIRouter()

ns_pkg = endpoints
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/courses/{id}",
    responses={
        200: {"model": CourseInfo, "description": "Course details"},
        403: {"description": "User not authorized"},
    },
    tags=["default"],
    summary="Get course details",
    response_model_by_alias=True,
)
async def get_course(
    id: Annotated[StrictInt, Field(description="ID of the course")] = Path(..., description="ID of the course"),
) -> CourseInfo:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_course(id)


@router.get(
    "/courses/{id}/reviews",
    responses={
        200: {"model": GetCourseReviews200Response, "description": "List of course reviews"},
        403: {"description": "User not authorized"},
    },
    tags=["default"],
    summary="Get course reviews",
    response_model_by_alias=True,
)
async def get_course_reviews(
    id: Annotated[StrictInt, Field(description="ID of the course")] = Path(..., description="ID of the course"),
    cursor: Annotated[Optional[StrictStr], Field(description="Pagination cursor")] = Query(None, description="Pagination cursor", alias="cursor"),
) -> GetCourseReviews200Response:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_course_reviews(id, cursor)


@router.get(
    "/courses",
    responses={
        200: {"model": GetCourses200Response, "description": "A list of courses"},
        403: {"description": "User not authorized"},
    },
    tags=["default"],
    summary="Get courss",
    response_model_by_alias=True,
)
async def get_courses(
    only_available: Optional[StrictBool] = Query(None, description="", alias="only_available"),
    have_extern: Optional[StrictBool] = Query(None, description="", alias="have_extern"),
    high_simplicity: Optional[StrictBool] = Query(None, description="", alias="high_simplicity"),
    high_teacher_rating: Optional[StrictBool] = Query(None, description="", alias="high_teacher_rating"),
    text_query: Annotated[Optional[StrictStr], Field(description="Text to search courses")] = Query(None, description="Text to search courses", alias="text_query"),
) -> GetCourses200Response:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_courses(only_available, have_extern, high_simplicity, high_teacher_rating, text_query)


@router.get(
    "/teachers",
    responses={
        200: {"model": List[Teacher], "description": "List of teachers"},
    },
    tags=["default"],
    summary="Search teachers",
    response_model_by_alias=True,
)
async def get_teachers(
    query: Annotated[Optional[StrictStr], Field(description="Search query for teachers")] = Query(None, description="Search query for teachers", alias="query"),
) -> List[Teacher]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_teachers(query)


@router.post(
    "/courses",
    responses={
        201: {"description": "Course created"},
        403: {"description": "User not authorized"},
    },
    tags=["default"],
    summary="Create a course",
    response_model_by_alias=True,
)
async def post_course(
    course_info: CourseInfo = Body(None, description=""),
) -> None:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().post_course(course_info)
