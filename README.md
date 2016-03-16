# jupyterhub-vanilla
This is a simple way of deploying JupyterHub in a container with a local spawner. It creates a handful of accounts without requiring a valid password to login. It is meant to be a starting point to experiment with various components like Spawners, Authenticators, and notebooks.

1. If on Mac or Windows
  1. Download and install [Docker Toolbox](https://www.docker.com/products/docker-toolbox).
  1. Open the Docker Quickstart Terminal application in Applications > Docker.
  1. Execute: `docker-machine upgrade`.
1. If on Linux, install docker.
1. In the terminal, cd to the directory where you cloned this repository and run: `docker build -t myhub .`
1. Run: `docker run -p 8000:8000 myhub`
1. If on Mac or Windows:
  1. Open Applications > Docker > Kinematic
  1. Click on the "myhub" container on the left side.
  1. Click on the web preview on the right side.
1. If on Linux, connect to http://localhost:8000 with a web browser.
1. Login as user0 through user9 with an empty password.
