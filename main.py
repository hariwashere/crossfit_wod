#!/usr/bin/env python

import os
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class WorkoutSession(db.Model):
    workoutType = db.StringProperty(required=True)
    workoutTime = db.DateTimeProperty(required=True)


class MyWorkoutSession(webapp.RequestHandler):
	def get(self):
#       list_of_equipment = self.request.get('list_of_equipment')
		self.response.out.write(unicode(template.render('wod.html', {})))
#		self.response.out.write('hello wodsup')


def main():
	app = webapp.WSGIApplication([
		(r'.*', MyWorkoutSession)], debug=True)
	wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()