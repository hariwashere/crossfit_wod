#!/usr/bin/env python

import os
import webapp2
import json

import wsgiref.handlers
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import scraper


class MyWorkoutSession(webapp2.RequestHandler):
	def get(self):
		self.response.out.write(unicode(template.render('wod.html', {})))

class GetWorkoutSession(webapp2.RequestHandler):
    def get(self):
        equipments = self.request.get("equipments").split(',')
        wods = scraper.get_wod_for_equipments(equipments)

        wod_dict = {}
        wod_dict['wods'] = []

        for wod in wods:
            inner_wod_dict = {}
            inner_wod_dict['wod'] = [wod]
            wod_dict['wods'].append(inner_wod_dict)

        """
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
        """
        output = json.dumps(wod_dict)
        self.response.write(output)


def main():
    app = webapp2.WSGIApplication(
                                  [('/', MyWorkoutSession),
                                   ('/get_workout_session', GetWorkoutSession),
                                   ], debug=True)
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == "__main__":
	main()


