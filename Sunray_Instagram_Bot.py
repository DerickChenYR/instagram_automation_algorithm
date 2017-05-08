#sunray

from InstagramAPI import InstagramAPI
from pprint import pprint
import json
import datetime
import time
import random
from random import randint, shuffle

timemark = datetime.datetime.now()
print ("Sunray IG Bot started at " + str(timemark))

my_username = "" #your username
my_password = "" #your password

userid = 0 #your userid
mediaid = 0 

API = InstagramAPI(my_username, my_password) #your username and password
print ("Logging into %s" % my_username)
API.login()

accounts= {

	'set1' : {	

		#key:user ID
		"key1":409064094,
		"key2":480466954	
	},

	'set2' : {
		
		'key3':284341891,
		'key4':22963539,
		'key5':259394152
	}
}


#Speed control to prevent ban

def throttle():
	sleeptime = randint(25,35)
	print ("Throttle in effect: bot sleeping for %i seconds." %sleeptime)
	print ("Paused at %s\n" %str(datetime.datetime.now()))
	time.sleep(sleeptime)



#Follow Procedures

def follow_procedure():

	follow_counter = 0
	follow_pool = []

	#Generate a recent follower pool for universities instagram accounts
	for sets in accounts:
		for key,value in accounts[sets].items():

			API.getUserFollowers(value)
			for i in API.LastJson['users']:
				follow_pool.append(i['pk'])
			
	print ("Follow Pool - Harvested %i\n" %len(follow_pool))

	#Follow harvested profiles in the follow_pool list
	random.shuffle(follow_pool)
	for i in follow_pool:
		legit_user = True
		API.userFriendship(i)
		friendship_status = API.LastJson

		API.getUsernameInfo(i)
		i_username = API.LastJson['user']['username']
		i_follower = API.LastJson['user']['follower_count']
		i_following = API.LastJson['user']['following_count']
		
		print ("---Retriving user data for: %s---" %i_username)
		
		#Skip if already following/request sent
		if friendship_status['outgoing_request'] == True or friendship_status['following'] == True:
			print ("Already following/sent follow request. Skip\n")
			follow_pool.remove(i)
			continue

		else:
			try:
				#Check for Celebgram
				if i_follower/i_following >=2:
					legit_user = False
					print ("Likely to be Celebgram. Skip\n")
					follow_pool.remove(i)
					continue

				#Check for Fake Acc
				elif i_following/i_follower >=2:
					legit_user = False
					print ("Likely to be Fake Acc. Skip\n")
					follow_pool.remove(i)
					continue

				#Follow healthy profile
				elif legit_user == True:
					
					print ("Attempting to follow %s" %i_username)
					API.follow(i)
					follow_counter += 1
					print ("Followed %s, Session Followed #%i\n" %(i_username, follow_counter))
					follow_pool.remove(i)
					throttle()

			except:
				print ("Error.\n")
				continue




