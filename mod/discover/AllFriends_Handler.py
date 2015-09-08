# -*- coding: utf-8 -*-
#!/usr/bin/env python

import tornado.web
import tornado.gen
import json
from mod.auth.Base_Handler import BaseHandler
import pymongo

from pymongo import MongoClient

from ..databases.tables import UsersCache,CookieCache
#/discover/add
class AllFriendsHandler(BaseHandler):
    @property
    def db(self):
        return self.application.db


    @property
    def Mongodb(self):
    	return self.application.Mongodb


    def on_finish(self):
        self.db.close()

    def post (self):
  		retjson = {'code':200,'content':'ok'}
  		# uid
  		user_cookie = self.current_user
  		uid = user_cookie.uid


  		try:
  			retjson['content']=self.Mongodb.friend_follow.find({
  				"uid":str(uid)
  				})
  			
  		except Exception, e:
  			retjson['code'] = 401
  			retjson['content'] = u'Database store is wrong'

  		ret = json.dumps(retjson,ensure_ascii=False, indent=2)
  		self.write(ret) 


  