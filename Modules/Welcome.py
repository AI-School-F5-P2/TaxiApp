from art import text2art
import os
from colorama import Fore, Style

# Definir colores
red = Fore.RED
green = Fore.GREEN
cyan = Fore.CYAN
reset = Style.RESET_ALL


class Welcome:
    def display_welcome_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        result = text2art("                               TaxiApp", font="small")
        print(f"{cyan}{result}")
        print(
            f"{green}\n                                 👉 Bienvenido, pulse Enter para ingresar 👈{reset}"
        )


class AppInstructions:
    def __init__(self):
        self.title_color = cyan  # Color para el título
        self.text_color = green  # Color para el texto
        self.bullet_point = "\u2756"  # Viñeta

    def print_formatted_text(self, text, color):
        print(f"{color}{text}{reset}")

    def display_title(self):
        self.print_formatted_text(
            "\n\n\u2728 La TaxiApp es una aplicación que simula un taxímetro y calcula el precio final de una carrera teniendo en cuenta dos tarifas:",
            self.title_color,
        )
        self.print_formatted_text(
            "    una para cuando el vehículo está en movimiento y otra para cuando está detenido.",
            self.title_color,
        )

    def display_instructions(self):
        print("\nInstrucciones:")
        instructions = f"\n{self.bullet_point}   Para iniciar una carrera, presiona la tecla 'Enter'. En este momento, la aplicación comenzará a calcular el precio con la tarifa de 'detenido'."
        instructions += f"\n\n{self.bullet_point}   Cada vez que el vehículo se ponga en movimiento, presiona la tecla 'Espacio' y calculará con la tarifa 'en movimiento'."
        instructions += f"\n\n{self.bullet_point}   Cuando el vehículo se detenga, presiona nuevamente la tecla 'Espacio'. La aplicación se detendrá y calculará el precio utilizando la tarifa de 'detenido'."
        instructions += f"\n\n{self.bullet_point}   Para finalizar la carrera, presiona la tecla 'Enter'. La aplicación mostrará en pantalla el total a pagar en euros."
        instructions += f"\n\n{self.bullet_point}   La aplicación quedará en espera, lista para iniciar una nueva carrera cuando se presione nuevamente la tecla 'Enter'."
        self.print_formatted_text(instructions, self.text_color)
        print(
            "\nDe esta manera, podrás utilizar la TaxiApp para simular tus carreras y conocer el precio estimado de cada una. ¡Disfruta de tu viaje!"
        )

    def again(self):
        user_input = input('Pulsa Enter para calcular otro viaje')
        if user_input == "":
            pass
        else:
            return False

    def main_screen(self):
        welcome = Welcome()
        welcome.display_welcome_screen()
        self.display_title()
        self.display_instructions()


#instructions = AppInstructions()
#instructions.main_screen()