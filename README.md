# jupyterhub-vanilla
This is a simple way of deploying JupyterHub in a container with a local spawner. It creates a handful of accounts without requiring a valid password to login. It is meant to be a starting point to experiment with various components like Spawners, Authenticators, and notebooks.

1. Build: `docker build -t myhub .`
1. Run: `docker run -p 8000:8000 myhub`
1. Connect to http://localhost:8000 with a web browser.
1. Login as user0 through user9 with an empty password.
