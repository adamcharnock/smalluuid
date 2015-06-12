from uuid import UUID, uuid4
import base64

 
def pack_uuid(uuid):
    packed_string = base64.urlsafe_b64encode(UUID(str(uuid)).bytes).decode("utf-8")
    packed_string = packed_string.rstrip('=\n').replace('/', '_')
    return packed_string

def unpack_uuid(short_uuid):
    return UUID(bytes=base64.urlsafe_b64decode((short_uuid + '==').replace('_', '/')))


def make_typed_uuid(type_bits, type_size):
    bits = uuid4().int
    id_size = 128 - type_size
    # Zero out the type bits
    bits &= pow(2, id_size) - 1
    # Now add in the type
    bits |= (type_bits << id_size)
    return UUID(int=bits)
