try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
 
import os

def getVersion():
    with open(os.path.join(os.path.dirname(__file__),'skua/version.py')) as f: exec(f.read())
    return __version__

setup(name = "skua",
    version = getVersion(),
    description = "skua is a tool to download pictures from websites.",
    author = "Thomas Locher",
    author_email = "thamasta@gmx.ch",
    url = "https://github.com/THLO/skua",
    download_url = "https://github.com/THLO/skua/tarball/v."+getVersion(),
    packages = ['skua'],
    scripts = ['skua/skua'],
    long_description = "skua offers a simple mechanism to download individual pictures, or collections of pictures from websites.\n\
More information on skua can be found at https://github.com/THLO/skua or by running skua --help.",
    license = 'GNU General Public License v3 (GPLv3)',
    platforms = 'POSIX',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Desktop Environment',
      ]
) 
