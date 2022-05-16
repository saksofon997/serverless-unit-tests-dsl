## DSL

Powered by [textX](https://github.com/textX/textX)

### Requirements

Dependencies are specified using Pipfile. It is recommended to manage dependencies using `pipenv`.

Install the dependencies using

```bash
$ pipenv install
```

### Usage

Run one-off python commands inside the virtual env with

```bash
$ pipenv run ...
```

Run python scripts by activating the virtual environment first, using

```bash
$ pipenv shell
```

Exit with

```bash
(venv) $ deactivate
```

and then

```bash
$ python -m name_of_the_script
```

To use VSCode import management, press shift+command+p, and enter "Python: Select Interpreter". Select the correct virtual environment.

### Packaging and using the packaged version

From the main projects(git repository) root folder, run the following command to install the ServerlessTestS generator as a PyPi package:

```bash
$ pip install -e dsl
```

Now it is possible to use the generator through textX, example:

```bash
$ textx generate serverless.sts --target sts-lang -o test
```
