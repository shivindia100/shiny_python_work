# import dtenv is a module that content function to load the dotenv file we can also write
from dotenv import load_dotenv
#import dotenv
import os

#dotenv.load_dotenv()
load_dotenv()
API_KEY = os.getenv("MY_API_KEY")
# if key is not found then it returns the none

if API_KEY:
    print("API is loaded successfully")
else:
    print("API is not loaded")