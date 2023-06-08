import flet as ft
from views import components
from typing import Callable


class MakananFormDisplay(ft.Column):
    text_field: ft.TextField

    def __init__(self, on_create: Callable[[str], None]) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH, spacing=20)
        self.on_create = on_create
        self.text_field = ft.TextField(
            label="Nama makanan",
            color="black",
            on_change=self.handle_change)

    def show_display(self):
        self.page.floating_action_button = None
        self.controls = [
            components.Text("Makanan Baru"),
            self.text_field,
            ft.Row(controls=[
                ft.ElevatedButton("Kirim", on_click=self.handle_create, color="0x008FE0", bgcolor=ft.colors.WHITE)],
                   alignment=ft.MainAxisAlignment.END)]
        self.page.update()
        self.update()

    def handle_create(self, e):
        if self.text_field.value is None or self.text_field.value == "":
            self.text_field.error_text = "Nama tidak boleh kosong"
            self.text_field.update()
        else:
            self.text_field.error_text = ""
            self.text_field.update()
            self.on_create(self.text_field.value)

    def handle_change(self, e):
        if self.text_field.value is None or self.text_field.value == "":
            self.text_field.error_text = "Nama tidak boleh kosong"
            self.text_field.update()
        else:
            self.text_field.error_text = ""
            self.text_field.update()