"""This file should include all API accessible endpoints and methods"""

from simple_rest_client.resource import Resource

class BuildersEventResource(Resource):
	actions = {
	    'list_builders': {'method': 'GET', 'url': 'builders'},
	    'builder_by_idName': {'method': 'GET', 'url': 'builders/{}'},
	    'forceSchedulers_by_builder': {'method': 'GET', 'url': 'builders/{}/forceschedulers'},
	    'buildrequests_by_builder': {'method': 'GET', 'url': 'builders/{}/buildrequests'},
	    'builds_by_builder': {'method': 'GET', 'url': 'builders/{}/builds'},
	    'build_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}'},
	    'stopbuild_by_builderBuildnbr': {'method': 'POST', 'url': 'builders/{}/builds/{}'},
	    'rebuild_by_builderBuildnbr': {'method': 'POST', 'url': 'builders/{}/builds/{}'},
	    'buildsteps_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}/steps'},
	    'buildstep_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}/steps/{}'},
	    'buildsteplogs_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}/steps/{}/logs'},
	    'buildsteplog_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}/steps/{}/logs/{}'},
	    'buildsteplogcontent_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}/steps/{}/logs/{}/contents'},
	    'buildsteplograw_by_builderBuildnbr': {'method': 'GET', 'url': 'builders/{}/builds/{}/steps/{}/logs/{}/raw'},
	}


class WorkersEventResource(Resource):
	actions = {
	'list_workers': {'method': 'GET', 'url': 'workers'},
	'worker_by_idName': {'method': 'GET', 'url': 'workers/{}'}
	}


class BuildsEventResource(Resource):
	actions = {
	'list_builds': {'method': 'GET', 'url': 'builds'},
	'build_byId': {'method': 'GET', 'url': 'builds/{}'}
	}
