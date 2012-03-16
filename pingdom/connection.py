# -*- coding: utf-8 -*-
"""

    pingdom.connection
    ~~~~~~~~

    John Costa, 3/16/2012
    License has been consolidated to LICENSE file in root.

"""

import logging

try:
    import json
except:
    import simplejson as json
import requests
from requests.auth import HTTPBasicAuth

from pingdom.resources import PingdomCheck
from pingdom.resources import PingdomContact
from pingdom.exception import PingdomError

BASE_URL = 'https://api.pingdom.com/api/'
BASE_VERSION = '2.0'
log = logging.getLogger(__name__)


class PingdomRequest(object):

    def _method(self, method, post_data):
        """ Returns a method used on Request

            defaults to `post` if post_data, `get` otherwise
        """
        if post_data:
            if not method:
                method = 'post'
        else:
            if not method:
                method = 'get'
        return method.lower()

    def __init__(self, connection, resource, post_data=None, method=None,
                 enable_gzip=True):
        """Representation of a Pingdom API HTTP request.

        :type connection: :class:`PingdomConnection`
        :param connection: Pingdom connection object populated with a username,
            password and base URL

        :type resource: string
        :param resource: Pingdom resource to query (in all lowercase)

        :type post_data: dict
        :param post_data: Data to be sent with a POST request

        :type method: string
        :param method: HTTP verb (GET, POST, DELETE, etc.) to use (defaults to
            GET or POST, depending on the presence of post_data)

        :type enable_gzip: bool
        :param enable_gzip: Whether or not to gzip the request (thus telling
            Pingdom to gzip the response)
        """
        self.url = connection.base_url + '/' + resource
        self.post_data = post_data
        self.method = self._method(method, post_data)
        self.auth = HTTPBasicAuth(connection.username, connection.password)
        self.headers = {'App-Key': connection.apikey}

        # TODO ensure this still works
#        # Enable gzip
#        if enable_gzip:
#            self.add_header('Accept-Encoding', 'gzip')

    def __repr__(self):
        return 'PingdomRequest:\n\t{0!r}\n\t{1!r}\n\t{2!r}' % \
               (self.url, self.method, self.auth)

    def fetch(self):
        """Execute the request."""
        try:
            msg = "`url`={0!r}\n`data`={1!r}".format(self.url, self.post_data)
            log.debug(msg)
            response = getattr(requests, self.method)(url=self.url,
                data=self.post_data, auth=self.auth, headers=self.headers)
        except requests.exceptions.RequestException, e:
            raise PingdomError(e)
        return PingdomResponse(response)


class PingdomResponse(object):
    def __init__(self, response):
        """Representation of a Pingdom API HTTP response."""

        self.headers = response.headers
        self.content = json.loads(response.content)

        if response.status_code >= 300:
            raise PingdomError(response)

    def __repr__(self):
        return 'PingdomResponse: %s' % self.content.keys()


class PingdomConnection(object):
    def __init__(self, username, password, apikey='',
                 base_url=BASE_URL + BASE_VERSION):
        """Interface to the Pingdom API."""

        self.username = username
        self.password = password
        self.apikey = apikey
        self.base_url = base_url

    def __repr__(self):
        return "Connection:%s" % self.base_url

    def list_checks(self):
        """List all Pingdom check names"""
        pingdom_checks = self.get_all_checks()
        check_list = [i.name for i in pingdom_checks]
        return check_list

    def get_all_checks(self, check_names=None, check_excludes=None):
        """Get a list of Pingdom checks, optionally filtered by check name"""
        if check_excludes is None:
            check_excludes = []

        response = PingdomRequest(self, 'checks').fetch()
        result = response.content

        pingdom_checks = []
        if check_names:
            for check_name in check_names:
                pingdom_checks += [PingdomCheck(r) for r in result['checks']
                                   if r['name'] == check_name]
        else:
            pingdom_checks += [PingdomCheck(r) for r in result['checks']
                                if r['name'] not in check_excludes]

        return pingdom_checks

    def get_check(self, check_id):
        """Get a Pingdom check by ID"""
        response = PingdomRequest(self, 'checks/%s' % check_id).fetch()
        pingdom_check = PingdomCheck(response.content['check'])
        return pingdom_check

    def get_raw_check_results(self, check_id, from_time=0, limit=100):
        """Get raw check results for a specific check by ID and limit"""
        rs = 'results/%s?from=%s&limit=%s' % (check_id, from_time, limit)
        response = PingdomRequest(self, rs).fetch()
        return response.content['results']

    def create_check(self, name, host, check_type, **kwargs):
        """Create a Pingdom check"""
        post_data = {'name': name,
                     'host': host,
                     'type': check_type}
        for key in kwargs:
            post_data[key] = kwargs[key]

        try:
            resp = PingdomRequest(self, 'checks', post_data=post_data).fetch()
        except PingdomError, e:
            logging.error(e)
        else:
            return PingdomCheck(resp.content['check'])

    def modify_check(self, check_id, **kwargs):
        """Modify a Pingdom check by ID"""
        post_data = {}
        for key in kwargs:
            post_data[key] = kwargs[key]

        try:
            rs = 'checks/%s' % check_id
            response = PingdomRequest(self, rs, post_data=post_data,
                method='PUT').fetch()
        except PingdomError, e:
            logging.error(e)
        else:
            return response.content['message']

    def delete_check(self, check_id):
        """Delete a Pingdom check by ID"""
        rs = 'checks/%s' % check_id
        response = PingdomRequest(self, rs, method='DELETE').fetch()
        return response.content

    def get_all_contacts(self):
        """Get a list of Pingdom contacts"""
        response = PingdomRequest(self, 'contacts').fetch()
        result = response.content

        contacts = [PingdomContact(r) for r in result['contacts']]
        return contacts

    def get_summary_average(self, check_id, from_time=0, to_time=0,
                            include_uptime='true'):
        """Get a summarized response time / uptime value
            for a specified check and time period."""
        rs = 'summary.average/%s?from=%s&to=%s&includeuptime=%s' % \
           (check_id, from_time, to_time, include_uptime)
        response = PingdomRequest(self, rs).fetch()
        return response.content['summary']
