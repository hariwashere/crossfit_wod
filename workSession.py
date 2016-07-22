#!/usr/bin/env python

import os
import wsgiref.handlers
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template


class WorkoutSession(webapp.RequestHandler):
    def get(self):
        return {'project': 'hello_ajax'}
#       list_of_equipments = self.request.get('list_of_equipments')}