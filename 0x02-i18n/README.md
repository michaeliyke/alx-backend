# Alx Backend

## 0x02. i18n

Internationlization (i18n) and localization (l10n) with Flask

### Learning Objectives

- How to extract text to external files
- How to integrate Flask-Babel in your applications
- How to parametrize Flask templates to display different languages
- How to infer the correct locale based on URL parameters, user settings or request headers
- How to localize timestamps

### Resources

**Read or watch**:

- [Flask-Babel](https://flask-babel.tkte.ch/)
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz](http://pytz.sourceforge.net/)
- [Babel](http://babel.pocoo.org/en/latest/)
- [Flask-Babel](https://pythonhosted.org/Flask-Babel/)

### Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` style (version 2.5.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Setup

- Install Flask

```bash
pip3 install Flask==2.0.1
```

- Install `Flask-Babel` in your `python3` environment

```bash
pip3 install Flask-Babel==2.0.0
```

### Install Babel

- Install `Babel` in your `python3` environment

```bash
pip3 install Babel==2.9.1
```

### Install pytz

- Install `pytz` in your `python3` environment

```bash
pip3 install pytz==2022.1
```

- Install `Jinja2` in your `python3` environment

```bash
pip3 install Jinja2==3.1.1
```

- Virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Translation commands

```bash
pybabel extract -F babel.cfg -o messages.pot . --ignore=venv
pybabel init -i messages.pot -d translations -l en
pybabel init -i messages.pot -d translations -l fr
pybabel compile -d translations
```
