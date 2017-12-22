# psycopg2
Precompiled postgres Python adapter for AWS Lambda systems.

Recently while working on project I ended up using AWS Lambda to load data from s3 to Redshift.  AWS Lambda doesn't come with appropriate postgres (psycopg2) installed and hence the need for packaging postgres adapter with the lambda function.

The shared library is statically linked and compiled on Amazon Linux AMI for Python2.7.  Package psycopg2 directory here with your lambda function, zip it and you should be able to connect to RDS postgres or Redshift from your lambda functions.

## Source code compilation
Using lynx download Postgres from https://ftp.postgresql.org/pub/source/v9.6.0/postgresql-9.6.0.tar.gz

After unzip and untar compile the code 

This will build psql, pg_config and other executables in <SOURCE_DIR>/bin folder


Similary do the same for adapter - http://initd.org/psycopg/tarballs/PSYCOPG-2-6/psycopg2-2.6.1.tar.gz

Modify setup.cfg for static link library and run python build

This will generate needed libary in <SOURCE_CODE>/psycopg2-2.6.1/build/lib.linux-x86_64-2.7/psycopg2

