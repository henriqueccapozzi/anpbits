# anpbits - Hands on ansible


## Setting up the easy way. (Requires internet connection)

- Navigate to [Docker Playground](https://labs.play-with-docker.com)

- Download the docker-compose and run docker-compose up
    
    ``` bash
    DOCKER_COMPOSE_URL='https://raw.githubusercontent.com/henriqueccapozzi/anpbits/main/docker-compose.yml'
    mkdir anpbits && cd anpbits && \
    curl ${DOCKER_COMPOSE_URL} -o docker-compose.yml && \
    docker-compose up -d
    ```


## Setting up locally. (Work in progress, just go the easy way for now)
- Make sure you have docker-compose installed. In case you don't have it yet please refer to the [official documentation](https://docs.docker.com/compose/install/)  


<br>
---
---
<br>
<br>

## Lesson 1 - Your first ansible command
Ansible uses in most cases ssh to manage remote hosts, but seems like our controller node does not have ssh installed.

Well lets run our first ansible commands to help up set up ansible =)

First **attach** to the container with

```bash
CONTROLLER_ID=$(docker ps | grep 'controller' | awk '{print $1}')
docker exec -it ${CONTROLLER_ID} bash
```

Then, run the following command
```bash
ansible localhost -m 'ansible.builtin.yum' -a 'name=openssh-clients' -v
```
Lets break it down a little more.

| Command | Explanation |
| --- | --- |
*ansible* |  Well, there's not much to say about that one
*localhost* | the ansible command **target host**
*-m ansible.builtin.yum* | ansible **module** name
*-a name=openssh-clients* | ansible **module argument** name=value

<br>
Test your ssh access, when prompted for 

```bash
[root@controller /]$ ssh student@client-1
"The authenticity of host 'client-1 (172.19.0.2)' can't be established.
ECDSA key fingerprint is SHA256:gijXgYcIb+y9Z5gCe3wDmKhnnlXW+ZrfT0KU92IhKWQ.
Are you sure you want to continue connecting (yes/no/[fingerprint])?" 
yes
"Warning: Permanently added 'client-1,172.19.0.2' (ECDSA) to the list of known hosts.
student@client-1's password:" 
# when prompted for a password enter ===> anpbits
anpbits
[student@client-1 ~]$
```