create table livros (
	id int auto_increment key,
	titulo varchar(30) not null,
	autor varchar(50) not null,
    ano int not null,
	status varchar(15) not null
);


select * from livros;


create table usuarios (
	id int auto_increment primary key,
	nome varchar(30) not null,
	cpf varchar(11) unique not null,
    email varchar(50) unique not null
);

select * from usuarios;


create table emprestimos (
	id int auto_increment primary key,
	livro_id int,
	usuario_id int,
    data_emprestimo date not null,
	previsão_de_devolucao date not null,
    data_devolucao date,
    foreign key(livro_id) references livros(id),
	foreign key(usuario_id) references usuarios(id)
);


select * from emprestimos;

