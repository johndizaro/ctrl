CREATE DATABASE IF NOT EXISTS orca;

USE orca;

CREATE TABLE  IF NOT EXISTS unidade_medida (
  um_id int AUTO_INCREMENT,
  um_sigla varchar(10) NOT NULL COMMENT 'sigla da unidade de mendida',
  um_descricao varchar(50) NOT NULL COMMENT 'descrição da unidade de medida',
  um_PRIMARY KEY (um_id),
  UNIQUE KEY uc_sigla (um_sigla),
  UNIQUE KEY uc_descricao (um_descricao)
) COMMENT='unidade de medida';



CREATE TABLE  IF NOT EXISTS converte_unidade_medida (
  id int  AUTO_INCREMENT,
  id_sigla_origem int NOT NULL COMMENT 'sigla da unidade de mendida origem',
  id_sigla_destino int NOT NULL COMMENT 'sigla da unidade de mendida destino',
  calculo VARCHAR(10) NOT NULL COMMENT ' calculo para convercao de uma unidade para outra',
  PRIMARY KEY (id),
  UNIQUE KEY uc_origem_destino (id_sigla_origem,id_sigla_destino ),
  CONSTRAINT converte_unidade_medida_od FOREIGN KEY (id_sigla_origem) REFERENCES unidade_medida(id) ON DELETE CASCADE,
  CONSTRAINT converte_unidade_medida_do FOREIGN KEY (id_sigla_destino) REFERENCES unidade_medida(id) ON DELETE CASCADE
) COMMENT='converção de unidade de medida';


