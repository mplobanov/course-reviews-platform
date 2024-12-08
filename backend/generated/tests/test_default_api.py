# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictBool, StrictInt, StrictStr  # noqa: F401
from typing import Any, List, Optional  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from openapi_server.models.course_info import CourseInfo  # noqa: F401
from openapi_server.models.get_course_reviews200_response import GetCourseReviews200Response  # noqa: F401
from openapi_server.models.get_courses200_response import GetCourses200Response  # noqa: F401
from openapi_server.models.teacher import Teacher  # noqa: F401


def test_get_course(client: TestClient):
    """Test case for get_course

    Get course details
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/courses/{id}".format(id=56),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_course_reviews(client: TestClient):
    """Test case for get_course_reviews

    Get course reviews
    """
    params = [("cursor", 'cursor_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/courses/{id}/reviews".format(id=56),
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_courses(client: TestClient):
    """Test case for get_courses

    Get courses
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


def test_get_teachers(client: TestClient):
    """Test case for get_teachers

    Search teachers
    """
    params = [("query", 'query_example')]
    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/teachers",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_post_course(client: TestClient):
    """Test case for post_course

    Create a course
    """
    course_info = {"has_extern":1,"prerequisites":[{"name":"name","id":5},{"name":"name","id":5}],"is_passed":1,"teacher":{"average_grade":1.4658129805029452,"name":"name","id":6},"extern_description":"extern_description","name":"name","general_description":"general_description","recredit_description":"recredit_description","id":0,"marks":[{"note":"note","name":"name","id":5,"value":2.3021358869347655,"max_value":7.061401241503109},{"note":"note","name":"name","id":5,"value":2.3021358869347655,"max_value":7.061401241503109}],"recredit_available":1}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/courses",
    #    headers=headers,
    #    json=course_info,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

