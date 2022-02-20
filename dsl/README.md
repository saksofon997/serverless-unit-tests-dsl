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

and then

```bash
$ python -m name_of_the_script
```
