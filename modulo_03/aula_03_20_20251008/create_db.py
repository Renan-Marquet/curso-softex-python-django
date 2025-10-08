# importa biblioteca do  
import sqlite3
conn = sqlite3.connect('meu_banco2.db')
print("Banco de dados'meu_banco2.db' criado com sucesso!")
conn.close()