# anpbits - Hands on ansible


## Setting up the easy way. (Requires internet connection)

- Navigate to [Docker Playground](https://labs.play-with-docker.com)

- Log in with you docker account. Or create one if you don't already have one

- Download the docker-compose.yml from this repo and run docker-compose up
    
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
Test your ssh access

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
Congratulations!

Now let's start with the good stuff 



## <a id="l2"></a> Lesson 2 - Adding hosts to our inventory

The standard way that ansible works is executing actions agains 1 or more **targets**
In the previous lesson we used **localhost** as the target for our command, but even though is very usefull to automate our ansible controller, the greatest
value is in automating things on other servers or networking equipment.

In order to get that to work, we need to use an [inventory](#inventory), to simplify the learning processes, we'll create one in the default path 
that Ansible looks for one which is '/etc/ansible/hosts'

```bash
# On real life things will not always be ready the way you would expect ;-)
mkdir -p /etc/ansible

echo 'client-1' >> /etc/ansible/hosts
echo 'client-2' >> /etc/ansible/hosts
```

Apart from the inventory let's add a couple of configurations
parameters so that the output of our commands are more friendly.

```bash
export ANSIBLE_PYTHON_INTERPRETER=/usr/libexec/platform-python
export ANSIBLE_HOST_KEY_CHECKING=false
```

Now that's out of our way, let's run another ansible command
```bash
ansible all -m ansible.builtin.shell -a 'echo Hello from $(hostname)' -u student -k
# when prompted for a password enter ===> anpbits
```

We added new command line parameters, and that's what they mean

| Parameter | Explanation |
| --- | --- |
*-u student* |  Tell ansible which user to use for the ssh connection against it's **targets**
*-k* | prompt's for the ssh user password
*-m ansible.builtin.shell* | Ansible **module** name
*-a 'echo Hello from $(hostname)'* | **module argument** which in this case does not have a name like the one used previously

<br>
<br>

