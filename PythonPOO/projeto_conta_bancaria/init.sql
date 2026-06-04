CREATE TABLE IF NOT EXISTS contas (
    id                     SERIAL PRIMARY KEY,
    titular                VARCHAR(100) NOT NULL,
    saldo                  NUMERIC(12, 2) NOT NULL DEFAULT 0,
    tipo                   VARCHAR(20) NOT NULL,
    data_ultimo_deposito   TIMESTAMP,
    data_ultimo_rendimento TIMESTAMP
);
