create database gestaoprof;
use gestaoprof;

create table alunos (
codAluno int primary key not null auto_increment,
nome varchar(45)
) Engine = InnoDB;

create table midia (
id int primary key not null auto_increment,
codNotas int not null,
foto varchar(250),
notas decimal(10,2) not null
) Engine = InnoDB;


insert into alunos (codAluno, nome) values ('', 'Maycon');
insert into midia (id, codNotas, foto, notas) values ('', '1', 'C:/Users/Maycon1', '10');

select * from alunos;
select *from midia;

update midia set notas = '6.2' where  id = '1';

drop table midia ;