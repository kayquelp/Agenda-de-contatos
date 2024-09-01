import sqlite3



conexao = sqlite3.connect('Contatos.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM contatos")

resultados = cursor.fetchall()
for linha in resultados:
    print(linha)

conexao.close()
