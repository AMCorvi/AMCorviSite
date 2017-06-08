
#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate


# Load sample data 
echo "Loading datadump"
python manage.py loaddata datadump.json
