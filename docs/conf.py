# -*- coding: utf-8 -*-

project = u'Flask-Bootstrap'
copyright = u'2013, Marc Brinkmann / 翻译: <a href="http://greyli.com" target="_blank">李辉</a>'
version = '3.3.7.1'
release = '3.3.7.1.dev1'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'alabaster']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build']
pygments_style = 'monokai'

html_theme = 'alabaster'
html_theme_options = {
    'github_user': 'greyli',
    'github_repo': 'flask-bootstrap-docs-zh',
    'description': 'All Bootstrap, no boilerplate.',
    'github_banner': True,
    'github_button': False,
    'show_powered_by': False,

    # required for monokai:
    'pre_bg': '#292429',
}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

intersphinx_mapping = {'http://docs.python.org/': None,
                       'http://flask-sqlalchemy.pocoo.org/': None,
                       'http://pythonhosted.org/flask-nav/': None,
                       'http://flask.pocoo.org/docs/': None,
                       'https://wtforms.readthedocs.org/en/latest/': None, }
