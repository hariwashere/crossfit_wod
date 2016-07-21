#!/usr/bin/env python

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MyHandler(webapp.RequestHandler):
	def get(self):
		content = template.render('main.html', {})
		self.response.out.write('hello wodsup')

def main():
	app = webapp.WSGIApplication([
		(r'.*', MyHandler)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()