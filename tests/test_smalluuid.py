import unittest
import uuid as _uu


class TestSmallUUIDClass(unittest.TestCase):

    def test_no_input(self):
        from smalluuid.smalluuid import SmallUUID
        uuid = SmallUUID()
        self.assertEqual(uuid.version, 4)

    def test_normal(self):
        from smalluuid.smalluuid import SmallUUID
        self.assertEqual(SmallUUID(int=0).small,
                         'AAAAAAAAAAAAAAAAAAAAAA')

    def test_short(self):
        from smalluuid.smalluuid import SmallUUID
        self.assertEqual(SmallUUID(small='AAAAAAAAAAAAAAAAAAAAAA').small,
                         'AAAAAAAAAAAAAAAAAAAAAA')

    def test_str(self):
        from smalluuid.smalluuid import SmallUUID
        self.assertEqual(str(SmallUUID(small='AAAAAAAAAAAAAAAAAAAAAA')),
                         'AAAAAAAAAAAAAAAAAAAAAA')

    def test_repr(self):
        from smalluuid.smalluuid import SmallUUID
        self.assertEqual(repr(SmallUUID(small='AAAAAAAAAAAAAAAAAAAAAA')),
                         "SmallUUID('AAAAAAAAAAAAAAAAAAAAAA')")

    def test_hex_grouped(self):
        from smalluuid.smalluuid import SmallUUID
        self.assertEqual(SmallUUID(small='AAAAAAAAAAAAAAAAAAAAAA').hex_grouped,
                         "00000000-0000-0000-0000-000000000000")

    def test_with_version(self):
        """Ensure the appropriate version bits get inserted"""
        from smalluuid.smalluuid import SmallUUID
        self.assertEqual(
            SmallUUID(small='AAAAAAAAAAAAAAAAAAAAAA', version=4).hex_grouped,
            "00000000-0000-4000-8000-000000000000"
        )


class TestSmallUUIDFunc(unittest.TestCase):
    def test_uuid4(self):
        from smalluuid.smalluuid import small_uuid
        self.assertEqual(small_uuid().version, 4)

    def test_uuid5_dns(self):
        from smalluuid.smalluuid import small_uuid
        uuid = small_uuid(name="foo.com")
        self.assertEqual(uuid.version, 5)
        self.assertEqual(uuid.hex_grouped, 'cb2b0427-a119-5e0e-b044-484d51ea6a2f')

    def test_uuid5_url(self):
        from smalluuid.smalluuid import small_uuid
        uuid = small_uuid(name="http://foo.com/xyz")
        self.assertEqual(uuid.version, 5)
        self.assertEqual(uuid.hex_grouped, '0742a68a-cfd8-5aa6-9a3d-26dfe936ce64')


class TestTypedSmallUUIDClass(unittest.TestCase):
    def test_get_type(self):
        from smalluuid.smalluuid import TypedSmallUUID
        self.assertEqual(TypedSmallUUID(int=(0b101010 << 122)).type, 0b101010)

    def test_new(self):
        from smalluuid.smalluuid import TypedSmallUUID
        self.assertEqual(TypedSmallUUID(type=63).type, 63)

    def test_overflow(self):
        from smalluuid.smalluuid import TypedSmallUUID
        self.assertRaises(ValueError, TypedSmallUUID, type=64)

    def test_value_or_type_required(self):
        from smalluuid.smalluuid import TypedSmallUUID
        self.assertRaises(ValueError, TypedSmallUUID)
