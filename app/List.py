'''
Created on Jul 24, 2011

@author: rod
'''
from google.appengine.ext import db
from admin.utils import KnownError
from google.appengine.api import users
from admin import df
import logging

class List(df.DomainFramework):
    google_id = db.StringProperty()
    name = db.StringProperty()
    name_index1 = db.StringProperty()
    #name_index2 = db.StringProperty()
    #name_index3 = db.StringProperty()
    #name_index4 = db.StringProperty()
    #name_index5 = db.StringProperty()
    description = db.StringProperty(multiline=True)
    items = db.TextProperty()
    private = db.BooleanProperty()
    
    def __init__(self, *args, **kwargs):  
        super(List, self).__init__(*args, **kwargs)

    def save_list(self, form):
        '''
        TO-DO Check the data in the backend
        '''
        errors=[]
        self.google_id=users.get_current_user().user_id()
        self.name = form['name']
        self.name_index1 = form['name'].lower()[0:3]
        self.description = form['description']
        self.items = form['items']
        self.private = form['private']
        
        if len(errors)>0: raise KnownError(errors)
        
        self.createNew()
        
        return True

    def update_list(self, form):
        '''
        TO-DO Check the data in the backend
        '''
        
        ls = self.get(form['loaded_id'])
        if users.get_current_user().user_id()<>ls.google_id:
            raise KnownError(['Cannot update because you are not the owner of this list'])  
        
        ls.name = form['name']
        ls.name_index1 = form['name'].lower()[0:3]
        ls.description = form['description']
        ls.items = form['items']
        ls.private = form['private']

        ls.update()
        
        return True

    def my_lists_authenticated(self, q):
        results = []
        query=self.all()
        query.filter("google_id = ", users.get_current_user().user_id())
        if q != "":
            query.filter("name_index1 = ", q.lower())
        query.order("name")
        for lItem in query.fetch(1000):
            results.append(lItem.toDictSearch())
        return results
    
    def all_lists_unauthenticated(self, q):
        results = []
        query=self.all()
        query.filter("private = ", False)
        if q != "":
            query.filter("name_index1 = ", q.lower())
        query.order("name")
        for lItem in query.fetch(1000):
            results.append(lItem.toDictSearch())
        return results

    #Probably just one get in the end, with all the checks
    def get_list(self, key):
        try:
            ls = self.get(key)
        except:
            raise KnownError(['You are trying to fetch a list that does not exist'])
        if ls.private:
            try:
                if ls.google_id <> users.get_current_user().user_id():
                    raise KnownError(['You do not have access to that list.'])
            except:
                raise KnownError(['Not available to you'])
        return ls.toDict()

    #Probably just one get in the end, with all the checks
    def delete_list(self, key):
        try:
            ls = self.get(key)
        except:
            raise KnownError(['You are trying to delete a list that does not exist'])

        try:
            if ls.google_id <> users.get_current_user().user_id():
                raise KnownError(['You do not have access to that list.'])
        except:
            raise KnownError(['You do not have access to that list to delete'])
        ls.delete()
        return {"success":True}
    
    def toDictSearch(self):
        return {"name":self.name,
                "key":str(self.key()),
                "description":self.description,  
                "private":self.private}

    def toDict(self):
        return {"key":str(self.key()),
                "name":self.name,
                 "description":self.description,
                 "items":self.items,  
                "private":self.private}