from unittest import TestCase
from controllers.hewan_controller import HewanController
from controllers.riwayat_hewan_controller import RiwayatHewanController
from controllers.makanan_controller import MakananController
from db import clear_db
from datetime import date


class TestRiwayatHewanController(TestCase):
    hewan_controller: HewanController
    riwayat_controller: RiwayatHewanController

    def setUp(self) -> None:
        makanan_controller = MakananController()
        self.riwayat_controller = RiwayatHewanController()
        self.hewan_controller = HewanController(
            makanan_controller, self.riwayat_controller)
        datasets = [{
            "nama": "Bob",
            "jenis": "Anjing",
            "tanggal_lahir": "2020-04-10"
        }, {
            "nama": "Milo",
            "jenis": "Kucing",
            "tanggal_lahir": date(2019, 1, 1),
        }, {
            "nama": "Coco",
            "jenis": "Capybara",
            "tanggal_lahir": date(2019, 1, 1)
        }]

        for data in datasets:
            self.hewan_controller.add_new_hewan(
                data["nama"], data["jenis"], data["tanggal_lahir"])

    def tearDown(self) -> None:
        clear_db()

    def test_add_new_riwayat(self):
        list_hewan = self.hewan_controller.get_all_hewan()

        hewan = list_hewan[0]

        result = self.riwayat_controller.add_new_riwayat(
            hewan, "Diare", "2023-04-01", "2023-04-04")

        self.assertEqual(result.riwayat, "Diare")
        self.assertEqual(result.waktu_awal, date(2023, 4, 1))
        self.assertEqual(result.waktu_akhir, date(2023, 4, 4))

    def test_riwayat_with_null(self):
        list_hewan = self.hewan_controller.get_all_hewan()
        hewan = list_hewan[0]

        result = self.riwayat_controller.add_new_riwayat(
            hewan, "Diare", None, None)
        riwayat = self.riwayat_controller.get_riwayat_by_id(result.id)

        self.assertEqual(result, riwayat)

    def test_get_riwayat_by_id(self):
        list_hewan = self.hewan_controller.get_all_hewan()
        hewan = list_hewan[1]
        riwayat = self.riwayat_controller.add_new_riwayat(
            hewan, "Demam", "2023-04-01", "2023-04-04")
        result = self.riwayat_controller.get_riwayat_by_id(riwayat.id)

        self.assertEqual(result, riwayat)

        riwayat_not_found = self.riwayat_controller.get_riwayat_by_id(-1)

        self.assertEqual(riwayat_not_found, None)

    def test_get_riwayat_by_hewan(self):
        list_hewan = self.hewan_controller.get_all_hewan()
        hewan = list_hewan[2]
        riwayat1 = self.riwayat_controller.add_new_riwayat(
            hewan, "Demam", "2023-04-01", "2023-04-04")
        riwayat2 = self.riwayat_controller.add_new_riwayat(
            hewan, "Hamil", "2023-02-01", "2023-04-04")

        results = self.riwayat_controller.get_riwayat_by_hewan(hewan)

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], riwayat1)
        self.assertEqual(results[1], riwayat2)
