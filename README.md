# Mva-meldingen

This repository contains the former Gatsby documentation for "System submission of VAT-report".

## Documentation status

The documentation is no longer published from this repository. Requests to the GitHub Pages site are redirected to the [VAT return documentation](https://skatteetaten.github.io/api-dokumentasjon/anvendelsesomraader/mvamelding).

To publish the redirect, run:

    npm run deploy

The deploy command publishes the minimal files in `redirect-site/` instead of Gatsby's generated `public/` directory. The root page redirects visitors, and `404.html` redirects requests to previously published subpages. GitHub Pages does not support wildcard HTTP redirects, so requests to old subpages may briefly receive a 404 response before the browser redirects.

The old Gatsby source and documentation remain in this repository but are not included in the published site.

## Gatsby development

The original documentation was generated using the Gatsby framework (https://www.gatsbyjs.com/).

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

### Deploy

    npm run deploy

This publishes the redirect site; do not run `npm run build` for deployment.

In order to log into GitHub, you need to have a **Personal Access Token** with the `repo` scope.  
You can create a personal access token by following these steps:

1. Go to: [https://github.com/settings/tokens](https://github.com/settings/tokens)
2. Choose **"Classic token"**
3. Click **Generate new token**
4. Give it a name and set how long it should be valid (e.g., 30 or 90 days)
5. Select the **`repo`** scope
6. Click **Generate token**
7. **Copy the token immediately** – it will only be shown once

When you run the command "npm run deploy":
1. Username: Your GitHub username 
2. Password: Paste the token

### Q&A

If you get the following error,

    ERROR #11329
    error:0308010C:digital envelope routines::unsupported

run this configuration setting in your terminal:

    export NODE_OPTIONS=--openssl-legacy-provider

If you get the following error,

     ERROR #98123  WEBPACK
     Generating JavaScript bundles failed
     mva-meldingen-dokumentasjon/src/components/Layout/layout.jsx: It's not possible to compile spread arguments in `super()` without
     compiling classes.
     Please add '@babel/plugin-transform-classes' to your Babel configuration. (This is an error on an internal node. Probably an internal error.)

run this in your terminal:

    npm install --save-dev @babel/plugin-transform-classes
    npm install gatsby@^2.25.0
