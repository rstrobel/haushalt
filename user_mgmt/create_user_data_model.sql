DROP TABLE haushalt.tb_users;

CREATE TABLE haushalt.tb_users
(
  usr_id serial PRIMARY KEY,
  usr_name varchar(30) NOT NULL,
  usr_role_id integer
);

INSERT INTO haushalt.tb_users VALUES (DEFAULT, 'Ronald', 1);
INSERT INTO haushalt.tb_users VALUES (DEFAULT, 'Simone', 1);
