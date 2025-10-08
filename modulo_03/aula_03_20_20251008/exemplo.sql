-- Active: 1759940690523@@127.0.0.1@3306
CREATE TABLE professores (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    id_professor INTEGER NOT NULL,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
);

DROP TABLE alunos; -- apaga a tabela e todo o seu conteúdo

INSERT INTO professores(nome) VALUES ('Anderson');
INSERT INTO professores(nome) VALUES ('Paulo'),('José');

SELECT * FROM professores;

INSERT INTO alunos(nome, id_professor) VALUES ('Pedro',1), ('Maria',2),('José Américo',1);

SELECT * FROM alunos;
DELETE FROM alunos WHERE id = 4 OR id = 5 OR id = 6;
DELETE FROM alunos WHERE id BETWEEN 4 AND 6;

SELECT id AS Identificador, nome , id_professor AS 'Registro Professor' FROM alunos;
SELECT alunos.nome AS Nome_aluno, professores.nome AS Nome_professor FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;

SELECT alunos.id ,alunos.nome AS Nome_aluno, professores.nome AS Nome_professor FROM alunos
INNER JOIN professores ON alunos.id_professor = professores.id;

