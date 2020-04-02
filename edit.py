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
        self.response.out.write(json.dumps({"response":"updated"}))

class DataUpdateList(webapp2.RequestHandler):
    #@url_inject("json")
    def post(self):
        ls = List()
        ls.update_list(json.loads(self.request.body))
        self.response.out.write(json.dumps({"response":"saved"}))

class DataMyList(webapp2.RequestHandler):
    #@url_inject("json")
    def get(self):
        try:
            q = self.request.GET['q']
        except:
            q=""        
        self.response.out.write(json.dumps(List().my_lists_authenticated(q)))
        
class DataGet(webapp2.RequestHandler):
    @url_inject("json")
    def get(self):
        key = self.request.GET['id']
        self.response.out.write(json.dumps(List().get_list(key)))
        
app = webapp2.WSGIApplication([('/edit/api/my-lists', DataMyList),
                               ('/edit/api/item.*', DataGet),
                               ('/edit/api/save', DataSaveList),
                               ('/edit/api/update', DataUpdateList),
                               ('/edit/.*', MainPageEdit),
                                      ],
                                     debug=True)