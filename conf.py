# -*- coding: utf-8 -*-
from recommonmark.parser import CommonMarkParser

extensions = ['sphinx.ext.todo',
    'sphinx.ext.imgmath',
    'sphinx.ext.githubpages']

templates_path = ['_templates']
# https://stackoverflow.com/questions/23211695/modifying-content-width-of-the-sphinx-theme-read-the-docs

source_suffix = ['.rst', '.md']
source_parsers = {'.md': CommonMarkParser}

master_doc = 'index'

# General information about the project.
project = u'Introdução a Sistemas Abertos'
copyright = u'2018, AUTOR'
author = u'AUTOR'
version = u'2018.1'
release = u'2018.1'
language = 'pt_BR'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
        }
html_static_path = ['_static']

# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}

htmlhelp_basename = 'IntroduoaSistemasAbertosdoc'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'IntroduoaSistemasAbertos.tex', u'Introdução a Sistemas Abertos Documentation',
     u'AUTOR', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'introduoasistemasabertos', u'Introdução a Sistemas Abertos Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'IntroduoaSistemasAbertos', u'Introdução a Sistemas Abertos Documentation',
     author, 'IntroduoaSistemasAbertos', 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


