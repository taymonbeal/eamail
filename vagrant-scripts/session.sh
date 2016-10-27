source ~/venv/bin/activate
export PYTHONPATH=/vagrant
export PYTHONDONTWRITEBYTECODE=True
export DJANGO_SETTINGS_MODULE=project.config.settings
alias runserver='~/venv/bin/django-admin runserver 0.0.0.0:8000'
cd /vagrant
