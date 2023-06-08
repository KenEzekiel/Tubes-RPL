import flet as ft
from models import Makanan, Hewan
from views import components
from typing import List


class MakananToHewanDisplay(ft.Column):
    def __init__(self, on_assign, on_back) -> None:
        super().__init__(expand=True, scroll=ft.ScrollMode.AUTO,
                         horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                         spacing=20)

        self.makanan = None
        self.on_assign = on_assign
        self.choice = None
        self.on_back = on_back
        self.dropdown = ft.Dropdown()

    def dropdown_on_change(self, e):
        self.dropdown.error_text = ""
        self.dropdown.update()
        self.choice = self.dropdown.value

    def get_all_hewan_to_option(self, list_hewan: List[Hewan]):
        for hewan in list_hewan:
            self.dropdown.options.append(
                ft.dropdown.Option(text=hewan.nama, key=hewan))

    def handle_assign(self, e):
        if self.dropdown.value is None:
            pass
            self.dropdown.error_text = "Pilih hewan"
            self.dropdown.update()
        else:
            self.dropdown.error_text = ""
            self.dropdown.update()
            self.on_assign(self.dropdown.value, self.makanan.id)

    def show_display(self, list_hewan: List[Hewan], makanan: Makanan, error_text: str):
        self.makanan = makanan
        self.page.floating_action_button = ft.FloatingActionButton(
            content=ft.Text("Kembali", size=16,
                            font_family="Quicksand Bold", color="0x008FE0"),
            shape=ft.RoundedRectangleBorder(radius=60),
            width=200,
            bgcolor=ft.colors.WHITE,
            on_click=self.on_back)

        self.dropdown = ft.Dropdown(
            error_text=error_text,
            label="Hewan",
            hint_text=f"Pilih hewan untuk makanan {makanan.nama_makanan}",
            options=[
                ft.dropdown.Option(text=hewan.nama, key=hewan.id) for hewan in list_hewan
            ],
            on_change=self.dropdown_on_change
        )

        self.controls = [
            components.Text("Pilih Hewan"),
            self.dropdown,
            ft.Row(controls=[
                ft.ElevatedButton("Assign", on_click=self.handle_assign, color="0x008FE0", bgcolor=ft.colors.WHITE)],
                alignment=ft.MainAxisAlignment.END
            )
        ]
        self.page.update()
        self.update()
