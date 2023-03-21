import requests

r = requests.get('')
print(r.json().get('result')[-1].get('message').get('text'))
text = r.json().get('result')[-1].get('message').get('text')


AUTH_TOKEN = ''
import gistyc



file_name_txt = 'file.txt'
# text = 'teste555!\n'

with open(file_name_txt, 'a') as f:
    f.write(text)


gist_api = gistyc.GISTyc(auth_token=AUTH_TOKEN)
# response_data = gist_api.create_gist(file_name=file_name_txt)


gist_list = gist_api.get_gists()
for gist in gist_list:
    file_name_gist = list(gist.get('files').keys())[0]
    if file_name_gist == file_name_txt:
        response_update_data = gist_api.update_gist(file_name=file_name_txt, gist_id=gist.get('id'))
        print(gist.get('id'))
        print('ok')


