# -*- coding: utf-8 -*-
"""

    pingdom.resources
    ~~~~~~~~

    John Costa, 3/16/2012
    License has been consolidated to LICENSE file in root.

"""


class PingdomCheck(object):
    def __init__(self, attributes):
        for attr in attributes.keys():
            setattr(self, attr, attributes[attr])

    def __repr__(self):
        return "Check:%s" % self.name

    def __eq__(self, other):
        return self.id == other.id


class PingdomContact(object):
    def __init__(self, attributes):
        for attr in attributes.keys():
            setattr(self, attr, attributes[attr])

    def __repr__(self):
        return "Contact:%s" % self.name
