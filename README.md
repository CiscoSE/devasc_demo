# DevNet Associate Demo Collection (Unofficial)

*Collection of DevAsc demo scripts*

## Motivation

This is a small repository used to store demo scripts and postman collections used during studying for the DevNet Associate exam.

Each chapter that the scripts relate to of the DEVASC course are stored in there specific directory.

## Usage

To use the examples read the appropriate readmes for the specific chapter. If environment variables are used a creds.template file is available that can be updated with the specific variables that are used in the scripts. That file is a template and is a git tracked file, do not add content directly to the file, first copy the file and rename the extension to .sh then update the new file, creds.sh is included in the git.ignore file to ensure secrets are not shared. As part of good practice store any authorization tokens in that new file and prior to script execution run the bash script to update your environment variables. 

## Installation

To begin using the scripts either fork the repository to your personal github account or then clone it to your machine. Alternatively clone the repository to your computer directly if you do not have your own github account.

Once you have cloned the repository to your projects directory move in to the newly created directory and create a python virtual environment. These scripts are tested at version 3.7, it is expected to work with any 3.7+ releases unless otherwise noted.
```
python -m venv venv
```
Once your virtual environment is created and is activated, update pip using the following:
```
pip install --upgrade pip
```
Now load the requirements file to install the needed dependancies.
```
pip install -r requirements.txt
```
At this point your have the appropriate libraries and can start leveraging the python scripts.

Some examples use Postman to execute the examples a current installation of postman should be installed if not follow the directions for your OS at:
    https://www.postman.com/downloads/

Instructions in each chapter for loading collections and postman environment files is included as required.

## Authors & Maintainers

- Russell Johnston <rujohns2@cisco.com>

## Credits

This project is based on the numerous contributors in the DevNet community with out the community I would been able to develop these to share.

## License

This project is licensed to you under the terms of the [Cisco Sample
Code License](./LICENSE).
