import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

cur.execute("CALL empregado_do_mes('2023-11-09');")

cur.close()

conn.close()