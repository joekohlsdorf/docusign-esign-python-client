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


class ScheduledSending(object):
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
        'resume_date': 'str',
        'rules': 'list[EnvelopeDelayRule]',
        'status': 'str'
    }

    attribute_map = {
        'resume_date': 'resumeDate',
        'rules': 'rules',
        'status': 'status'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """ScheduledSending - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._resume_date = None
        self._rules = None
        self._status = None
        self.discriminator = None

        setattr(self, "_{}".format('resume_date'), kwargs.get('resume_date', None))
        setattr(self, "_{}".format('rules'), kwargs.get('rules', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))

    @property
    def resume_date(self):
        """Gets the resume_date of this ScheduledSending.  # noqa: E501

          # noqa: E501

        :return: The resume_date of this ScheduledSending.  # noqa: E501
        :rtype: str
        """
        return self._resume_date

    @resume_date.setter
    def resume_date(self, resume_date):
        """Sets the resume_date of this ScheduledSending.

          # noqa: E501

        :param resume_date: The resume_date of this ScheduledSending.  # noqa: E501
        :type: str
        """

        self._resume_date = resume_date

    @property
    def rules(self):
        """Gets the rules of this ScheduledSending.  # noqa: E501

          # noqa: E501

        :return: The rules of this ScheduledSending.  # noqa: E501
        :rtype: list[EnvelopeDelayRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this ScheduledSending.

          # noqa: E501

        :param rules: The rules of this ScheduledSending.  # noqa: E501
        :type: list[EnvelopeDelayRule]
        """

        self._rules = rules

    @property
    def status(self):
        """Gets the status of this ScheduledSending.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this ScheduledSending.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ScheduledSending.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this ScheduledSending.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(ScheduledSending, dict):
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
        if not isinstance(other, ScheduledSending):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScheduledSending):
            return True

        return self.to_dict() != other.to_dict()
