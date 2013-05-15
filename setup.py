#! /usr/bin/env python

from setuptools import setup
import invewrapper

setup(
	name='invewrapper',
	version='0.1',
	description='tools to manage multiple virtualenv written in pure python',
	keywords=[],
	author='Dario Bertini',
	author_email='berdario+pypi@gmail.com',
	url='',
	license='Simplified BSD License',
	py_modules=['invewrapper'],
	data_files=[('', ['inve'])],  # XXX
	entry_points={
		'console_scripts':
			["{0} = invewrapper:{0}_cmd".format(cmd[:-4])
			for cmd in dir(invewrapper) if cmd.endswith("_cmd")]}
)
