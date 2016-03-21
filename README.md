# jupyterhub-vanilla
This is a simple way of deploying JupyterHub in a container with a local spawner. It creates a handful of accounts without requiring a valid password to login. It is meant to be a starting point to experiment with various components like Spawners, Authenticators, and notebooks.

## If on Mac:
1. Download and install [Docker Toolbox](https://www.docker.com/products/docker-toolbox).
1. Open the Docker Quickstart Terminal application in Applications > Docker.
1. Execute: `docker-machine upgrade`.
1. If on Linux, install docker.
1. In the terminal, cd to the directory where you cloned this repository and run: `docker build -t myhub .`
1. Run: `docker run -p 8000:8000 myhub`
1. Open Applications > Docker > Kinematic
1. Click on the "myhub" container on the left side.
1. Click on the web preview on the right side.
1. If on Linux, connect to http://localhost:8000 with a web browser.
1. Login as user0 through user9 with an empty password.

## If on Windows:
Before starting, make sure to have VT-x enabled or you will get an error at Step 2. Check if your CPU processor has the feature built-in. If so, go to BIOS and enable VT-x.

1. Download and install [Docker Toolbox](https://www.docker.com/products/docker-toolbox).
  1. After this step, Docker Quickstart Terminal shortcut and Kinematic shortcut may have been made on your Desktop.
2. Open the Docker Quickstart Terminal application.
  1. Running the Docker Quickstart Terminal will set-up your environment and install docker.
3. In your own terminal or the Docker Quickstart Terminal:
  1. Clone this git repository.
  1. Execute: `docker-machine upgrade`
  1. cd to the directory where you cloned this repository and run: `docker build -t myhub .`
  1. Run: `docker run -p 8000:8000 myhub`
4. Open the Kinematic application and you will see a 'myhub' container on the left side.
5. Click on the 'myhub' container.
6. Click on the web preview on the right side (it will open a new window/tab).
7. Login as user0 through user9 with an empty password.
