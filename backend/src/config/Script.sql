CREATE TABLE fabricantes(
   fab_id INT GENERATED ALWAYS AS IDENTITY,
   fab_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(fab_id)
);

CREATE TABLE processadores(
   pro_id INT GENERATED ALWAYS AS IDENTITY,
   pro_modelo VARCHAR(255) NOT NULL,
   pro_idFabricante INT not null,
   PRIMARY KEY(pro_id),
   foreign key (pro_idFabricante)
   		references fabricantes(fab_id)
   		ON DELETE CASCADE
);

CREATE TABLE memorias(
   mem_id INT GENERATED ALWAYS AS IDENTITY,
   mem_slot VARCHAR(5) NOT NULL,
   mem_frequencia VARCHAR(10) NOT NULL,
   mem_idFabricante int NOT NULL,
   PRIMARY KEY(mem_id),
   foreign key (mem_idFabricante)
   		references fabricantes(fab_id)
   		ON DELETE CASCADE
);

CREATE TABLE statusnotebook(
   sta_id INT GENERATED ALWAYS AS IDENTITY,
   sta_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(sta_id)
);

CREATE TABLE notebooks(
   not_id INT GENERATED ALWAYS AS IDENTITY,
   not_modelo VARCHAR(255) NOT NULL,
   not_serie VARCHAR(255) NOT NULL,
   not_fabricante VARCHAR(255) NOT NULL,
   not_patrimonio varchar(25),
   not_valor decimal,
   isSinobras boolean,
   not_idFabricante int NOT NULL,
   not_idProcessador int NOT NULL,
   not_idMemoria int NOT NULL,
   not_idStatus int NOT NULL,
   PRIMARY KEY(not_id),
   foreign key (not_idFabricante)
      references fabricantes(fab_id)
   	ON DELETE CASCADE,
   foreign key (not_idProcessador)
      references processadores (pro_id)
      ON DELETE CASCADE,
   foreign KEY (not_idMemoria)
      references memorias (mem_id)
      ON DELETE CASCADE,
   foreign key (not_idStatus)
      references statusnotebook(sta_id)
      ON DELETE CASCADE
);

CREATE TABLE acessorios(
   ace_id INT GENERATED ALWAYS AS IDENTITY,
   ace_nome VARCHAR(255) NOT NULL,
   ace_modelo VARCHAR(255) NOT NULL,
   ace_idFabricante int not null,
   PRIMARY KEY(ace_id),
   foreign key (ace_idFabricante)
      references fabricantes(fab_id)
   	ON DELETE CASCADE
);

CREATE TABLE perfis(
   per_id INT GENERATED ALWAYS AS IDENTITY,
   per_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(per_id)
);

CREATE TABLE usuarios(
   usu_id int GENERATED ALWAYS AS IDENTITY,
   usu_nome varchar(255),
   usu_cpf varchar(11),
   usu_login varchar(40),
   usu_password varchar(255),
   usu_idPerfil int not null,
   PRIMARY key (usu_id),
   foreign key (usu_idPerfil)
      references perfis(per_id)
      ON DELETE CASCADE
);

CREATE TABLE cargos(
   car_id INT GENERATED ALWAYS AS IDENTITY,
   car_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(car_id)
);

CREATE TABLE centrocustos(
   cen_id INT GENERATED ALWAYS AS IDENTITY,
   cen_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(cen_id)
);

CREATE TABLE departamentos(
   dep_id INT GENERATED ALWAYS AS IDENTITY,
   dep_nome VARCHAR(255) NOT NULL,
   dep_idCentoCusto int not null,
   PRIMARY KEY(dep_id),
   foreign key (dep_idCentoCusto)
      references centrocustos(cen_id)
      ON DELETE CASCADE
);

CREATE TABLE funcionarios(
   fun_id int GENERATED ALWAYS AS IDENTITY,
   fun_nome varchar(255),
   fun_cpf varchar(11),
   fun_email varchar(255),
   fun_matricula decimal,
   fun_idDerpatamento int not null,
   fun_idCargo int not null,
   PRIMARY key (fun_id),
   foreign key (fun_idDerpatamento)
      references departamentos(dep_id)
      ON DELETE CASCADE,
   foreign key (fun_idCargo)
      references cargos(car_id)
      ON DELETE CASCADE
);

CREATE TABLE tipotermo(
   tip_id INT GENERATED ALWAYS AS IDENTITY,
   tip_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(tip_id)
);

CREATE TABLE termos(
   ter_id INT GENERATED ALWAYS AS IDENTITY,
   ter_data DATETIME,
   ter_idTipoTermo int not null,
   ter_idNotebook int not null,
   ter_idAcessorios int not null,
   ter_idFuncionario int not null,
   ter_idUsuario int not null,
   foreign key (ter_idTipoTermo)
      references tipotermo(tip_id)
      ON DELETE CASCADE,
   foreign key (ter_idNotebook)
      references notebooks(not_id)
      ON DELETE CASCADE,
   foreign key (ter_idAcessorios)
      references acessorios(ace_id)
      ON DELETE CASCADE,
   foreign key (ter_idFuncionario)
      references funcionarios(fun_id)
      ON DELETE CASCADE,
   foreign key (ter_idUsuario)
      references usuarios(usu_id)
      ON DELETE CASCADE
);