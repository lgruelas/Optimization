[![Build Status](https://api.travis-ci.org/lgruelas/Optimization.svg?branch=master)](https://travis-ci.org/lgruelas/Differential-Evolution)
[![license](https://img.shields.io/badge/licence-GPL--3-blue.svg)](https://github.com/lgruelas/Optimization/blob/master/LICENSE)

# Optimization

![Python master race](assets/python.png?raw=true "python")

## Getting started

Install python and virtualenv.

```
sudo dnf -y install python2
sudo dnf -y install python2-pip
pip2 install --user virtualenv
```

Then create the virtual enviroment.

```
virtualenv -p python2 virtualenv_opt
```

To start the virtual enviroment use:

```
source virtualenv_opt/bin/activate
```

Install the package with 
```
chmod +x setup.sh
./setup.sh
```

to exit the virtual enviroment just run
```
deactivate
```

## Unit Tests

To run the test run install dependencies with
```
pip install -r requirements.txt 
```
and use
```
python -m pytest -v
```
whit the virtual environment activate

## Built With

* [Python](https://www.python.org/downloads/)


## Authors

* **Jorge Alanis** - [GitHub](https://github.com/GeorgeAlanis)
* **Germán Ruelas** - [GitHub](https://github.com/lgruelas)