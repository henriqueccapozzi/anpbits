FROM centos:8

RUN \
    yum --enablerepo=extras install --nogpgcheck -y epel-release && \
    yum install --nogpgcheck -y python3 sshpass && \
    pip3 install ansible paramiko
COPY ./resources /resources
ENV PATH="/resources/setup:${PATH}"

WORKDIR /anpbits