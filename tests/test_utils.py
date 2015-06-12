import unittest
import uuid as _uu


class TestUtils(unittest.TestCase):

    def test_pack_unpack(self):
        from smalluuid.utils import unpack_uuid, pack_uuid

        # for x in range(0, 10000):
        #     uuid = _uu.uuid4()
        #     self.assertEqual(uuid, unpack_uuid(pack_uuid(uuid)))

    def test_pack(self):
        from smalluuid.utils import pack_uuid

        uuid = _uu.UUID(int=0, version=4)
        self.assertEqual(pack_uuid(uuid), 'AAAAAAAAQACAAAAAAAAAAA')

        uuid = _uu.UUID(int=int('10' * 64, 2), version=4)
        self.assertEqual(pack_uuid(uuid), 'qqqqqqqqSqqqqqqqqqqqqg')

        uuid = _uu.UUID(int=pow(2, 128) - 1, version=4)
        self.assertEqual(pack_uuid(uuid), '________T_-__________w')

    def test_unpack(self):
        from smalluuid.utils import unpack_uuid

        self.assertEqual(str(unpack_uuid('AAAAAAAAQACAAAAAAAAAAA')),
                         '00000000-0000-4000-8000-000000000000')
        self.assertEqual(str(unpack_uuid('qqqqqqqqSqqqqqqqqqqqqg')),
                         'aaaaaaaa-aaaa-4aaa-aaaa-aaaaaaaaaaaa')
        self.assertEqual(str(unpack_uuid('________T_-__________w')),
                         'ffffffff-ffff-4fff-bfff-ffffffffffff')
