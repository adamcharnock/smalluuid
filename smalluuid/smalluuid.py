from __future__ import absolute_import
import uuid as _uu
from smalluuid.utils import unpack_uuid, pack_uuid


class SmallUUID(_uu.UUID):

    def __init__(self, small=None, hex=None, bytes=None, bytes_le=None,
                       fields=None, int=None, version=None,
                       *args, **kwargs):
        if [hex, bytes, bytes_le, fields, int, small].count(None) != 5:
            int = _uu.uuid4().int

        if small:
            int = unpack_uuid(small).int

        super(SmallUUID, self).__init__(hex=hex, bytes=bytes, bytes_le=bytes_le,
                                        fields=fields, int=int, version=version,
                                        *args, **kwargs)

    @property
    def small(self):
        return pack_uuid(self.hex)

    @property
    def hex_grouped(self):
        return super(SmallUUID, self).__str__()

    def __str__(self):
        return self.small

    def __repr__(self):
        return "{0}('{1}')".format(self.__class__.__name__, str(self))


class TypedSmallUUID(SmallUUID):
    type_bits = 6

    def __init__(self, small=None, hex=None, bytes=None, bytes_le=None,
                       fields=None, int=None, version=None, type=None,
                       *args, **kwargs):
        if [hex, bytes, bytes_le, fields, int, small, type].count(None) != 6:
            raise ValueError(
                'Either a value or the "type" parameter is '
                'required to instantiate a TypedSmallUUID'
            )
        super(TypedSmallUUID, self).__init__(
            small=small, hex=hex, bytes=bytes, bytes_le=bytes_le,
            fields=fields, int=int, version=version,
            *args, **kwargs
        )

        if type is not None:
            self._set_type(type)

    @property
    def type(self):
        return self.int >> 128 - self.type_bits

    def _set_type(self, type_num):
        if not 0 <= type_num < 1 << self.type_bits:
            raise ValueError(
                'Specified type_num of {0} outside range available '
                'to {1} bit types (0 to {2})'.format(
                    type_num, self.type_bits, (1 << self.type_bits) - 1,
                )
            )

        bits = self.int
        id_size = 128 - self.type_bits
        # Zero out the type bits
        bits &= pow(2, id_size) - 1
        # Now add in the type
        bits |= (type_num << id_size)

        if not 0 <= bits < 1 << 128:
            raise ValueError('Addition of type overflowed max value (128-bits max)')

        object.__setattr__(self, 'int', bits)


def small_uuid(name=None):
    if name is None:
        uuid = _uu.uuid4()
    elif "http" not in name.lower():
        uuid = _uu.uuid5(_uu.NAMESPACE_DNS, name)
    else:
        uuid = _uu.uuid5(_uu.NAMESPACE_URL, name)
    return SmallUUID(int=uuid.int)
