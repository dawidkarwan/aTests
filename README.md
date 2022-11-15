# aTests
Automatic tests project to control quality of web app http://testarena.pl/demo
based on
* Python
* Selenium


## Setup
To run this project

```
$ install Python 3.10
$ install mentioned packages e.g using pipenv
$ install allure and JRE
$ download chromedriver relevent to your Chrome browser version
$ add chromedriver and allure to path (user environmental varible)
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
###### Run tests by marker expression: <br>
`pytest -m commons` <br>
###### Run tests and generate report: <br>
`pytest --alluredir="reports_dir_path" -m e2e` <br>
`allure serve reports_dir_path`
![alt text](https://user-images.githubusercontent.com/57195955/201993713-cfea7ce8-52eb-4978-8edc-0e71c39872ff.png)


### Author and maintainer
Dawid Karwan