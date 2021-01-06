# This Readme shows steps for Unittesting done in this repository.

# Steps to get coverage running for the pylint: Coverage Report
0. coverage run -m --source=. unittest tests/*.py
1. coverage html
3. A new fiule should get created called htmlcov/index.html
4. Preview that file to check the Coverage Report.

# Steps to install necessary tools to install pylint and eslint
0. pip install pylint
1. pip install black
2. npm install -g eslint
3. npm init
* press enter to accept all default values
4. eslint --init
"To check syntax, find problems, and enforce code style"
"JavaScript modules (import/export)"
"React"
"Browser"
"Use a popular style guide"
"Javascript"
"Yes" in the end.

# Steps to check all the files using pylint and estlint
0. pylint <python files> for example: python app.py
1. estlint <jsx files> for example: estlint Button.jsx
* eslint --fix Button.jsx to fix some of the errors.
  
# Steps to run both unittest files under tests
0. python unmocked_unit_tests.py
1. python mocked_unit_tests.py

1. Why did you choose to test the code that you did? (details in rubric)
As you continue to work on your complex web app, it will get increasingly complicated to build, run, test, save, and deploy every change you make. You may very well quickly reach a point where it becomes nearly impossible to keep everything that is happening in code in your head at once. To help you build on top of what you have quickly, you will be setting up automated tooling, specifically, automated testing and automated continuous integration as we covered in class.

In the unmocking_unit_test- created unit tests THAT DO NOT USE MOCKING in tests/unmocked unit tests.py for the parsing logic.
In the unmocking_unit_test- created unit tests THAT DO USE MOCKING in tests/mocked unit tests.py that mocks API/DB/Socket logic for your app.

2. Is there anything else you would like to test if you had the time (or was asked to do so)?
I think that mocking unit test cases is primarily used in unit testing. An object under test may have dependencies on other (complex) objects. To isolate the behavior of the object you want to replace the other objects by mocks that simulate the behavior of the real objects. This is useful if the real objects are impractical to incorporate into the unit test. Therefore, any services that is being used in your system/app externaly should get mocked in unit testing.
