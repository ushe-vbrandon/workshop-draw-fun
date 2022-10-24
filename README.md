# Draw Fun With SQL
Discover the rules of the game by writing .sql files and running the draw command!

## How to Play
1. Create a file with the naming pattern [A-9].sql
2. Write a complete query of the integer dimensional parameters x, y, and z.  Make sure to terminate with a ";"
3. Run draw-fun with:
```bash
python main.py draw --all true
./draw-fun draw --all true
```

## Secret Rules
Add more files with more queries to discover how the draw-fun renderer works! 

Work with your team to craft the OBJECTIVE message!


## Environment
Supported OS:
- Windows 10
- Windows 11
- Ubuntu 20.04
- MacOS XX.X (untested)

**python version == 3.10**

### Virtual environment with Pipenv
Support Pipenv and Conda Python environment management via requirements.txt

**Pipenv**
Note: pipenv can be installed as an OS package ('dnf install pipenv') or as python package with base python installed ('pip install --user pipenv')
```bash
pipenv install -r requirements.txt
# activate shell
pipenv shell
```

**Conda**
```bash
conda create --name draw-fun python=3.10
conda activate draw-fun
conda install pip
pip install -r requirements.txt
```

