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


class LinkedExternalPrimaryAccount(object):
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
        'account_name': 'str',
        'configuration_id': 'str',
        'email': 'str',
        'link_id': 'str',
        'pdf_field_handling_option': 'str',
        'recipient_auth_requirements': 'ExternalPrimaryAccountRecipientAuthRequirements',
        'status': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'account_name': 'accountName',
        'configuration_id': 'configurationId',
        'email': 'email',
        'link_id': 'linkId',
        'pdf_field_handling_option': 'pdfFieldHandlingOption',
        'recipient_auth_requirements': 'recipientAuthRequirements',
        'status': 'status',
        'user_id': 'userId'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """LinkedExternalPrimaryAccount - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_name = None
        self._configuration_id = None
        self._email = None
        self._link_id = None
        self._pdf_field_handling_option = None
        self._recipient_auth_requirements = None
        self._status = None
        self._user_id = None
        self.discriminator = None

        setattr(self, "_{}".format('account_name'), kwargs.get('account_name', None))
        setattr(self, "_{}".format('configuration_id'), kwargs.get('configuration_id', None))
        setattr(self, "_{}".format('email'), kwargs.get('email', None))
        setattr(self, "_{}".format('link_id'), kwargs.get('link_id', None))
        setattr(self, "_{}".format('pdf_field_handling_option'), kwargs.get('pdf_field_handling_option', None))
        setattr(self, "_{}".format('recipient_auth_requirements'), kwargs.get('recipient_auth_requirements', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('user_id'), kwargs.get('user_id', None))

    @property
    def account_name(self):
        """Gets the account_name of this LinkedExternalPrimaryAccount.  # noqa: E501

          # noqa: E501

        :return: The account_name of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this LinkedExternalPrimaryAccount.

          # noqa: E501

        :param account_name: The account_name of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def configuration_id(self):
        """Gets the configuration_id of this LinkedExternalPrimaryAccount.  # noqa: E501

          # noqa: E501

        :return: The configuration_id of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._configuration_id

    @configuration_id.setter
    def configuration_id(self, configuration_id):
        """Sets the configuration_id of this LinkedExternalPrimaryAccount.

          # noqa: E501

        :param configuration_id: The configuration_id of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._configuration_id = configuration_id

    @property
    def email(self):
        """Gets the email of this LinkedExternalPrimaryAccount.  # noqa: E501

          # noqa: E501

        :return: The email of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this LinkedExternalPrimaryAccount.

          # noqa: E501

        :param email: The email of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def link_id(self):
        """Gets the link_id of this LinkedExternalPrimaryAccount.  # noqa: E501

          # noqa: E501

        :return: The link_id of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._link_id

    @link_id.setter
    def link_id(self, link_id):
        """Sets the link_id of this LinkedExternalPrimaryAccount.

          # noqa: E501

        :param link_id: The link_id of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._link_id = link_id

    @property
    def pdf_field_handling_option(self):
        """Gets the pdf_field_handling_option of this LinkedExternalPrimaryAccount.  # noqa: E501

          # noqa: E501

        :return: The pdf_field_handling_option of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._pdf_field_handling_option

    @pdf_field_handling_option.setter
    def pdf_field_handling_option(self, pdf_field_handling_option):
        """Sets the pdf_field_handling_option of this LinkedExternalPrimaryAccount.

          # noqa: E501

        :param pdf_field_handling_option: The pdf_field_handling_option of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._pdf_field_handling_option = pdf_field_handling_option

    @property
    def recipient_auth_requirements(self):
        """Gets the recipient_auth_requirements of this LinkedExternalPrimaryAccount.  # noqa: E501


        :return: The recipient_auth_requirements of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: ExternalPrimaryAccountRecipientAuthRequirements
        """
        return self._recipient_auth_requirements

    @recipient_auth_requirements.setter
    def recipient_auth_requirements(self, recipient_auth_requirements):
        """Sets the recipient_auth_requirements of this LinkedExternalPrimaryAccount.


        :param recipient_auth_requirements: The recipient_auth_requirements of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: ExternalPrimaryAccountRecipientAuthRequirements
        """

        self._recipient_auth_requirements = recipient_auth_requirements

    @property
    def status(self):
        """Gets the status of this LinkedExternalPrimaryAccount.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LinkedExternalPrimaryAccount.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def user_id(self):
        """Gets the user_id of this LinkedExternalPrimaryAccount.  # noqa: E501

          # noqa: E501

        :return: The user_id of this LinkedExternalPrimaryAccount.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this LinkedExternalPrimaryAccount.

          # noqa: E501

        :param user_id: The user_id of this LinkedExternalPrimaryAccount.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(LinkedExternalPrimaryAccount, dict):
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
        if not isinstance(other, LinkedExternalPrimaryAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LinkedExternalPrimaryAccount):
            return True

        return self.to_dict() != other.to_dict()
