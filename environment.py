from os import getenv

from dotenv import load_dotenv

load_dotenv()

PROJECT_ID = getenv('PROJECT_ID')
BUCKET_NAME = getenv('BUCKET_NAME')
