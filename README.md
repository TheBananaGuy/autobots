# Test automation example

## Task

### Description:
Write automation test script and submit link to git repository as an outcome of the assignment.
Add a readme.md file to the project, containing an instruction on the configuration and running of the script.

### Test case:
1. User navigates to _[https://www.google.com/](https://www.google.com/)_ website
2. User types "Opus Online" into searchbox
3. Press Enter button

### Expected result:
- Opus Online company overview block displayed on the right
- Block has correct:
	1. Company name
	2. Address
	3. phone number
	4. Navigate to website button

### Nice to have:
1. Multiple browsers support
2. Tests run in parallel
3. Page Object Pattern
4. Readable test report

## Setup documentation

### Prerequisites
- Python version 3.x.x
- Selenium WebDriver test automation framework
- Browser drivers for Selenium
	- Gecko
	- Chrome

Commands given below as an example are meant to be executed through Windows' command prompt.

### Step 1 - download Python

Go to the _[official source](https://www.python.org/downloads/)_ and download any latest **version 3** python.
Make sure all the environment variables are properly set during installation.

### Step 2 - doublecheck

Check versions of Python and the package manager (pip) to make sure that everything was installed correctly

```
python --version
pip --version
```

### Step 3 - install the dependencies

Update **pip** and install **Selenium**

```
python -m pip install --upgrade pip setuptools wheel
pip install selenium
```

Download latest **Gecko** driver _[here](https://github.com/mozilla/geckodriver/releases)_ and **Chrome** driver _[here](https://sites.google.com/a/chromium.org/chromedriver/downloads)_. Extract them to the script folder (auto-py).

## Running the script

Call the script via command prompt from the script folder (auto-py).

E.g.:
```
test.py
```

## TODO-s

- More stuff in the Browser object
	- optional user agent string
	- headless mode trigger
- Less repeatable code
- Prettier reports
- Parallel processing