import flet as ft
from controllers import HewanController, MakananController, RiwayatHewanController
from views.components import Button

class MainPage:
    makanan_controller: MakananController
    hewan_controller: HewanController
    riwayat_controller: RiwayatHewanController

    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.page.theme_mode = ft.ThemeMode.LIGHT
        page.title = "Apets"
        page.fonts = {
            "Quicksand": "/font/static/Quicksand-Regular.ttf",
            "Quicksand Bold": "/font/static/Quicksand-Bold.ttf",
        }
        page.window_width = 1280
        page.window_height = 720
        page.window_resizable = False
        page.window_full_screen = False
        page.window_maximizable = False
        background = ft.Container(
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
                colors=["0x91E7B8", "0x8CDBB1", "0x88D1AA", "0xBDE8D1"]),
            width=page.width,
            height=page.height,
            padding=ft.padding.all(10)
        )
        container = ft.Container(
            bgcolor="0xffffff",
            width=background.width,
            height=background.height,
            border_radius=10,
            padding=ft.padding.all(20)
        )
        background.content = ft.Card(
            content=container,
            elevation=100
        )
        self.page_content = ft.Container(expand=True)
        self.nav_buttons = ft.Row(
            alignment=ft.alignment.center,
            spacing=30,
            controls=[
                Button("Hewan", "0xffffff",
                       "0x008FE0", 32, 300, active_bgcolor="0xC9C9C9", on_click=self.show_hewan_list_menu),
                Button("Makanan", "0xffffff",
                       "0x008FE0", 32, 300, active_bgcolor="0xC9C9C9", on_click=self.show_list_makanan),
                Button("Aktivitas", "0xffffff",
                       "0x008FE0", 32, 300, active_bgcolor="0xC9C9C9"),
            ]
        )

        container.content = ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Image("/logo.png", width=50,
                                         height=50, fit=ft.ImageFit.CONTAIN),
                                ft.Text("Apets", size=30, font_family="Quicksand Bold",
                                        color="0x008FE0")
                            ]
                        ),
                        self.nav_buttons
                    ]
                ), self.page_content
            ]
        )

        page.padding = ft.padding.all(0)
        page.add(background)
        page.scroll = ft.ScrollMode.ALWAYS
        page.update()

        self.makanan_controller = MakananController(self.page_content)
        self.riwayat_controller = RiwayatHewanController(self.page_content)
        self.hewan_controller = HewanController(self.makanan_controller, self.riwayat_controller,
                                                self.page_content)
        self.show_hewan_list_menu(None)

    def show_hewan_list_menu(self, e):
        self.page.floating_action_button = None
        self.change_menu(0)
        self.hewan_controller.handle_view()

    def show_list_makanan(self, e):
        self.page.floating_action_button = None
        self.change_menu(1)
        self.makanan_controller.handle_list_view()

    def change_menu(self, menu_idx: int):
        for i in range(3):
            self.nav_buttons.controls[i].toggle_active(i == menu_idx)


if __name__ == '__main__':
    ft.app(target=MainPage, name="Apets", assets_dir="assets")
