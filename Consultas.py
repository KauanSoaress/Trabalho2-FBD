import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

# 1. Retorne todas as embarcações e o número de tripulantes de cada embarcação.
cur.execute("SELECT e.nome, COUNT(trp.id_trp) "
            "FROM Embarcacoes e INNER JOIN Tripulantes trp ON e.id_emb = trp.id_emb "
            "GROUP BY e.nome "
            "ORDER BY e.nome ASC")

# Acessando os valores da consulta 1
consulta_1 = cur.fetchall()

# 2. Retorne os Empregados envolvidos na movimentação de ID 1.
cur.execute("SELECT e.id_emp, e.nome, e.funcao " 
            "FROM (Empregados e INNER JOIN Movimentacao_Empregados me ON e.id_emp = me.id_emp) INNER JOIN Movimentacao m ON me.id_mov=m.id_mov " 
            "WHERE m.id_mov = 1")

# Acessando os valores da consulta 2
consulta_2 = cur.fetchall()

# 3. Retorne a quantidade de movimentações que envolvem embarcações do tipo “Cargueiro”.
cur.execute("SELECT COUNT(*) " 
            "FROM Movimentacao m INNER JOIN Embarcacoes e ON m.id_emb = e.id_emb " 
            "WHERE e.tipo = 'Cargueiro'")

# Descompactando a tupla para pegar o valor da consulta 3
consulta_3 = cur.fetchone()[0]

# Fechando o cursor
cur.close()

# Fechando a conexão
conn.close()

# Imprimindo os resultados
print("Consulta 1:")
print(consulta_1)

print("\nConsulta 2:")
print(consulta_2)

print("\nConsulta 3:")
print(consulta_3)