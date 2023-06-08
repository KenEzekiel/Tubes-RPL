from unittest import TestCase
from models import Hewan
from datetime import date
import mock


class MockDate(date):
    @classmethod
    def today(cls):
        return date(2023, 3, 1)


class TestHewan(TestCase):
    def test_hewan(self):
        hewan = Hewan(1, "Bob", "Anjing", "2020-04-10")
        self.assertEqual(hewan.id, 1)
        self.assertEqual(hewan.nama, "Bob")
        self.assertEqual(hewan.jenis, "Anjing")
        self.assertEqual(hewan.tanggal_lahir, date(2020, 4, 10))

        hewan.nama = "Milo"
        hewan.jenis = "Kucing"
        hewan.tanggal_lahir = date(2019, 1, 1)
        self.assertEqual(hewan.nama, "Milo")
        self.assertEqual(hewan.jenis, "Kucing")
        self.assertEqual(hewan.tanggal_lahir, date(2019, 1, 1))

        hewan2 = Hewan(1, "Milo", "Kucing", date(2019, 1, 1))
        self.assertEqual(hewan, hewan2)

    @mock.patch("models.hewan.date", MockDate)
    def test_hewan_tanggal_lahir(self):
        hewan = Hewan(1, "Bob", "Anjing", date(2020, 4, 2))
        self.assertEqual(hewan.tanggal_lahir, date(2020, 4, 2))
        self.assertEqual(hewan.usia, 2)
