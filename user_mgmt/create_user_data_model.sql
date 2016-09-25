__version__ = "0.01"
DROP TABLE haushalt.tb_users;

CREATE TABLE haushalt.tb_users
(
  usr_id serial PRIMARY KEY,
  usr_name varchar(30) NOT NULL,
  usr_role_id integer,
  usr_status char(1) NOT NULL
);

INSERT INTO haushalt.tb_users VALUES (DEFAULT, 'Ronald', 1, 'A');
INSERT INTO haushalt.tb_users VALUES (DEFAULT, 'Simone', 1, 'A');
