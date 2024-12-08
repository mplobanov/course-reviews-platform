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
from pydantic import StrictBool, StrictStr
from typing import Any, Optional
from openapi_server.models.get_courses200_response import GetCourses200Response


router = APIRouter()

ns_pkg = openapi_server.endpoints
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


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
