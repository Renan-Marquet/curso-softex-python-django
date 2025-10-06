-- Active: 1759768854365@@127.0.0.1@3306
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
);

INSERT INTO alunos (nome, idade) VALUES ('João', 20);
INSERT INTO alunos (nome, idade) VALUES ('Maria', 22);

SELECT * FROM alunos;
SELECT nome, idade FROM alunos;
SELECT * FROM alunos WHERE idade = 20;
SELECT * FROM alunos WHERE nome = 'Maria' AND idade = 22;
UPDATE alunos SET idade = 21 WHERE nome =  'João';
UPDATE alunos SET nome = 'André' WHERE id = 3;
-- Comentário em SQL
/*
bloco de comentário
pulei uma linha e continua sendo comentário
*/

DELETE FROM alunos WHERE nome = 'Maria';