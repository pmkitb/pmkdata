# pmkdata

A web application for managing PMK ITB's data.

## How to run

Prerequisites: Python and Pipenv installed

1. Clone this repository to your local machine
2. `cd <repo_directory>`
3. Copy `.env.example` to `.env`, then edit its contents as needed to adjust Django settings
4. `pipenv install --dev` to install dependencies
5. `pipenv shell` to set up virtualenv and environment variables automatically
6. `python manage.py migrate` to create DB tables
7. `python manage.py runserver` to start the development server, which can be accessed on `localhost:8000`

## How to deploy using Ansible

### Prerequisites

- Ansible installed on your local machine
- A Ubuntu 18.04 server or equivalent (DigitalOcean droplet recommended). Ensure you can SSH to the `root` user on your server using public key authentication.

WARNING: the Ansible playbook will disable SSH password logins by default. If you use password login for SSH, set the `ssh_disable_password_auth` variable to false in `ansible/vars/main.yml`.

### Steps

1. `cd <repo_directory>/ansible`
2. Edit variables `vars/main.yml` as needed
3. `ansible-vault edit vars/vault.yml --ask-vault-pass`, then enter the vault password. Set the repository deploy key (e.g. Github deploy private key) if necessary; comment it otherwise. Edit other variables as needed, then save and quit the editor
4. Edit `hosts` file - enter your server hostname
5. `ansible-playbook create-sudo-user.yml -i hosts --ask-vault-pass` to create `pmkdata` user (vault password required)
6. `ansible-playbook main.yml -i hosts --ask-vault-pass` to set up and deploy app (vault password required). Note: this step will also disable root SSH login for security reasons. From now on, you can use the `pmkdata` application user

### Creating the Django superuser

1. SSH to the `pmkdata` application user on the server
2. On the server, `cd /opt/pmkdata`
3. `pipenv shell`
4. `python manage.py createsuperuser`

### Notes

- To deploy on a provisioned system, use `ansible-playbook main.yml -i hosts -t deploy --ask-vault-pass`. WARNING: this will also run the DB migration
- The system Python will be used by default (requires Python 3)
- It is assumed that Gunicorn is installed as a Pipenv app dependency
- Firewall (UFW) is set to only allow SSH and Nginx HTTP and HTTPS
