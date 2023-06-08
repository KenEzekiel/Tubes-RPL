import flet as ft
from views import components
from typing import Callable
from models import Hewan
from typing import Union
from datetime import date


class HewanRiwayatFormDisplay(ft.Column):
    text_field: ft.TextField
    waktu_awal: components.DateSelector
    waktu_akhir: components.DateSelector
    hewan: Hewan

    def __init__(self, on_create: Callable[[Hewan, str, Union[date, None], Union[date, None]], None]) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=20)
        self.on_create = on_create
        self.text_field = ft.TextField(
            label="Riwayat",
            color="black",
            on_change=self.handle_change
            )
        self.waktu_akhir = components.DateSelector()
        self.waktu_awal = components.DateSelector()

    def show_display(self, hewan: Hewan):
        self.hewan = hewan
        self.page.floating_action_button = None
        self.controls = [
            components.Text("Riwayat Kesehatan Baru"),
            ft.Container(content=self.text_field, width=50, expand=False),
            ft.Container(content=ft.Text("Waktu awal", size=18, color="black"), padding=10),
            self.waktu_awal,
            ft.Container(content=ft.Text("Waktu akhir", size=18, color="black"), padding=10),
            self.waktu_akhir,
            ft.Row(controls=[
                ft.ElevatedButton("Kirim", on_click=self.handle_create, color="0x008FE0", bgcolor=ft.colors.WHITE)],
                alignment=ft.MainAxisAlignment.END)]
        self.page.update()
        self.update()

    def handle_create(self, e):
        if self.text_field.value is None or self.text_field.value == "":
            self.text_field.error_text = "Riwayat tidak boleh kosong"
            self.text_field.update()
        else:
            self.text_field.error_text = ""
            self.text_field.update()
            self.on_create(self.hewan, self.text_field.value, self.waktu_awal.get_date(), self.waktu_akhir.get_date())

    def handle_change(self, e):
        if self.text_field.value is None or self.text_field.value == "":
            self.text_field.error_text = "Riwayat tidak boleh kosong"
            self.text_field.update()
        else:
            self.text_field.error_text = ""
            self.text_field.update()