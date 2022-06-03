# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class EnvelopeDelayRule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'delay': 'str',
        'resume_date': 'str'
    }

    attribute_map = {
        'delay': 'delay',
        'resume_date': 'resumeDate'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopeDelayRule - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._delay = None
        self._resume_date = None
        self.discriminator = None

        setattr(self, "_{}".format('delay'), kwargs.get('delay', None))
        setattr(self, "_{}".format('resume_date'), kwargs.get('resume_date', None))

    @property
    def delay(self):
        """Gets the delay of this EnvelopeDelayRule.  # noqa: E501

          # noqa: E501

        :return: The delay of this EnvelopeDelayRule.  # noqa: E501
        :rtype: str
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this EnvelopeDelayRule.

          # noqa: E501

        :param delay: The delay of this EnvelopeDelayRule.  # noqa: E501
        :type: str
        """

        self._delay = delay

    @property
    def resume_date(self):
        """Gets the resume_date of this EnvelopeDelayRule.  # noqa: E501

          # noqa: E501

        :return: The resume_date of this EnvelopeDelayRule.  # noqa: E501
        :rtype: str
        """
        return self._resume_date

    @resume_date.setter
    def resume_date(self, resume_date):
        """Sets the resume_date of this EnvelopeDelayRule.

          # noqa: E501

        :param resume_date: The resume_date of this EnvelopeDelayRule.  # noqa: E501
        :type: str
        """

        self._resume_date = resume_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EnvelopeDelayRule, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnvelopeDelayRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopeDelayRule):
            return True

        return self.to_dict() != other.to_dict()
