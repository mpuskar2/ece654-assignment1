# This repository contains three files of importance:

## astAnalyzer.py
* This file contains the class used to analyze the AST and its visit functions.
* There is a sample block of code in the file, when the file is run the code is analyzed and the results are printed

## test.py
* This file defines the test cases using the unittest module
* There are 6 tests implemented, covering various true positives and true negatives
* Also covers edge cases such as async function definiton and global variables

## ci.yml
* This file defines the CI workflow for when code is pushed to the repository
* The test file is run with python 3.10 as this is the version I have installed locally
