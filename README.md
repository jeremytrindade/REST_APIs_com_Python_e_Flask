# REST_APIs_com_Python_e_Flask

Continua a dar-me 2.7

python --version

Python 2.7.16

Tenho de escrever python3 para aparecer a versão 3

python3 --version

Python 3.8.2

Para corrigir fiz:

alias python=python3.8

E assim que coloquei:

pip install virtualenv

apareceu logo no inicio:

DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support

depois no fim da instalação aparece:

WARNING: The script virtualenv is installed in '/Users/jeremydatrindade/Library/Python/2.7/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.


E quando uso o comando:

virtualenv ambvir --python=python3.8

recebo este erro:

zsh: command not found: virtualenv

Então usar o pip no python3 fiz:

 alias pip=pip3

depois:

pip install virtualenv

virtualenv ambvir --python=python3.8

Porém quando chego a parte de:

python app.py

Recebo:

Traceback (most recent call last):
  File "app.py", line 2, in <module>
    from flask_restufl import Resource, Api
ModuleNotFoundError: No module named 'flask_restufl'
