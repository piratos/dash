# dash
Python client for Buildbot REST API

This Client uses the exposed REST API for buildbot mentioned in this docs http://docs.buildbot.net/latest/developer/rest.html

## Installation
- This project requires simple_rest_client: `pip install simple_rest_client`
- Create a file called vars.py that contains : `APIROOTURL` which refer to the api url of your buildbot master server and `TWISTEDCOOCKIES` of the admin user

## Example
```
from BaseClient import BuildersClient, BuildsClient`

# Work on builders.
builderclient = BuildersClient()
builderclient.list()
builderclient.get_buildsteps(1, 1)

# Work on builds.
buildclient = BuildsClient()
buildsclient.list()
```
