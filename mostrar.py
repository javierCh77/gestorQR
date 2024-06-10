import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import ctypes 


def minimizar_consola():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
# Minimizar la consola al inicio
minimizar_consola()

def obtener_imagenes_directorio(ruta_directorio):
    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(ruta_directorio)

    # Filtrar los archivos para obtener solo las imágenes
    imagenes = [archivo for archivo in archivos if archivo.lower().endswith(
        (".png", ".jpg", ".jpeg", ".gif", ".bmp"))]

    return imagenes


def cerrar_todas_las_ventanas():
    for ventana in ventanas:
        ventana.destroy()
    sys.exit()


def mostrar_imagenes():
    # Ruta del directorio donde se encuentran las imágenes
    ruta_directorio = "imagenes"

    # Obtener la lista de imágenes en el directorio
    imagenes = obtener_imagenes_directorio(ruta_directorio)

    # Verificar si hay imágenes en el directorio
    if imagenes:
        # Coordenadas predefinidas para la primera ventana
        posiciones = [(50, 450), (450, 450), (850, 450), (1250, 450)]

        for i, imagen in enumerate(imagenes):
            # Coordenadas para la ventana actual
            pos_x, pos_y = posiciones[i]

            # Crear una nueva ventana para mostrar la imagen
            ventana = tk.Toplevel()
            # Utiliza el nombre de la imagen como título de la ventana
            ventana.title(imagen)
            ventana.geometry("300x400")  # Configura el tamaño de la ventanaasd
            # Configura el color de fondo de la ventana
            ventana.configure(bg="#466CF9")
            # Hace que la ventana no sea redimensionable en ningún eje
            ventana.resizable(False, False)
            #ventana.attributes('-topmost', True)  # Ventana siempre al frente
            ventana.lift()  # ventana siempre al frente
            ventana.protocol("WM_DELETE_WINDOW", cerrar_todas_las_ventanas)
            # Cargar la imagen desde la ruta
            imagen_ruta = os.path.join(ruta_directorio, imagen)
            imagen_obj = Image.open(imagen_ruta)
            # Redimensionar la imagen si es necesario
            imagen_obj = imagen_obj.resize((200, 200))

            # Convertir la imagen para mostrarla en Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen_obj)

            # Crear una etiqueta para mostrar la imagen en la ventana
            etiqueta_imagen = tk.Label(ventana, image=imagen_tk)
            etiqueta_imagen.image = imagen_tk
            etiqueta_imagen.pack()

            # Ubicar la ventana en las coordenadas predefinidas
            ventana.geometry(f"+{pos_x}+{pos_y}")
            etiqueta_imagen.place(relx=0.5, rely=0.4, anchor="center")

            # Agregar la imagen en lugar del texto
            imagen_ruta_logo = "logo/nslogo.png"  # Ruta de la imagen que deseas agregar
            imagen_obj_logo = Image.open(imagen_ruta_logo)
            # Redimensionar la imagen si es necesario
            imagen_obj_logo = imagen_obj_logo.resize((300, 100))
            imagen_tk_logo = ImageTk.PhotoImage(imagen_obj_logo)

            etiqueta_imagen_logo = tk.Label(ventana, image=imagen_tk_logo)
            etiqueta_imagen_logo.image = imagen_tk_logo
            etiqueta_imagen_logo.place(relx=0.5, rely=0.9, anchor="center")

    else:
        print("No se encontraron imágenes en el directorio.")

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()


# Lista para almacenar las ventanas
ventanas = []

# Crear la ventana principal (root) y ocultarla
root = tk.Tk()
root.withdraw()

# Mostrar las imágenes automáticamente al ejecutar el script
mostrar_imagenes()
