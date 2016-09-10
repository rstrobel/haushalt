DROP TABLE haushalt.tb_accounts;

CREATE TABLE haushalt.tb_accounts
(
  acc_id serial PRIMARY KEY,
  acc_name varchar (10) NOT NULL,
  acc_long_name varchar (30) NOT NULL,
  acc_payment_frequency char (1) NOT NULL CHECK (acc_payment_frequency IN ('W', 'M', 'J')),
  acc_payment_day integer,
  acc_payment_month integer,
  acc_payment_value numeric (8,2) NOT NULL
);

INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Miete', 'Wohnungsmiete', 'M', 1, 0, 1190.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Hausrat', 'Hausratversicherung', 'M', 1, 0, 30.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Karte', 'Karte Maestro', 'J', 1, 1, 7.00 );
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Sonja', 'Sonja Küng', 'M', 1, 0, 115.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Cablecom', 'Cablecom Anschluss', 'M', 0, 0, 35.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Tel/TV/Int', 'Telefon/Internet/TV', 'M', 1, 0, 85.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Billag', 'Billag', 'J', 0, 0, 38.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Vergnügen', 'Vergnügen (Ausgang, Ferien,…)', 'J', 0, 0, 300.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'EWL', 'EWL', 'J', 0, 0, 200.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Essen', 'Essen, Medizin, Hygieneartikel', 'M', 0, 0, 2000.00);
INSERT INTO haushalt.tb_accounts VALUES (DEFAULT, 'Remainder', 'Remainder undestinated Money', 'M', 0, 0, 0.00);

DROP TABLE haushalt.tb_balance;

CREATE TABLE haushalt.tb_balance
(
  bal_acc_id integer NOT NULL REFERENCES haushalt.tb_accounts,
  bal_acc_value numeric(8,2) NOT NULL DEFAULT 0
)

INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Miete'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Hausrat'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Karte'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Sonja'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Cablecom'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Tel/TV/Int'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Billag'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Vergnügen'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'EWL'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Essen'), 0);
INSERT INTO haushalt.tb_balance VALUES ((SELECT acc_id FROM haushalt.tb_accounts WHERE acc_name = 'Remainder'), 0);
