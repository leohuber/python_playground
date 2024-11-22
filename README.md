# Python Playground

## Python Environment

Create a virtual environment: It's generally recommended to use a virtual environment for your project dependencies instead of relying on globally installed libraries. This approach helps to avoid conflicts between different projects and ensures that your project has all the necessary dependencies with the correct versions.

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Upgrade pip: To ensure you have the latest version of pip, run the following command:

```bash
pip install --upgrade pip
```

Install dependencies: To install all the dependencies listed in the requirements.txt file, run the following command in your terminal. Make sure to activate the environment local_venv first.

```bash
pip install -r requirements.txt
```

Upgrade dependencies: If you need to update a specific package, you can edit the requirements.txt file to specify the new version and then run:

```bash
pip install -r requirements.txt --upgrade
```

Add dependencies: To add a new dependency to your project, you can use the `pip install` command followed by the package name. After installing the package, you should update the `requirements.txt` file to include the new dependency. You can do this by running:

```bash
pip freeze > requirements.txt
```

This command will overwrite the existing `requirements.txt` file with the current list of installed packages and their versions.