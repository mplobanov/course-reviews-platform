# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import StrictBool, StrictStr  # noqa: F401
from typing import Any, Optional  # noqa: F401
from openapi_server.models.get_courses200_response import GetCourses200Response  # noqa: F401


def test_get_courses(client: TestClient):
    """Test case for get_courses

    Get courss
    """
    params = [("only_available", True),     ("have_extern", True),     ("high_simplicity", True),     ("high_teacher_rating", True),     ("text_query", 'text_query_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/courses",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

