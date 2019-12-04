# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class AssetVersionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, asset_sid):
        """
        Initialize the AssetVersionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the AssetVersion resource is associated with
        :param asset_sid: The SID of the Asset resource that is the parent of the asset version

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionList
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionList
        """
        super(AssetVersionList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'asset_sid': asset_sid, }
        self._uri = '/Services/{service_sid}/Assets/{asset_sid}/Versions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams AssetVersionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists AssetVersionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return AssetVersionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of AssetVersionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return AssetVersionPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a AssetVersionContext

        :param sid: The SID that identifies the AssetVersion resource to fetch

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        return AssetVersionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            asset_sid=self._solution['asset_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a AssetVersionContext

        :param sid: The SID that identifies the AssetVersion resource to fetch

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        return AssetVersionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            asset_sid=self._solution['asset_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.AssetVersionList>'


class AssetVersionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the AssetVersionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the AssetVersion resource is associated with
        :param asset_sid: The SID of the Asset resource that is the parent of the asset version

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionPage
        """
        super(AssetVersionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AssetVersionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        return AssetVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            asset_sid=self._solution['asset_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.AssetVersionPage>'


class AssetVersionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, asset_sid, sid):
        """
        Initialize the AssetVersionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the AssetVersion resource from
        :param asset_sid: The SID of the Asset resource that is the parent of the AssetVersion resource to fetch
        :param sid: The SID that identifies the AssetVersion resource to fetch

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        super(AssetVersionContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'asset_sid': asset_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Assets/{asset_sid}/Versions/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the AssetVersionInstance

        :returns: The fetched AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return AssetVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            asset_sid=self._solution['asset_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.AssetVersionContext {}>'.format(context)


class AssetVersionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Visibility(object):
        PUBLIC = "public"
        PRIVATE = "private"
        PROTECTED = "protected"

    def __init__(self, version, payload, service_sid, asset_sid, sid=None):
        """
        Initialize the AssetVersionInstance

        :returns: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        super(AssetVersionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'asset_sid': payload.get('asset_sid'),
            'path': payload.get('path'),
            'visibility': payload.get('visibility'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'asset_sid': asset_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: AssetVersionContext for this AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionContext
        """
        if self._context is None:
            self._context = AssetVersionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                asset_sid=self._solution['asset_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the AssetVersion resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the AssetVersion resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the AssetVersion resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def asset_sid(self):
        """
        :returns: The SID of the Asset resource that is the parent of the asset version
        :rtype: unicode
        """
        return self._properties['asset_sid']

    @property
    def path(self):
        """
        :returns: The URL-friendly string by which the asset version can be referenced
        :rtype: unicode
        """
        return self._properties['path']

    @property
    def visibility(self):
        """
        :returns: The access control that determines how the asset version can be accessed
        :rtype: AssetVersionInstance.Visibility
        """
        return self._properties['visibility']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the AssetVersion resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def url(self):
        """
        :returns: The absolute URL of the AssetVersion resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the AssetVersionInstance

        :returns: The fetched AssetVersionInstance
        :rtype: twilio.rest.serverless.v1.service.asset.asset_version.AssetVersionInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.AssetVersionInstance {}>'.format(context)
