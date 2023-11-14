import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

cur.execute("""
            INSERT INTO movimentacao_empregados(id_mov, id_emp)
            VALUES (5, 5)
""")
cur.execute("""
            INSERT INTO movimentacao_empregados(id_mov, id_emp)
            VALUES (5, 2)
""")

cur.execute("""
            UPDATE Tripulantes
            SET funcao = 'Capitão'
            WHERE id_trp = 3
""")

# Commitar
conn.commit()

cur.close()

conn.close()