import sqlite3
import tkinter as tk



def verificar_valores():
    conexao = sqlite3.connect('Contatos.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM contatos")
    resultados = cursor.fetchall()
    for linha in resultados:
        print(f"Nome: {linha[0]}, Telefone: {linha[1]}, Email: {linha[2]}")
    conexao.close()


def adicionar_contato():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()
    
    if not nome or not telefone or not email:
        status_label.config(text="Todos os campos devem ser preenchidos.")
        return
    status_label.config(text="O contato foi adicionado com sucesso.")

    conexao = sqlite3.connect('Contatos.db')
    cursor = conexao.cursor()
    
    comando = '''
    INSERT INTO contatos (nome, telefone, email) 
    VALUES (?, ?, ?)
    '''

    cursor.execute(comando, (nome, telefone, email))
    
    conexao.commit()
    conexao.close()
    
    print(f"Contato {nome} adicionado com sucesso.")

    entrada_nome.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)
    entrada_email.delete(0, tk.END)



con = sqlite3.connect("Contatos.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS contatos(nome TEXT, telefone TEXT, email TEXT)")
res = cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='contatos'")
if res.fetchone():
    print("Tabela 'contatos' existe.")
else:
    print("Tabela 'contatos' não foi criada.")
con.close()

janela = tk.Tk()
janela.title("Agenda de Contatos")
janela.geometry("400x300")
janela.iconbitmap("./agenda.ico")



janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)
janela.rowconfigure(2, weight=1)
janela.rowconfigure(3, weight=1)

tk.Label(janela, text="Nome:", font=("Arial", 14)).grid(row=0, column=0, padx=20, pady=10, sticky="e")
entrada_nome = tk.Entry(janela, font=("Arial", 14))
entrada_nome.grid(row=0, column=1, padx=20, pady=10, sticky="w")

tk.Label(janela, text="Telefone:", font=("Arial", 14)).grid(row=1, column=0, padx=20, pady=10, sticky="e")
entrada_telefone = tk.Entry(janela, font=("Arial", 14))
entrada_telefone.grid(row=1, column=1, padx=20, pady=10, sticky="w")

tk.Label(janela, text="E-mail:", font=("Arial", 14)).grid(row=2, column=0, padx=20, pady=10, sticky="e")
entrada_email = tk.Entry(janela, font=("Arial", 14))
entrada_email.grid(row=2, column=1, padx=20, pady=10, sticky="w")

botao_adicionar = tk.Button(janela, text="Adicionar Contato", command=adicionar_contato, font=("Arial", 14))
botao_adicionar.grid(row=3, column=0, columnspan=2, pady=20)

status_label = tk.Label(janela,text="", font=("Arial", 14))
status_label.grid(row=4, column=0, columnspan=2, pady=20)

janela.mainloop()

verificar_valores()