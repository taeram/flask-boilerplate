# Flask Boilerplate

Flask Boilerplate is a set of default Flask files for quickly bootstrapping a new application.

Setup
=====
First, you'll need to clone the repo to your local machine:
```bash
    # Clone the repo
    git clone https://github.com/taeram/flask-boilerplate.git
    cd ./flask-boilerplate
```

Then, for local development setup:
```bash
    # Setup and activate virtualenv
    virtualenv .venv
    source ./.venv/bin/activate

    # Install the pip requirements for postgres and MySQL database support
    sudo apt-get install postgresql-client postgresql-common libpq-dev python-dev mysql-client libmysqld-dev
    pip install -r requirements.txt

    # Create the development database
    python manage.py database migrate upgrade
    python manage.py database setup

    # Next, create a MySQL database user, and give it access to a database called "boilerplate"

    # Start the application, prefixing with the required environment variables
    DATABASE_URL=mysql://user:password@localhost/boilerplate python server.py
```

When deploying to production, ensure the following environment variables are set:

* `FLASK_ENV` - Must be set to "production". Used to switch to the production configuration.
* `SECRET_KEY` - Must be a random hash. Used by to generate secure session hashes.
* `PORT` - The port to run the application on. Defaults to 5000.

Next, run the `migrate upgrade` and `setup` steps like you did locally:

* `python manage.py database migrate upgrade`
* `python manage.py database setup`

Upgrading to a new Release
==========================

When upgrading to a new release, simply pull down the new copy, and migrate the
database:

  * `python manage.py database migrate upgrade`
