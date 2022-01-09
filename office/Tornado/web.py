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
                self.render("../excel.html")

class DocxDisplayHandler(tornado.web.RequestHandler):
        def get(self):
                self.render("../python-docx读取doc.html")

def make_app():
        return tornado.web.Application([
        (r"/docx",DocxDisplayHandler),
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



