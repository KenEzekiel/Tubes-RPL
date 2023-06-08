import flet as ft
from models import Hewan, Makanan, RiwayatHewan
from views import components
from typing import List


class HewanDetailDisplay(ft.Column):
    def __init__(self, on_details, riwayat_controller) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=20)

        self.on_details = on_details
        self.riwayat_controller = riwayat_controller

    def show_detail_hewan_by_id(self, hewan: Hewan, list_makanan: List[Makanan], list_riwayat: List[RiwayatHewan]):
        self.hewan = hewan
        nama_hewan = hewan.nama
        jenis_hewan = hewan.jenis
        tgl_lahir_hewan = hewan.tanggal_lahir
        usia_hewan = hewan.usia
        self.makanan_hewan = list_makanan
        self.riwayat_hewan = list_riwayat

        makanan_row: list[ft.DataRow] = []
        if self.makanan_hewan is not None:
            for i, makanan in enumerate(self.makanan_hewan):
                makanan_row.append(ft.DataRow(
                    cells=[
                        ft.DataCell(components.Text(i + 1, size=24)),
                        ft.DataCell(components.Text(
                            makanan.nama_makanan, size=24))
                    ]
                ))

        riwayat_row: list[ft.DataRow] = []
        if self.riwayat_hewan is not None:
            for i, riwayat in enumerate(self.riwayat_hewan):
                riwayat_row.append(ft.DataRow(
                    cells=[
                        ft.DataCell(components.Text(i + 1, size=24)),
                        ft.DataCell(components.Text(riwayat.riwayat, size=24)),
                        ft.DataCell(components.Text(
                            riwayat.waktu_awal, size=24)),
                        ft.DataCell(components.Text(
                            riwayat.waktu_akhir, size=24))
                    ]
                ))

        self.controls = [
            components.Text(nama_hewan, size=40),
            ft.Row(controls=[
                ft.Column(controls=[
                    components.Text("Jenis", size=30),
                    components.Text("Tanggal Lahir", size=30),
                    components.Text("Usia", size=30)
                ],
                ),
                ft.Column(controls=[
                    components.Text(":", size=30),
                    components.Text(":", size=30),
                    components.Text(":", size=30)

                ],
                ),
                ft.Column(controls=[
                    components.Text(jenis_hewan, size=30),
                    components.Text(tgl_lahir_hewan, size=30),
                    components.Text(usia_hewan, size=30)
                ],
                ),
            ], spacing=100),
            components.Text("Makanan", size=40),
            ft.DataTable(
                vertical_lines=ft.border.BorderSide(1, "black"),
                horizontal_lines=ft.border.BorderSide(1, "black"),
                border_radius=30,
                border=ft.border.all(1, "black"),
                columns=[
                    ft.DataColumn(components.Text("No", size=24)),
                    ft.DataColumn(components.Text("Nama Makanan", size=24))
                ],
                rows=makanan_row),
            components.Text("Riwayat Kesehatan", size=40),
            ft.DataTable(
                vertical_lines=ft.border.BorderSide(1, "black"),
                horizontal_lines=ft.border.BorderSide(1, "black"),
                border_radius=30,
                border=ft.border.all(1, "black"),
                columns=[
                    ft.DataColumn(components.Text("No", size=24)),
                    ft.DataColumn(components.Text(
                        "Riwayat Penyakit", size=24)),
                    ft.DataColumn(components.Text("Waktu Awal", size=24)),
                    ft.DataColumn(components.Text("Waktu Akhir", size=24))
                ],
                rows=riwayat_row),
            ft.Container(height=30)]
        # self.page.floating_action_button = ft.FloatingActionButton(content=ft.Text(
        #     "Tambah", size=16, font_family="Quicksand Bold", color="0x008FE0"), shape=ft.RoundedRectangleBorder(radius=40), width=200, bgcolor=ft.colors.WHITE, on_click=self.on_create)
        self.page.floating_action_button = ft.FloatingActionButton(content=ft.Text(
            "Tambah Riwayat", size=16, font_family="Quicksand Bold", color="0x008FE0"),
            shape=ft.RoundedRectangleBorder(radius=60), width=200, bgcolor=ft.colors.WHITE,
            on_click=lambda e: self.riwayat_controller.show_riwayat_form(self.hewan, lambda: self.on_details(self.hewan.id)))
        self.page.update()
        self.update()
