import flet as ft
from views import components
from typing import Callable
from datetime import date


class HewanFormDisplay(ft.Column):
    text_field: ft.TextField
    tgl = components.DateSelector

    def __init__(self, on_create: Callable[[str, str, str], None]) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=20)
        self.on_create = on_create
        self.text_field_nama = ft.TextField(
            label="Nama Hewan",
            color="black",
            on_change=self.handle_change)
        self.text_field_jenis = ft.TextField(
            label="Jenis Hewan",
            color="black",
            on_change=self.handle_change)
        self.tgl = components.DateSelector(
        )

    def show_display(self):
        self.controls = [
            components.Text("Hewan Baru"),
            self.text_field_nama,
            self.text_field_jenis,
            self.tgl,
            ft.Row(controls=[ft.ElevatedButton("Kirim", on_click=self.handle_create, color="0x008FE0", bgcolor=ft.colors.WHITE)], alignment=ft.MainAxisAlignment.END)]
        self.page.floating_action_button = None
        self.page.update()
        self.update()

    def handle_create(self, e):
        if self.text_field_nama.value is None or self.text_field_nama.value == "":
            self.text_field_nama.error_text = "Nama tidak boleh kosong"
            self.text_field_nama.update()
        elif self.text_field_jenis.value is None or self.text_field_jenis.value == "":
            self.text_field_jenis.error_text = "Jenis tidak boleh kosong"
            self.text_field_jenis.update()
        elif self.tgl.get_date() is None or self.tgl.get_date() == "":

            self.tgl.update()
        else:
            self.text_field_nama.error_text = ""
            self.text_field_nama.update()
            self.text_field_jenis.error_text = ""
            self.text_field_jenis.update()
            self.tgl.update()
            self.on_create(self.text_field_nama.value,
                           self.text_field_jenis.value, self.tgl.get_date())

    def handle_change(self, e):
        if self.text_field_nama.value is None or self.text_field_nama.value == "":
            self.text_field_nama.error_text = "Nama tidak boleh kosong"
            self.text_field_nama.update()
        else:
            self.text_field_nama.error_text = ""
            self.text_field_nama.update()
        if self.text_field_jenis.value is None or self.text_field_jenis.value == "":
            self.text_field_jenis.error_text = "Jenis tidak boleh kosong"
            self.text_field_jenis.update()
        else:
            self.text_field_jenis.error_text = ""
            self.text_field_jenis.update()
        if self.tgl.get_date() is None or self.tgl.get_date() == "":
            self.tgl.error_text = "Tanggal tidak boleh kosong"
            self.tgl.update()
        else:
            self.tgl.error_text = ""
            self.tgl.update()
