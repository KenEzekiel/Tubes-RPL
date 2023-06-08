import flet as ft
from models import Makanan
from views import components
from typing import List


class MakananListDisplay(ft.Column):
    def __init__(self, on_create, on_add) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=20)

        self.on_create = on_create
        self.on_add = on_add

    def show_list_makanan(self, list_makanan: List[Makanan]):
        def create_callback(i, d):
            def callback(e):
                self.on_add(i, d)
            return callback

        rows: list[ft.DataRow] = []
        for i, makanan in enumerate(list_makanan):
            rows.append(ft.DataRow(
                cells=[
                    ft.DataCell(components.Text(i + 1, size=24)),
                    ft.DataCell(components.Text(
                        makanan.nama_makanan, size=24)),
                    ft.DataCell(components.Button("Tambah", size=20,
                                                  bgcolor="white",
                                                  color="0x008FE0",
                                                  width=150,
                                                  on_click=create_callback(makanan, "")))
                ]
            ))
        self.controls = [
            ft.DataTable(
                vertical_lines=ft.border.BorderSide(1, "black"),
                horizontal_lines=ft.border.BorderSide(1, "black"),
                border_radius=40,
                border=ft.border.all(1, "black"),
                columns=[
                    ft.DataColumn(components.Text("No", size=24)),
                    ft.DataColumn(components.Text("Nama Makanan", size=24)),
                    ft.DataColumn(components.Text("Tambah ke Hewan", size=24)),
                ],
                rows=rows,
            ), ft.Container(height=50)]

        self.page.floating_action_button = ft.FloatingActionButton(
            content=ft.Text("Tambah Makanan", size=16,
                            font_family="Quicksand Bold", color="0x008FE0"),
            shape=ft.RoundedRectangleBorder(radius=60),
            width=200,
            bgcolor=ft.colors.WHITE,
            on_click=self.on_create)
        self.page.update()
        self.update()
