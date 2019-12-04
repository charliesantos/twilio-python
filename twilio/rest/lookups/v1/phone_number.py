# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class PhoneNumberList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the PhoneNumberList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberList
        """
        super(PhoneNumberList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, phone_number):
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number to fetch in E.164 format

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number, )

    def __call__(self, phone_number):
        """
        Constructs a PhoneNumberContext

        :param phone_number: The phone number to fetch in E.164 format

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        return PhoneNumberContext(self._version, phone_number=phone_number, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V1.PhoneNumberList>'


class PhoneNumberPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the PhoneNumberPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberPage
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberPage
        """
        super(PhoneNumberPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of PhoneNumberInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        return PhoneNumberInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Lookups.V1.PhoneNumberPage>'


class PhoneNumberContext(InstanceContext):
    """  """

    def __init__(self, version, phone_number):
        """
        Initialize the PhoneNumberContext

        :param Version version: Version that contains the resource
        :param phone_number: The phone number to fetch in E.164 format

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        super(PhoneNumberContext, self).__init__(version)

        # Path Solution
        self._solution = {'phone_number': phone_number, }
        self._uri = '/PhoneNumbers/{phone_number}'.format(**self._solution)

    def fetch(self, country_code=values.unset, type=values.unset,
              add_ons=values.unset, add_ons_data=values.unset):
        """
        Fetch the PhoneNumberInstance

        :param unicode country_code: The ISO country code of the phone number
        :param unicode type: The type of information to return
        :param unicode add_ons: The unique_name of an Add-on you would like to invoke
        :param dict add_ons_data: Data specific to the add-on you would like to invoke

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        data = values.of({
            'CountryCode': country_code,
            'Type': serialize.map(type, lambda e: e),
            'AddOns': serialize.map(add_ons, lambda e: e),
        })
        data.update(serialize.prefixed_collapsible_map(add_ons_data, 'AddOns'))

        payload = self._version.fetch(method='GET', uri=self._uri, params=data, )

        return PhoneNumberInstance(self._version, payload, phone_number=self._solution['phone_number'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V1.PhoneNumberContext {}>'.format(context)


class PhoneNumberInstance(InstanceResource):
    """  """

    class Type(object):
        LANDLINE = "landline"
        MOBILE = "mobile"
        VOIP = "voip"

    def __init__(self, version, payload, phone_number=None):
        """
        Initialize the PhoneNumberInstance

        :returns: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        super(PhoneNumberInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'caller_name': payload.get('caller_name'),
            'country_code': payload.get('country_code'),
            'phone_number': payload.get('phone_number'),
            'national_format': payload.get('national_format'),
            'carrier': payload.get('carrier'),
            'add_ons': payload.get('add_ons'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'phone_number': phone_number or self._properties['phone_number'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: PhoneNumberContext for this PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberContext
        """
        if self._context is None:
            self._context = PhoneNumberContext(self._version, phone_number=self._solution['phone_number'], )
        return self._context

    @property
    def caller_name(self):
        """
        :returns: The name of the phone number's owner
        :rtype: dict
        """
        return self._properties['caller_name']

    @property
    def country_code(self):
        """
        :returns: The ISO country code for the phone number
        :rtype: unicode
        """
        return self._properties['country_code']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def national_format(self):
        """
        :returns: The phone number, in national format
        :rtype: unicode
        """
        return self._properties['national_format']

    @property
    def carrier(self):
        """
        :returns: The telecom company that provides the phone number
        :rtype: dict
        """
        return self._properties['carrier']

    @property
    def add_ons(self):
        """
        :returns: A JSON string with the results of the Add-ons you specified
        :rtype: dict
        """
        return self._properties['add_ons']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, country_code=values.unset, type=values.unset,
              add_ons=values.unset, add_ons_data=values.unset):
        """
        Fetch the PhoneNumberInstance

        :param unicode country_code: The ISO country code of the phone number
        :param unicode type: The type of information to return
        :param unicode add_ons: The unique_name of an Add-on you would like to invoke
        :param dict add_ons_data: Data specific to the add-on you would like to invoke

        :returns: The fetched PhoneNumberInstance
        :rtype: twilio.rest.lookups.v1.phone_number.PhoneNumberInstance
        """
        return self._proxy.fetch(
            country_code=country_code,
            type=type,
            add_ons=add_ons,
            add_ons_data=add_ons_data,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Lookups.V1.PhoneNumberInstance {}>'.format(context)
