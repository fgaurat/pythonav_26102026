CREATE TABLE customers_tbl (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	first_name TEXT,
	last_name TEXT,
	email TEXT,
	gender TEXT,
	ip_address TEXT,
	CONSTRAINT customers_tbl_pk PRIMARY KEY (id)
);
