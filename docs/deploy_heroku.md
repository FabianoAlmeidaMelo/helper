## Instalar HEROKU Toolbelt

wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

## Vá para a pasta raíz do Repositório (onde está o requirements.txt)

cd WORKSPACE/helper

## Logar-se no HEROKU (e-mail e senha requeridos)

heroku login

## Criar uma instância de servidor no HEROKU

heroku create

Sua instância poderá ser vista em https://dashboard.heroku.com/apps

## Iniciar deploy

git push heroku master
