#!/usr/bin/env python
#
# $Id: setup.py,v 1.11 2005/02/15 16:32:22 warnes Exp $

CVS=0

from distutils.core import setup, Command, Extension


def load_version():
    """
    Load the version number by executing the version file in a variable. This
    way avoids executing the __init__.py file which load nearly everything in
    the project, including fpconst which is not yet installed when this script
    is executed.

    Source: https://github.com/mitsuhiko/flask/blob/master/flask/config.py#L108
    """

    import imp
    from os import path

    filename = path.join(path.dirname(__file__), 'SOAPpy', 'version.py')
    d = imp.new_module('version')
    d.__file__ = filename
    
    try:
        execfile(filename, d.__dict__)
    except IOError, e:
        e.strerror = 'Unable to load the version number (%s)' % e.strerror
        raise
    
    return d.__version__


__version__ = load_version()


url="http://pywebsvcs.sf.net/"

long_description="SOAPpy provides tools for building SOAP clients and servers.  For more information see " + url


if CVS:
    import time
    __version__ += "_CVS_"  + time.strftime('%Y_%m_%d')


setup(
    name="SOAPpy",
    version=__version__,
    description="SOAP Services for Python",
    maintainer="Gregory Warnes",
    maintainer_email="Gregory.R.Warnes@Pfizer.com",
    url = url,
    long_description=long_description,
    packages=['SOAPpy','SOAPpy/wstools'],
    provides = ['SOAPpy'],
    install_requires=[
        'fpconst',
        'pyxml'
    ]
)

