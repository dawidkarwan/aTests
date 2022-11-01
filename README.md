# aTests
Automatic tests project to control quality of webapp http://testarena.pl/demo
based on
* Python
* Selenium


## Setup
To run this project

```
$ install Python 3.10
$ install mentioned packages e.g using pipenv
$ download chromedriver relevent to your Chrome browser version
$ add chromedriver to path (user environmental varible)
```

### Packages
```
allure-pytest = "*"
assertpy = "*"
pytest = "*"
selenium = "4.4.3"
dacite = "*"
```

### Example of use
Run tests by marker expression: `pytest -m 2e2`

### Author and maintainer
Dawid Karwan