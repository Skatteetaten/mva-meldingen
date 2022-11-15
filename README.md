# Mva-meldingen
If you are visiting this github project in order to manually test a submission of the VAT-report with the Python script,
please visit http://skatteetaten.github.io/mva-meldingen/test_with_python_script/

This is the github project for the documentation "System submission of VAT-report".
Please visit the documentation at http://skatteetaten.github.io/mva-meldingen/

## How to update the "System submission of VAT-report" documentation
This documentation is generated using the Gatsby framework (https://www.gatsbyjs.com/)

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

If you get the following error,

    ERROR #11329
    error:0308010C:digital envelope routines::unsupported

run this configuration setting in your terminal:

    export NODE_OPTIONS=--openssl-legacy-provider
