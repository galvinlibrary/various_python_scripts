import requests

batch = 1
offset = 0
api_call = ('https://eit.ebscohost.com/Services/SearchService.asmx/Search?prof=s8989826.main.eitws&pwd=ebs5056&query=JN+Journal+of+Marketing&db=bth&numrec=200')
save_dir = ('C:\\Users\\tfluhr\\Desktop\\pquest_jm\\')


while offset <= 10200:
    off_plus = offset + 1
    call = (api_call  + '&startrec=' + str(off_plus))
    print('batch ' + str(batch))
    print('offset ' + str(offset))
    batch+=1
    offset = offset + 200
    
    write_url = (save_dir + str(batch) + '.xml' )
    print(write_url)
    
    response = requests.get(call)
    with open(write_url, 'wb') as file:
        file.write(response.content)
    
