Ambiente virtual

python3 -m venv nome-do-ambiente
source nome-do-ambiente/bin/activate

pip install --upgrade
pip setuptools wheel
pip install pygobject PyGObject-stubs
pip install vext
pip install vext.gi
pip install sqlalchemy
pip istall mysql-connector-python
pip install pandas
#panda é um data frame muito poderoso

pip install pymysql # driver do banco mysql


pip install pydantic[email]
# or
pip install pydantic[dotenv]
# or just
pip install pydantic[email,dotenv]

pip install datamodel-code-generator

pip install dacite

para testar
python3 -c "import gi"

pip freeze > requirements.txt

como instalar  mysql
PASSO 1
INTALAÇÃO

sudo mysql
sudo apt install mysql-server
sudo systemctl start mysql.service

PASSO 2
CONFIGURANDO MYSQL

mysql -u root -p---->root@localhost psw aoDt1snnMYSQL
select user from mysql.user;
CREATE USER 'johndizaro'@'localhost' IDENTIFIED BY 'ao[D]t1snnMYSQL';
DROP USER 'johndizaro'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'johndizaro'@'localhost';
SHOW GRANTS;


mysql -u johndizaro -p ---->johndizaro@localhost psw ao[D]t1snnMYSQL
CREATE DATABASE orca;
SHOW DATABASES;
USE orca ---> orca é nome do banco de dados que vc quer usar
exit


Como ativar o Gtk inspector

Para poder utilizar o Gtk inspector com aplicativos que utilizam um sistema de empacotamento tradicional (deb, rpm, etc), abra um terminal e digite o seguinte comando:

gsettings set org.gtk.Settings.Debug enable-inspector-keybinding true

Para utilizar a depuração interativa, abra um aplicativo GTK e pressione as telas de atalho

Ctrl + Shift + d ou Ctrl + Shift + i.


