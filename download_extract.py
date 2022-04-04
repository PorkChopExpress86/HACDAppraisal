from zipfile import ZipFile as zf
from load_data import load_data_to_sqlite
from datetime import datetime
import wget
import os
import glob


def download_zip(year=datetime.now().strftime("%Y")):
    '''
    Removes files from a directory and downloads the zip files needed

    Parameter
    year = '2000', default is the current year if no parameter is passed

    '''
    # remove files from Downloaded Data
    files = glob.glob('Downloaded Data/*.zip')
    for file in files:
        try:
            os.remove(file)
        except OSError as e:
            print(f"Error: {file} : {e.strerror}")

    # Download files
    wget.download(url=('https://download.hcad.org/data/CAMA/' + year + '/Real_building_land.zip'),
                  out='Downloaded Data/Real_building_land.zip')
    wget.download(url=('https://download.hcad.org/data/CAMA/' + year + '/Real_acct_owner.zip'),
                  out='Downloaded Data/Real_acct_owners.zip')


def unzip_file(file, dest):
    '''
    Unzip a *.zip file to the destination directory

    Parameters
    file= string of file path, ex. 'Download.zip'
    dest= string of directory path, ex. 'Data/'

    '''
    file_list = ['land.txt', 'building_res.txt', 'real_acct.txt']

    with zf(file, 'r') as zip_obj:
        list_of_file_names = zip_obj.namelist()

        for file_name in list_of_file_names:
            if file_name in file_list:
                zip_obj.extract(file_name, dest)


if __name__ == '__main__':
    # Download files
    download_zip()

    # Extract files
    unzip_file('Downloaded Data/Real_building_land.zip', 'Data/')
    unzip_file('Downloaded Data/Real_acct_owners.zip', 'Data/')

    load_data_to_sqlite()
