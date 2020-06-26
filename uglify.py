# -*- coding: utf-8 -*-

from pelican import signals
from subprocess import check_call
import logging
import os

logger = logging.getLogger(__name__)

"""
Minify CSS and JS files in output path with uglifyjs and uglifycss.
Required: an existing installation of uglifyjs/ uglifycss Compressor.
"""

def minify(pelican):
    """
      Minify CSS and JS with uglifyjs/ uglifycss
      :param pelican: The Pelican instance
    """
    js = pelican.settings.get("UGLIFYJS_EXECUTABLE", "uglifyjs")
    css = pelican.settings.get("UGLIFYCSS_EXECUTABLE", "uglifycss")
    for dirpath, _, filenames in os.walk(pelican.settings["OUTPUT_PATH"]):
        for name in filenames:
            _name = os.path.splitext(name)
            if _name[1] in ".css" and _name[0][-3:] != "min":
                filepath = os.path.join(dirpath, name)
                logger.info(f"minify {filepath}")
                check_call([css, filepath], stdout=open(filepath[:-4] + ".min.css", "w+"))
            elif os.path.splitext(name)[1] in ".js" and  _name[0][-3:] != "min":
                filepath = os.path.join(dirpath, name)
                logger.info(f"minify {filepath}")
                check_call([js, filepath], stdout=open(filepath[:-3] + ".min.js", "w+"))


def register():
    signals.finalized.connect(minify)