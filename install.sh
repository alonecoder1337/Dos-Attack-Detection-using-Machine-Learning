#!/bin/bash

sudo apt-get update
sudo apt-get install -f
sudo apt-get install python-setuptools python-numpy python-scipy python-matplotlib python-pip -y
sudo pip install numpy scipy matplotlib scikit-learn luminol -y
