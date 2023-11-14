import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

cur.execute("""
            CREATE OR REPLACE FUNCTION check_capitao()
            RETURNS TRIGGER AS $$
            DECLARE
              existing_capitao INTEGER;
            BEGIN
              IF NEW.funcao = 'Capitão' THEN
                IF TG_OP = 'UPDATE' THEN
                  SELECT COUNT(*) INTO existing_capitao 
                  FROM Tripulantes 
                  WHERE funcao = 'Capitão' 
                  AND id_emb = NEW.id_emb 
                  AND id_trp != OLD.id_trp;
                ELSE
                  SELECT COUNT(*) INTO existing_capitao 
                  FROM Tripulantes 
                  WHERE funcao = 'Capitão' 
                  AND id_emb = NEW.id_emb;
                END IF;
                IF existing_capitao > 0 THEN
                  RAISE EXCEPTION 'Já existe um Capitão registrado nesta embarcação';
                END IF;
              END IF;
              RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER tripulante_check_capitao
            BEFORE INSERT OR UPDATE OF funcao, id_emb ON Tripulantes
            FOR EACH ROW
            EXECUTE FUNCTION check_capitao();
""")

cur.execute("""
            CREATE OR REPLACE FUNCTION restringe_mov()
            RETURNS TRIGGER AS $$
            DECLARE
              funcao_empregado TEXT;
              tipo_movimentacao TEXT;
            BEGIN
              SELECT e.funcao INTO funcao_empregado
              FROM Empregados e 
              WHERE e.id_emp = NEW.id_emp;

              SELECT mov.tipo INTO tipo_movimentacao
              FROM Movimentacao mov
              WHERE mov.id_mov = NEW.id_mov;

              IF tipo_movimentacao = 'Manutenção' AND funcao_empregado != 'Manutenção' THEN
              RAISE EXCEPTION 'Somente empregados da manutenção podem ser escolhidos para executar movimentações desse tipo';
              END IF;

              RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER restringe_mov_empregados
            BEFORE INSERT ON movimentacao_empregados
            FOR EACH ROW
            EXECUTE FUNCTION restringe_mov();
""")

# Commitar as inserções
conn.commit()

cur.close()

conn.close()