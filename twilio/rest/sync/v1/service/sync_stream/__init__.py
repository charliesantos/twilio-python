# coding=utf-8
"""
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
from twilio.rest.sync.v1.service.sync_stream.stream_message import StreamMessageList


class SyncStreamList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid):
        """
        Initialize the SyncStreamList

        :param Version version: Version that contains the resource
        :param service_sid: Service Instance SID.

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamList
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamList
        """
        super(SyncStreamList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid}
        self._uri = '/Services/{service_sid}/Streams'.format(**self._solution)

    def create(self, unique_name=values.unset):
        """
        Create a new SyncStreamInstance

        :param unicode unique_name: Stream unique name.

        :returns: Newly created SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        data = values.of({'UniqueName': unique_name})

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return SyncStreamInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def stream(self, limit=None, page_size=None):
        """
        Streams SyncStreamInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'])

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists SyncStreamInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size})

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return SyncStreamPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of SyncStreamInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return SyncStreamPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a SyncStreamContext

        :param sid: Stream SID or unique name.

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        return SyncStreamContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a SyncStreamContext

        :param sid: Stream SID or unique name.

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        return SyncStreamContext(self._version, service_sid=self._solution['service_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncStreamList>'


class SyncStreamPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the SyncStreamPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: Service Instance SID.

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamPage
        """
        super(SyncStreamPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SyncStreamInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        return SyncStreamInstance(self._version, payload, service_sid=self._solution['service_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Sync.V1.SyncStreamPage>'


class SyncStreamContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, sid):
        """
        Initialize the SyncStreamContext

        :param Version version: Version that contains the resource
        :param service_sid: The service_sid
        :param sid: Stream SID or unique name.

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        super(SyncStreamContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid}
        self._uri = '/Services/{service_sid}/Streams/{sid}'.format(**self._solution)

        # Dependents
        self._stream_messages = None

    def fetch(self):
        """
        Fetch a SyncStreamInstance

        :returns: Fetched SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SyncStreamInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the SyncStreamInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    @property
    def stream_messages(self):
        """
        Access the stream_messages

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        """
        if self._stream_messages is None:
            self._stream_messages = StreamMessageList(
                self._version,
                service_sid=self._solution['service_sid'],
                stream_sid=self._solution['sid'],
            )
        return self._stream_messages

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncStreamContext {}>'.format(context)


class SyncStreamInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, sid=None):
        """
        Initialize the SyncStreamInstance

        :returns: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        super(SyncStreamInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'unique_name': payload['unique_name'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'url': payload['url'],
            'links': payload['links'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'created_by': payload['created_by'],
        }

        # Context
        self._context = None
        self._solution = {'service_sid': service_sid, 'sid': sid or self._properties['sid']}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SyncStreamContext for this SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamContext
        """
        if self._context is None:
            self._context = SyncStreamContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: Stream SID.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def unique_name(self):
        """
        :returns: Stream unique name.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def account_sid(self):
        """
        :returns: Twilio Account SID.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: Service Instance SID.
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def url(self):
        """
        :returns: URL of this Stream.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: Nested resource URLs.
        :rtype: unicode
        """
        return self._properties['links']

    @property
    def date_created(self):
        """
        :returns: The date this Stream was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Stream was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: Identity of the Stream creator.
        :rtype: unicode
        """
        return self._properties['created_by']

    def fetch(self):
        """
        Fetch a SyncStreamInstance

        :returns: Fetched SyncStreamInstance
        :rtype: twilio.rest.sync.v1.service.sync_stream.SyncStreamInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the SyncStreamInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    @property
    def stream_messages(self):
        """
        Access the stream_messages

        :returns: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        :rtype: twilio.rest.sync.v1.service.sync_stream.stream_message.StreamMessageList
        """
        return self._proxy.stream_messages

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Sync.V1.SyncStreamInstance {}>'.format(context)
