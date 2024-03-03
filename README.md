# AWS Redshift ETL Process

The given python scripts (create_tables.py, etl.py) used in conjunction with the configuration file (dwh.cfg) helps in establishing an ETL process with AWS Redshift.


## Table of Contents 
- [Setup](#setup)
- [Scripts](#scripts)
- [Instructions](#instructions)
- [Configurations](#configurations)


## Setup

The Setup is managed by three files:
- create_tables.py : Python script responsible for connecting with AWS Redshift instance and creating the tables defined in sql_queries.py.
- etl.py : Python script responsible for executing the ETL process.
- dwh.cfg: Contains necessary AWS credentials and configuration info for the scripts.

## Scripts

Scripts included in the project:

1. `create_tables.py` - This script will drop old tables (if exist) and re-create new tables
2. `etl.py` - This script will read JSON every file contained in /data folder, parse them, build relations between them and insert the data back to the created tables.

## Instructions

- To run this project, you will need to fill the `dwh.cfg` file with your personal AWS information.
- Run the `create_tables.py` to set up the database and tables.
- Run the `etl.py` script to extract data from the files in the `/data` directory, transform it, and load it into the tables.

## Configurations

`dwh.cfg` Contains necessary AWS credentials and configuration info. The configuration file includes the following details:

[AWS]
- KEY= YOUR_AWS_KEY
- SECRET= YOUR_AWS_SECRET

[CLUSTER]
- HOST= YOUR_AWS_RESHSHIFT_CLUSTER_ENDPOINT_URL
- DB_NAME= YOUR_DATABASE_NAME
- DB_USER= YOUR_DATABASE_USER
- DB_PASSWORD= YOUR_DATABASE_PASSWORD
- DB_PORT= YOUR_DATABASE_PORT

[IAM_ROLE]
- ARN= YOUR_IAM_ROLE_ARN

[S3]
- LOG_DATA='s3://udacity-dend/log_data'
- LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
- SONG_DATA='s3://udacity-dend/song_data'