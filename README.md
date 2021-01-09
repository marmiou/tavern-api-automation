# QA Tavern API framework

QA API testing framework built for [reqres sample API](https://reqres.in/) with Tavern

## Getting Started

```
git clone git@github.com:marmiou/tavern-api-automation.git
```

### Prerequisites
 Tavern only supports Python 3.4 and up. At the time of writing we test against Python 3.4-3.7 and pypy3. 
 Python 2 is now unsupported. You will also need to have virtuaenv and virtualenvwrapper installed on your machine

 Also, make sure that you have setup your project to PYTHONPATH correctly (at least tests/ directory) 
 in your rc file (zshrc, bashrc etc). This is needed for calling external functions in Tavern:
 [Tavern docs](https://tavern.readthedocs.io/en/latest/basics.html#strict-key-checking)
 section: Calling external functions
    
 ```
 TAVERN_API=$CODE/tavern-api-automation
 TAVERN_API_TESTS=$TAVERN_API/tests
 TAVERN_API_CONFIG=$TAVERN_API/config
 PYTHONPATH=$PYTHONPATH:$TAVERN_API_CONFIG:$TAVERN_API_TESTS
 ```
### Installing
Install required packages:
```
pipenv install
```

To activate this project's virtualenv, run:
```
pipenv shell
```


## Running the tests

Run all tests:
```
cd tests/; pytest 
```

Run all tests in file:
```
cd tests/; pytest test_sample.tavern.yaml
```

Run test by keyword:
```
cd tests/; pytest -k '316'
```

Run with configuration file (different than the default):
```
cd tests/; pytest --tavern-global-cfg=../config/staging-global-cfg.yaml
```

Run test by allure:
```
cd tests/; pytest -v --alluredir {framework-dir}/report-allure -k "TEST";
```

See allure results:
```
allure serve {framework-dir}/report-allure;
```

## Built With

* [Tavern](https://tavern.readthedocs.io/en/latest/)
* [Pytest](https://docs.pytest.org/en/stable/)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Allure](http://allure.qatools.ru/)
* [Colorlog](https://pydigger.com/pypi/colorlog)
* [Sure](https://sure.readthedocs.io/en/latest/)
## Contributing

Please read [CONTRIBUTING.md](add a link here)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* *contributors* - Markella

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details

