-- Active: 1759768854365@@127.0.0.1@3306
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    primeiro_nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL, 
    email TEXT,
    senha INTEGER
)

CREATE TABLE postagens (
    id INTEGER PRIMARY KEY,
    titulo TEXT NOT NULL,
    postagem TEXT NOT NULL, 
    id_autor INTEGER
);

INSERT INTO usuarios (primeiro_nome, sobrenome, email, senha)
VALUES 
('João','de Sá','joao_sa@email.com', 1234),
('André','da Silva','andre450@email.com',4521),
('Marta','Richete','m.richete@email.com',1728),
('Júlia','Gama','gama_julia@email.com',5211),
('Humberto','Moraes','hm423@email.com',1212);

INSERT INTO postagens (titulo,postagem,id_autor)
VALUES 
('Casa Grande','no jornal ', 1),
('Último Trem','e-book', 2),
('Tricô para Leitos','em pdf',3),
('Tabela de comandos','em pdf',4),
('Mar Azul','pintura em .jpg',5);

SELECT * FROM usuarios;
select * FROM postagens;

UPDATE postagens SET titulo = 'Tricô para Leigos' WHERE id_autor = 3;
