import flet as ft
from models import Hewan, Makanan, RiwayatHewan
from views import components
from typing import List, Callable, Tuple, Dict


class HewanListDisplay(ft.Column):
    def __init__(self, on_create, on_details, get_group_makanan: Callable[[], Tuple[Dict[int, Hewan], List[Makanan], List[Dict[str, int]]]],
                 get_group_riwayat: Callable[[], Tuple[Dict[int, Hewan], List[str], Dict[str, List[int]]]]) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=20)
        self.jenis_makanan_button = components.Button(
            "Jenis Makanan", bgcolor="white", color="0x008FE0", size=24, width=300, active_bgcolor="0xC9C9C9", on_click=lambda e: self.show_hewan_by_makanan())
        self.riwayat_button = components.Button("Riwayat Kesehatan",
                                                bgcolor="white", color="0x008FE0", size=24, width=300, active_bgcolor="0xC9C9C9", on_click=lambda e: self.show_hewan_by_riwayat())
        self.header = ft.Row(
            controls=[
                components.Text("Pengelompokkan: ", size=24),
                self.jenis_makanan_button,
                self.riwayat_button
            ]
        )
        self.on_create = on_create
        self.on_details = on_details
        self.get_group_makanan = get_group_makanan
        self.get_group_riwayat = get_group_riwayat

    def create_hewan_detail_callback(self, hewan_id):
        def callback(e):
            self.on_details(hewan_id)
        return callback

    def create_list_table(self, list_hewan: List[Hewan]):
        rows: list[ft.DataRow] = []
        for i, hewan in enumerate(list_hewan):
            rows.append(ft.DataRow(
                cells=[
                    ft.DataCell(components.Text(i + 1, size=24)),
                    ft.DataCell(components.Text(hewan.nama, size=24)),
                    ft.DataCell(components.Text(hewan.jenis, size=24)),
                    ft.DataCell(components.Button("Show", size=20,
                                                  bgcolor="white", color="0x008FE0", width=150, on_click=self.create_hewan_detail_callback(hewan.id))),
                ]
            ))
        return ft.DataTable(
            vertical_lines=ft.border.BorderSide(1, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            border_radius=40,
            border=ft.border.all(1, "black"),
            columns=[
                ft.DataColumn(components.Text("No", size=24)),
                ft.DataColumn(components.Text("Nama", size=24)),
                ft.DataColumn(components.Text("Jenis", size=24)),
                ft.DataColumn(components.Text("Detail", size=24)),
            ],
            rows=rows,
        )

    def show_list_hewan(self, list_hewan: List[Hewan]):
        table = self.create_list_table(list_hewan)
        self.controls = [
            self.header,
            table,
            ft.Container(height=50)]
        self.page.floating_action_button = ft.FloatingActionButton(content=ft.Text(
            "Tambah", size=16, font_family="Quicksand Bold", color="0x008FE0"), shape=ft.RoundedRectangleBorder(radius=60), width=200, bgcolor=ft.colors.WHITE, on_click=self.on_create)
        self.page.update()
        self.update()
        self.jenis_makanan_button.toggle_active(False)
        self.riwayat_button.toggle_active(False)

    def show_group(self, tables: List):
        self.controls = [self.header]
        for table in tables:
            self.controls.append(components.Text(
                table[0], size=24, text_align=ft.TextAlign.LEFT))
            self.controls.append(table[1])
        self.controls.append(ft.Container(height=50))
        self.update()

    def show_hewan_by_makanan(self):
        self.jenis_makanan_button.toggle_active(True)
        self.riwayat_button.toggle_active(False)
        dict_hewan, list_makanan, list_jenis_makanan = self.get_group_makanan()
        tables: List[Tuple(str, ft.DataTable)] = []
        for makanan in list_makanan:
            hewan_ids = filter(
                lambda x: x["id_makanan"] == makanan.id, list_jenis_makanan)
            hewan_in_group = [dict_hewan[jenis["id_hewan"]]
                              for jenis in hewan_ids]
            tables.append(
                (makanan.nama_makanan, self.create_list_table(hewan_in_group)))
        self.show_group(tables)

    def show_hewan_by_riwayat(self):
        self.jenis_makanan_button.toggle_active(False)
        self.riwayat_button.toggle_active(True)
        dict_hewan, list_riwayat, hewan_riwayat = self.get_group_riwayat()
        tables: List[Tuple(str, ft.DataTable)] = []
        for riwayat in list_riwayat:
            hewan_in_group: List[Hewan] = [dict_hewan[id_hewan]
                                           for id_hewan in hewan_riwayat[riwayat]]
            tables.append((riwayat, self.create_list_table(hewan_in_group)))
        self.show_group(tables)
