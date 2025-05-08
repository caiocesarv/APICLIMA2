import customtkinter as ctk
import requests
from tkinter import messagebox

# Configurações iniciais do customtkinter
ctk.set_appearance_mode("System")  # "Dark", "Light", ou "System"
ctk.set_default_color_theme("blue")  # Pode trocar para "dark-blue", "green", etc.

# Sua chave da API
API_KEY = ""

def buscar_clima():
    cidade = entrada_cidade.get().strip().replace(" ", "%20")
    if cidade:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br&units=metric"
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            dados = resposta.json()

            clima = dados["weather"][0]["description"]
            temperatura = dados["main"]["temp"]

            resultado = f"Clima: {clima.capitalize()}\n Temperatura: {temperatura}°C"
            label_resultado.configure(text=resultado)

        except requests.exceptions.HTTPError:
            messagebox.showerror("Erro", "Cidade não encontrada ou chave inválida.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")
    else:
        messagebox.showwarning("Atenção", "Por favor, digite uma cidade.")

# Janela principal
app = ctk.CTk()
app.geometry("400x300")
app.title("Consulta Clima")

# Título
titulo = ctk.CTkLabel(app, text="Consultar o clima atual", font=ctk.CTkFont(size=18, weight="bold"))
titulo.pack(pady=20)

# Campo de entrada
entrada_cidade = ctk.CTkEntry(app, placeholder_text="Digite o nome da cidade")
entrada_cidade.pack(pady=10)

# Botão de busca
botao_buscar = ctk.CTkButton(app, text="Buscar Clima", command=buscar_clima)
botao_buscar.pack(pady=10)

# Resultado
label_resultado = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
label_resultado.pack(pady=20)

# Iniciar
app.mainloop()


