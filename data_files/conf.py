












import sys, os













extensions = ['sphinx.ext.pngmath']


templates_path = ['_templates']


source_suffix = '.rst'





master_doc = 'index'


project = u'ns-3'
copyright = u'2008-11, ns-3 project'






version = 'ns-3.13'

release = 'ns-3.13'







today = 'December 23, 2011'





exclude_patterns = []
















pygments_style = 'sphinx'









html_theme = 'default'




























html_static_path = ['_static']











































htmlhelp_basename = 'ns-3doc'












latex_documents = [
  ('index', 'ns-3-tutorial.tex', u'ns-3 Tutorial',
   u'ns-3 project', 'manual'),
]





























man_pages = [
    ('index', 'ns-3-tutorial', u'ns-3 Tutorial',
     [u'ns-3 project'], 1)
]
