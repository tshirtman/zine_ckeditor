# -*- coding: utf-8 -*-
"""
    zine.plugins.zine_ckeditor
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    A plugin to use ckeditor when editing an entry.
    :copyright: (c) 2011 by gabriel pettier for more details.
    :license: BSD, see LICENSE for more details.
"""
import os
from os.path import join, dirname

from zine.api import *

SHARED_FILES = join(dirname(__file__), 'shared')

def inject_ckeditor(req, context):
    """This is called before the admin response is rendered. We add the
    """
    add_script(url_for('zine_ckeditor/shared', filename='ckeditor/ckeditor.js'))
    add_header_snippet('''
        <script type="text/javascript">
        $(document).ready(function() {
        ckeditor = CKEDITOR.replace('f_text');
        })
        </script>''');

def setup(app, plugin):
    """This function is called by Zine in the application initialization
    phase. Here we connect to the events and register our template paths,
    url rules, views etc.
    """
    app.connect_event('before-admin-response-rendered', inject_ckeditor)
    app.add_shared_exports('zine_ckeditor', SHARED_FILES)
