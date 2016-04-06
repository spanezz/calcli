#!/usr/bin/env python3

from distutils.core import setup
import sys

setup(
    name = "calcli",
    requires=[ 'khal', 'icalendar' ],
    version = "0.1",
    description = "khal-based command line calendar tool with a taskwarrior-like interface",
    author = ["Enrico Zini"],
    author_email = ["enrico@enricozini.org"],
    url = "https://github.com/spanezz/calcli",
    license = "http://www.gnu.org/licenses/gpl-3.0.html",
    scripts = ['calcli']
)
