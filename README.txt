Ambiente virtual

python3 -m venv nome-do-ambiente
source nome-do-ambiente/bin/activate

pip install --upgrade pip setuptools wheel
pip install pygobject PyGObject-stubs
pip install sqlalchemy

para testar
python3 -c "import gi"

pip freeze > requirements.txt