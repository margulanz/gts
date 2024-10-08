CREATE USER reader_user WITH PASSWORD 'reader_password';


GRANT CONNECT ON DATABASE postgres TO reader_user;
GRANT USAGE ON SCHEMA public TO reader_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT SELECT ON TABLES TO reader_user;