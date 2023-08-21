# MLOps
Flask==2.2.5
pandas==1.5.3
numpy==1.23.5
pycaret==3.0.4
catboost==1.2
scikit-learn==1.2.2

These are the versions used in Flask (VSC/Pycharm) & Jupyter Notebook.
The mainapp.py is the one we used to try to integrate but failed to do so with only one app working while the other two is not working as expected. Hence, we have individual apps in a different folder with all the necessary files.

Downloading submitted files on Github is advised as they are of most up to date. Thank you.

## Tools used in this project
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/2023/06/12/poetry-a-better-way-to-manage-python-dependencies/)
* [hydra](https://hydra.cc/): Manage configuration files - [article](https://mathdatasimplified.com/2023/05/25/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
* [DVC](https://dvc.org/): Data version control - [article](https://mathdatasimplified.com/2023/02/20/introduction-to-dvc-data-version-control-tool-for-machine-learning-projects-2/)

## Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make env 
```

## Install dependencies
To install all dependencies for this project, run:
```bash
poetry install
```

To install a new package, run:
```bash
poetry add <package-name>
```

## Version you data
To track changes to the "data" directory, type:
```bash
dvc add data
```

This command will create the "data.dvc" file, which contains a unique identifier and the location of the data directory in the file system.

To keep track of the data associated with a particular version, commit the "data.dvc" file to Git:
```bash
git add data.dvc
git commit -m "add data"
```

## Auto-generate API documentation

To auto-generate API document for your project, run:

```bash
make docs
```
