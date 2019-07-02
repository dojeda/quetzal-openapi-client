# coding: utf-8

"""
    Quetzal API

    Quetzal: an API to manage data files and their associated metadata.  # noqa: E501

    OpenAPI spec version: 0.3.0
    Contact: support@quetz.al
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaginatedFiles(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'page': 'int',
        'pages': 'int',
        'results': 'list[BaseMetadata]',
        'total': 'int'
    }

    attribute_map = {
        'page': 'page',
        'pages': 'pages',
        'results': 'results',
        'total': 'total'
    }

    def __init__(self, page=None, pages=None, results=None, total=None):  # noqa: E501
        """PaginatedFiles - a model defined in OpenAPI"""  # noqa: E501

        self._page = None
        self._pages = None
        self._results = None
        self._total = None
        self.discriminator = None

        self.page = page
        self.pages = pages
        self.results = results
        self.total = total

    @property
    def page(self):
        """Gets the page of this PaginatedFiles.  # noqa: E501

        Current page number  # noqa: E501

        :return: The page of this PaginatedFiles.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this PaginatedFiles.

        Current page number  # noqa: E501

        :param page: The page of this PaginatedFiles.  # noqa: E501
        :type: int
        """
        if page is None:
            raise ValueError("Invalid value for `page`, must not be `None`")  # noqa: E501

        self._page = page

    @property
    def pages(self):
        """Gets the pages of this PaginatedFiles.  # noqa: E501

        Number of pages available in the collection  # noqa: E501

        :return: The pages of this PaginatedFiles.  # noqa: E501
        :rtype: int
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this PaginatedFiles.

        Number of pages available in the collection  # noqa: E501

        :param pages: The pages of this PaginatedFiles.  # noqa: E501
        :type: int
        """
        if pages is None:
            raise ValueError("Invalid value for `pages`, must not be `None`")  # noqa: E501

        self._pages = pages

    @property
    def results(self):
        """Gets the results of this PaginatedFiles.  # noqa: E501


        :return: The results of this PaginatedFiles.  # noqa: E501
        :rtype: list[BaseMetadata]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this PaginatedFiles.


        :param results: The results of this PaginatedFiles.  # noqa: E501
        :type: list[BaseMetadata]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def total(self):
        """Gets the total of this PaginatedFiles.  # noqa: E501

        Total number of items in the collection  # noqa: E501

        :return: The total of this PaginatedFiles.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PaginatedFiles.

        Total number of items in the collection  # noqa: E501

        :param total: The total of this PaginatedFiles.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PaginatedFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
