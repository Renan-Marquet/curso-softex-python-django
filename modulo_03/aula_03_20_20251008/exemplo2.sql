-- Active: 1759940690523@@127.0.0.1@3306

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE cursos (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL
);

CREATE TABLE alunos_cursos (
    id_aluno INTEGER,
    id_curso INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

INSERT INTO alunos (nome) VALUES ('Pedro'), ('Maria'),('José Américo');
SELECT * FROM alunos;

INSERT INTO cursos (titulo) VALUES ('Matemática'), ('Português'),('Inglês');

SELECT * FROM cursos;

SELECT * FROM alunos_cursos;

INSERT INTO alunos_cursos (id_aluno,id_curso) VALUES (1,1), (1,3),(2,2),(2,1),(3,1),(3,2),(3,3);

SELECT 
    A.nome AS nome_aluno,
    C.titulo AS titulo_curso
FROM
    alunos AS A
INNER JOIN alunos_cursos AS AC ON A.id = AC.id_aluno
INNER JOIN cursos AS C ON AC.id_curso = C.id;


SELECT alunos.nome , cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id;

DROP TABLE alunos_cursos;

SELECT COUNT(*) FROM alunos;
SELECT count(*) FROM alunos_cursos WHERE id_curso = 3;

SELECT Count(alunos.nome) , cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id
GROUP BY cursos.titulo;

SELECT Count(alunos.nome) , cursos.titulo FROM alunos
INNER JOIN alunos_cursos ON alunos_cursos.id_aluno = alunos.id
INNER JOIN cursos ON alunos_cursos.id_curso = cursos.id
GROUP BY cursos.titulo
HAVING count(alunos.nome) > 2;

