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
folder_day7 = (date.today()-timedelta(days=1)).strftime("%Y-%m-%d")
folder_day6 = (date.today()-timedelta(days=2)).strftime("%Y-%m-%d")
folder_day5 = (date.today()-timedelta(days=3)).strftime("%Y-%m-%d")
folder_day4 = (date.today()-timedelta(days=4)).strftime("%Y-%m-%d")
folder_day3 = (date.today()-timedelta(days=5)).strftime("%Y-%m-%d")
folder_day2 = (date.today()-timedelta(days=6)).strftime("%Y-%m-%d")
folder_day1 = (date.today()-timedelta(days=7)).strftime("%Y-%m-%d")
createFolder('./library/' + folder_day1 + '/')
createFolder('./library/' + folder_day2 + '/')
createFolder('./library/' + folder_day3 + '/')
createFolder('./library/' + folder_day4 + '/')
createFolder('./library/' + folder_day5 + '/')
createFolder('./library/' + folder_day6 + '/')
createFolder('./library/' + folder_day7 + '/')




try:
	# Instantiating the Arlo object automatically calls Login(), which returns an oAuth token that gets cached.
	# Subsequent successful calls to login will update the oAuth token.
	arlo = Arlo(USERNAME, PASSWORD)
	# At this point you're logged into Arlo.
    
	# Specify dates for the previous 7 days preceeding today in correct format
	download_day7 = (date.today()-timedelta(days=1)).strftime("%Y%m%d")
	download_day6 = (date.today()-timedelta(days=2)).strftime("%Y%m%d")
	download_day5 = (date.today()-timedelta(days=3)).strftime("%Y%m%d")
	download_day4 = (date.today()-timedelta(days=4)).strftime("%Y%m%d")
	download_day3 = (date.today()-timedelta(days=5)).strftime("%Y%m%d")
	download_day2 = (date.today()-timedelta(days=6)).strftime("%Y%m%d")
	download_day1 = (date.today()-timedelta(days=7)).strftime("%Y%m%d")

	#today = (date.today()-timedelta(days=0)).strftime("%Y%m%d")
	#seven_days_ago = (date.today()-timedelta(days=7)).strftime("%Y%m%d")
	#yesterday = (date.today()-timedelta(days=1)).strftime("%Y%m%d")
	#day_before_yesterday = (date.today()-timedelta(days=2)).strftime("%Y%m%d")
	
	# Get all of the recordings for a date range.
	# library_all = arlo.GetLibrary(download_day1, download_day7)
	
	# Get all of the recordings for specific day.
	library_day1 = arlo.GetLibrary(download_day1, download_day1)

	# Iterate through the recordings in the library_day1.
	for recording in library_day1:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day1 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day1)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day1 + ' completed successfully.')

	# Get all of the recordings for specific day.
	library_day2 = arlo.GetLibrary(download_day2, download_day2)

	# Iterate through the recordings in the library_day2.
	for recording in library_day2:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day2 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day2)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day2 + ' completed successfully.')

	# Get all of the recordings for specific day.
	library_day3 = arlo.GetLibrary(download_day3, download_day3)

	# Iterate through the recordings in the library_day3.
	for recording in library_day3:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day3 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day3)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day3 + ' completed successfully.')

	# Get all of the recordings for specific day.
	library_day4 = arlo.GetLibrary(download_day4, download_day4)

	# Iterate through the recordings in the library_day4.
	for recording in library_day4:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day4 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day4)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day4 + ' completed successfully.')

	# Get all of the recordings for specific day.
	library_day5 = arlo.GetLibrary(download_day5, download_day5)

	# Iterate through the recordings in the library_day5.
	for recording in library_day5:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day5 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day5)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day5 + ' completed successfully.')

	# Get all of the recordings for specific day.
	library_day6 = arlo.GetLibrary(download_day6, download_day6)

	# Iterate through the recordings in the library_day6.
	for recording in library_day6:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day6 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day6)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day6 + ' completed successfully.')

	# Get all of the recordings for specific day.
	library_day7 = arlo.GetLibrary(download_day7, download_day7)

	# Iterate through the recordings in the library_day7.
	for recording in library_day7:

		videofilename = datetime.datetime.fromtimestamp(int(recording['name'])//1000).strftime('%Y-%m-%d-%H-%M-%S') + '-' + recording['uniqueId'] + '.mp4'
		
		# Get video as a chunked stream; this function returns a generator.
		stream = arlo.StreamRecording(recording['presignedContentUrl'])
		with open('library/'+ folder_day7 + '/' + videofilename, 'wb') as f:
			for chunk in stream:
				f.write(chunk)
			f.close()

		print('Downloaded video '+videofilename+' from '+recording['createdDate']+'.')

	# Delete all of the videos you just downloaded from the Arlo library.
	result = arlo.BatchDeleteRecordings(library_day7)

	# If we made it here without an exception, then the videos were successfully deleted.
	print('Batch deletion of videos for DATE ' + folder_day7 + ' completed successfully.')

	arlo.Logout()
	print('Logged out')

	# Rename files with replacing arlo device unique ID with its name

	path_day1 =  os.getcwd() + '/library/' + folder_day1
	path_day2 =  os.getcwd() + '/library/' + folder_day2
	path_day3 =  os.getcwd() + '/library/' + folder_day3
	path_day4 =  os.getcwd() + '/library/' + folder_day4
	path_day5 =  os.getcwd() + '/library/' + folder_day5
	path_day6 =  os.getcwd() + '/library/' + folder_day6
	path_day7 =  os.getcwd() + '/library/' + folder_day7

	filenames_day1 = os.listdir(path_day1)

	for filename in filenames_day1:
		os.rename(path_day1 + '/' + filename, path_day1 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day1 = os.listdir(path_day1)
    
	for filename in filenames_day1:
		os.rename(path_day1 + '/' + filename, path_day1 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	filenames_day2 = os.listdir(path_day2)

	for filename in filenames_day2:
		os.rename(path_day2 + '/' + filename, path_day2 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day2 = os.listdir(path_day2)
    
	for filename in filenames_day2:
		os.rename(path_day2 + '/' + filename, path_day2 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	filenames_day3 = os.listdir(path_day3)

	for filename in filenames_day3:
		os.rename(path_day3 + '/' + filename, path_day3 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day3 = os.listdir(path_day3)
    
	for filename in filenames_day3:
		os.rename(path_day3 + '/' + filename, path_day3 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	filenames_day4 = os.listdir(path_day4)

	for filename in filenames_day4:
		os.rename(path_day4 + '/' + filename, path_day4 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day4 = os.listdir(path_day4)
    
	for filename in filenames_day4:
		os.rename(path_day4 + '/' + filename, path_day4 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	filenames_day5 = os.listdir(path_day5)

	for filename in filenames_day5:
		os.rename(path_day5 + '/' + filename, path_day5 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day5 = os.listdir(path_day5)
    
	for filename in filenames_day5:
		os.rename(path_day5 + '/' + filename, path_day5 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	filenames_day6 = os.listdir(path_day6)

	for filename in filenames_day6:
		os.rename(path_day6 + '/' + filename, path_day6 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day6 = os.listdir(path_day6)
    
	for filename in filenames_day6:
		os.rename(path_day6 + '/' + filename, path_day6 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	filenames_day7 = os.listdir(path_day7)

	for filename in filenames_day7:
		os.rename(path_day7 + '/' + filename, path_day7 + '/' + filename.replace("300-5293895_4CD365ST1B5C8", "crib"))

	filenames_day7 = os.listdir(path_day7)
    
	for filename in filenames_day7:
		os.rename(path_day7 + '/' + filename, path_day7 + '/' + filename.replace("300-5293895_4CD365S91B43C", "play-yard"))

	print('All arlo video files renamed successfully.')

except Exception as e:
    print(e)
