from simple_rest_client.api import API
from simple_rest_client.exceptions import ClientError

import json

from dash.APIResources import BuildersEventResource, WorkersEventResource, BuildsEventResource

# Sensitive data
from dash.vars import APIROOTURL, TWISTEDCOOKIES


# Base client class
class BaseClient(object):
    """Base class for resources operations."""
    def __init__(self):
        self.api =  API(
            api_root_url=APIROOTURL,
            params={},
            headers={'Cookie':TWISTEDCOOKIES},
            timeout=2,
            append_slash=False,
            json_encode_body=True,
            )

    # Add resource
    def add_resource(self, resource, resource_class=None):
        if resource_class:
            self.api.add_resource(resource_name=resource, resource_class=resource_class)
        else:
            self.api.add_resource(resource_name=resource)
            try :
                getattr(self.api, resource).list()
            except ClientError as e:
                print("[!] Error please make sure the resource exists")
                raise e


class BuildersClient(BaseClient):
    """Handle Builders operations."""
    def __init__(self):
        super(BuildersClient, self).__init__()
        self.resource_name = 'builders'
        self.add_resource(self.resource_name, BuildersEventResource)

    # Return a list of all the builders
    def list(self):
        resp = self.api.builders.list_builders()
        return json.loads(resp.body)['builders']

    # Restart a given build by builderId buildId/name
    def rebuild(self, builder, build):
        body = {
            "jsonrpc": "2.0",
            "id": 1250,
            "method": "rebuild",
            "params": {}
        }
        headers = {"Content-Type": "application/json"}
        return self.api.builders.rebuild_by_builderBuildnbr(
            builder,
            build,
            headers=headers,
            body=body).body

    # Restart a given build by builderId buildId/name
    def stopbuild(self, builder, build):
        body = {
            "jsonrpc": "2.0",
            "id": 1250,
            "method": "stop",
            "params": {
                'reason': 'no reason'
            }
        }
        headers = {"Content-Type": "application/json"}
        return self.api.builders.stopbuild_by_builderBuildnbr(
            builder,
            build,
            headers=headers,
            body=body).body

    # Get build requests by builder
    def get_buildrequests(self, builder):
        self.api.builders.buildrequests_by_builder(builder).body

    # Get build requests by builder
    def get_builds(self, builder):
        self.api.builders.builds_by_builder(builder).body

    # Get buildsteps for a given build
    def get_buildsteps(self, builder, build):
        return self.api.builders.buildsteps_by_builderBuildnbr(builder, build).body

    # Get a build step for a given build
    def get_buildstep(self, builder, build, stepname):
        return self.api.builders.buildstep_by_builderBuildnbr(builder, build, stepname).body

    # Get logs for a given buildstep
    def getlogs_bystep(self, builder, build, stepname):
        return self.api.builders.buildsteplogs_by_builderBuildnbr(builder, build, stepname).body

    # Get a log for a given buildstep
    def getlog_bystep(self, builder, build, stepname, logname):
        return self.api.builders.buildsteplogs_by_builderBuildnbr(builder, build, stepname, logname).body

    # Get log content
    def getlogcontent_bystep(self, builder, build, stepname, logname):
        return self.api.builders.buildsteplogcontent_by_builderBuildnbr(builder, build, stepname, logname).body
    # Get log raw
    def getlograw_bystep(self, builder, build, stepname, logname):
        return self.api.builders.buildsteplograw_by_builderBuildnbr(builder, build, stepname, logname).body



class BuildsClient(BaseClient):
    """Handle Builds operations."""
    def __init__(self):
        super(BuildsClient, self).__init__()
        self.resource_name = 'builds'
        self.add_resource(self.resource_name, BuildsEventResource)

    # Return a list of all the builds
    def list(self):
        resp = self.api.builds.list_builds()
        return json.loads(resp.body)['builds']


class SchedulersClient(BaseClient):
    """Handle schedulers operations."""
    def __init__(self):
        super(SchedulersClient, self).__init__()
        self.resource_name = 'schedulers'
        self.add_resource(self.resource_name)

    # Return a list of all the schedulers
    def list(self):
        resp = self.api.schedulers.list()
        return json.loads(resp.body)['schedulers']


class WorkersClient(BaseClient):

    def __init__(self):
        super(WorkersClient, self).__init__()
        self.resource_name = 'workers'
        self.add_resource(self.resource_name, WorkersEventResource)

    # Return a list of all the workers
    def list(self):
        resp = self.api.workers.list_workers()
        return json.loads(resp.body)['workers']

