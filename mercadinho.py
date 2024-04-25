import flet as ft

def main(page: ft.Page):
    #page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 390
    page.title = 'Mercadinho'
    page.window_always_on_top = True









ft.app(target=main)