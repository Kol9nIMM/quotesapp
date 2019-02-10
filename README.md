# quotesapp
Random generated quotes with Python/Vue.js stack

# Config Python

1) Download Python from official website: https://www.python.org/
2) Install Python. You can find a tutorial how to install it on different OS in the Internet.
3) Install pip. This is package manager for Python.

Ok, you have python and pip on your machine. Let`s configure virtualenv 

- Using pip download 'virtualenv' package.
```sh
$ pip install virtualenv
``` 
- Create new virtualenv
```sh
$ virtualenv -p python=python<version> <name of virtual env>
```
- Activate new virtualenv
```sh
$ source <name of virtualenv>/bin/activate
```
 - Virtualenv is activated. Install all the packages needed in this projects
 ```sh
$ pip install -r requirements.txt
``` 
 