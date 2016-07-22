#!/usr/bin/env python

import os
import webapp2
import json
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class MyWorkoutSession(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(unicode(template.render('wod.html', {})))

class WorkoutSession(webapp2.RequestHandler):
    def get(self):
        dict = {
            'wods': [
                {
                    'wod': [
                        '8 deadlifts',
                        '40 GHD sit-ups',
                        '80 double-unders',
                        '4 rope climbs',
                        '80 wall-ball shots',
                        '80 double-unders',
                    ],
                },
                {
                    'wod': [
                        '8 deadlifts',
                        '40 GHD sit-ups',
                        '80 double-unders',
                        '4 rope climbs',
                        '80 wall-ball shots',
                        '80 double-unders',
                    ],
                },
                {
                    'wod': [
                        '8 deadlifts',
                        '40 GHD sit-ups',
                        '80 double-unders',
                        '4 rope climbs',
                        '80 wall-ball shots',
                        '80 double-unders',
                    ],
                },
                {
                    'wod': [
                        '8 deadlifts',
                        '40 GHD sit-ups',
                        '80 double-unders',
                        '4 rope climbs',
                        '80 wall-ball shots',
                        '80 double-unders',
                    ],
                },
            ]
        }
        output = json.dumps(dict)
        self.response.write(output)

def main():
    app = webapp2.WSGIApplication([('/', MyWorkoutSession),('/get_workout_session', WorkoutSession),], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()


