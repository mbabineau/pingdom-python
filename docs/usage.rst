-------------
Library Usage
-------------
Set up a Pingdom connection:

    >>> import pingdom
    >>> c = pingdom.PingdomConnection(PINGDOM_USERNAME, PINGDOM_PASSWORD, API_KEY)  # Same credentials you use for the Pingdom website

Create a new Pingdom check:


    >>> # The wrong way:
    >>> c.create_check('EA2D Website', 'http://ea2d.com', 'http')
    ERROR:root:PingdomError: HTTP 400 Bad Request returned with message, "Invalid parameter value: host"
    >>> # The right way:
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

Get the raw results for the last 5 checks by check ID:

    >>> raw_results = c.get_raw_check_results(check.id, 5)
    >>> for r in raw_results:
    ...     print r
    ...
    {u'status': u'up', u'statusdesclong': u'OK', u'probeid': 43, u'responsetime': 344, u'time': 1311110541, u'statusdesc': u'OK'}
    {u'status': u'up', u'statusdesclong': u'OK', u'probeid': 44, u'responsetime': 437, u'time': 1311110482, u'statusdesc': u'OK'}
    {u'status': u'up', u'statusdesclong': u'OK', u'probeid': 46, u'responsetime': 599, u'time': 1311110421, u'statusdesc': u'OK'}
    {u'status': u'up', u'statusdesclong': u'OK', u'probeid': 53, u'responsetime': 775, u'time': 1311110361, u'statusdesc': u'OK'}
    {u'status': u'up', u'statusdesclong': u'OK', u'probeid': 47, u'responsetime': 765, u'time': 1311110301, u'statusdesc': u'OK'}


Modify a Pingdom check:

    >>> c.modify_check(210702, paused=True)  # Pause the check
    u'Modification of check was successful!'
    >>> check = c.get_check(210702)
    >>> check.status
    u'paused'

Delete a Pingdom check:

    >>> c.delete_check(302632)
    {u'message': u'Deletion of check was successful!'}