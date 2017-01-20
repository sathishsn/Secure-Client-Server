import tornado.ioloop
import tornado.web
import os
import ssl
import tornado.httpserver 
import clients

class mainhandler(tornado.web.RequestHandler):
	def get(self):
		if self.request.remote_ip in clients.ip_range:
	        	self.render("templates/main.html")			
		else:
			self.render("templates/error_page.html")

class secondhandler(tornado.web.RequestHandler):
	def get(self):
		if self.request.remote_ip in clients.ip_range:
			self.set_header('Content-type', 'templates/imagefile.jpeg')
			self.write(open('templates/imagefile.jpeg').read())  
		else:
			self.render("templates/error_page.html")

class thirdhandler(tornado.web.RequestHandler):
	def get(self):
		if self.request.remote_ip in clients.ip_range:
			self.set_header('Content-type', 'templates/alanwalker.wav')
			self.write(open('templates/alanwalker.wav').read())   
		else:
			self.render("templates/error_page.html")

class fourthhandler(tornado.web.RequestHandler):
	def get(self):
		if self.request.remote_ip in clients.ip_range:
			self.set_header('Content-type', 'templates/video.3gp')
			self.write(open('templates/video.3gp').read()) 
		else:
			self.render("templates/error_page.html")

routes = tornado.web.Application([
    	(r"/", mainhandler),
    	(r"/second", secondhandler),
	(r"/third", thirdhandler),
	(r"/fourth", fourthhandler)
])

ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain(os.path.join("newcert/", "server.crt"),
                        os.path.join("newcert/", "server.key"))


application = tornado.httpserver.HTTPServer(routes, ssl_options=ssl_ctx)
if __name__ == "__main__":	
	application.listen(4443)
	tornado.ioloop.IOLoop.current().start()




