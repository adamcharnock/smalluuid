smalluuid
===========================================================

.. image:: https://badge.fury.io/py/smalluuid.png
    :target: https://badge.fury.io/py/smalluuid

.. image:: https://pypip.in/d/smalluuid/badge.png
    :target: https://pypi.python.org/pypi/smalluuid

Installation
------------

Installation using pip::

    pip install smalluuid

Basic Usage
-----------

A drop-in replacement for Python's UUID class which – by default – 
represents UUIDs as 22 character base64-encoded values. 

```python
>>> from smalluuid import SmallUUID
>>> uuid = SmallUUID()
>>> uuid
SmallUUID('IBNApQOzTHGzdjkSt6t-Jg')
>>> SmallUUID().hex
'44a30f95b86f429f83c5669fed1998ab'
>>> uuid.hex_grouped
'201340a5-03b3-4c71-b376-3912b7ab7e26'
>>> SmallUUID('IBNApQOzTHGzdjkSt6t-Jg')
SmallUUID('IBNApQOzTHGzdjkSt6t-Jg')
>>> SmallUUID(hex='44a30f95b86f429f83c5669fed1998ab')
SmallUUID('RKMPlbhvQp-DxWaf7RmYqw')
```

Notable differences from Python's UUID implementation:

* Instantiating without a value will assign a random value of the given version (default: 4) 
  rather than raise an exception.

Typed UUID Usage
----------------

An extension of ``SmallUUID`` is available in the form of ``TypedSmallUUID``:

```python
>>> from smalluuid import TypedSmallUUID
>>> uuid = TypedSmallUUID(type=42)
>>> uuid
TypedSmallUUID('qHHvXuUwT6y7t7dnsiksvg')
>>> uuid.type
42
>>> TypedSmallUUID('qHHvXuUwT6y7t7dnsiksvg').type
42
```

The use case here is that of having UUIDs from which one can determine 
both an object's ID and the object's type/table/model.

Credits
-------

*Any credits here*

This project borrowed a little code and inspiration from 
[shortuuid](https://github.com/stochastic-technologies/shortuuid).

``smalluuid`` is packaged using seed_.

.. _seed: https://github.com/adamcharnock/seed/

