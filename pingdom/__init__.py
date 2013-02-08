# -*- coding: utf-8 -*-
"""

    pingdom.__init__

"""

__author__ = 'Mike Babineau <michael.babineau@gmail.com>'
__copyright__ = "Copyright 2011 Electronic Arts Inc."
__license__ = "Apache v2.0"

from pingdom.connection import (PingdomRequest, PingdomResponse,
                                 PingdomConnection)
from pingdom.exception import PingdomError
from pingdom.resources import PingdomCheck, PingdomContact
