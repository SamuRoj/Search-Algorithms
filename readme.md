# About this repo

Simple python project that tests some searching in array algorithms, explaining how they work and comparing his complexity and efficiency.

## Problem statement
​
The search in array problem tries to locate a specific target element within a given array. The objective is to determine whether the target exists in the array and, if so, return its position or some relevant information about it.

## Algorithms tested

## Linear Search

Linear Search goes through each element of an array one by one until it finds the target value. It does not assume any order in the array, so every element may need to be checked. 

## Binary Search

Binary Search works on a sorted array. It repeatedly divides the search interval in half by comparing the target value to the middle element of the array.

## Ternary Search

Ternary Search is also applied to sorted arrays and splits the array into three parts by using two midpoints. It determines which of the three segments may contain the target value and continues the search only in that segment.

## Jump Search

Jump Search is designed for sorted arrays. It works by jumping ahead by fixed steps (blocks) instead of checking every element. Once it finds a block where the target could be, it performs a linear search within that block. Each block has a size of √n

### Examples



# Python version
Python 3.13.1
​
# Running locally and testing

* Note: This instructions are for mac. Windows or linux may require some changes. 
* A good idea for this project, is to use a virtual environment, you could set up one with: [virtualenv](https://virtualenv.pypa.io/en/latest/).
* To create the virtual environment: `virtualenv env`
* To activate it:`source env/bin/activate`
* To install dependencies: `pip3 install -r requirements.txt`
* To run unit testing: `./test.sh`
* To try a default example, run: `: ./run.sh`. In the file ./run.sh is just an example, you can modify it. Theck the `app.py` file to get to understand how it works.

# Current coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `coverage run -m unittest discover` and after that run `coverage report` to get the following table:

```
Name                          Stmts   Miss  Cover
-------------------------------------------------
search\__init__.py                0      0   100%
search\algorithms.py             53      1    98%
search\constants.py               2      0   100%
search\data_generator.py          9      1    89%
test\__init__.py                  0      0   100%
test\test_algorithms.py          30      1    97%
test\test_data_generator.py      29      1    97%
-------------------------------------------------
TOTAL                           123      4    97%
```

# Code beautifier
This code has been beautify using black: https://github.com/psf/black. 
The command to use is `black . -l 120`.
