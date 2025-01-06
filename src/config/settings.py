import os
from os.path import dirname
from os.path import join

from dotenv import load_dotenv

dotenv_path = join(dirname('.'), '.env')
load_dotenv(dotenv_path)

SHAREPOINT_URL = os.environ.get('SHAREPOINT_URL')
USER_CREDENTIAL = os.environ.get('USER_CREDENTIAL')
USER_PASSWORD = os.environ.get('USER_PASSWORD')

__all__ =  ['SHAREPOINT_URL', 'USER_CREDENTIAL', 'USER_PASSWORD']
