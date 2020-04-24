"""Top-level package for datetime_gui."""

from my_package.calc import Calc
from my_package.calc import Distance
from my_package.geosp import Wt
from my_package.geosp import Gh
from my_package.files.csv_file import check

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
