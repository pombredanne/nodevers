"""
This module will handle Node installations.
Note that this module should not print anything
and instead raise exceptions.
The install module will handle these.
"""

import os
import sys
import tarfile

from . import misc

if sys.version_info >= (3, 0):
    from urllib.error import URLError
    from urllib.error import HTTPError
    from urllib.error import ContentTooShortError
    from urllib.request import urlopen
    from urllib.request import urlretrieve
else:
    from urllib2 import URLError
    from urllib2 import HTTPError
    from urllib import ContentTooShortError
    from urllib2 import urlopen
    from urllib import urlretrieve

class MissingToolError(StandardError):
    """
    Will be thrown if GNU make or
    python (2.x) is missing.
    """
    pass

class BuildError(StandardError):
    """
    Will be thrown when ./configure, make
    or make install fails.
    """
    pass

class NoSuchVersionError(StandardError):
    """
    Will be thrown if misc.valid_version_string() returns
    False.
    """
    pass

class NodeInstaller(object):
    """
    This will install Node.
    """
    def __init__(self, version, install_path, build_args=None):
        self.version = version
        self.install_path = install_path
        self.build_args = build_args
        self.url = "http://nodejs.org/dist/v%s/node-v%s.tar.gz" % (self.version,
                self.version)
        try:
            urlopen(self.url)
        except HTTPError:
            raise NoSuchVersionError("Cannot download node-v%s.tar.gz" % self.version)
        except URLError:
            raise OSError("Make sure you are connected to the Internet")
        self.tmpdir = misc.get_tmp_dir()

    def download_source(self):
        """
        This will download the source packages.
        """
        os.chdir(self.tmpdir)
        package = "node-v%s.tar.gz" % self.version
        if os.path.exists(package):
            pass
        else:
            urlretrieve(self.url, package)
