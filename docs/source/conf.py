# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'social-casino-api'
copyright = 'casino-company'
author = 'casino-company'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'social-casino': ('https://projectfluent.io/', None),
    'casino-company': ('https://projectfluent.io/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
