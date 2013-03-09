#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Prabhjot Singh on 2013-02-04.
Copyright (c) 2013 Prabhjot Singh. All rights reserved.
"""
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import users
from utils import PrabhRequestHandler, administrator
from blog import Entry

class AdminHandler(PrabhRequestHandler):
    @administrator
    def get(self):
        self.render("templates/admin.html")

class EntryListHandler(PrabhRequestHandler):
    @administrator
    def get(self):
        entries = Entry.all().order("-published")
        self.render("templates/admin_entrylist.html",
            entries=entries)

class ConfigHandler(PrabhRequestHandler):
    @administrator
    def get(self):
        self.render("templates/config.html")
    @administrator    
    def post(self):
        config = Config.all()
        config = config.fetch(1)[0]
        config.title = self.request.get("title")
        config.disqus = self.request.get("disqus")
        config.put()
        self.redirect('/')

