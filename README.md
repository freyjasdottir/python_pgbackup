pgbackup
========

CLI for backing up PostgreSQL databases locally or to AWS S3.
A practice project for python learning

## Usage

Pass in a full database url, the storage driver, and destination.

S3 Example

```
$ pgbackup postgres://something@someurl.com:5432/db_one  --drive s3 backups
```

Local example

```
$ pgbackup postgres://something@someurl.com:5432/db_one --driver local /some/backup/path
```

## Install from source

From within the project directory:

```
$ pip install --user -e .
```

## Preparing to develop

1. Ensure 'pip' and 'pipenv' are installed
2. Clone the repo
3. `cd` into the repo directory
4. `pipenv shell` to start the virtualenv
5. `pipenv install` to install dependencies
