import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

# Inserindo dados na tabela Embarcacoes
cur.execute("INSERT INTO Embarcacoes(id_emb, nome, tipo) VALUES (%s, %s, %s)", (1, 'Navio1', 'Cargueiro'))
cur.execute("INSERT INTO Embarcacoes(id_emb, nome, tipo) VALUES (%s, %s, %s)", (2, 'Navio2', 'Passageiro'))
cur.execute("INSERT INTO Embarcacoes(id_emb, nome, tipo) VALUES (%s, %s, %s)", (3, 'Navio3', 'Petroleiro'))
cur.execute("INSERT INTO Embarcacoes(id_emb, nome, tipo) VALUES (%s, %s, %s)", (4, 'Navio4', 'Cargueiro'))

# Inserindo dados na tabela Tripulantes
cur.execute("INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s, %s)", (1, 'Tripulante1', '1990-01-15', 'Oficial de Convés', 1))
cur.execute("INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s, %s)", (2, 'Tripulante2', '1992-03-20', 'Engenheiro', 1))
cur.execute("INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s, %s)", (3, 'Tripulante3', '1988-11-05', 'Comissário de Bordo', 2))
cur.execute("INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s, %s)", (4, 'Tripulante4', '1995-06-30', 'Oficial de Convés', 3))
cur.execute("INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s, %s)", (5, 'Tripulante5', '1991-07-10', 'Capitão', 4))
cur.execute("INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s, %s)", (6, 'Tripulante6', '1994-09-25', 'Engenheiro', 4))

# Inserindo dados na tabela Empregados
cur.execute("INSERT INTO Empregados(id_emp, nome, data_nasc, funcao) VALUES (%s, %s, %s, %s)", (1, 'Employee1', '1985-05-12', 'Manutenção'))
cur.execute("INSERT INTO Empregados(id_emp, nome, data_nasc, funcao) VALUES (%s, %s, %s, %s)", (2, 'Employee2', '1993-02-28', 'Segurança'))
cur.execute("INSERT INTO Empregados(id_emp, nome, data_nasc, funcao) VALUES (%s, %s, %s, %s)", (3, 'Employee3', '1987-09-18', 'Logística'))
cur.execute("INSERT INTO Empregados(id_emp, nome, data_nasc, funcao) VALUES (%s, %s, %s, %s)", (4, 'Employee4', '1990-12-05', 'Limpeza'))
cur.execute("INSERT INTO Empregados(id_emp, nome, data_nasc, funcao) VALUES (%s, %s, %s, %s)", (5, 'Employee5', '2001-08-30', 'Manutenção'))

# Inserindo dados na tabela Movimentacao
cur.execute("INSERT INTO Movimentacao(id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (1, '2023-09-01', 'Carga', 1))
cur.execute("INSERT INTO Movimentacao(id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (2, '2023-09-02', 'Embarque de Passageiros', 2))
cur.execute("INSERT INTO Movimentacao(id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (3, '2023-10-03', 'Abastecimento', 3))
cur.execute("INSERT INTO Movimentacao(id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (4, '2023-10-05', 'Descarga', 1))
cur.execute("INSERT INTO Movimentacao(id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (5, '2023-10-05', 'Manutenção', 4))

# Inserindo dados na tabela Movimentacao_Empregados
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (1, 1))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (1, 3))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (2, 2))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (3, 1))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (3, 4))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (4, 1))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (4, 3))
cur.execute("INSERT INTO Movimentacao_Empregados(id_mov, id_emp) VALUES (%s, %s)", (5, 1))

# Commitar as inserções
conn.commit()

cur.close()

conn.close()