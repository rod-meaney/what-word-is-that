import webapp2
from frameworks.WebContainer import StandardPage
from google.appengine.ext.webapp import template
from app.wrapper import url_inject
from app.List import List
import json
import logging

class MainPageEdit(StandardPage):
    @url_inject("web")
    def get(self):
        self.response.out.write(template.render('edit/index.html', self.template_values))

class DataSaveList(webapp2.RequestHandler):
    #@url_inject("json")
    def post(self):
        ls = List()
        ls.save_list(json.loads(self.request.body))
        self.response.out.write(json.dumps({"response":"saved"}))
        
app = webapp2.WSGIApplication(
                                     [('/edit/api/save', DataSaveList),
                                         ('/edit/.*', MainPageEdit),
                                      ],
                                     debug=True)