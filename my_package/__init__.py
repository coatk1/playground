"""Top-level package for datetime_gui."""

from calc import Calc
from calc import Distance
from geosp import Wt
from geosp import Gh
from files.csv_file import check

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
