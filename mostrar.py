import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import ctypes 


def minimize_consola():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
minimize_consola()

def get_images_directory(ruta_directorio):
    # Obtener la lista de archivos en el directorio
    files = os.listdir(ruta_directorio)

    # Filtrar los archivos para obtener solo las imágenes
    images = [archivo for archivo in files if archivo.lower().endswith(
        (".png", ".jpg", ".jpeg", ".gif", ".bmp"))]

    return images


def close_all_the_windows():
    for window in windows:
        window.destroy()
    sys.exit()


def show_images():
    # Ruta del directorio donde se encuentran las imágenes
    directory_path = "imagenes"

    # Obtener la lista de imágenes en el directorio
    images = get_images_directory(directory_path)

    # Verificar si hay imágenes en el directorio
    if images:
        # Coordenadas predefinidas para la primera windows
        positions = [(50, 450), (450, 450), (850, 450), (1250, 450)]

        for i, image in enumerate(images):
            # Coordenadas para la windows actual
            pos_x, pos_y = positions[i]

            # Crear una nueva windows para mostrar la imagen
            windows = tk.Toplevel()
            # Utiliza el nombre de la imagen como título de la windows
            windows.title(image)
            windows.geometry("300x400")  # Configura el tamaño de la windowsasd
            # Configura el color de fondo de la windows
            windows.configure(bg="#466CF9")
            # Hace que la windows no sea redimensionable en ningún eje
            windows.resizable(False, False)
            #windows.attributes('-topmost', True)  # windows siempre al frente
            windows.lift()  # windows siempre al frente
            windows.protocol("WM_DELETE_WINDOW", close_all_the_windows)
            # Cargar la imagen desde la ruta
            image_path = os.path.join(directory_path, image)
            imagen_obj = Image.open(image_path)
            # Redimensionar la imagen si es necesario
            imagen_obj = imagen_obj.resize((200, 200))

            # Convertir la imagen para mostrarla en Tkinter
            image_tk = ImageTk.PhotoImage(imagen_obj)

            # Crear una etiqueta para mostrar la imagen en la windows
            label_image = tk.Label(windows, image=image_tk)
            label_image.image = image_tk
            label_image.pack()

            # Ubicar la windows en las coordenadas predefinidas
            windows.geometry(f"+{pos_x}+{pos_y}")
            label_image.place(relx=0.5, rely=0.4, anchor="center")

            # Agregar la imagen en lugar del texto
            image_path_logo = "logo/nslogo.png"  # Ruta de la imagen que deseas agregar
            image_obj_logo = Image.open(image_path_logo)
            # Redimensionar la imagen si es necesario
            image_obj_logo =  image_obj_logo.resize((300, 100))
            image_tk_logo = ImageTk.PhotoImage(image_obj_logo)

            label_image_logo = tk.Label(windows, image=image_tk_logo)
            label_image_logo.image = image_tk_logo
            label_image_logo.place(relx=0.5, rely=0.9, anchor="center")

    else:
        print("No se encontraron imágenes en el directorio.")

    # Ejecutar el bucle principal de la windows
    windows.mainloop()


# Lista para almacenar las windowss
windows = []

# Crear la windows principal (root) y ocultarla
root = tk.Tk()
root.withdraw()

# Mostrar las imágenes automáticamente al ejecutar el script
show_images()
