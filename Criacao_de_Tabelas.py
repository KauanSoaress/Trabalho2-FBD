import psycopg2;

# Conectando ao banco de dados
conn = psycopg2.connect(host="200.129.44.249", database="537063", user="537063", password="537063@fbd")

# Criando um cursor
cur = conn.cursor()

# Criando a tabela
cur.execute("CREATE TABLE Embarcacoes ("
            "id_emb INTEGER PRIMARY KEY, "
            "nome VARCHAR(50) NOT NULL, "
            "tipo VARCHAR(50) NOT NULL)")

cur.execute("CREATE TABLE Tripulantes ("
            "id_trp INTEGER PRIMARY KEY, "
            "nome VARCHAR(50) NOT NULL, "
            "data_nasc DATE NOT NULL, "
            "funcao VARCHAR(50) NOT NULL, "
            "id_emb INTEGER NOT NULL, "
            "CONSTRAINT id_emb_fk FOREIGN KEY (id_emb) REFERENCES Embarcacoes ON DELETE CASCADE)")

cur.execute("CREATE TABLE Empregados ("
            "id_emp INTEGER PRIMARY KEY, "
            "nome VARCHAR(50) NOT NULL, "
            "data_nasc DATE NOT NULL, "
            "funcao VARCHAR(50) NOT NULL)")

cur.execute("CREATE TABLE Movimentacao ("
            "id_mov INTEGER PRIMARY KEY, "
            "data DATE NOT NULL, "
            "tipo VARCHAR(50) NOT NULL, "
            "id_emb INTEGER NOT NULL, "
            "CONSTRAINT id_emb_fk FOREIGN KEY (id_emb) REFERENCES Embarcacoes)")

cur.execute("CREATE TABLE Movimentacao_Empregados ("
            "id_mov INTEGER, "
            "id_emp INTEGER, "
            "CONSTRAINT mov_emp_pk PRIMARY KEY (id_mov, id_emp), "
            "CONSTRAINT mov_fk FOREIGN KEY (id_mov) REFERENCES Movimentacao, "
            "CONSTRAINT emp_fk FOREIGN KEY (id_emp) REFERENCES Empregados)")

# Commitar a criação
conn.commit()

cur.close()

conn.close()