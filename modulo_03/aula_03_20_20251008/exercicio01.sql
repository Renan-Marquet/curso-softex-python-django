
CREATE TABLE autores (
    id_autor INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE TABLE livros(
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor)
)

INSERT INTO autores (nome,nacionalidade) VALUES ('Garcia Marques','Colombia'), ('Victor Hugo','França');

SELECT * FROM autores;

INSERT INTO livros (titulo,ano_publicacao,id_autor) VALUES ('100 anos de solidão',1980,1), ('Os Miseráveis',1780,2),('O amor nos tempos do cólera',1990,1);

SELECT * FROM livros;

DROP TABLE livros;

--SELECT  AS Nome_aluno, professores.nome AS Nome_professor FROM alunos
--INNER JOIN professores ON alunos.id_professor = professores.id;