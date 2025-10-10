-- Active: 1759940690523@@127.0.0.1@3306

CREATE TABLE autores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL
);

CREATE TABLE livros(
    id_livro INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    ano_publicacao INTEGER,
    id_autor INTEGER,
    FOREIGN KEY (id_autor) REFERENCES autores(id)
)

INSERT INTO autores (nome,nacionalidade) VALUES ('Garcia Marques','Colombia'), ('Victor Hugo','França'),('Charles Dikens','Inglaterra');

SELECT * FROM autores;

INSERT INTO livros (titulo,ano_publicacao,id_autor) VALUES ('100 anos de solidão',1980,1), ('Os Miseráveis',1780,2),('O amor nos tempos do cólera',1990,1),('Grandes Esperanças',1871,3);

SELECT * FROM livros;

DROP TABLE livros;
DROP TABLE autores;

SELECT livros.titulo AS Titulo , autores.nome AS Autor FROM livros
INNER JOIN autores ON livros.id_autor = autores.id;

SELECT livros.titulo AS Titulo , autores.nome AS 'Autor Britânico' FROM livros
INNER JOIN autores ON livros.id_autor = autores.id WHERE autores.nacionalidade = 'Inglaterra';

SELECT autores.nome AS 'Autor', count(livros.id_autor) As 'Livros' FROM livros
INNER JOIN autores ON livros.id_autor=autores.id 
GROUP BY autores.nome;
