# PostgreSQL Commands
- Check PostgreSQL version: `psql --version`
- Start PostgreSQL server: `sudo service postgresql start`
- Connect to PostgreSQL: `psql -U postgres`

# Flask Commands
- Run the server: `python run.py`

# Common Errors
- psycopg2 not installed: `pip install psycopg2-binary`


# PostgreSQL Login Warning
When using `sudo -u postgres psql` inside personal folders, the system may show:
"could not change directory ... Permission denied"
This is not a critical error. It only warns about directory access, but PostgreSQL will work fine.

# PostgreSQL Clean Login (Optional)
Use:
sudo -i -u postgres
cd ~
psql


# PostgreSQL Setup Notes

## Correct PostgreSQL Console Usage
1. Enter as postgres user:
   sudo -i -u postgres

2. Start PostgreSQL console:
   psql

3. Now run SQL commands:
   CREATE DATABASE booklibrary;
   CREATE USER myuser WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE booklibrary TO myuser;

4. Exit PostgreSQL console:
   \q

5. Exit postgres user:
   exit
