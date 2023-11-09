import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

cur.execute("""CREATE OR REPLACE PROCEDURE empregado_do_mes(data_parametro DATE)
LANGUAGE plpgsql
AS $$
DECLARE
    max_movimentacoes int := 0;
    empregado_id int;
    empregado_nome text;
	empregado_rec empregados%rowtype;
BEGIN
    FOR empregado_rec IN
        SELECT e.id_emp, e.nome, COUNT(m.id_mov) AS num_movimentacoes
        FROM (empregados e INNER JOIN movimentacao_empregados me ON me.id_emp = e.id_emp) INNER JOIN movimentacao m ON m.id_mov = me.id_mov
        WHERE EXTRACT(YEAR FROM m.data) = EXTRACT(YEAR FROM data_parametro)
          AND EXTRACT(MONTH FROM m.data) = EXTRACT(MONTH FROM data_parametro)
        GROUP BY e.id_emp, e.nome
    LOOP
        IF empregado_rec.num_movimentacoes > max_movimentacoes THEN
            max_movimentacoes := empregado_rec.num_movimentacoes;
            empregado_id := empregado_rec.id_emp;
            empregado_nome := empregado_rec.nome;
        END IF;
    END LOOP;

    -- Imprime o resultado na saída
    RAISE NOTICE 'Empregado do mês: ID= %, Nome= %', empregado_id, empregado_nome;
END;
$$;""")

# Commitar as inserções
conn.commit()

cur.close()

conn.close()