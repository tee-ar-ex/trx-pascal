import os
import sys

sys.path.insert(0, os.path.abspath('.'))

project = 'trx-pascal'
copyright = '2026, trx-pascal contributors'
author = 'trx-javascript contributors'
release = '1.0'

extensions = [
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinx_design',
]

js_source_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
jsdoc_config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'jsdoc.json'))

templates_path = ['_templates']
exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store', 'node_modules']

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/tee-ar-ex/trx-cpp",
            "icon": "fa-brands fa-github",
        },
    ],
    "logo": {
        "image_light": "_static/trx_logo.png",
        "image_dark": "_static/trx_logo.png",
        "alt_text": "TRX",
        "link": "https://tee-ar-ex.github.io",
        },
    "show_toc_level": 2,
    "navigation_depth": 4,
    "navigation_with_keys": True,
    "show_nav_level": 2,
    "navbar_align": "left",
    "header_links_before_dropdown": 5,
}

html_sidebars = {
    "**": ["sidebar-nav-bs.html", "implementation-links.html"],
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
    "tasklist",
]

autosectionlabel_prefix_document = True
