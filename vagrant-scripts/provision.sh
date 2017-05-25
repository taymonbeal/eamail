#!/usr/bin/env bash
set -o errexit
set -o pipefail
sudo apt-get --assume-yes update
sudo DEBIAN_FRONTEND=noninteractive apt-get --assume-yes install build-essential libbz2-dev libmysqlclient-dev libreadline-dev libsqlite3-dev libssl-dev mysql-server-5.7 ruby-dev
sudo apt-get --assume-yes autoremove
sudo gem install mailcatcher
wget --output-document=- --progress=bar:force https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
~/.pyenv/bin/pyenv install --verbose 2.7.13
~/.pyenv/versions/2.7.13/bin/pip install --upgrade pip
~/.pyenv/versions/2.7.13/bin/pip install virtualenv
~/.pyenv/versions/2.7.13/bin/virtualenv ~/venv
source /vagrant/vagrant-scripts/session.sh
pip install --requirement=/vagrant/requirements.txt
mysql_tzinfo_to_sql ~/venv/lib/python2.7/site-packages/pytz/zoneinfo | sudo mysql mysql
sudo service mysql restart
sudo mysql </vagrant/vagrant-scripts/provision.sql
django-admin migrate --no-input
python /vagrant/vagrant-scripts/provision.py
echo >>~/.bashrc
echo 'source /vagrant/vagrant-scripts/session.sh' >>~/.bashrc
