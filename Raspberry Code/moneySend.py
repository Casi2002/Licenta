from appwrite.client import Client
from appwrite.services.users import Database
from hx import *

client = Client()
(client
    .set_endpoint('https://cloud.appwrite.io/v1')
    .set_project('667383840019dae936a2') 
    .setPlatform('com.BachelorDegree.SmartSafe')
)
# Initialize the Database service
database = Database(client)

def main_money():
    money = get_weight(offset, reference_unit)/6.1

    result = database.create_document(
        collection_id='66784de500356f421ce3', # Your collection ID
        document_id='unique()', # Unique document ID or use 'unique()' for a new one
        data=money
    )