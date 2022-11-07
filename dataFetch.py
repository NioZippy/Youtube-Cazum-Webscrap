import scrapetube
import json
#UC9-y-6csu5WGm29I7JiwpnA
#
videos = scrapetube.get_channel("UC0E9-appMl_mwjPVzdB3qZw")

datas = []

i = 0;

for video in videos:
    i += 1

    print(i)

    url = "https://www.youtube.com/watch?v=" + video["videoId"]
    titulo = video["title"]["runs"][0]["text"]
    time = video["publishedTimeText"]["simpleText"]
    duracao = video["lengthText"]["simpleText"]
    thumbnail = video["thumbnail"]["thumbnails"][3]["url"]
    views = video["shortViewCountText"]["simpleText"]
    
    data = {"titulo" : titulo, "url" : url, "thumb" : thumbnail, "duracao" : duracao, "views" : views, "dataPublicacao" : time}

    datas.append(data)

json_object = json.dumps(datas, indent=4)

# Writing to sample.json
with open("videos_data.json", "w") as outfile:
    outfile.write(json_object)