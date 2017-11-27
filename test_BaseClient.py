from BaseClient import *


def test_Builders():
	b = BuildersClient()
	print(b.list())
	assert b.list()

def test_rebuild_Builders():
	b = BuildersClient()
	print(b.rebuild(2, 2))

def test_stopbuild_Builders():
	b = BuildersClient()
	#print(b.rebuild(2, 2))
	print(b.stopbuild(2, 8))

def test_getbuildsteps_Builders():
	b = BuildersClient()
	print(b.get_buildsteps(2, 2))

def test_Builds():
	b = BuildsClient()
	assert b.list()

def test_Schedulers():
	s = SchedulersClient()
	assert s.list()


def test_list_workers():
	w = WorkersClient()
	assert w.list()

def test_list_builds():
	bc = BuildsClient()
	print(bc.list())

if __name__ == '__main__':
	# test_Schedulers()
	# test_Builds()
	# test_Builders()
	# test_getbuildsteps_Builders()
	# test_list_workers()
	# test_rebuild_Builders()
	# test_stopbuild_Builders()
	test_list_builds()