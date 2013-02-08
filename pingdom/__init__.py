# -*- coding: utf-8 -*-
"""

    pingdom.__init__
    ~~~~~~~~

    John Costa, 3/16/2012
    License has been consolidated to LICENSE file in root.

"""

__author__ = 'Mike Babineau <mikeb@ea2d.com>'
__copyright__ = "Copyright 2011 Electronic Arts Inc."
__license__ = "Apache v2.0"

from pingdom.connection import (PingdomRequest, PingdomResponse,
                                 PingdomConnection)
from pingdom.exception import PingdomError
from pingdom.resources import PingdomCheck, PingdomContact
