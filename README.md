# python-base-repo
An example repository for Python projects that aims to use some of the best software development practices.

## Dependencies
* Python >= 3.10
* Anaconda >= 4.10

## Setup
1. Clone or download this repo. `cd` yourself to it's root directory.
2. Set up a Python virtual enviromnent, e.g. using [Anaconda](https://www.anaconda.com/) this can be achieved with:

`$ conda create python=3.10 --name ${env}`

`$ conda activate ${env}`

4. Install dependencies: `pip install -r requirements.txt`
5. Install development/test dependencies: `pip install -r requirement-dev.txt`
6. Set up pre-commit hooks: `pre-commit install`
7. Test the setup by running `python -m pytest -v`

We suggest using [Pycharm](https://www.jetbrains.com/pycharm/) as an IDE. After following above steps, create a new project in Pycharm with previously configured interpreter (select virtual environment from step 2 above).

![Screenshot 2022-01-27 at 08 33 44](https://user-images.githubusercontent.com/79791019/151312300-cf84f203-8b8e-4be7-965a-678e17d3313a.png)


## Development

In order to foster maintainability and accessibility of the code, it is encouraged to use [pre-commit hooks](https://github.com/AmanaAdvisors/mwmquant/blob/main/.pre-commit-config.yaml) when contributing to the repo. Hooks execute **formatting** ([black](https://black.readthedocs.io/en/stable/index.html), [docformatter](https://github.com/myint/docformatter)), **linting** ([flake8](https://github.com/PyCQA/flake8)) and **type-checking** ([mypy](http://mypy-lang.org)) checks before code is commited to the repo. If the checks are found to be too restrictive, use `git commit --no-verify` (use sparingly, though).


#### Misc:
- [black](https://black.readthedocs.io/en/stable/index.html) formatting can be automated via
[integration with PyCharm](https://black.readthedocs.io/en/stable/integrations/editors.html). Use *File Watchers* plugin so that black reformats
your code on every save.
- for docstring style, [**reST** format](https://stackoverflow.com/a/24385103/9816164) is used (this is also Pycharm's default docstirngs format)



## Deployment

```
# TODO: 
#   - docker
#   - k8s, skaffold
#   - python package release (setup.py)
 ```


## TODO

- explore [pylint](https://github.com/PyCQA/pylint) linter as an [alternative](https://www.slant.co/versus/12630/12632/~pylint_vs_flake8) to [flake8](https://github.com/PyCQA/flake8)
- [pdoc3](https://pdoc3.github.io/pdoc/) (or alternatives) for automatic generating of documentation
- [coverage.py](https://github.com/nedbat/coveragepy) (or alternatives) to track the test coverage in the repo



