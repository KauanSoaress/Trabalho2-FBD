import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

# Criando o procedimento que deve realizar 1. Crie um procedimento armazenado no banco de dados com nome empregado do mes que recebe como
# parâmetro uma data e retorna o id e nome do empregado que participou de mais movimentações naquela
# combinação Ano/Mês;
cur.execute("""
            CREATE OR REPLACE FUNCTION empregado_do_mes(IN data_parametro DATE)
            RETURNS TABLE (empregado_id INTEGER, empregado_nome VARCHAR)
            AS $$
            BEGIN
                -- Seleciona o empregado que participou de mais movimentações naquele mês
                SELECT e.id_emp, e.nome INTO empregado_id, empregado_nome
                FROM Empregados e 
                INNER JOIN Movimentacao_Empregados me ON e.id_emp = me.id_emp
                INNER JOIN Movimentacao mov ON me.id_mov=mov.id_mov
                WHERE EXTRACT(MONTH FROM mov.data) = EXTRACT(MONTH FROM data_parametro) AND EXTRACT(YEAR FROM mov.data) = EXTRACT(YEAR FROM data_parametro)
                GROUP BY e.id_emp, e.nome
                ORDER BY COUNT(*) DESC
                LIMIT 1;

                RETURN NEXT;
            END;
            $$ LANGUAGE plpgsql;
""")

# Commitar as inserções
conn.commit()

cur.close()

conn.close()