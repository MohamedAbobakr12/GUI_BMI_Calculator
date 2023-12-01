import flet as ft


def main(page: ft.page):
    page.window_width = 850
    page.window_height = 520
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_resizable = False
    page.bgcolor = "#242423"
    page.title = "BMI Calculator"

    height = ft.TextField(value="0", height=50, width=120, label="Height", text_align="center", suffix_text="cm")
    weight = ft.TextField(value="0", height=50, width=120, label="Weight", text_align="center", suffix_text="kg")
    calc = ft.TextField(height=55, width=120, label="BMI", text_align="center", disabled=True)
    rated = ft.TextField(height=55, width=140, label="Rating", text_align="center", disabled=True)

    def height_sub(e):
        height.value = str(int(height.value) - 1)
        page.update()

    def height_add(e):
        height.value = str(int(height.value) + 1)
        page.update()

    def weight_sub(e):
        weight.value = str(int(weight.value) - 1)
        page.update()

    def weight_add(e):
        weight.value = str(int(weight.value) + 1)
        page.update()

    def calc_bmi(e):
        try:
            kg = (int(weight.value) * 10000)
            m2 = (int(height.value) ** 2)
            try:
                total = float(kg / m2)
            except ZeroDivisionError:
                def close_dlg(e):
                    message.open = False
                    page.update()

                message = ft.AlertDialog(title=ft.Text(value="Division Error", color="#f5cb5c", font_family="poppins"),
                                         content=ft.Text(value="You Can't Divide on Zero", color="#f5cb5c", size=25,
                                                         font_family="poppins"), modal=True, open=True, actions=[
                        ft.IconButton(icon=ft.icons.DONE, icon_color="#f5cb5c", on_click=close_dlg)],
                                         actions_alignment="end")
                page.add(message)

            total = round(total, 2)
            calc.value = total
            if (int(calc.value) < 16):
                rated.value = "Underweight III"
            elif (int(calc.value) >= 16 and int(calc.value) <= 16.9):
                rated.value = "Underweight II"
            elif (int(calc.value) >= 17 and int(calc.value) <= 18.4):
                rated.value = "Underweight I"
            elif (int(calc.value) >= 18.5 and int(calc.value) <= 24.9):
                rated.value = "Normal"
            elif (int(calc.value) >= 25 and int(calc.value) <= 29.9):
                rated.value = "Overweight"
            elif (int(calc.value) >= 30 and int(calc.value) <= 34.9):
                rated.value = "Obese I"
            elif (int(calc.value) >= 35 and int(calc.value) <= 39.9):
                rated.value = "Obese II"
            elif (int(calc.value) >= 40):
                rated.value = "Obese III"
        except ValueError:
            def close_dlg(e):
                message.open = False
                page.update()

            message = ft.AlertDialog(title=ft.Text(value="Input Error", color="#f5cb5c", font_family="poppins"),
                                     content=ft.Text(value="You Can't Add Non-Numeric Inputs", color="#f5cb5c", size=25,
                                                     font_family="poppins"), modal=True, open=True, actions=[
                    ft.IconButton(icon=ft.icons.DONE, icon_color="#f5cb5c", on_click=close_dlg)],
                                     actions_alignment="end")
            page.add(message)
        page.update()

    page.add(ft.Text(value="BMI Calculator", color="#f5cb5c", font_family="poppins", size=50))

    page.add(ft.Row(alignment='center', controls=[
        ft.IconButton(icon=ft.icons.REMOVE, on_click=height_sub, icon_color="#f5cb5c"),
        height,
        ft.IconButton(icon=ft.icons.ADD, on_click=height_add, icon_color="#f5cb5c")]))

    page.add(ft.Row(alignment='center', controls=[
        ft.IconButton(icon=ft.icons.REMOVE, on_click=weight_sub, icon_color="#f5cb5c"),
        weight,
        ft.IconButton(icon=ft.icons.ADD, on_click=weight_add, icon_color="#f5cb5c")]))

    page.add(ft.Row(alignment='center', controls=[calc,
                                                  ft.IconButton(icon=ft.icons.CALCULATE_ROUNDED, icon_color="#f5cb5c",
                                                                icon_size=35, tooltip="Calculate", on_click=calc_bmi),
                                                  rated]))


ft.app(target=main)
