import flet as ft
from typing import Optional, Union


class Button(ft.ElevatedButton):
    def __init__(self, text: Optional[str] = None, bgcolor: Optional[str] = None, color: Optional[str] = None, size: Union[None, int, float] = 30, width: Union[None, int, float] = None, active_bgcolor: Optional[str] = None, on_click=None):
        super().__init__(content=ft.Text(
            text, size=size, font_family="Quicksand Bold", color=color),
            bgcolor=bgcolor,
            elevation=5,
            on_click=on_click, width=width, style=ft.ButtonStyle(
            padding=ft.padding.symmetric(6, 4),
        ))
        self.active_bgcolor = active_bgcolor
        self.normal_bgcolor = bgcolor

    def toggle_active(self, active: bool):
        if self.active_bgcolor is None:
            return

        if active:
            self.bgcolor = self.active_bgcolor
        else:
            self.bgcolor = self.normal_bgcolor
        self.update()
