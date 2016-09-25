__version__ = "0.01"
DROP TABLE haushalt.haushalt_db;

CREATE TABLE haushalt.haushalt_db
(
  name varchar(32)
);

INSERT INTO haushalt.haushalt_db VALUES ('Production Haushalt Kontrole DB');
-- or
INSERT INTO haushalt.haushalt_db VALUES ('Development Haushalt Kontrole DB');
