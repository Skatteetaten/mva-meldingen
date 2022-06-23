# Mva-meldingen

Documentation for mva-meldingen

We are re-arranging and updating documentation to include "komensasjonsmeldingmreverdiavgift" and prepare for "omvendt avgiftsplikt".

The work is expected to be completed by 29th of june. In the meanwhile the

## Notebook Examples

How to get the examples up and running(Linux Ubuntu).

### Initial setup

<i>Open terminal in this repository(mva-meldingen). </i> <br>
Install jupyter notebook

    snap install jupyter

Check that you have python and pip installed.

    #Check the system Python version
    python --version

    #Check the Python 2 version
    python2 --version

    #Check the Python 3 version
    python3 --version

    #Python 2
    pip --version

    #Python 3
    pip3 --version

If you are missing them, then you need to install them. <br>
Using python3 moving forward. Change 3.8 with a 2.x.x if desired and python3 with python to use Python2.
  
 sudo apt-get update
sudo apt-get install python3.8
sudo apt install python3-pip

### Running notebook

Move to the example files folder.

    cd docs/documentation/test

To run jupyter notebook.

    jupyter notebook

Choose browser, we use Chrome. <br>
Open innsending-eksempel.ipynb
<br>
<br>
To run the script. Click on a box and press "Run"
You can do this for each box or you can go to the toolbar and click "Cell" and then "Run All"
<br>
If you want to do changes or re-run the script then it's sensible to restart the kernel. "Kernel" -> "Restart"
<br>
Also useful to remove the output prints. "Cell" -> "All Output" -> "Clear"
<br>
<br>
To run the script you need a test account in digdirs minid, as well as change the organisation number, <br>
which is defined as a variable in the script and in the MvaMeldingInnsending ("konvolutt") and mvamelding .xml files.

## Documentation

### Initial setup

Getting the gatsby-starter-skatteetaten module (TODO: Add more docs)

    git submodule init
    git submodule update

### How to build

The project is built using npm from the current Node LTS. Install with [nvm](https://github.com/creationix/nvm);

    nvm install --lts

Then run

    npm install

to install the dependencies.

    npm start

will start a local web server and continuously build the documentation as you make changes.

### Deploying to github pages
