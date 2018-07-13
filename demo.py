import tornado.ioloop
import tornado.web
from cache import Cache


class SetData(tornado.web.RequestHandler):
    def get(self):
        Cache().setex("data","Hello World", 60*60)
        self.write("Ok")
        
        
class GetData(tornado.web.RequestHandler):
    def get(self):
        data = Cache().get("data")
        self.write(str(data))


def make_app():
    return tornado.web.Application([
        (r"/set_data", SetData),
        (r"/get_data", GetData),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()