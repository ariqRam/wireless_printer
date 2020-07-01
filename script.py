from __future__ import print_function
import pickle
import os
import sys
import base64
import urllib.request
import time
from apiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#Pinging Google
def is_connected(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False
#connecting to the internet before running the API requests
print("connecting to the internet", end="")
while not is_connected():
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.2)
    
print("internet connected successfully")

creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        #define SCOPES, the Gmail API scope that is to be accessed.
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

SERVICE = build('gmail', 'v1', credentials=creds)

def ListMessagesMatchingQuery(service, user_id, query='', max_results = 1):
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query, maxResults = max_results).execute()
    messages = []
    if not 'messages' in response:
      return 0
    else:
      messages.extend(response['messages'])
    print('message list created')
    print(messages)
    return messages
  except (errors.HttpError, error):
    print('An error occurred: %s' % error)

def GetMessage(service, user_id, msg_id):
  print('getting message...')
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    print('message returned')
    return message
  except (errors.HttpError, error):
    print('An error occurred: %s' % error)

def ModifyMessage(service, user_id, msg_id, msg_labels):
  print("modifying messages...")
  try:
    message = service.users().messages().modify(userId=user_id, id=msg_id,
                                                body=msg_labels).execute()

    label_ids = message['labelIds']

    print('   Message ID: %s - With Label IDs %s' % (msg_id, label_ids))
    return message
  except (errors.HttpError, error):
    print('   An error occurred: %s' % error)

def GetAttachments(service, user_id, msg_id, store_dir):
  print("getting attachments...")
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    for part in message['payload']['parts']:
      if part['filename']:
        if 'data' in part['body']:
            data = part['body']['data']
        else:
            att_id = part['body']['attachmentId']
            att = service.users().messages().attachments().get(userId=user_id, messageId=msg_id,id=att_id).execute()
            data = att['data']

        file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))

        path = ''.join([store_dir, part['filename']])
        print('Saving %s...' %path)
        with open(path, 'wb') as f:
            f.write(file_data)
        print('File saved in %s' %path)
        os.system("lowriter -p %s" % path)
        print('%s printed successfully' %part['filename'])
  except (errors.HttpError, error):
    print('An error occurred: %s' % error)

emailNotFound = True

print('matching query...')
print("Waiting for the email", end="")
#Keep looking for unread emails with the matching subject
while emailNotFound:
  #define PASSWORD, the email subject that the API looks for
  msg = ListMessagesMatchingQuery(SERVICE, "me", query=PASSWORD + " is:unread")
  if not msg == 0:
    emailNotFound = False
    print("Email found")
  sys.stdout.write(".")
  sys.stdout.flush()
  time.sleep(0.2)
  
#the message id    
threadId = msg[0]['threadId']

print("   threadId : %s" % threadId)

#getting the email
email = GetMessage(SERVICE, 'me', threadId)

print("   message : %s" % email["snippet"])


msg_label = {
  "removeLabelIds": [
      "UNREAD"
  ],
  "addLabelIds" : [
      
  ],
}
#changing the "unread" label to "read"
modified_msg = ModifyMessage(SERVICE, 'me', threadId, msg_label)

#define ATTACHMENT_DIR, in which the computer saves the attachment.
GetAttachments(SERVICE, "me", threadId, ATTACHMENT_DIR)

os.system("python3 script.py")
