# MIGRATIONS PACKAGE MARKER - Makes This Directory a Python Package
# 
# This file tells Python that the 'migrations' directory is a Python package.
# Django's migration system needs this to import and run database migrations.
#
# WHAT MIGRATIONS ARE:
# Migrations are like version control for your database. They track changes
# to your database schema (tables, columns, indexes) over time.
#
# DJANGO MIGRATION COMMANDS:
# python manage.py makemigrations  # Create new migration files
# python manage.py migrate         # Apply migrations to database
# python manage.py showmigrations  # Show migration status