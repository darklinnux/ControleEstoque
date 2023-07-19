

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
   CONSTRAINT fk_fabricantes
   	foreign key (pro_idFabricante)
   		references fabricantes(fab_id)
   		ON DELETE CASCADE
);

CREATE TABLE memorias(
   mem_id INT GENERATED ALWAYS AS IDENTITY,
   mem_slot VARCHAR(5) NOT NULL,
   mem_frequencia VARCHAR(10) NOT NULL,
   PRIMARY KEY(pro_id),
   CONSTRAINT fk_fabricantes
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
   not_serie VARCHAR(255) NOT NULL
   not_fabricante VARCHAR(255) NOT NULL,
   not_patrimonio varchar(25),
   not_valor decimal,
   isSinobras boolean,
   PRIMARY KEY(not_id)
   CONSTRAINT fk_fabricantes
      foreign key (not_idFabricante)
   		references fabricantes(fab_id)
   		ON DELETE CASCADE,
   CONSTRAINT fk_processoradores
      foreign key (not_idProcessador)
         references processadores (pro_id)
         ON DELETE CASCADE,
   CONSTRAINT fk_memorias
      
);

CREATE TABLE acessorios(
   ace_id INT GENERATED ALWAYS AS IDENTITY,
   ace_nome VARCHAR(255) NOT NULL,
   ace_modelo VARCHAR(255) NOT NULL,
   PRIMARY KEY(ace_id),
   CONSTRAINT fk_fabricantes
   	foreign key (ace_idFabricante)
   		references fabricantes(fab_id)
   		ON DELETE CASCADE
);

CREATE TABLE perfis(
   per_id INT GENERATED ALWAYS AS IDENTITY,
   per_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(per_id)
);

CREATE TABLE cargos(
   car_id INT GENERATED ALWAYS AS IDENTITY,
   car_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(car_id)
);

CREATE TABLE departamentos(
   dep_id INT GENERATED ALWAYS AS IDENTITY,
   dep_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(dep_id)
);

CREATE TABLE centrocusto(
   cen_id INT GENERATED ALWAYS AS IDENTITY,
   cen_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(cen_id)
);

CREATE TABLE tipotermo(
   tip_id INT GENERATED ALWAYS AS IDENTITY,
   tip_nome VARCHAR(255) NOT NULL,
   PRIMARY KEY(tip_id)
);



