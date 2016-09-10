DROP TABLE haushalt.tb_operations;

CREATE TABLE haushalt.tb_operations
(
  opr_id serial PRIMARY KEY,
  opr_timestamp timestamp NOT NULL,
  opr_date date NOT NULL,
  opr_type char(1) NOT NULL CHECK (opr_type IN ('C', 'D', 'X')),
  opr_value numeric(8,2) NOT NULL DEFAULT 0,
  opr_usr_id integer NOT NULL REFERENCES haushalt.tb_users,
  opr_acc_id integer NOT NULL REFERENCES haushalt.tb_accounts
);

CREATE INDEX ix_operations_01
  ON haushalt.tb_operations USING btree (opr_date ASC NULLS LAST)
  TABLESPACE tb_data
;
