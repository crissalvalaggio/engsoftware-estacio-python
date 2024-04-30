import tkinter as tk
from tkinter import ttk
from time import strftime

#relogio ao vivo

def atualizar_horario():
    # Obter a hora atual
    horario_atual = strftime('%H:%M:%S %p')

    # Atualizar o rótulo com a hora atual
    lbl_horario['text'] = horario_atual

    # Atualizar o rótulo a cada 1000 milissegundos (1 segundo)
    lbl_horario.after(1000, atualizar_horario)

# Criar uma janela
janela = tk.Tk()
janela.title("Relógio Digital")

# Criar um rótulo para exibir a hora
lbl_horario = ttk.Label(janela, font=('calibri', 40, 'bold'), background='black', foreground='white')
lbl_horario.pack(anchor='center')

# Iniciar a função para atualizar o horário
atualizar_horario()

# Executar o loop principal da janela
janela.mainloop()