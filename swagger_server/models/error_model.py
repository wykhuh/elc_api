# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ErrorModel(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type: str=None, title: str=None, detail: str=None, status: int=None):
        """
        ErrorModel - a model defined in Swagger

        :param type: The type of this ErrorModel.
        :type type: str
        :param title: The title of this ErrorModel.
        :type title: str
        :param detail: The detail of this ErrorModel.
        :type detail: str
        :param status: The status of this ErrorModel.
        :type status: int
        """
        self.swagger_types = {
            'type': str,
            'title': str,
            'detail': str,
            'status': int
        }

        self.attribute_map = {
            'type': 'type',
            'title': 'title',
            'detail': 'detail',
            'status': 'status'
        }

        self._type = type
        self._title = title
        self._detail = detail
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'ErrorModel':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The errorModel of this ErrorModel.
        :rtype: ErrorModel
        """
        return deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """
        Gets the type of this ErrorModel.
        MIME type or about:blank

        :return: The type of this ErrorModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this ErrorModel.
        MIME type or about:blank

        :param type: The type of this ErrorModel.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def title(self) -> str:
        """
        Gets the title of this ErrorModel.
        HTTP status code description

        :return: The title of this ErrorModel.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """
        Sets the title of this ErrorModel.
        HTTP status code description

        :param title: The title of this ErrorModel.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def detail(self) -> str:
        """
        Gets the detail of this ErrorModel.
        Brief description of the error

        :return: The detail of this ErrorModel.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """
        Sets the detail of this ErrorModel.
        Brief description of the error

        :param detail: The detail of this ErrorModel.
        :type detail: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")

        self._detail = detail

    @property
    def status(self) -> int:
        """
        Gets the status of this ErrorModel.
        HTTP numeric status code

        :return: The status of this ErrorModel.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """
        Sets the status of this ErrorModel.
        HTTP numeric status code

        :param status: The status of this ErrorModel.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

