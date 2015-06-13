# Web Doctor Educator (Server)

## Overview
This is the server component for the Web Doctor Educator, a project sponsored
through the Rochester Institute of Technology. The goal of the WDE is to
provide a tool for doctors in Rwanda to use when on the job to help them
obtain treatment-related information easily when in a low-bandwith environment.

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