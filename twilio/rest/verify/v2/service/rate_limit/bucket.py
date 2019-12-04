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


class BucketList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, rate_limit_sid):
        """
        Initialize the BucketList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with
        :param rate_limit_sid: Rate Limit Sid.

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketList
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketList
        """
        super(BucketList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'rate_limit_sid': rate_limit_sid, }
        self._uri = '/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets'.format(**self._solution)

    def create(self, max, interval):
        """
        Create the BucketInstance

        :param unicode max: Max number of requests.
        :param unicode interval: Number of seconds that the rate limit will be enforced over.

        :returns: The created BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        data = values.of({'Max': max, 'Interval': interval, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            rate_limit_sid=self._solution['rate_limit_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams BucketInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists BucketInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of BucketInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return BucketPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of BucketInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return BucketPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a BucketContext

        :param sid: A string that uniquely identifies this Bucket.

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        """
        return BucketContext(
            self._version,
            service_sid=self._solution['service_sid'],
            rate_limit_sid=self._solution['rate_limit_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a BucketContext

        :param sid: A string that uniquely identifies this Bucket.

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        """
        return BucketContext(
            self._version,
            service_sid=self._solution['service_sid'],
            rate_limit_sid=self._solution['rate_limit_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.BucketList>'


class BucketPage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the BucketPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the resource is associated with
        :param rate_limit_sid: Rate Limit Sid.

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketPage
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketPage
        """
        super(BucketPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of BucketInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            rate_limit_sid=self._solution['rate_limit_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Verify.V2.BucketPage>'


class BucketContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, service_sid, rate_limit_sid, sid):
        """
        Initialize the BucketContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the resource is associated with
        :param rate_limit_sid: Rate Limit Sid.
        :param sid: A string that uniquely identifies this Bucket.

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        """
        super(BucketContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'rate_limit_sid': rate_limit_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/RateLimits/{rate_limit_sid}/Buckets/{sid}'.format(**self._solution)

    def update(self, max=values.unset, interval=values.unset):
        """
        Update the BucketInstance

        :param unicode max: Max number of requests.
        :param unicode interval: Number of seconds that the rate limit will be enforced over.

        :returns: The updated BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        data = values.of({'Max': max, 'Interval': interval, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            rate_limit_sid=self._solution['rate_limit_sid'],
            sid=self._solution['sid'],
        )

    def fetch(self):
        """
        Fetch the BucketInstance

        :returns: The fetched BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return BucketInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            rate_limit_sid=self._solution['rate_limit_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the BucketInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.BucketContext {}>'.format(context)


class BucketInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, payload, service_sid, rate_limit_sid, sid=None):
        """
        Initialize the BucketInstance

        :returns: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        super(BucketInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'rate_limit_sid': payload.get('rate_limit_sid'),
            'service_sid': payload.get('service_sid'),
            'account_sid': payload.get('account_sid'),
            'max': deserialize.integer(payload.get('max')),
            'interval': deserialize.integer(payload.get('interval')),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'rate_limit_sid': rate_limit_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: BucketContext for this BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketContext
        """
        if self._context is None:
            self._context = BucketContext(
                self._version,
                service_sid=self._solution['service_sid'],
                rate_limit_sid=self._solution['rate_limit_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Bucket.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def rate_limit_sid(self):
        """
        :returns: Rate Limit Sid.
        :rtype: unicode
        """
        return self._properties['rate_limit_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def max(self):
        """
        :returns: Max number of requests.
        :rtype: unicode
        """
        return self._properties['max']

    @property
    def interval(self):
        """
        :returns: Number of seconds that the rate limit will be enforced over.
        :rtype: unicode
        """
        return self._properties['interval']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The URL of this resource.
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, max=values.unset, interval=values.unset):
        """
        Update the BucketInstance

        :param unicode max: Max number of requests.
        :param unicode interval: Number of seconds that the rate limit will be enforced over.

        :returns: The updated BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        return self._proxy.update(max=max, interval=interval, )

    def fetch(self):
        """
        Fetch the BucketInstance

        :returns: The fetched BucketInstance
        :rtype: twilio.rest.verify.v2.service.rate_limit.bucket.BucketInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the BucketInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Verify.V2.BucketInstance {}>'.format(context)
