Ambiente virtual

python3 -m venv nome-do-ambiente
source nome-do-ambiente/bin/activate

pip install --upgrade
pip setuptools wheel
pip install pygobject PyGObject-stubs
ip install vext
pip install vext.gi
pip install sqlalchemy

para testar
python3 -c "import gi"

pip freeze > requirements.txt