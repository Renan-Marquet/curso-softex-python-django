import sqlite3
from database import DatabaseConnection


class AdressModel:
    """Gerencia a tabela 'adress' (Outro lado do N:N)."""

    def __init__(self, db_conn: DatabaseConnection):
        self.db_conn = db_conn
        self._create_table()

    def _create_table(self):
        """Cria a tabela de endereços."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS adress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                adress TEXT NOT NULL,
                num TEXT
            );
        """
        )
        self.db_conn.close()

    def create_adress(self, local, num):
        """Cria um novo endereço."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                "INSERT INTO cursos (local, num) VALUES (?, ?);",
                (local, num),
            )
            print(f"[SUCESSO] Endereço '{local}' criado.")
        except sqlite3.IntegrityError:
            print(f"[ERRO] O Endereço '{local}' não pode ficar em branco.")
        finally:
            self.db_conn.close()

    def find_adress_by_id(self, adress_id):
        """Busca um endereço pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM adress WHERE id = ?;", (adress_id,))
        adress = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return adress

    def get_all_adress(self):
        """Retorna todos os endereços."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM adress;")
        adress = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return adress
    


    def get_students_by_adress(self, adress_id):
        """Busca todos os alunos matriculados em um curso específico.
        (Consulta N:N - Adress -> Alunos)
        """
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            SELECT a.id, a.nome, a.email, e.local, e.num
            FROM adress e
            INNER JOIN alunos a ON a.endereco_id = e.id 
            WHERE endereco_id = ?;
            """,
            (adress_id,),
        )
        adress = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return adress
