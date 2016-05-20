#!/bin/bash
# Script to setup docker on OS X

PROJECTNAME = babydocker

# Check that brew is installed.
if ! which -s aws; then
    echo "Install brew: http://brew.sh";
    exit 1;
fi

# Install docker-machine, no need to install docker-toolbox as that includes
# a bunch of extra things, like a GUI you don't need.
if ! which -s docker-machine; then
    brew update;
    brew install docker-machine;
fi

# Install docker-compose
if ! which -s docker-compose; then
    brew update;
    brew cask install docker-compose;
fi

# Install virtualbox
if ! which -s virtualbox; then
    brew update;
    brew cask install virtualbox;
fi

# Create docker instance
echo "Creating default docker instance..."
echo "docker-machine create --driver virtualbox default"
docker-machine create --driver virtualbox default

# Configure shell
echo "Configuring shell..."
eval $(docker-machine env default)

echo "$(docker-machine version) is up and running!"
