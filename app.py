from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
import tornado.autoreload

from app.routes import route

define('port', default=4000, help= 'port to listen on')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = route()
    http_server = HTTPServer(app)
    http_server.listen(options.port)
    print("======================================")
    print('App listening at: http://localhost:%i/' % options.port)
    tornado.autoreload.start()
    IOLoop.current().start()

# run : pipenv run python app.py