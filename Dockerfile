FROM jupyter/jupyterhub:0.5.0
EXPOSE 8000

# Let in everyone without password
RUN sed -i -e '/pam_deny/s/^/#/' /etc/pam.d/common-auth

# Install notebook in case we're not using an exotic spawner
RUN conda install notebook==4.1.0
