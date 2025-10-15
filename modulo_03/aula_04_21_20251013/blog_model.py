"""
Crie a class BlogModel seguindo o exemplo da UserModel;
BlogModel deve ter os atributos:
 - conn do tipo DatabaseConnection
 - criar a tabela quando instanciado

tabela blogs:
 - id;
 - titulo;
 - conteudo;
 - data_criacao;
 - data_atualizacao;
 - id_user (chave estrangeira referente a tabela usuarios);

Faça um CRUD para:
- criar postagem
- ler todas as postagens
- ler postagens pelo id
- ler postagens pelo id_user
- atualizar postam (pelo id da postagem)
- deletar postagem (pedo id da postagem)

**Consulte o UserModel para se guiar
"""


import sqlite3
from datetime import datetime
from database import DatabaseConnection


class BlogModel:
    """Gerencia a tabela 'blogs' todas as operações de CRUD."""

    def __init__(self):
        self.db_conn = DatabaseConnection()
        self._create_blogs()

    def _create_blogs(self):
        """Método privado para criar a tabela de blogs."""
        self.db_conn.connect()
        self.db_conn.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS postagem (
                id_post INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL UNIQUE,
                conteudo TEXT NOT NULL,
                data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
                id_user INTEGER,
                FOREIGN KEY (id_user) REFERENCES usuarios(id)
            );
        """
        )
        self.db_conn.close()
 
    def create_post(self, titulo, conteudo, id_user):
        """Cria um novo post."""
        self.db_conn.connect()
        try:
            self.db_conn.cursor.execute(
                """
                INSERT INTO postagem (titulo, conteudo, id_user)
                VALUES (?, ?, ?);
            """,
                (titulo, conteudo, id_user),
            )
            print("Post criado com sucesso!")
        except sqlite3.IntegrityError:
            print(f"Erro: O e-mail '{titulo}' já está em uso.")
        finally:
            self.db_conn.close()

    def find_post_by_id(self, id_post):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM postagem WHERE id = ?;", (id_post,))
        post = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return post
       
    def find_post_by_id_user(self, id_user):
        """Busca um usuário pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM postagem WHERE id = ?;", (id_user,))
        post = self.db_conn.cursor.fetchone()
        self.db_conn.close()
        return post

    def update_post_by_id_post(self, id_post, titulo=None, conteudo=None):
        """Atualiza informações de um usuário pelo ID."""
        self.db_conn.connect()
        updates = []
        params = []
        if titulo:
            updates.append("titulo = ?")
            params.append(titulo)
        if conteudo:
            updates.append("conteudo = ?")
            params.append(conteudo)

        if not updates:
            print("Nada para atualizar.")
            self.db_conn.close()
            return

        updates.append("data_atualizacao = ?")
        params.append(datetime.now())
        params.append(id_post)
        query = f"UPDATE postagem SET {', '.join(updates)} WHERE id = ?;"

        self.db_conn.cursor.execute(query, params)
        print("Usuário atualizado com sucesso!")
        self.db_conn.close()

    def delete_post_by_id(self, id_post):
        """Deleta uma postagem pelo ID."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("DELETE FROM postagem WHERE id = ?;", (id_post,))
        print("Postagem deletada com sucesso!")
        self.db_conn.close()
            
    def get_all_posts(self):
        """Retorna todas as postagens."""
        self.db_conn.connect()
        self.db_conn.cursor.execute("SELECT * FROM postagem;")
        posts = self.db_conn.cursor.fetchall()
        self.db_conn.close()
        return posts

