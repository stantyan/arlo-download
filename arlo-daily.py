from datetime import timedelta, date
from Arlo import Arlo
import datetime
import sys
import os

USERNAME = 'EMAIL'
PASSWORD = 'PASSWORD'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory) 

# Create folders for the previous 7 days preceeding today
folder_yesterday = (date.today()-timedelta(days=1)).strftime("%Y-%m-%d")
createFolder('/home/arlo/arlo/library/' + folder_yesterday + '/')




try:
	# Instantiating the Arlo object automatically calls Login(), which returns an oAuth token that gets cached.
	# Subsequent successful calls to login will update the oAuth token.
	arlo = Arlo(USERNAME, PASSWORD)
	# At this point you're logged into Arlo.
    
	# Specify dates for the previous 7 days preceeding today in correct format
	download_yesterday = (date.today()-timedelta(days=1)).strftime("%Y%m%d")

	#today = (date.today()-timedelta(days=0)).strftime("%Y%m%d")
	#seven_days_ago = (date.today()-timedelta(days=7)).strftime("%Y%m%d")
	#yesterday = (date.today()-timedelta(days=1)).strftime("%Y%m%d")
	#day_before_yesterday = (date.today()-timedelta(days=2)).strftime("%Y%m%d")
	
	# Get all of the recordings for a date range.
	# library_all = arlo.GetLibrary(download_day1, download_yesterday)

	# Get all of the recordings for specific day.
	library_yesterday = arlo.GetLibrary(download_yesterday, download_yesterday)

	# Iterate through the recordings in the library_yesterday.
	for recording in library_yesterday:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('/home/arlo/arlo/library/'+ folder_yesterday + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_yesterday)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE' + folder_yesterday + 'completed successfully.')

	arlo.Logout()
	print('Logged out')

	# Rename files with replacing arlo device unique ID with its name

	path_yesterday =  '/home/arlo/arlo/library/' + folder_yesterday

	filenames_yesterday = os.listdir(path_yesterday)

	for filename in filenames_yesterday:
		os.rename(path_yesterday + '/' + filename, path_yesterday + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_yesterday = os.listdir(path_yesterday)
    
	for filename in filenames_yesterday:
		os.rename(path_yesterday + '/' + filename, path_yesterday + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	print('All arlo video files renamed successfully.')

except Exception as e:
    print(e)
