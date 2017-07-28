FROM docker.io/curiouscontainers/cc-image-debian:0.12

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl unzip libxt6 \
&& mkdir /mcr-install \
&& curl -L https://www.mathworks.com/supportfiles/downloads/R2015a/deployment_files/R2015a/installers/glnxa64/MCR_R2015a_glnxa64_installer.zip > /mcr-install/installer.zip \
&& unzip /mcr-install/installer.zip -d /mcr-install \
&& /mcr-install/install -agreeToLicense yes -mode silent \
&& rm -r /mcr-install

COPY ./bin/linux/x86_64/R2015a/run_sn_TDS.sh /app/run_sn_TDS.sh
COPY ./bin/linux/x86_64/R2015a/sn_TDS /app/sn_TDS
COPY ./cc_wrapper.py /app/cc_wrapper.py
COPY ./cc_custom_downloaders.py /app/cc_custom_downloaders.py
COPY ./cc_custom_uploaders.py /app/cc_custom_uploaders.py
COPY ./config.json /root/.config/cc-container-worker/config.json

ENV PATH /app:${PATH}
ENV PYTHONPATH /app:${PYTHONPATH}

RUN chmod -R 775 /app
