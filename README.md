# Web Doctor Educator (Server)

## Overview
This is the server component for the Web Doctor Educator, a project sponsored
through the Rochester Institute of Technology. The goal of the WDE is to
provide a tool for doctors in Rwanda to use when on the job to help them
obtain treatment-related information easily when in a low-bandwidth environment.

## Installation
To run the server you will need Python 3 or greater which should come with
`pip` pre-installed. Once you have that run `pip install -r requirements.txt`
to install all the requirements. Using [virtualenv](https://virtualenv.pypa.io/en/latest/)
is recommended to make it easier to manage your Python environment.

## Running
To actually start the server simply `cd` into the directory and run
`python manage.py runserver`.

## WSGI and FastCGI
Because webdoctor-server uses Django it can also be run using WSGI or FastCGI.
Please refer to the Django documentation for how to accomplish this.

## About the Code
### Style
The code should conform to Python's [PEP8](https://www.python.org/dev/peps/pep-0008/)
style guide. Comments are not mandatory but almost everything should be
commented.

### Modules
The `discussion` module deals with the integrated discussion boards.

The `login` module deals with authentication and verification. This includes
password resets and verifying that a doctor is licensed to practice.

Finally the (NYI) `content` module deals with content which is used by clients
for performing medicine. This includes searchable documents and anything else
relevant. These files will be managed by administrators and updated on the device
when the are changed on the server.


