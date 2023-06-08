''' 
You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.
The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:
    Use the ftplib library to connect to the external FTP server and list the files in the directory.
    Use the os library to check for the existence of a local directory where the files will be stored.
    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.
    Use the shutil library to move the files from the local directory to the internal network.
    Use the schedule library to schedule the script to run daily at a specific time.
    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. 
'''

from ftplib import FTP
import os
import shutil
import schedule
import time

#Use the ftplib library to connect to the external FTP server.
def connect_server(address, username='anonymous', password=''):
    try:
        ftp = FTP(address)
        ftp.login(username, password)
        return ftp
    except Exception as e:
        print(f'Failed to connect to FTP server. Reason: {e}')
        return None

#list the files in the directory.
def files_list(ftp, directory=''):
    try:
        # Try to change to the specified directory
        if directory != '':
            ftp.cwd(directory)
    except Exception as e:
        # If an error occurred (e.g. the directory does not exist), print an error message and return None
        print(f"Failed to change to directory '{directory}'. Reason: {e}")
        return None
    # If changing to the directory was successful, return the list of files
    return ftp.nlst()

#ftp.dir()
#ftp.retrlines('LIST')

def check_dir(directory):
    if os.path.isdir(directory):
        print("Directory exists.")
    else:
        os.makedirs(directory)
        print("Directory created.")
    return directory

def download_files(ftp, local_dir, file_list):
    # Iterate through the files and download them
    for file in file_list:
        local_filepath = os.path.join(local_dir, file)
        try:
            with open(local_filepath, 'wb') as local_file:
                ftp.retrbinary('RETR ' + file, local_file.write, 1024)
                print(f"Downloaded {file}")
        except Exception as e:
            print(f"Failed to download {file}. Reason: {e}")

#Use the shutil library to move the files from the local directory to the internal network.
def move_files(src_dir, end_dir):
    for file in os.listdir(src_dir):
        try:
            source_path = os.path.join(src_dir, file)
            destination_path = os.path.join(end_dir, file)
            shutil.move(source_path, destination_path)
            print(f"Successfully moved {file} to {end_dir}.")
        except Exception as e:
            print(f"Failed to move {file}. Reason: {e}")

def main_pipe():
    
    address = 'ftp.ncei.noaa.gov' #National Oceanic and Atmospheric Administration (NOAA)
    ftp = connect_server(address) #the NOAA FTP doesn't take username or password
    
    directory = '/pub/data/cdo/samples/' #directory containing the files I want
    file_list = files_list(ftp, directory) #a list wtith the files names

    local_dir = r'C:\Users\migue\Documents\Brainnest_python\ftp_data'
    local_dir = check_dir(local_dir) #check on local dir to store data
    
    download_files(ftp, local_dir, file_list) #fetching the files and storing them
    
    src_dir = local_dir
    end_dir = r'C:\Users\migue\Documents\Brainnest_python\ftp_data2'
    end_dir = check_dir(end_dir)
    move_files(src_dir, end_dir) #move the files internally
        
    ftp.quit()
    
    print('\nEnd of job')
    
    return schedule.CancelJob

#Use the schedule library to schedule the script to run daily at a specific time.
schedule.every().day.at("14:52").do(main_pipe)

def main():
    while True:
        schedule.run_pending()

main()

'''
This script is a Python application designed to connect to an FTP server, download files from a specified directory, and then move these files to another directory on the local system. It is scheduled to run this process daily at a specific time. 

## Code Description

The script is broken down into several functions each performing a specific task in the overall process. It starts with a function to connect to the FTP server (`connect_server()`), then lists the files in the directory (`files_list()`), checks if a local directory exists or creates one if it doesn't (`check_dir()`), downloads the files from the FTP server to the local directory (`download_files()`), and finally moves the files to a new local directory (`move_files()`). The script also includes a `main_pipe()` function that calls these functions in sequence and is scheduled to run daily.

Brief overview of each function:

1. `connect_server(address, username='anonymous', password='')` : This function establishes a connection to the FTP server at the given address, with the given username and password.

2. `files_list(ftp, directory='')` : This function retrieves and returns a list of all files in a specified directory on the FTP server.

3. `check_dir(directory)` : This function checks if a specified directory exists on the local system. If it doesn't exist, it creates it.

4. `download_files(ftp, local_dir, file_list)` : This function downloads all files from the FTP server's specified directory to a local directory.

5. `move_files(src_dir, end_dir)` : This function moves files from one local directory to another.

6. `main_pipe()` : This function calls all the other functions in the right order to accomplish the task. It first connects to the FTP server, fetches a list of files, ensures local directories exist (or creates them if they don't), downloads the files, and finally moves the files to the desired local directory. This function is scheduled to run every day.


## Libraries

The script uses the following Python libraries:

1. `ftplib` : This is a library included in Python's standard library that includes functions to support the FTP protocol. This script uses it to connect to the FTP server, navigate the server's file system, and download files.

2. `os` : This library provides a way of using operating system dependent functionality. The script uses this library to interact with the system's file directory to check if a directory exists (`os.path.isdir()`), create a directory (`os.makedirs()`), build file paths (`os.path.join()`), and list files in a directory (`os.listdir()`).

3. `shutil` : This module offers a number of high-level operations on files and collections of files. It is used in this script to move files from one directory to another (`shutil.move()`).

4. `schedule` : This is an in-process scheduler for periodic jobs that uses the builder pattern for configuration. This script uses it to schedule the `main_pipe()` function to run every day at a specific time.

5. `time` : This is a built-in Python library for dealing with time-related tasks. While the library is imported in the script, it is not directly used in the code provided.

## Implementation

To implement this script, you would need to make sure you have the necessary permissions to access the FTP server and the directories you wish to manipulate on your local system. Make sure the FTP server address, username, password, and directories in the script are changed to match your specific requirements.

You can schedule the script to run at any specific time by changing the time in the `schedule.every().day.at("14:52").do(main_pipe)` line. The time is in 

24-hour format.

Finally, the script continuously checks if it's time to run the `main_pipe()` function and runs it when the scheduled time comes. This is done in the `main()` function using an infinite loop and the `schedule.run_pending()` method.

You would then run the script by executing it as a Python script on your system. Make sure Python and the necessary libraries (`ftplib`, `os`, `shutil`, `schedule`) are installed on your system.
'''