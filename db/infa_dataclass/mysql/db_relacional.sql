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


-- orca.converte_unidade_medida definition
CREATE TABLE  IF NOT EXISTS converte_unidade_medida (
  cum_id int NOT NULL AUTO_INCREMENT,
  cum_id_sigla_origem int NOT NULL COMMENT 'sigla da unidade de mendida origem',
  cum_id_sigla_destino int NOT NULL COMMENT 'sigla da unidade de mendida destino',
  cum_calculo varchar(20) NOT NULL COMMENT 'operação a ser relizada para converter a unidade de medida [*, /, +, -]',
  PRIMARY KEY (cum_id),
  UNIQUE KEY uc_origem_destino (cum_id_sigla_origem,cum_id_sigla_destino),
  KEY id_sigla_destino (cum_id_sigla_destino),
  CONSTRAINT converte_unidade_medida_ibfk_1 FOREIGN KEY (cum_id_sigla_origem) REFERENCES unidade_medida (um_id) ON DELETE CASCADE,
  CONSTRAINT converte_unidade_medida_ibfk_2 FOREIGN KEY (cum_id_sigla_destino) REFERENCES unidade_medida (um_id) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='converção de unidade de medida';

