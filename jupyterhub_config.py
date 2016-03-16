# Configuration file for Jupyter Hub
c = get_config()

# Base configuration
c.JupyterHub.log_level = "INFO"
c.JupyterHub.db_url = 'sqlite:////srv/jupyterhub/jupyterhub.sqlite'
c.JupyterHub.proxy_check_interval = 30
c.JupyterHub.admin_access = True
c.JupyterHub.confirm_no_ssl = True

c.LocalAuthenticator.create_system_users = True

c.Authenticator.whitelist = set()
for i in range(10):
	c.Authenticator.whitelist.add('user{}'.format(i))

#import os
#import sys

# Configure the authenticator
#c.JupyterHub.authenticator_class = 'docker_oauth.DockerOAuthenticator'
#c.DockerOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']
#c.DockerOAuthenticator.create_system_users = True
# c.Authenticator.admin_users = admin = set()
# c.Authenticator.whitelist = whitelist = set()

# Configure the spawner
#c.JupyterHub.spawner_class = 'swarmspawner.SwarmSpawner'
#c.SystemUserSpawner.container_image = 'systemuser'
#c.DockerSpawner.tls_cert = '{{ docker_tls_path }}/cert.pem'
#c.DockerSpawner.tls_key = '{{ docker_tls_path }}/key.pem'
#c.DockerSpawner.remove_containers = True
#c.Spawner.start_timeout = 300
#c.Spawner.http_timeout = 150

# Possibly prevent NFS locking issues with sqlite
# https://github.com/jupyter/dockerspawner/issues/46
# c.HistoryManager.enabled = False

# The docker instances need access to the Hub, so the default loopback port
# doesn't work:
#c.JupyterHub.hub_ip = '{{ servicenet_ip }}'

# Add users to the admin list, the whitelist, and also record their user ids
#root = os.environ.get('OAUTHENTICATOR_DIR', os.path.dirname(__file__))
#sys.path.insert(0, root)

#with open(os.path.join(root, 'userlist')) as f:
#    for line in f:
#        if line.isspace():
#            continue
#        parts = line.split()
#        name = parts[0]
#        whitelist.add(name)
#        if len(parts) > 1 and parts[1] == 'admin':
#            admin.add(name)

