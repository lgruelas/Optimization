[![Build Status](https://api.travis-ci.org/lgruelas/Optimization.svg?branch=master)](https://travis-ci.org/lgruelas/Optimization)
[![codecov](https://codecov.io/gh/lgruelas/Optimization/branch/master/graph/badge.svg)](https://codecov.io/gh/lgruelas/Optimization)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0427f6cf79164385bcd5c59ba59d0334)](https://app.codacy.com/app/lgruelas/Optimization?utm_source=github.com&utm_medium=referral&utm_content=lgruelas/Optimization&utm_campaign=Badge_Grade_Dashboard)
[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/Optimization/blob/master/LICENSE)

# Optimization

![Python master race](assets/python.png?raw=true "python")

## Getting started

Install python and virtualenv.

```bash
sudo dnf -y install python2
sudo dnf -y install python2-pip
pip2 install --user virtualenv
```

Then create the virtual enviroment.

```bash
virtualenv -p python2 virtualenv_opt
```
if fails try with
```bash
python -m virtualenv -p python2 virtualenv_opt
```
To start the virtual enviroment use:

```bash
source virtualenv_opt/bin/activate
```

Install the package with 
```bash
chmod +x setup.sh
./setup.sh
```

to exit the virtual environment just run
```bash
deactivate
```

## Unit Tests

To run the test run install dependencies with
```bash
pip install -r requirements.txt 
```
and use
```bash
python -m pytest -v
```
whit the virtual environment activate

## Built With

*   [Python](https://www.python.org/downloads/)

## Authors

*   **Jorge Alanis** - [GitHub](https://github.com/GeorgeAlanis)
*   **Germán Ruelas** - [GitHub](https://github.com/lgruelas)