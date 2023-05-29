from ftplib import FTP
import os

address = 'ftp.ncei.noaa.gov'

ftp = FTP(address)
ftp.login()

#ftp.dir()
#ftp.retrlines('LIST')

#change directory. Here, we have files to download!
ftp.cwd('/pub/data/cdo/samples/')

# Get list of files in the remote directory
file_list = ftp.nlst()

local_dir = r'C:\Users\migue\Documents\Brainnest_python\ftp_data'

if os.path.isdir(local_dir):
    print("Directory exists.")
else:
    os.makedirs(local_dir)
    print("Directory created.")

# Iterate through the files and download them
for file in file_list:
    local_filepath = os.path.join(local_dir, file)
    try:
        with open(local_filepath, 'wb') as local_file:
            ftp.retrbinary('RETR ' + file, local_file.write, 1024)
            print(f"Downloaded {file}")
    except Exception as e:
        print(f"Failed to download {file}. Reason: {e}")
'''
This line uses the FTP retrbinary() method to retrieve the contents of the remote file specified by 'RETR ' + filename 
and write it to the local_file using the write() method. The 'RETR ' prefix is used to specify the FTP command to retrieve 
the file.
'''

ftp.quit()