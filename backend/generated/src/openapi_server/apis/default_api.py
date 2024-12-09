# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from openapi_server.apis.default_api_base import BaseDefaultApi
import openapi_server.endpoints

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
from pydantic import StrictBool, StrictInt, StrictStr
from typing import Any, List, Optional
from openapi_server.models.course_info import CourseInfo
from openapi_server.models.get_course_reviews200_response import GetCourseReviews200Response
from openapi_server.models.get_courses200_response import GetCourses200Response
from openapi_server.models.teacher import Teacher


router = APIRouter()

ns_pkg = openapi_server.endpoints
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.get(
    "/courses/{id}",
    responses={
        200: {"model": CourseInfo, "description": "Course details"},
        403: {"description": "User not authorized"},
        404: {"description": "Course not found"},
    },
    tags=["default"],
    summary="Get course details",
    response_model_by_alias=True,
)
async def get_course(
    id: StrictInt = Path(..., description=""),
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
    id: StrictInt = Path(..., description=""),
) -> GetCourseReviews200Response:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_course_reviews(id)


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
    text_query: Optional[StrictStr] = Query(None, description="", alias="text_query"),
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
    query: Optional[StrictStr] = Query(None, description="", alias="query"),
) -> List[Teacher]:
    if not BaseDefaultApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseDefaultApi.subclasses[0]().get_teachers(query)
