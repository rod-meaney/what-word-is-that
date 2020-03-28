'''
Created on Jul 24, 2011

@author: rod
'''
from google.appengine.ext import db
from admin.utils import KnownError, convertToDate, convertFromDate, cleanJSField
from google.appengine.api import users
from admin import df
from datetime import timedelta
import logging

class List(df.DomainFramework):
    google_id = db.StringProperty()
    name = db.StringProperty()
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
        ls.description = form['description']
        ls.items = form['items']
        ls.private = form['private']

        ls.update()
        
        return True

    def my_lists_authenticated(self):
        results = []
        query=self.all()
        query.filter("google_id = ", users.get_current_user().user_id())
        query.order("name")
        for lItem in query.fetch(1000):
            results.append(lItem.toDictSearch())
        return results
    
    def all_lists_unauthenticated(self):
        results = []
        query=self.all()
        query.filter("private = ", False)
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


# Everytjhing below here is up for grabs - everything above is valid

    def toDictOld(self, sort_order):
        return {"ts":{"key":str(self.key()),
                        "task":self.task,
                          "minutes":self.minutes,  
                          "date":convertFromDate(self.date),
                          "so":sort_order}}
        
    def toCSV(self):
        return [convertFromDate(self.date),
                self.task,
                self.minutes]
        
    def validate_task(self, task):
        errors=[]
        if task=='':errors.append('Must enter a value for task')  
        if not cleanJSField(task):errors.append('Please only use basic text and numbers - also allowed @._-=()')
        return errors
        
    def update_timsheet(self, items):
        '''
        only updating task currently
        '''
        new_task=items['task'].strip()
        current_key=items['key'].strip()
        
        errors=self.validate_task(new_task)
        
        ts = self.get(current_key)
        if users.get_current_user().user_id()<>ts.google_id:
            errors.append('This is not your task to update')
        ts.task = new_task
        
        try:
            ts.minutes=int(items['minutes'])
        except:
            errors.append('Minutes must be an integer')    
        try:
            ts.date = convertToDate(items['date']) 
        except:
            errors.append('Invalid date format - yyyy-mm-dd')
                
        if len(errors)>0: raise KnownError(errors) 
        
        ts.update()
    
    def save_timsheet(self, items):
        '''
        Only save or deleting
        no updating
        '''
        self.google_id=users.get_current_user().user_id()
        new_item=items['task'].strip()
        errors=self.validate_task(new_item)
        self.task=new_item
        
        try:
            self.minutes=int(items['minutes'])
        except:
            errors.append('Minutes must be an integer')        
        try:
            self.date = convertToDate(items['date']) 
        except:
            errors.append('Invalid date format - yyyy-mm-dd')
            
        
        if len(errors)>0: raise KnownError(errors)
        self.createNew()
        
        return True

    def my_timesheets(self, start, end):
        query=self.all()
        query.filter("google_id = ", users.get_current_user().user_id())
        query.filter("date >= ", convertToDate(start))
        query.filter("date <= ", convertToDate(end))
        query.order("-date")
        query.order("-created")
        return query.fetch(1000)
        
    def my_timesheets_json(self, start, end):
        result = {"all_ts":[]}
        tss=self.my_timesheets(start, end)
        count=0
        for ts in tss:
            count=count+1
            result['all_ts'].append(ts.toDict(count))
        return result
    
    def my_timesheets_csv(self, start, end):
        result = []
        tss=self.my_timesheets(start, end)
        for ts in tss:
            result.append(ts.toCSV())
        return result

    def my_timesheets_csv_by_day(self, start, end, hyphen):
        matrix={}
        tss=self.my_timesheets(start, end)
        for ts in tss:
            if hyphen=='yes':
                val=ts.task.split('-')[0].strip()
            else:
                val=ts.task.strip()
            c_date=convertFromDate(ts.date)
            if val in matrix:
                if c_date in matrix[val]:
                    matrix[val][c_date]=matrix[val][c_date]+ts.minutes
                else:
                    matrix[val][c_date]=ts.minutes
            else:
                matrix[val]={c_date:ts.minutes}
        
        result = []
        start_date=convertToDate(start)
        end_date = convertToDate(end)
        delta = timedelta(days=1)
                
        '''
        Create the header
        '''
        header=['']
        i_date = start_date
        while i_date <= end_date:
            header.append(convertFromDate(i_date))
            i_date += delta
        result.append(header)
        
        '''
        iterate through the tasks and date range
        '''
        for x in matrix:
            line=[x]
            i_date = start_date
            while i_date <= end_date:
                c_date = convertFromDate(i_date)
                if c_date in matrix[x]:
                    line.append(matrix[x][c_date])
                else:
                    line.append('')
                i_date += delta            
            result.append(line)

        return result
    
    def delete_timesheets(self, timesheet_list):
        self.delete_list(timesheet_list)
        return "Deleted %d timesheet(s)" % len(timesheet_list)