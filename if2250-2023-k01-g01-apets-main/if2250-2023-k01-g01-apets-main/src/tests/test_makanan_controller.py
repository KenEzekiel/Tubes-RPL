from unittest import TestCase
from controllers.hewan_controller import HewanController, RiwayatHewanController, MakananController
from db import clear_db
from datetime import date
from models.hewan import Hewan
from models.makanan import Makanan


class TestMakananController(TestCase):
    makanan_controller: MakananController
    hewan_controller: HewanController

    def setUp(self) -> None:
        self.makanan_controller = MakananController()
        self.riwayat_controller = RiwayatHewanController()
        self.hewan_controller = HewanController(
            self.makanan_controller, self.riwayat_controller)

    def tearDown(self) -> None:
        clear_db()

    def test_add_new_makanan(self):
        daftar_makanan = [
            "Royal Canin Adults",
            "Royal Canin Kids"
        ]

        for each in daftar_makanan:
            makanan = self.makanan_controller.add_new_makanan(each)
            self.assertEqual(makanan.nama_makanan, each)

    def test_get_makanan_by_id(self):
        makanan = self.makanan_controller.add_new_makanan("Royal Canin Kidult")
        result = self.makanan_controller.get_makanan_by_id(makanan.id)

        self.assertEqual(result, makanan)

        riwayat_not_found = self.makanan_controller.get_makanan_by_id(-1)

        self.assertEqual(riwayat_not_found, None)

    def test_get_riwayat_by_hewan(self):
        self.makanan_controller.add_new_makanan("Royal Canin Adults")
        self.makanan_controller.add_new_makanan("Royal Canin Kids")
        self.makanan_controller.add_new_makanan("Royal Canin Kidult")
        makanan = self.makanan_controller.get_all_makanan()

        self.assertEqual(len(makanan), 3)
        self.assertEqual(makanan[0].nama_makanan, "Royal Canin Adults")
        self.assertEqual(makanan[1].nama_makanan, "Royal Canin Kids")
        self.assertEqual(makanan[2].nama_makanan, "Royal Canin Kidult")

    def test_add_makanan_to_hewan(self):
        self.makanan_controller.add_new_makanan("Royal Canin Adults")
        self.makanan_controller.add_new_makanan("Royal Canin Kids")

        makanan = self.makanan_controller.get_all_makanan()

        self.hewan_controller.add_new_hewan("Bob", "Anjing", "2020-04-10")
        self.hewan_controller.add_new_hewan("Milo", "Kucing", "2019-01-01")

        hewan = self.hewan_controller.get_all_hewan()

        self.makanan_controller.add_makanan_to_hewan(
            hewan[0].id, makanan[0].id)

        self.makanan_controller.add_makanan_to_hewan(
            hewan[0].id, makanan[1].id)

        makanan_hewan_0 = self.makanan_controller.get_makanan_by_hewan(
            hewan[0])

        self.assertEqual(len(makanan_hewan_0), 2)

        self.assertEqual(makanan_hewan_0[0].nama_makanan, "Royal Canin Adults")

        self.assertEqual(makanan_hewan_0[1].nama_makanan, "Royal Canin Kids")
