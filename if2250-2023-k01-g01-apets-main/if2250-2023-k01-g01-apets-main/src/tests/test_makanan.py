from unittest import TestCase
from models import Makanan


class TestMakanan(TestCase):
    def test_riwayat_hewan(self):
        makanan = Makanan(1, "Royal Canin")
        self.assertEqual(makanan.id, 1)
        self.assertEqual(makanan.nama_makanan, "Royal Canin")

        makanan.nama_makanan = "Royal Canin Kitten"

        self.assertEqual(makanan.nama_makanan, "Royal Canin Kitten")

        makanan2 = Makanan(1, "Royal Canin Kitten")
        self.assertEqual(makanan, makanan2)
