import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Iniciando a transação
try:
    # Criando um cursor
    cur = conn.cursor()
    
    # 1. Inserir nova Movimentação: (6, ‘2023-10-05’, ‘Manutenção’, 1)
    cur.execute("INSERT INTO Movimentacao (id_mov, data, tipo, id_emb) VALUES (%s, %s, %s, %s)", (6, '2023-10-05', 'Manutenção', 1))
    
    # 2. Inserir nova Movimentação_Empregado: (6, 1)
    cur.execute("INSERT INTO Movimentacao_Empregados (id_mov, id_emp) VALUES (%s, %s)", (6, 1))
    
    # 3. Retornar a quantidade de movimentacões que envolvem embarcacões do tipo “Cargueiro”.
    cur.execute("SELECT COUNT(*) "
                "FROM Movimentacao m INNER JOIN Embarcacoes e ON m.id_emb = e.id_emb "
                "WHERE e.tipo = 'Cargueiro'")
    
    # 3.1 Descompactando a tupla para pegar o valor da consulta 3
    consulta_3 = cur.fetchone()[0]
    
    # 3.2 Imprimindo o resultado da instrução 3 
    print(f"Consulta 3: {consulta_3}")
    
    # Commitando a transação
    conn.commit()
    
    # Fechando o cursor
    cur.close()
    
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    conn.rollback()

finally:
    if conn is not None:
        # Fechando a conexão
        conn.close()
