# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CpsList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CpsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.cps.CpsList
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsList
        """
        super(CpsList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a CpsContext

        :returns: twilio.rest.preview.trusted_comms.cps.CpsContext
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsContext
        """
        return CpsContext(self._version, )

    def __call__(self):
        """
        Constructs a CpsContext

        :returns: twilio.rest.preview.trusted_comms.cps.CpsContext
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsContext
        """
        return CpsContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.CpsList>'


class CpsPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CpsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.trusted_comms.cps.CpsPage
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsPage
        """
        super(CpsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CpsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.trusted_comms.cps.CpsInstance
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsInstance
        """
        return CpsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.TrustedComms.CpsPage>'


class CpsContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CpsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.trusted_comms.cps.CpsContext
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsContext
        """
        super(CpsContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/CPS'.format(**self._solution)

    def fetch(self):
        """
        Fetch the CpsInstance

        :returns: The fetched CpsInstance
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CpsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.CpsContext {}>'.format(context)


class CpsInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the CpsInstance

        :returns: twilio.rest.preview.trusted_comms.cps.CpsInstance
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsInstance
        """
        super(CpsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'cps_url': payload.get('cps_url'),
            'phone_number': payload.get('phone_number'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CpsContext for this CpsInstance
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsContext
        """
        if self._context is None:
            self._context = CpsContext(self._version, )
        return self._context

    @property
    def cps_url(self):
        """
        :returns: CPS URL of the phone number.
        :rtype: unicode
        """
        return self._properties['cps_url']

    @property
    def phone_number(self):
        """
        :returns: Phone number passed.
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the CpsInstance

        :returns: The fetched CpsInstance
        :rtype: twilio.rest.preview.trusted_comms.cps.CpsInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.TrustedComms.CpsInstance {}>'.format(context)
