#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# ome documentation build configuration file, created by
# sphinx-quickstart on Wed Feb 22 20:24:38 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# Append the top level directory of the docs, so we can import from the config dir.
sys.path.insert(0, os.path.abspath('../common'))
from conf import *


# -- General configuration -----------------------------------------------------

# General information about the project.
project = u'OME Contributing Developer'
title = project + u' Documentation'

main_github_root = github_root + 'openmicroscopy'
scc_github_root = github_root + 'snoopycrimecop'

# cf. omero_github_root, bf_github_root
omero_main_github_root = main_github_root + '/openmicroscopy/'
bf_main_github_root = main_github_root + '/bioformats/'

# OME contributing-specific extlinks
contributing_extlinks = {
    # Github links
    'omero_source' : (omero_github_root + 'blob/'+ branch + '/%s', ''),
    'omero_sourcedir' : (omero_github_root + 'tree/'+ branch + '/%s', ''),
    'omero_commit' : (omero_github_root + 'commit/%s', ''),
    'omero_pr' : (omero_main_github_root + 'pull/%s', ''),
    'omero_scc_branch' : (scc_github_root + '/openmicroscopy/tree/%s', ''),
    'bf_source' : (bf_github_root + 'blob/'+ branch + '/%s', ''),
    'bf_sourcedir' : (bf_github_root + 'tree/'+ branch + '/%s', ''),
    'bf_commit' : (bf_github_root + 'commit/%s', ''),
    'bf_pr' : (bf_main_github_root + 'pull/%s', ''),
    'bf_scc_branch' : (scc_github_root + '/bioformats/tree/%s', ''),
    'omedoc_scc_branch' : (scc_github_root + '/ome-documentation/tree/%s', ''),
    'omehelp_scc_branch' : (scc_github_root + '/ome-help/tree/%s', ''),
    'figure_scc_branch' : (scc_github_root + '/figure/tree/%s', ''),
    
    # Doc links
    'omero_doc' : (oo_site_root + '/support/omero/%s', ''),
    'bf_doc' : (oo_site_root + '/support/bio-formats/%s', ''),
    'model_doc' : (oo_site_root + '/support/ome-model/%s', ''),
    }
extlinks.update(contributing_extlinks)

extensions += ['sphinx.ext.graphviz']
graphviz_dot_args = [
    '-Nfontname=Helvetica',
    '-Nfontsize=9',
    '-Nshape=box',
    '-Gfixedsize=true']
graphviz_output_format = 'svg'

rst_epilog += """
.. _GitHub: https://github.com
.. _openmicroscopy.git: https://github.com/openmicroscopy/openmicroscopy
.. _bioformats.git: https://github.com/openmicroscopy/bioformats
.. _ome-documentation.git: https://github.com/openmicroscopy/ome-documentation
.. _ome-cmake-superbuild.git: https://github.com/ome/ome-cmake-superbuild
.. _scripts.git: https://github.com/ome/scripts
.. _Sonatype: https://www.sonatype.com/
..  |merge| replace:: Merges PRs using :ref:`scc merge`
..  |buildOMERO| replace:: Builds the OMERO.server and the clients using :omero_source:`OMERO.sh <docs/hudson/OMERO.sh>`
..  |archiveOMEROartifacts| replace:: Archives the build artifacts
..  |copyreleaseartifacts| replace:: Copies the build artifacts to a LDAP-protected folder under downloads.openmicroscopy.org
..  |promoteOMERO| replace:: copies the artifacts to necromancer
..  |updatesubmodules| replace:: Updates submodules using ``scc update-submodules``
..  |buildBF| replace:: Builds Bio-Formats using ``clean release tools utils docs docs-sphinx dist-bftools dist-matlab dist-octave test``
..  |buildFiles| replace:: Builds OME Files components from git using ``cmake``
..  |buildFilesSB| replace:: Builds OME Files components and third-party dependencies using ``cmake``
..  |buildFilesSRC| replace:: Builds OME Files components from source release archives using ``cmake``
..  |sphinxbuild| replace:: Runs ``make clean html`` to build the HTML Sphinx documentation
..  |linkcheck| replace:: Runs ``make linkcheck`` and :ref:`parse the Sphinx linkcheck output <linkcheck_parser>`
..  |ssh-doc| replace:: Copies the HTML documentation over SSH to
..  |deploy-doc| replace:: Runs :ref:`scc deploy` to update
"""

# Edit on GitHub prefix
edit_on_github_prefix = 'contributing'

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
#target = 'OME-Contributing-Developer' + '.tex'
#latex_documents = [
#  (master_doc, target, title, author, 'manual'),
#]

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = '../common/images/ome-tight.pdf'

# -- Options for the linkcheck builder ----------------------------------------

# Regular expressions that match URIs that should not be checked when doing a linkcheck build
linkcheck_ignore += [r'http://localhost:\d+/?', 'http://localhost/',
    'http://www.hibernate.org',
    r'https?://www\.openmicroscopy\.org/site/team/.*',
    r'.*[.]?example\.com/.*',
    r'https?://www\.openmicroscopy\.org/site/support/faq.*',
    r'https://spreadsheets.google.com/.*',
    r'http://trac.openmicroscopy.org/ome/admin/.*',
    r'https?://hake.openmicroscopy.org/.*',
    r'https?://eel.openmicroscopy.org/.*',
    r'https?://burbot.openmicroscopy.org/.*',
    r'https?://seabass.openmicroscopy.org/.*',
    r'https?://trout.openmicroscopy.org/.*',
]
