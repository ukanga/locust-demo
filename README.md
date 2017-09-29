Simple Locust Demo for PyConKE 2017
===================================

Requirements
------------

```
$ virtualenv .locust_venv
$ source .locust_venv/bin/activate
$ pip install -r requirements.txt
```

Run locust
----------

```
$ locust -f crunch_user.py -H http://crunch.goodbot.ai
```

Run locust distributed
----------------------

```
# master
$ locust -f crunch_user.py -H http://crunch.goodbot.ai --master

# slave
$ locust -f crunch_user.py -H http://crunch.goodbot.ai --slave
```
