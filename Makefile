all:
	tox -e py27

rpm:
	python setup.py bdist_rpm --requires=`python rpm-requires.py`

clean:
	-rm *.pyc
	-rm *~
	-rm -rf build
	-rm -rf .tox
	-rm -rf taskflow_amqp_worker.egg-info
	-rm -rf pbr-0.8.2-py2.7.egg
