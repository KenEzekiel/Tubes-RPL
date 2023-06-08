from unittest import TestCase
from controllers.hewan_controller import HewanController
from controllers.makanan_controller import MakananController
from controllers.riwayat_hewan_controller import RiwayatHewanController
from db import clear_db
from datetime import date
from models.hewan import Hewan


class TestHewanController(TestCase):
    def setUp(self) -> None:
        makanan_controller = MakananController()
        riwayat_controller = RiwayatHewanController()
        self.controller = HewanController(
            makanan_controller, riwayat_controller)
        self.tests = [{
            "nama": "Bob",
            "jenis": "Anjing",
            "tanggal_lahir": "2020-04-10"
        }, {
            "nama": "Milo",
            "jenis": "Kucing",
            "tanggal_lahir": date(2019, 1, 1)
        }]

    def tearDown(self) -> None:
        clear_db()

    def test_add_new_hewan(self):
        for i, test in enumerate(self.tests):
            result = self.controller.add_new_hewan(
                test["nama"], test["jenis"], test["tanggal_lahir"])
            hewan = Hewan(i + 1, test["nama"],
                          test["jenis"], test["tanggal_lahir"])
            self.assertEqual(result, hewan)

    def test_get_all_hewan(self):
        list_hewan: list[Hewan] = []
        for i, test in enumerate(self.tests):
            self.controller.add_new_hewan(
                test["nama"], test["jenis"], test["tanggal_lahir"])
            list_hewan.append(Hewan(i + 1, test["nama"],
                                    test["jenis"], test["tanggal_lahir"]))

        result = self.controller.get_all_hewan()
        self.assertEqual(len(result), 2)
        for i in range(len(result)):
            self.assertEqual(result[i], list_hewan[i])

        for _ in range(10):
            self.controller.add_new_hewan("Zob", "Anjing", "2020-04-10")

        result = self.controller.get_all_hewan()
        self.assertEqual(len(result), 12)
        for i in range(len(result)):
            self.assertEqual(result[i].id, i + 1)

    def test_get_group_makanan(self):
        list_hewan: list[Hewan] = []
        for i, test in enumerate(self.tests):
            self.controller.add_new_hewan(
                test["nama"], test["jenis"], test["tanggal_lahir"])
            list_hewan.append(Hewan(i + 1, test["nama"],
                                    test["jenis"], test["tanggal_lahir"]))
        makanan_a = self.controller.makanan_controller.add_new_makanan(
            "Makanan A")
        makanan_b = self.controller.makanan_controller.add_new_makanan(
            "Makanan B")
        makanan_c = self.controller.makanan_controller.add_new_makanan(
            "Makanan C")

        self.controller.makanan_controller.add_makanan_to_hewan(
            list_hewan[0].id, makanan_a.id)
        self.controller.makanan_controller.add_makanan_to_hewan(
            list_hewan[0].id, makanan_b.id)
        self.controller.makanan_controller.add_makanan_to_hewan(
            list_hewan[0].id, makanan_c.id)
        self.controller.makanan_controller.add_makanan_to_hewan(
            list_hewan[1].id, makanan_a.id)

        hewan_dict, list_makanan, list_jenis_makanan = self.controller.get_hewan_group_by_makanan()
        for key, value in hewan_dict.items():
            self.assertEqual(list_hewan[key - 1], value)
        self.assertEqual(list_makanan, [makanan_a, makanan_b, makanan_c])
        self.assertEqual(len(list_jenis_makanan), 4)

    def test_group_riwayat(self):
        list_hewan: list[Hewan] = []
        for i, test in enumerate(self.tests):
            self.controller.add_new_hewan(
                test["nama"], test["jenis"], test["tanggal_lahir"])
            list_hewan.append(Hewan(i + 1, test["nama"],
                                    test["jenis"], test["tanggal_lahir"]))
        self.controller.riwayat_controller.add_new_riwayat(
            list_hewan[0], "Sakit", "2020-04-10", "2020-04-11"
        )
        self.controller.riwayat_controller.add_new_riwayat(
            list_hewan[0], "Sakit", "2020-05-12", "2020-05-13"
        )
        self.controller.riwayat_controller.add_new_riwayat(
            list_hewan[1], "Sakit", "2020-04-10", "2020-04-11"
        )
        self.controller.riwayat_controller.add_new_riwayat(
            list_hewan[1], "Sakit2", "2020-04-15", "2020-04-16"
        )
        hewan_dict, list_riwayat, hewan_riwayat = self.controller.get_hewan_group_by_riwayat()
        for key, value in hewan_dict.items():
            self.assertEqual(list_hewan[key - 1], value)
        self.assertEqual(list_riwayat, ["Sakit", "Sakit2"])
        self.assertEqual(len(hewan_riwayat), 2)
        self.assertEqual(hewan_riwayat[list_riwayat[0]], [1, 2])
        self.assertEqual(hewan_riwayat[list_riwayat[1]], [2])

    def test_get_hewan_by_id(self):
        list_hewan: list[Hewan] = []
        for i, test in enumerate(self.tests):
            self.controller.add_new_hewan(
                test["nama"], test["jenis"], test["tanggal_lahir"])
            list_hewan.append(Hewan(i + 1, test["nama"],
                                    test["jenis"], test["tanggal_lahir"]))
        result = self.controller.get_hewan_by_id(1)
        self.assertEqual(list_hewan[0], result)
        result = self.controller.get_hewan_by_id(2)
        self.assertEqual(list_hewan[1], result)
