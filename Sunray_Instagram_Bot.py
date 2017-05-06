#sunray

from InstagramAPI import InstagramAPI
from pprint import pprint
import json
import datetime
import time

timemark = datetime.datetime.now()



API = InstagramAPI("","") #your username and password
API.login()

userid = 0
mediaid = 0
maxid = ''

cities= {

	'NYC' : {	

		#key:user ID
		"NYU":409064094,
		"Columbia":480466954	
	},

	'Boston' : {
		
		'BU':284341891,
		'BC':22963539,
		'Harvard' :259394152,
		'MIT Engineering' :3183954478,
		'Tufts' :1366008,
		'Northeastern':4558614
	},

	'London' : {
		
		'UCL':1112437534,
		'LSE':1686206464,
		'ICL':1360916305
	},


	'SF' : {
		
		'Stanford':466003,
		'USF':249226070,
		'UCB':249761036
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

	for city in cities:
		for sch,value in cities[city].items():
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
			continue

		else:

			try:

				i_follower = len(API.getTotalFollowers(i))
				i_following = len(API.getTotalFollowings(i))

				#Check for Celebgram
				if i_follower/i_following >=2:
					legit_user = False
					print ("Likely to be Celebgram. Skip\n")
					continue

				#Check for Fake Acc
				elif i_following/i_follower >=2:
					legit_user = False
					print ("Likely to be Fake Acc. Skip\n")
					continue

				#Follow healthy profile
				elif legit_user == True:
					
					print ("Attempting to follow %s" %i_username)
					API.follow(i)
					follow_counter += 1
					print ("Followed %s, Session Followed #%i\n" %(i_username, follow_counter))
					throttle()

			#Follow private profile
			except:
				print ("Private Account, attempting to follow")
				API.follow(i)
				follow_counter += 1
				print ("Followed %s, Session Followed #%i\n" %(i_username, follow_counter))
				throttle()





