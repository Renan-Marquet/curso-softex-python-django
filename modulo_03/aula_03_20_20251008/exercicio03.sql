-- Active: 1759940690523@@127.0.0.1@3306
CREATE TABLE alunos (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
);

INSERT INTO alunos(nome,idade) VALUES ('José Marcos',25),('Marília Costa',22),('Antônio Carlos',30);

DROP TABLE alunos;

SELECT * FROM alunos;

CREATE TABLE materias(
    id_materia INTEGER PRIMARY KEY,
    nome_materia TEXT NOT NULL
);
INSERT INTO materias(nome_materia) VALUES ('Matemática'),('História'),('Ciências');

CREATE TABLE avaliacoes(
    aluno INTEGER,
    materia INTEGER,
    nota FLOAT,
    FOREIGN KEY (aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (materia) REFERENCES materias(id_materia)
)

INSERT INTO avaliacoes(aluno,materia,nota) VALUES (1,1,8.2),(1,2,7.5),(2,1,6.8),(2,3,6.7),(3,2,6.4),(3,3,10);

DROP TABLE avaliacoes;

SELECT * FROM avaliacoes;

SELECT alunos.nome, materias.nome_materia , avaliacoes.nota FROM avaliacoes
INNER JOIN alunos ON avaliacoes.aluno = alunos.id_aluno
INNER JOIN materias ON avaliacoes.materia= materias.id_materia;

SELECT materias.nome_materia , avg(avaliacoes.nota) FROM avaliacoes
INNER JOIN alunos ON avaliacoes.aluno = alunos.id_aluno
INNER JOIN materias ON avaliacoes.materia= materias.id_materia
GROUP BY materias.nome_materia

SELECT alunos.nome , avg(avaliacoes.nota) FROM avaliacoes
INNER JOIN alunos ON avaliacoes.aluno = alunos.id_aluno
INNER JOIN materias ON avaliacoes.materia= materias.id_materia
GROUP BY avaliacoes.aluno;

SELECT materias.nome_materia, min(avaliacoes.nota) , max(avaliacoes.nota) FROM avaliacoes
INNER JOIN alunos ON avaliacoes.aluno = alunos.id_aluno
INNER JOIN materias ON avaliacoes.materia= materias.id_materia
GROUP BY avaliacoes.materia;

SELECT alunos.nome , avg(avaliacoes.nota) FROM avaliacoes
INNER JOIN alunos ON avaliacoes.aluno = alunos.id_aluno
INNER JOIN materias ON avaliacoes.materia= materias.id_materia
GROUP BY avaliacoes.aluno
HAVING avg(avaliacoes.nota)>7.0;

