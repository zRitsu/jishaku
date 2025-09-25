# -*- coding: utf-8 -*-

"""
jishaku.meta
~~~~~~~~~~~~

Meta information about jishaku.

:copyright: (c) 2021 Devon (Gorialis) R
:license: MIT, see LICENSE for more details.

"""
import importlib.metadata
from collections import namedtuple

__all__ = (
    '__author__',
    '__copyright__',
    '__docformat__',
    '__license__',
    '__title__',
    '__version__',
    'version_info'
)

# pylint: disable=invalid-name
VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=2, minor=6, micro=6, releaselevel='final', serial=0)

__author__ = 'Gorialis, Kraots'
__copyright__ = 'Copyright 2021 Devon (Gorialis) R'
__docformat__ = 'restructuredtext en'
__license__ = 'MIT'
__title__ = 'jishaku'
__version__ = '.'.join(map(str, (version_info.major, version_info.minor, version_info.micro)))

# This ensures that when jishaku is reloaded, pkg_resources requeries it to provide correct version info
try:
    __version__ = importlib.metadata.version('jishaku')
except importlib.metadata.PackageNotFoundError:
    pass
