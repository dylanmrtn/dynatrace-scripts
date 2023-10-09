import requests
import json

#-------Define Variables
env=""
token=""
entitySelector="type(PROCESS_GROUP),tag(dotnet)"
schema=""
value = ''

# Run the script to get the entities and apply the settings
def main():
    entities=getEntityIds(entitySelector)
    if( len(entities) < 1):
        print('no entities found')
        return
    
    print('Applying ' + schema + ' changes to ' + str(len(entities)) + ' entities.')
    applySettings(entities)

# Get the list of entity Ids based on the provided entitySelector
def getEntityIds(entitySelector):
    url=env + '/api/v2/entities' + '?entitySelector='+ entitySelector + '&Api-Token=' + token
    response=requests.get(url)
    data = json.loads(response.content)
    entities_list= []

    for i in data['entities']:
        entities_list.append(i['entityId'])

    return entities_list

# Apply the settings object provided to each entity in list
def applySettings(entities):

    url= env + '/api/v2/settings/objects' + '?Api-Token=' + token
    headers = {'content-type': 'application/json'}
    success = 0
    fail = 0
    for i in entities:
        response=requests.post(url,data=setRequestBody(i),headers=headers)
        if (response.status_code == 200):
            success += 1
        else:
            fail += 1
    print('Settings applied successfully for ' + str(success) + ' entities. ' + str(fail) + ' failures.')

# Set the settings object request body using the entity ID  
def setRequestBody(entityId):
    
    body={
    "schemaId": schema,
    "scope": entityId,
    "value": json.loads(value)
    }
    
    return "["+json.dumps(body)+"]"

# Initialize script
if __name__ == "__main__":
    main()