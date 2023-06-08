import flet as ft
from typing import Optional
from flet import OptionalNumber


class Text(ft.Text):
    def __init__(self, value: Optional[str] = None, color: Optional[str] = "black", font_family: Optional[str] = "Quicksand Bold", size: OptionalNumber = 32, width: OptionalNumber = None, text_align=ft.TextAlign.CENTER):
        super().__init__(value, color=color, font_family=font_family,
                         size=size, text_align=text_align, width=width, selectable=True)
