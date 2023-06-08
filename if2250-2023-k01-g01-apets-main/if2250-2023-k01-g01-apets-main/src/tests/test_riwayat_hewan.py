from unittest import TestCase
from models import RiwayatHewan
from datetime import date


class TestRiwayatHewan(TestCase):
    def test_riwayat_hewan(self):
        riwayat = RiwayatHewan(1, "Diare", "2023-04-03", "2023-04-05")
        self.assertEqual(riwayat.id, 1)
        self.assertEqual(riwayat.riwayat, "Diare")
        self.assertEqual(riwayat.waktu_awal, date(2023, 4, 3))
        self.assertEqual(riwayat.waktu_akhir, date(2023, 4, 5))

        riwayat.riwayat = "Diare akut"
        riwayat.waktu_awal = date(2023, 4, 1)
        riwayat.waktu_akhir = date(2023, 4, 3)

        self.assertEqual(riwayat.riwayat, "Diare akut")
        self.assertEqual(riwayat.waktu_awal, date(2023, 4, 1))
        self.assertEqual(riwayat.waktu_akhir, date(2023, 4, 3))

        riwayat2 = RiwayatHewan(1, "Diare akut", date(2023, 4, 1), date(2023, 4, 3))
        self.assertEqual(riwayat, riwayat2)

    def test_null_riwayat(self):
        riwayat = RiwayatHewan(2, "Demam", "2023-04-03", None)
        self.assertEqual(riwayat.id, 2)
        self.assertEqual(riwayat.riwayat, "Demam")
        self.assertEqual(riwayat.waktu_awal, date(2023, 4, 3))
        self.assertEqual(riwayat.waktu_akhir, None)

        riwayat.riwayat = "Demam ringan"
        riwayat.waktu_awal = None
        riwayat.waktu_akhir = "2023-04-05"

        self.assertEqual(riwayat.riwayat, "Demam ringan")
        self.assertEqual(riwayat.waktu_awal, None)
        self.assertEqual(riwayat.waktu_akhir, date(2023, 4, 5))