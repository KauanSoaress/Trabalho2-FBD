import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

# Escreve um novo script Python que chama o procedimento armazenado criado no item anterior passando
# como parâmetro a data 2023-10-01.
cur.execute("SELECT * FROM empregado_do_mes('2023-10-01')")

# Descompactando a tupla para pegar o valor da consulta
(idEmpregado, nomeEmpregado) = cur.fetchone()

# Fecha o cursor
cur.close()

# Fecha a conexão
conn.close()

# Exibindo os resultados da consulta
print("ID do empregado do mês: " + str(idEmpregado))
print("Nome do empregado do mês: " + nomeEmpregado)