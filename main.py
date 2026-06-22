import flet as ft

def main(page: ft.Page):
    page.title = "Simple Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    welcome_text = ft.Text("Welcome to Calculator", size=24, weight=ft.FontWeight.BOLD)
    num1_input = ft.TextField(label="First number", width=250, keyboard_type=ft.KeyboardType.NUMBER)
    num2_input = ft.TextField(label="Second number", width=250, keyboard_type=ft.KeyboardType.NUMBER)
    result_text = ft.Text("Answer: ", size=20, color=ft.Colors.GREEN)

    def add_clicked(e):
        try:
            n1 = float(num1_input.value)
            n2 = float(num2_input.value)
            result_text.value = f"Answer: {n1 + n2}"
        except ValueError:
            result_text.value = "Please enter valid numbers!"
        page.update()

    add_button = ft.ElevatedButton("Add Numbers", on_click=add_clicked, width=250)

    page.add(welcome_text, num1_input, num2_input, add_button, result_text)

ft.app(target=main)
