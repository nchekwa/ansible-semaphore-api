# coding: utf-8

"""
    SEMAPHORE

    Semaphore API

    The version of the OpenAPI document: 2.2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from semaphore_api.models.project_backup_environments_inner import ProjectBackupEnvironmentsInner
from semaphore_api.models.project_backup_inventories_inner import ProjectBackupInventoriesInner
from semaphore_api.models.project_backup_keys_inner import ProjectBackupKeysInner
from semaphore_api.models.project_backup_meta import ProjectBackupMeta
from semaphore_api.models.project_backup_repositories_inner import ProjectBackupRepositoriesInner
from semaphore_api.models.project_backup_templates_inner import ProjectBackupTemplatesInner
from semaphore_api.models.project_backup_views_inner import ProjectBackupViewsInner
from typing import Optional, Set
from typing_extensions import Self

class ProjectBackup(BaseModel):
    """
    ProjectBackup
    """ # noqa: E501
    meta: Optional[ProjectBackupMeta] = None
    templates: Optional[List[ProjectBackupTemplatesInner]] = None
    repositories: Optional[List[ProjectBackupRepositoriesInner]] = None
    keys: Optional[List[ProjectBackupKeysInner]] = None
    views: Optional[List[ProjectBackupViewsInner]] = None
    inventories: Optional[List[ProjectBackupInventoriesInner]] = None
    environments: Optional[List[ProjectBackupEnvironmentsInner]] = None
    __properties: ClassVar[List[str]] = ["meta", "templates", "repositories", "keys", "views", "inventories", "environments"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProjectBackup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in templates (list)
        _items = []
        if self.templates:
            for _item in self.templates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['templates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in repositories (list)
        _items = []
        if self.repositories:
            for _item in self.repositories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['repositories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in keys (list)
        _items = []
        if self.keys:
            for _item in self.keys:
                if _item:
                    _items.append(_item.to_dict())
            _dict['keys'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inventories (list)
        _items = []
        if self.inventories:
            for _item in self.inventories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inventories'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in environments (list)
        _items = []
        if self.environments:
            for _item in self.environments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['environments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProjectBackup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "meta": ProjectBackupMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "templates": [ProjectBackupTemplatesInner.from_dict(_item) for _item in obj["templates"]] if obj.get("templates") is not None else None,
            "repositories": [ProjectBackupRepositoriesInner.from_dict(_item) for _item in obj["repositories"]] if obj.get("repositories") is not None else None,
            "keys": [ProjectBackupKeysInner.from_dict(_item) for _item in obj["keys"]] if obj.get("keys") is not None else None,
            "views": [ProjectBackupViewsInner.from_dict(_item) for _item in obj["views"]] if obj.get("views") is not None else None,
            "inventories": [ProjectBackupInventoriesInner.from_dict(_item) for _item in obj["inventories"]] if obj.get("inventories") is not None else None,
            "environments": [ProjectBackupEnvironmentsInner.from_dict(_item) for _item in obj["environments"]] if obj.get("environments") is not None else None
        })
        return _obj


