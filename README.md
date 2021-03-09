# Mva-meldingen

Documentation for mva-meldingen

## Notebook Ekamples
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

Move to the example files folder. 

    cd docs/documentation/test

To run jupyter notebook.

    jupyter notebook

Choose browser, we use Chrome. <br>
Open innsending-eksempel.ipynb
<br>
<br>
When runnin the notebook script there are these boxes with code in them that can be run. 
You can either click on a box and press run, and do this for each box. 
Or you can go to the toolbar and click "Cell" and then "Run All"
<br>
If you want to do changes then it's sensible to restart the kernel. "Kernel" -> "Restart"
<br>
To remove the output prints. "Cell" -> "All Output" -> "Clear"

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
