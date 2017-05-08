#sunray

from InstagramAPI import InstagramAPI
from pprint import pprint
import json
import datetime
import time
from random import randint

timemark = datetime.datetime.now()



API = InstagramAPI("","") #your username and password
API.login()

userid = 0 #add the userid of your account
mediaid = 0
maxid = ''

accounts= {

	'set1' : {	

		#key:user ID
		"key1":409064094,
		"key2":480466954	
	},

	'set2' : {
		
		'key3':284341891,
		'key4':22963539,
		'key5' :259394152,
	}
}


#Speed control to prevent ban

def throttle():
	sleeptime = randint(5,10)
	print ("Throttle in effect: bot sleeping for %i seconds.\n" %sleeptime)
	time.sleep(sleeptime)


#Generate a recent follower pool for universities instagram accounts




#Follow harvested profiles in the follow_pool list

def follow_procedure():

	follow_counter = 0
	follow_pool = []

	for sets in accounts:
		for key,value in accounts[sets].items():
			#print (str(value))

			API.getUserFollowers(value)
			for i in API.LastJson['users']:
				follow_pool.append(i['pk'])
			time.sleep(1)

	#print (follow_pool)
	print ("Follow Pool - Harvested %i\n" %len(follow_pool))

	for i in follow_pool:
		legit_user = True
		API.userFriendship(i)
		friendship_status = API.LastJson

		API.getUsernameInfo(i)
		i_username = API.LastJson['user']['username']

		print ("---Retriving user data for: %s ---" %i_username)
		
		#Skip if already following/request sent
		if friendship_status['outgoing_request'] == True or friendship_status['following'] == True:
			print ("Already following/sent follow request. Skip\n")
			follow_pool.remove(i)
			continue

		else:

			try:

				i_follower = len(API.getTotalFollowers(i))
				i_following = len(API.getTotalFollowings(i))

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

			#Follow private profile
			except:
				print ("Private Account, attempting to follow")
				API.follow(i)
				follow_counter += 1
				print ("Followed %s, Session Followed #%i\n" %(i_username, follow_counter))
				follow_pool.remove(i)
				throttle()





