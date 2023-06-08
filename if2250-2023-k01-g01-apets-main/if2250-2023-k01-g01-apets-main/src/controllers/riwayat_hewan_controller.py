from db import cursor, commit
from models.hewan import Hewan
from models.riwayat_hewan import RiwayatHewan
from views import HewanRiwayatFormDisplay
from typing import Union, Dict, Any, List, Callable
from datetime import date
import flet as ft


class RiwayatHewanController:
    page_content: Union[ft.Container, None]
    created_callback: Callable[[], None]

    def __init__(self, page_content: ft.Container = None) -> None:
        self.page_content = page_content

    def add_new_riwayat(self, hewan: Hewan, riwayat: str,
                        waktu_awal: Union[str, date, None],
                        waktu_akhir: Union[str, date, None]) -> RiwayatHewan:
        cursor.execute(
            "INSERT INTO RiwayatHewan (id_hewan, riwayat, waktu_awal, waktu_akhir) VALUES (?, ?, ?, ?)",
            (hewan.id, riwayat, waktu_awal, waktu_akhir)).fetchone()

        new_riwayat = RiwayatHewan(
            cursor.lastrowid, riwayat, waktu_awal, waktu_akhir)
        commit()
        return new_riwayat

    def get_riwayat_by_id(self, id_riwayat: int) -> Union[RiwayatHewan, None]:
        result: Union[Dict[str, Any], None] = cursor.execute("SELECT * FROM RiwayatHewan WHERE id_riwayat = ?",
                                                             [id_riwayat]).fetchone()

        if result is None:
            return None

        riwayat = RiwayatHewan(
            result["id_riwayat"], result["riwayat"], result["waktu_awal"], result["waktu_akhir"])

        return riwayat

    def get_riwayat_by_hewan(self, hewan: Hewan) -> List[RiwayatHewan]:
        db_result = cursor.execute(
            "SELECT * FROM RiwayatHewan WHERE id_hewan = ?", [hewan.id]).fetchall()

        list_riwayat: List[RiwayatHewan] = []

        for row in db_result:
            list_riwayat.append(RiwayatHewan(row["id_riwayat"],
                                             row["riwayat"],
                                             row["waktu_awal"],
                                             row["waktu_akhir"]))
        return list_riwayat

    def get_all_riwayat_name(self) -> List[str]:
        db_result = cursor.execute(
            "SELECT DISTINCT riwayat FROM RiwayatHewan").fetchall()
        return list(map(lambda x: x["riwayat"], db_result))

    def get_all_hewan_riwayat(self):
        db_result = cursor.execute(
            "SELECT DISTINCT id_hewan, riwayat FROM RiwayatHewan").fetchall()
        result: Dict[str, List[int]] = {}
        for row in db_result:
            list_riwayat = result.setdefault(row["riwayat"], [])
            list_riwayat.append(row["id_hewan"])
        return result

    def show_riwayat_form(self, hewan: Hewan, callback: Callable[[], None]):
        self.created_callback = callback
        self.page_content.floating_action_button = None
        riwayat_create_display = HewanRiwayatFormDisplay(self.handle_submit)
        self.page_content.content = riwayat_create_display
        self.page_content.update()
        riwayat_create_display.show_display(hewan)

    def handle_submit(self, hewan: Hewan,
                      riwayat: str,
                      waktu_awal: Union[date, None],
                      waktu_akhir: Union[date, None]):
        self.add_new_riwayat(hewan, riwayat, waktu_awal, waktu_akhir)
        self.created_callback()
