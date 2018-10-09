import os
from twisted.internet import reactor, endpoints
from twisted.web.server import Site
from twisted.web.resource import Resource
import time

PORT = int(os.environ.get('PORT', 8080))


class ClockPage(Resource):
    isLeaf = True

    def render_GET(self, request):
        return (b"<!DOCTYPE html><html><head><meta charset='utf-8'>"
                b"<title></title></head><body>" + time.ctime().encode('utf-8'))


resource = ClockPage()
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, PORT)
endpoint.listen(factory)
reactor.run()

# https://twistedmatrix.com/documents/current/web/howto/web-in-60/dynamic-content.html
