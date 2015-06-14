smalluuid
=========

.. image:: https://img.shields.io/pypi/v/smalluuid.svg
    :target: https://pypi.python.org/pypi/smalluuid/

.. image:: https://img.shields.io/pypi/dm/smalluuid.svg
    :target: https://pypi.python.org/pypi/smalluuid/

.. image:: https://img.shields.io/github/license/adamcharnock/smalluuid.svg
    :target: https://pypi.python.org/pypi/smalluuid/

.. image:: https://img.shields.io/travis/adamcharnock/smalluuid.svg
    :target: https://travis-ci.org/adamcharnock/smalluuid/

.. image:: https://coveralls.io/repos/adamcharnock/smalluuid/badge.svg
    :target: https://coveralls.io/r/adamcharnock/smalluuid/


Installation
------------

Installation using pip::

    pip install smalluuid

**Do you use Django?** See django-smalluuid_.

Basic Usage
-----------

A drop-in replacement for Python's UUID class which – by default – 
represents UUIDs as 22 character base64-encoded values. 

.. code-block:: python

    >>> from smalluuid import SmallUUID
    >>> uuid = SmallUUID()
    
    # Displays as short UUID by default
    >>> uuid
    SmallUUID('IBNApQOzTHGzdjkSt6t-Jg')
    >>> print(uuid)
    IBNApQOzTHGzdjkSt6t-Jg
    
    # Hex output still available
    >>> SmallUUID().hex
    '44a30f95b86f429f83c5669fed1998ab'
    >>> uuid.hex_grouped
    '201340a5-03b3-4c71-b376-3912b7ab7e26'
    
    # Will initialise from short UUID
    >>> SmallUUID('IBNApQOzTHGzdjkSt6t-Jg')
    SmallUUID('IBNApQOzTHGzdjkSt6t-Jg')
    
    # Will load as a hex value
    >>> SmallUUID(hex='201340a5-03b3-4c71-b376-3912b7ab7e26')
    SmallUUID('RKMPlbhvQp-DxWaf7RmYqw')

Notable differences from Python's UUID implementation:

* Short-form UUIDs accepted as first parameter to ``__init__``
* Instantiating without a value will assign a random value of the given version (default: 4) 
  rather than raise an exception.
* Addition of ``hex_grouped`` property to provide access to grouped hex style UUIDs, formally 
  provided by ``__str__``.


Typed UUID Usage
----------------

An extension of ``SmallUUID`` is available in the form of ``TypedSmallUUID``:

.. code-block:: python

    >>> from smalluuid import TypedSmallUUID
    
    # Takes a type during instantiation
    >>> uuid = TypedSmallUUID(type=42)
    >>> uuid
    TypedSmallUUID('qHHvXuUwT6y7t7dnsiksvg')
    
    # Type is stored within the UUID
    >>> uuid.type
    42
    
    # Type determined from provided UUID value
    >>> TypedSmallUUID('qHHvXuUwT6y7t7dnsiksvg').type
    42

The use case here is that of having UUIDs from which one can determine 
both an object's ID and the object's type/table/model.

Credits
-------

*Any credits here*

This project borrowed a little code and inspiration from 
shortuuid_.

``smalluuid`` is packaged using seed_.

.. _seed: https://github.com/adamcharnock/seed/
.. _shortuuid: https://github.com/stochastic-technologies/shortuuid
.. _django-smalluuid: https://github.com/adamcharnock/django-smalluuid
