# Matlab TDS

Matlab TDS is an implementation of the Time Delay Stability algorithm, introduced by Bashan et al. [doi:10.1038/ncomms1705](https://doi.org/10.1038/ncomms1705). It can be used in sleep research to determine the topology of the physiological networks by analysis of a polysomnographic recording. The Matlab TDS software is developed at CBMI (HTW Berlin - University of Applied Sciences)

The application is packaged as [Curious Containers](https://www.curious-containers.cc) compatible Docker image, available in the official [DockerHub](https://hub.docker.com/r/curiouscontainers/cc-tds-app/) registry.

The repo allows you to reproduce a computer experiment we conducted for a scientific publication on physiological networks [doi:10.1088/1361-6579/aa614e](https://doi.org/10.1088/1361-6579/aa614e). This repo is a demonstration of how digital experiments can be stored in a reproducible way [doi:10.1145/3147234.3148104](https://doi.org/10.1145/3147234.3148104). As part of the demonstration, the data is protected and can only be accessed with valid user credentials. We will soon create a version with accessible data and will update this guide accordingly. If you want to try the method with free data, use the sample implementation based on a pre-built docker container (https://github.com/somnonetz/tds-experiment-cap)

# Getting Started

## Prerequisites

You require virtualbox and vagrant.

## Setup environent

Description for Linux

1. Clone the repo:

   git clone https://github.com/somnonetz/cc-tds-app.git
   
2. Move into the directory cc-tds-up
   
   cd cc-tds-up
   
3. Create your vagrant box

   vagrant up
   
4. Log into the vagrant box

   vagrant ssh
   
5. Change to the /vagrant directory 

   [vagrant@localhost ~]$ cd /vagrant

6. Build your docker container

    [vagrant@localhost vagrant]$ docker build -t "tds_app_tawian" . 

7. Install cc-faice (will be included into the vagrant provisioning soon!)

   pip3 install --user cc-faice==3.2
   
## Run the application

    [vagrant@localhost vagrant]$ faice agent red --disable-pull ./red.yml

At this point you will be asked to give the user credentials. If you are supercurious, please contact us, if you have a bit of patience, wait for the update, we will update the repo with accessible data soon.    
   
   

