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