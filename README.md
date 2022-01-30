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

In order to ensure high code quality, the following is done:

1. For code guide style, [black](https://black.readthedocs.io/en/stable/index.html) auto-formatter is used. Set up
[integration with PyCharm](https://black.readthedocs.io/en/stable/integrations/editors.html) so that black reformats
your code on every save (via *File Watchers* plugin).








## Deployment
