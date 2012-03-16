# -*- coding: utf-8 -*-
"""

    pingdom.exception
    ~~~~~~~~

    John Costa, 3/16/2012
    License has been consolidated to LICENSE file in root.

"""
from urllib2 import HTTPError

try:
    import json
except:
    import simplejson as json

import logging
log = logging.getLogger(__name__)

class PingdomError(Exception):

    def __init__(self, http_response):
        """
        """
        content = json.loads(http_response.content)
        self.status_code = http_response.status_code
        self.status_desc = content['error']['statusdesc']
        self.error_message  = content['error']['errormessage']
        super(PingdomError, self).__init__(self.__str__() )

    def __repr__(self):
        return 'PingdomError: HTTP `%s - %s` returned with message, "%s"' % \
               (self.status_code, self.status_desc, self.error_message)

    def __str__(self):
        return self.__repr__()
