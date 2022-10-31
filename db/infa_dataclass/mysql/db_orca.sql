CREATE DATABASE IF NOT EXISTS orca;

USE orca;

CREATE TABLE  IF NOT EXISTS a01_unidade_medida (
  a01_id int AUTO_INCREMENT,
  a01_sigla varchar(2) NOT NULL COMMENT 'sigla da unidade de mendida',
  a01_descricao varchar(30) NOT NULL COMMENT 'descrição da unidade de medida',
  PRIMARY KEY (a01_id),
  UNIQUE KEY a01_1_uk (a01_sigla),
  UNIQUE KEY a01_2_uk (a01_descricao)
) COMMENT='unidade de medida';


-- orca.a02_converte_unidade_medida definition
CREATE TABLE  IF NOT EXISTS a02_converte_unidade_medida (
  a02_id int AUTO_INCREMENT,
  a02_id_sigla_origem int NOT NULL COMMENT 'sigla da unidade de mendida origem',
  a02_id_sigla_destino int NOT NULL COMMENT 'sigla da unidade de mendida destino',
  a02_tp_operacao char(1) NOT NULL COMMENT 'operação a ser relizada para converter a unidade de medida [*, /, +, -]',
  a02_razao float NOT NULL COMMENT 'razão para calculo da converção',
  PRIMARY KEY (a02_id),
  UNIQUE KEY a02_1_uk (a02_id_sigla_origem,a02_id_sigla_destino),
  CONSTRAINT a02_1_fk FOREIGN KEY (a02_id_sigla_origem) REFERENCES a01_unidade_medida (a01_id) ON DELETE CASCADE,
  CONSTRAINT a02_2_fk FOREIGN KEY (a02_id_sigla_destino) REFERENCES a01_unidade_medida (a01_id) ON DELETE CASCADE


) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='converção de unidade de medida';

