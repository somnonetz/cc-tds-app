FROM docker.io/curiouscontainers/cc-image-debian:0.11

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl unzip libxt6 \
&& mkdir /mcr-install \
&& curl -L https://www.mathworks.com/supportfiles/downloads/R2015a/deployment_files/R2015a/installers/glnxa64/MCR_R2015a_glnxa64_installer.zip > /mcr-install/installer.zip \
&& unzip /mcr-install/installer.zip -d /mcr-install \
&& /mcr-install/install -agreeToLicense yes -mode silent \
&& rm -r /mcr-install

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3

COPY ./bin/linux/x86_64/R2015a/run_sn_TDS.sh /root/run_sn_TDS.sh
COPY ./bin/linux/x86_64/R2015a/sn_TDS /root/sn_TDS
COPY ./tds_app.py /root/tds_app.py
COPY ./config.json /opt/config.json
COPY ./custom_downloaders.py /opt/container_worker/custom_downloaders.py