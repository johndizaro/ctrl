Ambiente virtual

python3 -m venv nome-do-ambiente
source nome-do-ambiente/bin/activate
pip install --upgrade pip setuptools wheel
pip install pygobject PyGObject-stubs

para testar
python3 -c "import gi"