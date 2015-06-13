from __future__ import absolute_import

# It must be possible to import this file with
# none of the package's dependencies installed

__version__ = '0.1.4'

DEFAULT_ALPHABET = tuple("23456789ABCDEFGHJKLMNPQRSTUVWXYZ"
                      "abcdefghijkmnopqrstuvwxyz")

from smalluuid.smalluuid import (
 SmallUUID,
 TypedSmallUUID,
)
