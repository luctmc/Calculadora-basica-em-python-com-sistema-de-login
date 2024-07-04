import tkinter as tk
from tkinter import messagebox
from hashlib import sha256

# Simulando um banco de dados
users = {}

# Função para registrar um novo usuário
def register():
    username = entry_username_reg.get()
    password = entry_password_reg.get()
    confirm_password = entry_confirm_password_reg.get()

    if username in users:
        messagebox.showerror("Erro", "Usuário já existe!")
        return

    if password != confirm_password:
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return

    hashed_password = sha256(password.encode()).hexdigest()
    users[username] = hashed_password
    messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
    entry_username_reg.delete(0, tk.END)
    entry_password_reg.delete(0, tk.END)
    entry_confirm_password_reg.delete(0, tk.END)

# Função para fazer login
def login():
    username = entry_username_login.get()
    password = entry_password_login.get()
    hashed_password = sha256(password.encode()).hexdigest()

    if username in users and users[username] == hashed_password:
        messagebox.showinfo("Sucesso", "Login bem-sucedido!")
        show_calculator()
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos!")

# Função para exibir a janela de cadastro
def show_register():
    login_frame.pack_forget()
    register_frame.pack()

# Função para exibir a janela de login
def show_login():
    register_frame.pack_forget()
    login_frame.pack()

# Função para exibir a janela da calculadora
def show_calculator():
    login_frame.pack_forget()
    register_frame.pack_forget()
    calculator_frame.pack()

# Função para realizar operações matemáticas
def calculate():
    expression = entry_expression.get()
    try:
        result = eval(expression)
        label_result.config(text=f"Resultado: {result}")
    except Exception as e:
        label_result.config(text="Erro na expressão")

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Login e Calculadora")
root.geometry("300x400")

# Frame de Registro
register_frame = tk.Frame(root)

label_username_reg = tk.Label(register_frame, text="Usuário")
label_username_reg.pack()
entry_username_reg = tk.Entry(register_frame)
entry_username_reg.pack()

label_password_reg = tk.Label(register_frame, text="Senha")
label_password_reg.pack()
entry_password_reg = tk.Entry(register_frame, show="*")
entry_password_reg.pack()

label_confirm_password_reg = tk.Label(register_frame, text="Confirmar Senha")
label_confirm_password_reg.pack()
entry_confirm_password_reg = tk.Entry(register_frame, show="*")
entry_confirm_password_reg.pack()

button_register = tk.Button(register_frame, text="Registrar", command=register)
button_register.pack()

button_show_login_from_reg = tk.Button(register_frame, text="Já tem uma conta? Faça login", command=show_login)
button_show_login_from_reg.pack()

# Frame de Login
login_frame = tk.Frame(root)

label_username_login = tk.Label(login_frame, text="Usuário")
label_username_login.pack()
entry_username_login = tk.Entry(login_frame)
entry_username_login.pack()

label_password_login = tk.Label(login_frame, text="Senha")
label_password_login.pack()
entry_password_login = tk.Entry(login_frame, show="*")
entry_password_login.pack()

button_login = tk.Button(login_frame, text="Login", command=login)
button_login.pack()

button_show_register_from_login = tk.Button(login_frame, text="Não tem uma conta? Cadastre-se", command=show_register)
button_show_register_from_login.pack()

# Frame da Calculadora
calculator_frame = tk.Frame(root)

label_welcome = tk.Label(calculator_frame, text="Bem-vindo à Calculadora")
label_welcome.pack()

label_expression = tk.Label(calculator_frame, text="Expressão")
label_expression.pack()
entry_expression = tk.Entry(calculator_frame)
entry_expression.pack()

button_calculate = tk.Button(calculator_frame, text="Calcular", command=calculate)
button_calculate.pack()

label_result = tk.Label(calculator_frame, text="")
label_result.pack()

# Inicializando a interface com a janela de login
show_login()

# Inicializando a interface
root.mainloop()
