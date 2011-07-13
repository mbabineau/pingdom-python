pingdom-python
=====================
3rd-party Python library for [Pingdom](http://pingdom.com)'s new REST API.  Note that this API is still in beta, so may change at any time.  For more information about the API, see Pingdom's blog [post](http://royal.pingdom.com/2011/03/22/new-pingdom-api-enters-public-beta/).

Currently, the library supports:

* Checks (create, delete, get, list)

Love writing code? [EA2D](http://ea2d.com) is [hiring](http://ea2d.com/jobs/)!


Requirements
--------------------
- Pingdom account
- simplejson (Python 2.5 and earlier)


Installation
--------------------
Install using the provided `setup.py`:

    sudo setup.py install

Or install from PyPI:

    sudo easy_install pingdom


Library Usage
--------------------
Set up a Pingdom connection:
    
    >>> import pingdom
    >>> c = pingdom.PingdomConnection(PINGDOM_USERNAME, PINGDOM_PASSWORD, API_KEY)  # Same credentials you use for the Pingdom website
        
Create a new Pingdom check:

    # The wrong way:
    >>> c.create_check('EA2D Website', 'http://ea2d.com', 'http')
    ERROR:root:PingdomError: HTTP 400 Bad Request returned with message, "Invalid parameter value: host"
    # The right way:
    >>> c.create_check('EA2D Website', 'ea2d.com', 'http')
    Check:EA2D Website
    
Get basic information about a Pingdom check:

    >>> check = c.get_all_checks(['EA2D Website'])[0]   # Expects a list, returns a list
    >>> dir(check)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'id', 'lasterrortime', 'lastresponsetime', 'lasttesttime', 'name', 'status', 'type']
    >>> check.id
    302632
    >>> check.status
    u'up'

Get more detailed information about a Pingdom check:

    >>> check = c.get_check(210702)  # Look up by check ID
    >>> dir(check)
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'contactids', 'created', 'hostname', 'id', 'lasterrortime', 'lasttesttime', 'name', 'notifyagainevery', 'notifywhenbackup', 'resolution', 'sendnotificationwhendown', 'sendtoemail', 'sendtoiphone', 'sendtosms', 'sendtotwitter', 'status', 'type']
    >>> check.lasterrortime
    1289482981

Modify a Pingdom check:

    >>> c.modify_check(210702, paused=True)  # Pause the check
    u'Modification of check was successful!'
    >>> check = c.get_check(210702)
    >>> check.status
    u'paused'

Delete a Pingdom check:

    >>> c.delete_check(302632)
    {u'message': u'Deletion of check was successful!'}


Contributing
--------------------
Use GitHub's standard fork/commit/pull-request cycle.  If you have any questions, email <ops@ea2d.com>.

Contributors
--------------------
Awesome people who have fixed bugs, added features, or otherwise improved the project:

* David King ([ketralnis](https://github.com/ketralnis))
* John Walsh ([walsh159](https://github.com/walsh159))


License
--------------------

    Copyright 2011 Electronic Arts Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
