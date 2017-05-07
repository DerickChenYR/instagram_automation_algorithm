from InstagramAPI import InstagramAPI
from pprint import pprint
import json
import datetime
import time
from random import randint
import threading


timemark = datetime.datetime.now()

API = InstagramAPI("","") #username, password
API.login()

userid =  #int userid given by instagram

def throttle():
	sleeptime = randint(15,30)
	print ("Throttle in effect: bot sleeping for %i seconds.\n" %sleeptime)
	time.sleep(sleeptime)

def unfollow_procedure():

	has_more_data = True
	maxid = ''

	unfollow_counter = 0
	unfollow_pool = []


	while has_more_data == True:

		API.getUserFollowings(userid,maxid)

		for i in API.LastJson['users']:
			unfollow_pool.append(i['pk'])

		has_more_data = API.LastJson["big_list"]

		if API.LastJson["big_list"] == True:
			maxid = API.LastJson['next_max_id']

	#print (unfollow_pool))
	print ("Unfollow Pool - Harvested %i\n" %len(unfollow_pool))

	for i in unfollow_pool:
		print ("Trying to unfollow %s" %str(i))
		API.unfollow(i)
		unfollow_counter += 1
		print ("Unfollowed %s, Session Unfollowed #%i\n" %(i, unfollow_counter))
		throttle()








unfollow_procedure()