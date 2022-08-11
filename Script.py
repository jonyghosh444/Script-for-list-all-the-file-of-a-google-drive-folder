from Google import Create_Service


CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json' #Nedd a client secret json file
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '####'   # Target Folder ID

query = f"parents = '{folder_id}'"
response = service.files().list(q=query).execute()

files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

print(files)