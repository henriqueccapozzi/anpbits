# anpbits - Ansible na prática

[English version](README_en.md)
<br>
<br>

## Começando do jeito fácil. (É necessário ter conexão com a internet)


- Acesse a página [Docker Playground](https://labs.play-with-docker.com)

- Faça login com sua conta Docker. Ou crie uma se você ainda não tiver.

- Faça o download do arquivo docker-compose.yml and run docker-compose up
    
    ``` bash
    DOCKER_COMPOSE_URL='https://raw.githubusercontent.com/henriqueccapozzi/anpbits/main/docker-compose.yml'
    mkdir anpbits && cd anpbits && \
    curl ${DOCKER_COMPOSE_URL} -o docker-compose.yml && \
    docker-compose up -d
    ```

## Índice

- [Lição 1 - Primeiro comando ansible](#l1)

- [Lição 2 - Adicionando nossos primeiros hosts ao inventario](#l2)

- [Lição 3 - Instalando o python nos nossos alvos](#l3)

<br>
<br>
<br>
<br>


## <a id="l1"></a> Lição 1 - Primeiro comando ansible
O Ansible usa conexões SSH para muitos de seus modulos. Mas nossa maquina que ira rodar o ansible não tem SSH instalado. 

Bom, vamos usar o ansible para nos ajudar com isso

Primeiro precisamos nos 'conectar' com o container usando o comando abaixo

```bash
CONTROLLER_ID=$(docker ps | grep 'controller' | awk '{print $1}')
docker exec -it ${CONTROLLER_ID} bash
```

Depois disso vamos usar um comando ansible no modo **adhoc** para instalar um pacote usando o 
modulo 'yum'

```bash
ansible localhost -m 'ansible.builtin.yum' -a 'name=openssh-clients' -v
```
Vamos detalhar um pouco o que acabamos de fazer

| Commando | Explicação |
| --- | --- |
*ansible* |  Bom, dispensa comentários
*localhost* | **alvos** para o comando 'ansible'
*-m ansible.builtin.yum* | Nome do **modulo** ansible
*-a name=openssh-clients* | **argumento para o módulo** nome=valor

<br>
Teste o acesso SSH
<br>
<br>

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
Parabens!

Agora vamos começar a parte boa

<br>
<br>


## <a id="l2"></a> Lição 2 - Adicionando nossos primeiros hosts ao inventario

A forma padrão de trabalho do Ansible é de executar ações contra 1 ou mais **alvos**
Na lição passada usamos **localhost** como o alvo do nosso comando, mas apesar de 
ser de grande utilidade automatizar processos no controller do ansible, o grande valor
está em automatizar outros servidores.

Para isso vamos precisar usar um [inventario](#inventario), e para simplificar o aprendizado, vamos criar um no local onde o Ansible vai procurar por padrão.

```bash
# Na vida real as coisas não estaram sempre prontas ;-)
mkdir -p /etc/ansible

echo 'client-1' >> /etc/ansible/hosts
echo 'client-2' >> /etc/ansible/hosts
```

Além do inventário vamos adicionar alguns parametros de configuração para que as respostas iniciais fiquem mais amigáveis

```bash
export ANSIBLE_PYTHON_INTERPRETER=/usr/libexec/platform-python
export ANSIBLE_HOST_KEY_CHECKING=false
```

Feito isso podemos executar nosso próximo comando 
```bash
ansible all -m ansible.builtin.shell -a 'echo Ola do $(hostname)' -u student -k
# Lembrando que a senha é ==> anpbits
```

Nesse comando temos a adição de novos parâmetros de linha de comando

| Parametro | Explicação |
| --- | --- |
*-u student* |  especifica qual o usuário o ansible vai usar na conexão ssh com os **alvos**
*-k* | faz um prompt para inserir a senha que será usada na conexão ssh
*-m ansible.builtin.shell* | Nome do **modulo** ansible
*-a 'echo Ola do $(hostname)'* | **argumento para o módulo** neste caso o módulo nao tem parâmetros nominais como o usado anteriormente

<br>
<br>



## <a id="l3"></a> Lição 3 - Instalando o python nos nossos alvos

Python é a linguagem nativa do Ansible, e grande parte de sua funcionalidade é através do uso de bibliotecas python.
Como nossos 'clientes' simulam uma instalação minima de um sistema centos8 (usando containers), somente uma pequena parte do python esta disponível neles.

Vamos usar o ansible para já deixar nossos clientes 'preparados' para as próximas etapas.

```bash
# Se você não completou a lição 2 agora, faça os preparativos abaixo primeiro
mkdir -p /etc/ansible

echo 'client-1' >> /etc/ansible/hosts
echo 'client-2' >> /etc/ansible/hosts
export ANSIBLE_PYTHON_INTERPRETER=/usr/libexec/platform-python
export ANSIBLE_HOST_KEY_CHECKING=false

# -------------------------------
# Se você já exportou as variaveis anteriormente, contunie daqui
# -------------------------------
ansible all -m ansible.builtin.dnf -a 'name=python38' -u student -k --become
# Lembrando que a senha é ==> anpbits
```


Nesse comando a nossa única novidade é o parametro de linha de comando '--become'
que é usado no ansible para executar comandos no modo privilegiado



<br>
<br>

## <a id="l4"></a> Lição 4 - Executando nosso primeiro playbook

Até agora executamos comandos 'ansible', que são chamados **comandos adhoc**
eles são relativamente simples de usar, porem é fácil de ver que para casos complexos o comando ficaria bem difícil de trabalhar.

Os comandos adhoc são geralmente usados para tarefas pontuais, ou para o que fizemos nas lições de 1 a 3, que foi preparar a infra estrutura necessária para
o que vem pela frente.

### O comando: ansible-playbook

A melhor forma de aproveitar o poder do ansible é usando [playbooks](#playbook)

Um playbook é um arquivo no formato [yaml](https://yaml.org), que especifica o que o ansible deve fazer ao interagir com cada um dos seus alvos

```bash
```

<br>


# Definições

#### inventario
#### controller
#### alvo
#### playbook