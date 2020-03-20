import webapp2
from frameworks.WebContainer import StandardPage
from google.appengine.ext.webapp import template
from app.wrapper import url_inject
from app.List import List
import json
import logging

class MainPage(StandardPage):
    @url_inject("web")
    def get(self):
        self.response.out.write(template.render('read/index.html', self.template_values))

class DataTest(webapp2.RequestHandler):
    #@url_inject("json")
    def get(self):
        self.response.out.write(json.dumps({"test":"into the breach we go"}))

class DataSearch(webapp2.RequestHandler):
    #@url_inject("json")
    def get(self):
        self.response.out.write(json.dumps(List().all_lists_unauthenticated()))

class DataGet(webapp2.RequestHandler):
    @url_inject("json")
    def get(self):
        key = self.request.GET['id']
        self.response.out.write(json.dumps(List().get_unauthenticated(key)))
        
app = webapp2.WSGIApplication([
        ('/api/search', DataSearch),
        ('/api/test', DataTest),
        ('/api/get.*', DataGet),
        ('/.*', MainPage),
        ],debug=True)