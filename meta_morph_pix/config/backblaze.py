import os

from dotenv import load_dotenv
load_dotenv()

application_key_id = os.getenv('B2_APPLICATION_KEY_ID')
application_key = os.getenv('B2_APPLICATION_KEY')
bucket_name = os.getenv("B2_BUCKET_NAME")
