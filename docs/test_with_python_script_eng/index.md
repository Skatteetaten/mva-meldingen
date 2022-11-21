---
icon: "cloud"
title: "Test & Production"
description: "Information regarding testing and production"
---

## Change log

| Date       | What changed?                                       |
| :--------- |:----------------------------------------------------|
| 2022.22.11 | Created page about how to run a python script       |

# Test of application using Python script

There is a Python script that can be used for testing the solution against the Tax Authority. 
[Python script for retrieval, validation and submission](https://github.com/Skatteetaten/mva-meldingen/blob/master/test_with_phyton_script_files/mva_melding_innnsending.py).
Clone the entire repository or download the directory below:

    /test_with_Python_script_files

Before running the script you need to install Python and some libraries.

## Check if python and pip are installed (Minimum python3 version 3.6.X)
  
    python3 --version

    pip3 --version

If they are not installed, they can be installed through the terminal window

### Mac
    brew install python

    python3 -m pip install --upgrade pip

Alternatively, a version management package can be used instead. For more information about python on Mac, you can read on homebrew:

https://formulae.brew.sh/formula/pyenv

https://docs.brew.sh/Homebrew-and-Python

### Linux Ubuntu
    sudo apt-get update
    sudo apt-get install python3.8
    sudo apt install python3-pip

## Install python libraries
Open the terminal in the project folder and navigate to the 
    
    `/test_with_python_script` folder.<br>
Then install all necessary libraries.<br>
You can also use a venv instead of installing globally, read more here: https://docs.python.org/3/library/venv.html

    cd docs/test_with_Python_script

    pip3 install -r requirements.txt
    
## Run the Python script
1. Download the directory `test_with_Python_script` under https://github.com/Skatteetaten/mva-meldingen/tree/master/docs
2. Find a test user with an associated business as described in the User Guide for Tenor Test Data Search.
3. Note national identity number of the test user and the organization number of the business for which this test user can submit
4. Make changes to the following files
  * Organization number in the file `mva_melding_innnsending.py` (See under the comment "# Enter the org_number you want to submit for"). This is currently hardcoded to 999999999
  * Organization number in the envelope file you wish to submit (example_files/envelope)
  * Organization number in the VAT report file you wish to submit (example_files/melding)
  * Other test data such as taxation period (Skatteleggingsperiode), report category (meldingskategori) etc
  * Update the file names in the file `mva_melding_innnsending.py` for the files you wish to use:
    1.	`mvaMeldingInnsending_filnavn = "kompensasjon_mvakonvolutt.xml`
    2.	`mvaMelding_filnavn` = "kompensasjon_mvamelding.xml`
6. Note! Remember to make sure that the envelope and VAT report match the test data
5. Run the Python script
6. After the script has started, a browser is opened. Press "TestID" and use the national ID number you noted in step 3.	
