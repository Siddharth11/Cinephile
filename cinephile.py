# get movie/series/episode details on command prompt
# this script is using omdb api to fetch data
# api link: http://www.omdbapi.com/

import urllib
import urllib2
import json

def check_if_required_key_entered(var, var_alias_name, print_text):
	if(len(var) == 0):
		print "{0} field is required!".format(var_alias_name)
		var = raw_input(print_text)
		check_if_required_key_entered(var, var_alias_name, print_text)
	else:
		pass

def search():
	# get item type to be searched
	item_type = raw_input("Type (movie/series/episode) : ")
	check_if_required_key_entered(item_type, 'Type', 'Type (movie/series/episode) : ')

	if(item_type.lower() == "episode" or item_type.lower() == "series"):
		# get item title
		title = raw_input("Series Title : ")
		check_if_required_key_entered(title, 'Title', 'Series Title : ')
		title = urllib.urlencode({'': title})[1:]

		# get season and episode number
		if(item_type.lower() == "episode"):
			season = raw_input("Season : ")
			check_if_required_key_entered(season, 'Season', 'Season : ')

			episode = raw_input("Episode number : ")
			check_if_required_key_entered(episode, 'Episode', 'Episode number : ')

	else:
		# get item title
		title = raw_input("Movie Title : ")
		check_if_required_key_entered(title, 'Title', 'Movie Title : ')
		title = urllib.urlencode({'': title})[1:]

	# base url
	url = 'http://www.omdbapi.com/?tomatoes=true&plot=full&'

	# add search parameters
	url += 't=' + title + '&'

	url += 'type=' + item_type + '&'

	if(item_type == 'episode'):
		url += 'season=' + season + '&' + 'episode=' + episode

	# print url

	response = urllib2.urlopen(url)

	url_data = json.load(response)

	outputArray = ['Title', 'Year', 'Released', 'Runtime', 'Country', 'Language', 'Genre', 'Director', 'Writer', 'Actors', 'Awards', 'Actors', 'imdbRating', 'imdbVotes', 'Plot']
	url_data_keys = url_data.keys()

	if(url_data['Response'] == 'True'):
		print '\n'
		print '-------------**************-------------'
		print '\n'

		for item in outputArray:

			if(item in url_data_keys and url_data[item] != 'N/A'):
				if(item == 'imdbVotes'):
					print 'IMDB Votes:'
				elif(item == 'imdbRating'):
					print 'IMDB Rating:'
				else:
					print item + ':'
				print url_data[item].encode('utf-8')
				print '\n'

		print '-------------**************-------------'
		print '\n'

	else:
		print 'Error fetching data'
		print '\n'

	search_again = raw_input('Wanna search again? (y/n): ')

	if(search_again.lower() == 'y' or search_again.lower() == 'yes'):
		print '\n'
		search()
	else:
		pass

search()