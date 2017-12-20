# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Reference(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, author: List[str]=None, citation: str=None, identifier: List[str]=None, journal: List[str]=None, title: str=None, type: str=None, year: str=None):
        """
        Reference - a model defined in Swagger

        :param author: The author of this Reference.
        :type author: List[str]
        :param citation: The citation of this Reference.
        :type citation: str
        :param identifier: The identifier of this Reference.
        :type identifier: List[str]
        :param journal: The journal of this Reference.
        :type journal: List[str]
        :param title: The title of this Reference.
        :type title: str
        :param type: The type of this Reference.
        :type type: str
        :param year: The year of this Reference.
        :type year: str
        """
        self.swagger_types = {
            'author': List[str],
            'citation': str,
            'identifier': List[str],
            'journal': List[str],
            'title': str,
            'type': str,
            'year': str
        }

        self.attribute_map = {
            'author': 'author',
            'citation': 'citation',
            'identifier': 'identifier',
            'journal': 'journal',
            'title': 'title',
            'type': 'type',
            'year': 'year'
        }

        self._author = author
        self._citation = citation
        self._identifier = identifier
        self._journal = journal
        self._title = title
        self._type = type
        self._year = year

    @classmethod
    def from_dict(cls, dikt) -> 'Reference':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The reference of this Reference.
        :rtype: Reference
        """
        return deserialize_model(dikt, cls)

    @property
    def author(self) -> List[str]:
        """
        Gets the author of this Reference.
        Parsed list of author names

        :return: The author of this Reference.
        :rtype: List[str]
        """
        return self._author

    @author.setter
    def author(self, author: List[str]):
        """
        Sets the author of this Reference.
        Parsed list of author names

        :param author: The author of this Reference.
        :type author: List[str]
        """

        self._author = author

    @property
    def citation(self) -> str:
        """
        Gets the citation of this Reference.
        Formated APA citation. For legacy reasons, this is all that is currently available for Neotoma references

        :return: The citation of this Reference.
        :rtype: str
        """
        return self._citation

    @citation.setter
    def citation(self, citation: str):
        """
        Sets the citation of this Reference.
        Formated APA citation. For legacy reasons, this is all that is currently available for Neotoma references

        :param citation: The citation of this Reference.
        :type citation: str
        """

        self._citation = citation

    @property
    def identifier(self) -> List[str]:
        """
        Gets the identifier of this Reference.
        Container for DOI and unique database reference index

        :return: The identifier of this Reference.
        :rtype: List[str]
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier: List[str]):
        """
        Sets the identifier of this Reference.
        Container for DOI and unique database reference index

        :param identifier: The identifier of this Reference.
        :type identifier: List[str]
        """

        self._identifier = identifier

    @property
    def journal(self) -> List[str]:
        """
        Gets the journal of this Reference.
        Container for journal or book name, editors, pages and volume

        :return: The journal of this Reference.
        :rtype: List[str]
        """
        return self._journal

    @journal.setter
    def journal(self, journal: List[str]):
        """
        Sets the journal of this Reference.
        Container for journal or book name, editors, pages and volume

        :param journal: The journal of this Reference.
        :type journal: List[str]
        """

        self._journal = journal

    @property
    def title(self) -> str:
        """
        Gets the title of this Reference.
        Title of the reference material

        :return: The title of this Reference.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """
        Sets the title of this Reference.
        Title of the reference material

        :param title: The title of this Reference.
        :type title: str
        """

        self._title = title

    @property
    def type(self) -> str:
        """
        Gets the type of this Reference.
        Nature of the reference publication. Journal, book etc.

        :return: The type of this Reference.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """
        Sets the type of this Reference.
        Nature of the reference publication. Journal, book etc.

        :param type: The type of this Reference.
        :type type: str
        """

        self._type = type

    @property
    def year(self) -> str:
        """
        Gets the year of this Reference.
        Publication year of the reference material

        :return: The year of this Reference.
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year: str):
        """
        Sets the year of this Reference.
        Publication year of the reference material

        :param year: The year of this Reference.
        :type year: str
        """

        self._year = year

