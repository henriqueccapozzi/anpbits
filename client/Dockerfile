FROM centos:8

RUN yum install -y \
    --nogpgcheck \
    openssh-server

RUN echo "==> Setting up sshd" && \
    ssh-keygen -A && \
    mkdir -p /var/run/sshd && \
    rm -f /run/nologin && \
    echo "==> Creating users and setting passwords" && \
    useradd student && \
    echo 'student:anpbits' | chpasswd && \
    echo 'root:anpbits' | chpasswd && \
    echo "==> Creating entrypoint.sh" && \
    echo "#!/bin/bash" > /entrypoint.sh && \
    echo "echo Container started" >> /entrypoint.sh && \
    echo "/usr/sbin/sshd -p 22 -E /var/log/sshd.log" >> /entrypoint.sh && \
    echo "tail -f /var/log/sshd.log" >> /entrypoint.sh && \
    touch /var/log/sshd.log && \
    chmod +x /entrypoint.sh

EXPOSE 22

ENTRYPOINT /entrypoint.sh