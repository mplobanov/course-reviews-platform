# coding: utf-8

"""
    Course Management API

    API for managing courses, teachers, reviews, and users.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_server.models.course_info_all_of_marks_inner import CourseInfoAllOfMarksInner
from openapi_server.models.course_short_info_prerequisites_inner import CourseShortInfoPrerequisitesInner
from openapi_server.models.teacher import Teacher
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CourseInfo(BaseModel):
    """
    CourseInfo
    """ # noqa: E501
    id: StrictInt
    name: StrictStr
    is_passed: StrictBool
    has_extern: StrictBool
    recredit_available: StrictBool
    teacher: Teacher
    prerequisites: List[CourseShortInfoPrerequisitesInner]
    avg_mark: Optional[Union[StrictFloat, StrictInt]] = None
    marks: List[CourseInfoAllOfMarksInner]
    general_description: StrictStr
    extern_description: Optional[StrictStr] = None
    recredit_description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "name", "is_passed", "has_extern", "recredit_available", "teacher", "prerequisites", "avg_mark", "marks", "general_description", "extern_description", "recredit_description"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CourseInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of teacher
        if self.teacher:
            _dict['teacher'] = self.teacher.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in prerequisites (list)
        _items = []
        if self.prerequisites:
            for _item in self.prerequisites:
                if _item:
                    _items.append(_item.to_dict())
            _dict['prerequisites'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in marks (list)
        _items = []
        if self.marks:
            for _item in self.marks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['marks'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CourseInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "is_passed": obj.get("is_passed"),
            "has_extern": obj.get("has_extern"),
            "recredit_available": obj.get("recredit_available"),
            "teacher": Teacher.from_dict(obj.get("teacher")) if obj.get("teacher") is not None else None,
            "prerequisites": [CourseShortInfoPrerequisitesInner.from_dict(_item) for _item in obj.get("prerequisites")] if obj.get("prerequisites") is not None else None,
            "avg_mark": obj.get("avg_mark"),
            "marks": [CourseInfoAllOfMarksInner.from_dict(_item) for _item in obj.get("marks")] if obj.get("marks") is not None else None,
            "general_description": obj.get("general_description"),
            "extern_description": obj.get("extern_description"),
            "recredit_description": obj.get("recredit_description")
        })
        return _obj


