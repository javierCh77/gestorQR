import os
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import qrcode
from PIL import Image, ImageTk, ImageDraw, ImageFont  # Import ImageFont
from datetime import datetime

def generar_qr(data, filename, ip_text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Crear el objeto ImageDraw
    draw = ImageDraw.Draw(img)
    
    
    # Agregar texto de la IP encima del código QR
    font = ImageFont.truetype("arial.ttf", 30)  # Specify font and size
    x = 95  # Ajusta la coordenada x según sea necesario
    y = -4  # Ajusta la coordenada y para agregar un espacio entre la QR y el texto IP
    draw.text((x, y), f"IP: {ip_text}", fill=("black"), font=font)
    
    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Guardar la imagen en el archivo
    img.save(filename)
    return img

def leer_qr():
    ssid = entry_ssid.get()
    tipo = entry_tipo.get()
    password = entry_password.get()
    hidden = entry_hidden.get()
    ip_address = entry_ip.get()
    
    if not ssid or not tipo or not password or not hidden or not ip_address:
        messagebox.showwarning("Campos incompletos", "Todos los campos son obligatorios.")
        return
    
    data_str = f'MOTO-WIFI:S:{ssid};T:{tipo};P:{password};H:{hidden};IP:{ip_address};'
    
    # Definir el nombre del archivo y la ruta
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f'imagenes/codigo_qr_{timestamp}.png'
    
    # Generar y guardar el código QR
    img = generar_qr(data_str, filename, ip_address)
    
    # Mostrar el mensaje de información
    messagebox.showinfo("Texto QR", f"Contenido del QR:\n{data_str}\n\n¡QR guardado como '{filename}'!")
    
    # Mostrar la QR en la ventana
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

root = tk.Tk()
root.title("Generador y Lector de Código QR")

# Configurar la geometría de la ventana
root.geometry("400x500")
root.resizable(False, False)

# Crear y organizar los widgets
tk.Label(root, text="SSID:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
entry_ssid = tk.Entry(root)
entry_ssid.grid(row=0, column=1, padx=10, pady=10, sticky=tk.EW)

tk.Label(root, text="Tipo (T):").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
entry_tipo = tk.Entry(root)
entry_tipo.grid(row=1, column=1, padx=10, pady=10, sticky=tk.EW)

tk.Label(root, text="Contraseña (P):").grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
entry_password = tk.Entry(root)
entry_password.grid(row=2, column=1, padx=10, pady=10, sticky=tk.EW)

tk.Label(root, text="Oculto (H) (true/false):").grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
entry_hidden = tk.Entry(root)
entry_hidden.grid(row=3, column=1, padx=10, pady=10, sticky=tk.EW)

tk.Label(root, text="IP:").grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
entry_ip = tk.Entry(root)
entry_ip.grid(row=4, column=1, padx=10, pady=10, sticky=tk.EW)

tk.Button(root, text="Generar QR", command=leer_qr).grid(row=5, columnspan=2, pady=10)

# Etiqueta para mostrar la QR generada
qr_label = tk.Label(root)
qr_label.grid(row=6, columnspan=2, pady=10)

# Ajustar el tamaño de las columnas
root.grid_columnconfigure(1, weight=1)

root.mainloop()