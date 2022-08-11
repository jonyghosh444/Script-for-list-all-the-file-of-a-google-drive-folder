from Google import Create_Service


CLIENT_SECRET_FILE = 'Json File'  #Need a client secret json file
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = 'Target Folder Id'  #Target Folder ID

query = f"parents = '{folder_id}'"
response = service.files().list(q=query).execute()

files = response.get('files')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = service.files().list(q=query).execute()
    files.extend(response.get('files'))
    nextPageToken = response.get('nextPageToken')

print(files)

for i in files:
    print(i['name'])