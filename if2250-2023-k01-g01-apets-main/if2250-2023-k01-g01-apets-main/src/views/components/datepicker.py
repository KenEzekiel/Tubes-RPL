from flet import UserControl, Dropdown, Row, Container, Icon, dropdown, icons, colors, MainAxisAlignment
import datetime
from typing import Union


class DateSelector(UserControl):
    """Date selector."""

    def __init__(self):
        super().__init__()

        self.day_dropdown = Dropdown(
            label="D",
            options=[
                dropdown.Option(day) for day in range(1, 32)
            ],
            color="black",
            bgcolor=colors.WHITE,
            width=50,
        )

        self.month_dropdown = Dropdown(
            label="M",
            options=[
                dropdown.Option(month) for month in range(1, 13)
            ],
            color="black",
            bgcolor=colors.WHITE,
            width=50,
        )

        self.year_dropdown = Dropdown(
            label="Y",
            options=[
                dropdown.Option(year) for year in range(2005, 2024)
            ],
            color="black",
            bgcolor=colors.WHITE,
            width=100,
        )

        self.view = Container(
            content=Row(
                [
                    self.day_dropdown,
                    self.month_dropdown,
                    self.year_dropdown,
                ],
                alignment=MainAxisAlignment.START,
            )
        )

    def build(self):
        return self.view

    def get_date(self) -> Union[datetime.date, None]:
        """Return the selected timeframe."""
        if self.year_dropdown.value is None or self.month_dropdown.value is None or self.day_dropdown.value is None:
            return None

        date = datetime.date(
            year=int(self.year_dropdown.value),
            month=int(self.month_dropdown.value),
            day=int(self.day_dropdown.value),
        )
        return date
