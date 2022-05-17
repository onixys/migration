# Migration tool - testing

```
$ python -m pip install mypy   # checking typings
$ python -m pip install flake8 # checking code style - linting
$ python -m pip install pytest # run tests
$ python -m pip install tox    # tests for multiple envs

$ mypy src
$ flake8 src
$ pytest

$ pip install -r ./requirements_dev.txt
$ pytest
``` 