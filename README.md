## Installation

Having poetry installed in the wsl, run

cd code
poetry install

This will create a venv on ~/.cache/pypoetry/virtualenvs
On any python file you can configure vscode project interpreter to point to that virtualenvs /bin/python
Restarting terminal on vscode should target this new environment
Running the debug command on Run & Debug (Crtl Shft D) part of vscode will start the app
Note: it is likely that first you need to pip install poetry on that venv for it to work

Once the app is started with this mode you can use debug inside the project.

## Generator

./generator.sh grabs the open_api.yml and

Generates the spec
Moves it into /code/generated_api
Some seds for correct behaviour

One code is generated we can use the recommender project inside of code for implementing the clases
