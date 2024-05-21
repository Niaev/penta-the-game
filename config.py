# General imports
import os

# Environment variables stuff
from dotenv import load_dotenv
load_dotenv()

env = os.getenv

# Server stuff
PROTOCOL=env('PROTOCOL')
HOST=env('HOST')
PORT=env('PORT')

# Project root folder
CWDIR=env('CWDIR')

# Development stuff
DEBUG=bool(env('DEBUG'))