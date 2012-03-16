# -*- coding: utf-8 -*-
"""

    pingdom.exception
    ~~~~~~~~

    John Costa, 3/16/2012
    License has been consolidated to LICENSE file in root.

"""

import gzip
import StringIO
import urllib2

try:
    import json as simplejson
except:
    import simplejson


class PingdomError(urllib2.HTTPError):
    def __init__(self, http_error):
        urllib2.HTTPError.__init__(self, http_error.filename, http_error.code,
            http_error.msg, http_error.hdrs, http_error.fp)

        if self.headers.get('content-encoding') == 'gzip':
            data = gzip.GzipFile(
                fileobj=StringIO.StringIO(http_error.read())).read()
        else:
            data = self.read()

        j = simplejson.loads(data)
        error = j['error']
        self.statuscode = error['statuscode']
        self.statusdesc = error['statusdesc']
        self.errormessage = error['errormessage']

    def __repr__(self):
        return 'PingdomError: HTTP %s %s returned with message, "%s"' % \
               (self.statuscode, self.statusdesc, self.errormessage)

    def __str__(self):
        return self.__repr__()
