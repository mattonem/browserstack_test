# browserstack_test

a simple python test suite example that runs 3 tests across web 5 browers on Browserstack in parallele.

## setup

```
pip install requirements.txt
```

Make sure you have `python3 python3-pytest python3-pytest-xdist` installed

Make sure your env variables are correctly set:

```
BROWSERSTACK_USERNAME=username
BROWSERSTACK_ACCESS_KEY=key
```

## run

```
python3 -m pytest -n 3 -rA
```
