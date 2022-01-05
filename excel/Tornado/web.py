import tornado.ioloop
import tornado.web
import sys
class MainHandler(tornado.web.RequestHandler):
        def get(self):
                self.write("welcome!")
class ReadDemoHandler(tornado.web.RequestHandler):
        def get(self):
                f=open("demo.txt","r")
                self.write(f.read())
class ExcelDisplayHandler(tornado.web.RequestHandler):
        def get(self):
                self.render("demo.html")
def make_app():
        return tornado.web.Application([
        (r"/demo",ReadDemoHandler),
        (r"/excel",ExcelDisplayHandler),
        (r"/",MainHandler)
])
if __name__ == "__main__":
        a=sys.argv
        print(a)
        if len(a) >2 :
                port=int(a[2])
        else:
                port=8888
        app=make_app()
        app.listen(port)
        tornado.ioloop.IOLoop.current().start()

a = ['web.py', '--port', '8000', '--host', '127.0.1']
l_a=[]
l_b=[]
for i in a:
        lem_a = a.index(i)
        if lem_a%2 == 0:
                l_a.append(i)
                a=a+1
        else:
                l_b.append(i)
                a=a+1

