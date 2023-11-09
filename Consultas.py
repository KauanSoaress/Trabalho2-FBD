import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

# Retorne todas as embarcações e o número de tripulantes de cada embarcação.

# Retorne os Empregados envolvidos na movimentação de ID 1.
cur.execute("SELECT e.id_emp, e.nome, e.funcao FROM (Empregados e INNER JOIN Movimentacao_Empregados me ON e.id_emp = me.id_emp) INNER JOIN Movimentacao m ON me.id_mov=m.id_mov WHERE m.id_mov = 1")

empregados = cur.fetchall()

# Retorne a quantidade de movimentações que envolvem embarcações do tipo “Cargueiro”.

cur.close()

conn.close()

print("Consulta 1:")
print(empregados)

print("Consulta 2:")
print(empregados)

print("Consulta 3:")
print(empregados)