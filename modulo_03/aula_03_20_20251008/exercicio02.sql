-- Active: 1759940690523@@127.0.0.1@3306
CREATE TABLE alunos (
    id_aluno INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
);

INSERT INTO alunos(nome,idade) VALUES ('José Marcos',25),('Marília Costa',22),('Antônio Carlos',30);

DROP TABLE alunos;

SELECT * FROM alunos;

CREATE TABLE aulas(
    id_aula INTEGER PRIMARY KEY,
    nome_aula TEXT NOT NULL
);

INSERT INTO aulas(nome_aula) VALUES ('Musculação'),('Zumba'),('Atletismo');

SELECT * FROM aulas

CREATE TABLE alunos_aulas(
    aluno INTEGER,
    aula INTEGER,
    FOREIGN KEY (aluno) REFERENCES alunos(id_aluno),
    FOREIGN KEY (aula) REFERENCES aulas(id_aula)
)

DROP TABLE alunos_aulas;

INSERT INTO alunos_aulas VALUES (1,1),(1,3),(2,2),(2,1);

SELECT * FROM alunos_aulas;

SELECT alunos.nome AS 'Nome do Aluno', aulas.nome_aula AS 'Nome da Aula' FROM alunos_aulas
INNER JOIN alunos ON alunos_aulas.aluno = alunos.id_aluno
INNER JOIN aulas ON alunos_aulas.aula = aulas.id_aula;

SELECT alunos.nome FROM alunos_aulas
INNER JOIN alunos ON alunos_aulas.aluno = alunos.id_aluno
INNER JOIN aulas ON alunos_aulas.aula = aulas.id_aula
WHERE aulas.nome_aula = 'Zumba';

SELECT aulas.nome_aula, Count(aulas.nome_aula) FROM alunos_aulas
INNER JOIN alunos ON alunos_aulas.aluno = alunos.id_aluno
INNER JOIN aulas ON alunos_aulas.aula = aulas.id_aula
GROUP BY nome_aula;

SELECT aulas.nome_aula , alunos.nome FROM alunos_aulas
INNER JOIN alunos ON alunos_aulas.aluno = alunos.id_aluno
INNER JOIN aulas ON alunos_aulas.aula = aulas.id_aula
WHERE aulas.id_aula = 1 or aulas.id_aula = 3;

SELECT aulas.nome_aula , alunos.nome FROM alunos_aulas
INNER JOIN alunos ON alunos_aulas.aluno = alunos.id_aluno
INNER JOIN aulas ON alunos_aulas.aula = aulas.id_aula
Where aulas.id_aula IN (1,3);


