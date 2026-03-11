# -*- coding: utf-8 -*-
#
# conf.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.apidoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax'
]

# sphinx.ext.apidoc configuration
apidoc_module_dir = '../odetoolbox'
apidoc_output_dir = 'api'
apidoc_separate_modules = True
apidoc_module_first = True

autodoc_default_options = {
    'private-members': True,
    'show-inheritance': True,
}

source_suffix = ['.rst']

master_doc = "index"

# -- Project information --------------------------------------------------

project = u'ode-toolbox'
copyright = u'2004, nest-simulator'
author = u'nest-simulator'

version = '2.1'
release = '2.1'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'manni'

todo_include_todos = False

numfig = True
numfig_secnum_depth = 2
numfig_format = {'figure': 'Figure %s', 'table': 'Table %s',
                 'code-block': 'Code Block %s'}

# -- Options for HTML output ----------------------------------------------

html_theme = "sphinx_rtd_theme"
html_title = "ODE-toolbox"

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 4,
    'collapse_navigation': False,
}

html_logo = "https://raw.githubusercontent.com/nest/ode-toolbox/master/doc/fig/ode-toolbox-logo.png"

html_static_path = ['css']
html_css_files = [
    'custom.css'
]

htmlhelp_basename = 'ode-toolbox-doc'

html_show_sphinx = False
html_show_copyright = False

# -- autodoc skip configuration -------------------------------------------

def skip(app, what, name, obj, would_skip, options):
    if name in ["__init__", "__str__"]:
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'ode-toolbox-doc.tex', u'ode-toolbox documentation',
     u'ode-toolbox documentation', 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'ode-toolbox-doc', u'ode-toolbox documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
    (master_doc, 'ode-toolbox-doc', u'ode-toolbox documentation',
     author, 'ode-toolbox-doc', 'ode-toolbox documentation',
     'Miscellaneous'),
]
