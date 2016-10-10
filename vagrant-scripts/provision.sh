#!/usr/bin/env bash
set -o errexit
set -o pipefail
sudo apt-get --assume-yes update
sudo DEBIAN_FRONTEND=noninteractive apt-get --assume-yes install libbz2-dev libmysqlclient-dev libreadline-dev libsqlite3-dev libssl-dev mysql-server-5.7
sudo apt-get --assume-yes autoremove
wget --output-document=- --progress=bar:force https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
~/.pyenv/bin/pyenv install --verbose 2.7.12
~/.pyenv/versions/2.7.12/bin/pip install --upgrade pip
~/.pyenv/versions/2.7.12/bin/pip install virtualenv
~/.pyenv/versions/2.7.12/bin/virtualenv ~/venv
source /vagrant/vagrant-scripts/session.sh
pip install --requirement=/vagrant/requirements.txt
sudo mysql </vagrant/vagrant-scripts/provision.sql
django-admin migrate --no-input
python /vagrant/vagrant-scripts/provision.py
echo >>~/.bashrc
echo 'source /vagrant/vagrant-scripts/session.sh' >>~/.bashrc
