from tkinter import messagebox, Label, Button, FALSE, Tk, Entry, PhotoImage
import re
# Diccionario para almacenar los usuarios registrados
users = {"":""}

def try_login():
    user = user_guess.get()
    password = contra_guess.get()


    if user.strip() and password.strip():
        if user in users and users[user] == password:
            messagebox.showinfo("-- BIENVENIDO --", "Estás logeado", icon="info")
        else:
            messagebox.showinfo("-- ERROR --", "¡Por favor ingresa la información correcta!", icon="warning")
    else:
        messagebox.showinfo("-- ERROR --", "¡Por favor ingresa un correo y contraseña!", icon="warning")

def register():
    user = user_guess.get()
    password = contra_guess.get()
    
    # Verificar el formato del correo electrónico
    if not re.match(r"[^@]+@gmail\.com$", user):
        messagebox.showinfo("-- ERROR --", "¡Por favor ingresa un correo válido de Gmail!", icon="warning")
        return
    
    # Verificar la longitud y caracteres de la contraseña
    if not re.match(r"^[a-zA-Z0-9]{5,8}$", password):
        messagebox.showinfo("-- ERROR --", "¡La contraseña debe tener entre 5 y 8 caracteres alfanuméricos!", icon="warning")
        return
    
    if user and password:
        users[user] = password
        messagebox.showinfo("-- REGISTRADO --", "¡Usuario registrado con éxito!", icon="info")
    else:
        messagebox.showinfo("-- ERROR --", "¡Por favor ingresa un correo y contraseña!", icon="warning")


# Ventana principal
ventana = Tk()
ventana.resizable(0, 0)
ventana.title("Inicio de sesión")
ventana.geometry("300x250")


# Etiquetas y campos de entrada para nombre de usuario y contraseña
user_text = Label(ventana, text="Correo:", justify="left", font=("Arial", 10, "bold"))
user_guess = Entry(ventana)
contra_text = Label(ventana, text="Contraseña:", justify="left", font=("Arial", 10, "bold") )
contra_guess = Entry(ventana, show="*")


# Botón de inicio de sesión
buttonl_style = {"bg": "green", "fg": "#FFFFFF", "font": ("Arial", 12, "bold"), "relief": "flat", "width": 15} #bg = colorfondo, fg = colortexto, font = fuente, relief = relieve del boton, width = ancho
login_btn = Button(text="Ingresar", command=try_login, **buttonl_style)


# Botón de registro 
buttonr_style = {"bg": "green", "fg": "#FFFFFF", "font": ("Arial", 12, "bold"), "relief": "flat", "width": 15}
registro_btn = Button(text="Registrarse", command=register, **buttonr_style)

# Espacio en blanco
espaciador1 = Label(ventana, text=" ", width=50)
espaciador2 = Label(ventana, text=" ", width=50)


# Empaquetar los elementos en la ventana
user_text.pack()
user_guess.pack()
contra_text.pack()
contra_guess.pack()
espaciador1.pack()
login_btn.pack()
espaciador2.pack()
registro_btn.pack()

# Iniciar la aplicación
ventana.mainloop()