# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DeviceList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the DeviceList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.device.DeviceList
        :rtype: twilio.rest.preview.trusted_comms.device.DeviceList
        """
        super(DeviceList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Devices'.format(**self._solution)

    def create(self, phone_number, push_token):
        """
        Create the DeviceInstance

        :param unicode phone_number: The end user Phone Number
        :param unicode push_token: The Push Token for this Phone Number

        :returns: The created DeviceInstance
        :rtype: twilio.rest.preview.trusted_comms.device.DeviceInstance
        """
        data = values.of({'PhoneNumber': phone_number, 'PushToken': push_token, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return DeviceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.DeviceList>'


class DevicePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the DevicePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.device.DevicePage
        :rtype: twilio.rest.preview.trusted_comms.device.DevicePage
        """
        super(DevicePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeviceInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.device.DeviceInstance
        :rtype: twilio.rest.preview.trusted_comms.device.DeviceInstance
        """
        return DeviceInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.DevicePage>'


class DeviceInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the DeviceInstance

        :returns: twilio.rest.preview.trusted_comms.device.DeviceInstance
        :rtype: twilio.rest.preview.trusted_comms.device.DeviceInstance
        """
        super(DeviceInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'binding_sid': payload.get('binding_sid'),
            'phone_number': payload.get('phone_number'),
            'sid': payload.get('sid'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def binding_sid(self):
        """
        :returns: Binding Sid.
        :rtype: unicode
        """
        return self._properties['binding_sid']

    @property
    def phone_number(self):
        """
        :returns: The end user Phone Number
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Device.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.DeviceInstance>'
