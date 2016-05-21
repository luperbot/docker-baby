===========
Baby-Docker
===========

Baby-Docker is a quick setup for Docker on OS X. It contains sample services
that can be copied into a new project.

The setup_docker.sh script does not contain the Docker toolbox GUI. For that,
you must download [Docker Toolbox](https://www.docker.com/products/docker-toolbox).
Otherwise, if you are comfortable with OS X command line, the setup_docker.sh
script will provide everything you need to start. The only dependency required
is that brew and Xcode are installed. 

=====
Steps
=====

The below command only needs to be run the very first time you use docker on your
computer. It will install everything you need to develop on and run Docker.

.. code:: bash

        $ # Setup Docker for the first time on OS X
        $ bash setup_docker.sh

The below command needs to be run everytime you open a new terminal, in order to
connect your shell to a specific docker machine. By default, the name of
your initial docker machine is called 'default'.
If you will only be using a single docker machine, you can append the command
to your ~/.bash_profile to avoid typing it each time you open a new terminal
window.

.. code:: bash

        $ # Connect your shell to the 'default' machine
        $ eval $(docker-machine env default)

The first time you run docker-compose, it will search your computer for the
images listed in docker-compose.yml and all Dockerfiles. If they aren't already
downloaded, docker will download them from the internet (Docker Hub).

.. code:: bash

        $ # Run all of the services
        $ docker-compose up
        $ # Run only python-flask and rabbitmq services
        $ docker-compose run python-flask rabbitmq

In the docker-compose.yml file, the 'python-flask' service has port 5000 linked
to port 5000. Which means that you can view the running flask services via
your local browser. To find the IP Address, type `docker-machine ls`, and connect
to the IP Address list, with port 5000 (example: http://192.168.99.100:5000). 

==========
Developing
==========

As long as the service has a volumne listed, you can edit the files in your
cloned git repo, and the files will automatically sync with those in the Docker
container. 

Example:
If I change the python-flask/app.py file in debug mode, then those changed will
automatically appear in the docker image, the flask app will restart, and I can
view those changes in my local browser.
