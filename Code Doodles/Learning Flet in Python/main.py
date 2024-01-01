import flet as ft


def main(page: ft.Page) -> None:
    page.title = "Increment Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    textNumber = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=80)

    def decrement(e: ft.ControlEvent) -> None:
        if int(textNumber.value) > 0:
            textNumber.value = str(int(textNumber.value) - 1)
        page.update()

    def increment(e: ft.ControlEvent) -> None:
        textNumber.value = str(int(textNumber.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=decrement),
                textNumber,
                ft.IconButton(ft.icons.ADD, on_click=increment),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
