# Matlab TDS

Matlab TDS is an implementation of the Time Delay Stability algorithm, introduced by Bashan et al. ([doi:10.1038/ncomms1705](https://doi.org/10.1038/ncomms1705)). It can be used in sleep research to determine the topology of the physiological networks by analysis of a polysomnographic recording. The Matlab TDS software is developed at CBMI (HTW Berlin - University of Applied Sciences)

The application is packaged as [Curious Containers](https://www.curious-containers.cc) compatible Docker image, available in the official [DockerHub](https://hub.docker.com/r/curiouscontainers/cc-tds-app/) registry.

This experiment is a demonstration of how digital experiments can be stored in a reproducible way ([doi:10.1145/3147234.3148104](https://doi.org/10.1145/3147234.3148104)). The current experiment uses the freely available dataset from physiobank's [SHHS Polysomnography Database](https://physionet.org/physiobank/database/shhpsgdb/).

# Getting Started

## Prerequisites

To execute the experiment you need a Linux environment with Docker, Python3 and CC-FAICE. See [CC-FAICE](https://www.curious-containers.cc/cc-faice.html) in the Curious Containers documentation for detailed installation instructions.

   pip3 install --user cc-faice==5.2

## Run the Experiment

1. Clone the repo:

   git clone https://github.com/somnonetz/physiological-networks-tds-experiments
   
2. Move into the directory physiological-networks-tds-experiments
   
   cd physiological-networks-tds-experiments
   
3. Start the faice agent

    faice agent red --ignore-outputs ./red.yml

## Explore the results

The results are stored in the `work` folder, called  that faice has created in your current working directory. These are matlab-archives. You presumably need a matlab-license to open and inspect them.  


   
   

