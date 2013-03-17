import os
from google.appengine.ext.webapp import template

def templ(filename, vals={}):
  path = os.path.join(os.path.dirname(__file__), filename + '.html')
  return template.render(path, vals)