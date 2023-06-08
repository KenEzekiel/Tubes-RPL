from db import cursor, commit
from models import Makanan, Hewan, RiwayatHewan
from typing import Union, Dict, Tuple
from datetime import date
import flet as ft
from views import HewanListDisplay, HewanFormDisplay, HewanDetailDisplay
from .makanan_controller import MakananController
from .riwayat_hewan_controller import RiwayatHewanController
from typing import List


class HewanController:
    def __init__(self, makanan_controller: MakananController, riwayat_controller: RiwayatHewanController, page_content: ft.Container = None) -> None:
        self.hewan_form_display = HewanFormDisplay(self.handle_created_hewan)

        def on_details(id_hewan: int):
            self.page_content.content = self.hewan_detail_display
            self.page_content.update()
            hewan = self.get_hewan_by_id(id_hewan)
            list_makanan = self.makanan_controller.get_makanan_by_hewan(hewan)
            # list_makanan = self.makanan_controller.get_all_makanan()
            list_riwayat = self.riwayat_controller.get_riwayat_by_hewan(hewan)
            self.hewan_detail_display.show_detail_hewan_by_id(
                hewan, list_makanan, list_riwayat)

        self.hewan_detail_display = HewanDetailDisplay(
            on_details, riwayat_controller)
        self.makanan_controller = makanan_controller
        self.riwayat_controller = riwayat_controller
        self.page_content = page_content

        def on_create(e):
            self.hewan_form_display = HewanFormDisplay(
                self.handle_created_hewan)
            self.page_content.content = self.hewan_form_display
            self.page_content.update()
            self.hewan_form_display.show_display()

        self.hewan_list_display = HewanListDisplay(
            on_details=on_details, on_create=on_create, get_group_makanan=self.get_hewan_group_by_makanan, get_group_riwayat=self.get_hewan_group_by_riwayat)

    def add_new_hewan(self, nama: str, jenis: str, tanggal_lahir: Union[str, date]):
        cursor.execute(
            "INSERT INTO Hewan (nama, jenis, tanggal_lahir) VALUES (?, ?, ?)",
            (nama, jenis, tanggal_lahir)).fetchone()

        new_hewan = Hewan(cursor.lastrowid, nama, jenis, tanggal_lahir)
        commit()
        return new_hewan

    def get_all_hewan(self):
        db_result = cursor.execute(
            "SELECT * FROM hewan ORDER BY nama ASC").fetchall()
        list_hewan: List[Hewan] = []
        for row in db_result:
            list_hewan.append(Hewan(row["id_hewan"], row["nama"],
                                    row["jenis"], row["tanggal_lahir"]))
        return list_hewan

    def get_hewan_group_by_makanan(self) -> Tuple[Dict[int, Hewan], List[Makanan], List[Dict[str, int]]]:
        list_hewan = self.get_all_hewan()
        hewan_dict: Dict[int, Hewan] = {}
        for hewan in list_hewan:
            hewan_dict[hewan.id] = hewan
        list_makanan = self.makanan_controller.get_all_makanan()
        list_jenis_makanan = self.makanan_controller.get_all_jenis_makanan()
        return (hewan_dict, list_makanan, list_jenis_makanan)

    def get_hewan_group_by_riwayat(self) -> Tuple[Dict[int, Hewan], List[str], Dict[str, List[int]]]:
        list_hewan = self.get_all_hewan()
        hewan_dict: Dict[int, Hewan] = {}
        for hewan in list_hewan:
            hewan_dict[hewan.id] = hewan
        list_riwayat = self.riwayat_controller.get_all_riwayat_name()
        hewan_riwayat = self.riwayat_controller.get_all_hewan_riwayat()
        return (hewan_dict, list_riwayat, hewan_riwayat)

    def get_hewan_by_id(seld, id: int):
        db_result = cursor.execute(
            "SELECT * FROM hewan WHERE id_hewan = %d" % id).fetchone()
        if db_result is not None:
            return Hewan(db_result["id_hewan"], db_result["nama"], db_result["jenis"], db_result["tanggal_lahir"])

    def handle_view(self):
        self.page_content.content = self.hewan_list_display
        self.page_content.update()
        self.hewan_list_display.show_list_hewan(self.get_all_hewan())

    def handle_created_hewan(self, nama: str, jenis: str, tgl: str):
        self.add_new_hewan(nama, jenis, tgl)
        self.handle_view()
