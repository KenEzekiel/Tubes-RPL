from db import cursor, commit
from models.hewan import Hewan
from models.makanan import Makanan
from typing import Union, Dict, Any, List, Tuple
from views import MakananListDisplay, MakananFormDisplay, MakananToHewanDisplay
import flet as ft


class MakananController:
    page_content: Union[ft.Container, None]
    makanan_list_display: MakananListDisplay
    makanan_create_display: MakananFormDisplay
    makanan_to_hewan_display: MakananToHewanDisplay

    def __init__(self, page_content: ft.Container = None) -> None:
        self.page_content = page_content
        self.makanan_list_display = MakananListDisplay(
            lambda e: self.handle_create_view(), lambda e, d: self.handle_add_makanan_to_hewan_view(e, d))
        self.makanan_create_display = MakananFormDisplay(
            lambda e: self.handle_created_makanan(e))
        self.makanan_to_hewan_display = MakananToHewanDisplay(
            lambda e, d: self.handle_added_makanan_to_hewan(e, d), lambda e: self.handle_list_view())

    def add_new_makanan(self, nama_makanan: str) -> Makanan:
        cursor.execute(
            "INSERT INTO Makanan (nama_makanan) VALUES (?)",
            (nama_makanan,)).fetchone()

        new_makanan = Makanan(cursor.lastrowid, nama_makanan)
        commit()
        return new_makanan

    def add_makanan_to_hewan(self, id_hewan: int, id_makanan: int) -> bool:
        try:
            cursor.execute(
                "INSERT INTO JenisMakanan (id_hewan, id_makanan) VALUES (?, ?)",
                (id_hewan, id_makanan)).fetchone()
            commit()
            return True
        except Exception as e:
            return False

    def get_makanan_by_id(self, id_makanan: int) -> Union[Makanan, None]:
        result: Union[Dict[str, Any], None] = cursor.execute("SELECT * FROM Makanan WHERE id_makanan = ?",
                                                             [id_makanan]).fetchone()

        if result is None:
            return None

        makanan = Makanan(result["id_makanan"], result["nama_makanan"])

        return makanan

    def get_all_makanan(self) -> List[Makanan]:
        db_result = cursor.execute(
            "SELECT * FROM Makanan").fetchall()
        list_makanan: List[Makanan] = []
        for row in db_result:
            list_makanan.append(
                Makanan(row["id_makanan"], row["nama_makanan"]))
        return list_makanan

    def get_all_hewan(self) -> List[Hewan]:
        db_result = cursor.execute(
            "SELECT * FROM Hewan").fetchall()
        list_hewan: List[Hewan] = []
        for row in db_result:
            list_hewan.append(
                Hewan(row["id_hewan"], row["nama"], row["jenis"], row["tanggal_lahir"]))
        return list_hewan

    def get_makanan_by_hewan(self, hewan: Hewan) -> List[Makanan]:
        db_result = cursor.execute(
            "SELECT * FROM Makanan WHERE id_makanan IN (SELECT id_makanan FROM JenisMakanan WHERE id_hewan = ?)", [hewan.id]).fetchall()
        list_makanan: List[Makanan] = []
        for row in db_result:
            list_makanan.append(
                Makanan(row["id_makanan"], row["nama_makanan"]))
        return list_makanan

    def get_all_jenis_makanan(self) -> List[Dict[str, int]]:
        db_result = cursor.execute("SELECT * FROM JenisMakanan").fetchall()
        return db_result

    def handle_list_view(self):
        self.page_content.content = self.makanan_list_display
        self.page_content.update()
        self.makanan_list_display.show_list_makanan(self.get_all_makanan())

    def handle_create_view(self):
        self.page_content.content = self.makanan_create_display
        self.page_content.update()
        self.makanan_create_display.show_display()

    def handle_created_makanan(self, text: str):
        self.add_new_makanan(text)
        self.handle_list_view()

    def handle_add_makanan_to_hewan_view(self, makanan: Makanan, error_text: str):
        self.page_content.content = self.makanan_to_hewan_display
        self.page_content.update()
        self.makanan_to_hewan_display.show_display(
            self.get_all_hewan(), makanan, error_text)

    def handle_added_makanan_to_hewan(self, id_hewan: int, id_makanan: int):
        if (self.add_makanan_to_hewan(id_hewan, id_makanan)):
            self.handle_list_view()
        else:
            error_text = "Hewan sudah memiliki makanan tersebut"
            self.handle_add_makanan_to_hewan_view(
                self.get_makanan_by_id(id_makanan), error_text)
