from com.prashanth.datamodels.UserData import UserData
import webapp2

class StoreData(webapp2.RequestHandler):
    def post(self):        
        userdata = UserData()
        userdata.name = self.request.get('name')
        userdata.gender = self.request.get('gender')
        userdata.age = 24
        userdata.put()
        self.redirect('/')

class TestDatabaseSamplePage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.out.write("""
        <html><body>
        <form action="/store" method="post">
        <div>Name : <input type="text" name="name" rows="3" cols="60"></input></div>
       <div>Gender : <input type="text" name="gender" rows="3" cols="60"></input></div>
       <div>Age : <input type="text" name="age" rows="3" cols="60"></input></div>
       
        <div><input type="submit" value="Submit"></div>
        
        </form>
        </body></html>
        """)


app = webapp2.WSGIApplication([('/', TestDatabaseSamplePage), ('/store', StoreData)],debug=True)
