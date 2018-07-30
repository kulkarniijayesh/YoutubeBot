#Youtube API Communicator
import requests;
print("---------------Youtube API Communicator---------------");

#Global variables
videoDb = list();
apiKey = 'AIzaSyCfTwWBCtd3yCKtkyKHecDEhgZxBZsk4Qk';
videoId = 'A1Qj7mlZ0xE';

#Youtube API : youtube.search.list - Get similar videos based on video id
def GetSimilarVideos(videoId):

    url = '''https://www.googleapis.com/youtube/v3/search?
    part=snippet&maxResults=25&relatedToVideoId='''+videoId+'''&relevanceLanguage=hi&type=video&videoCategoryId=10&key='''+apiKey;

    response = requests.get(url,params=[['part','snippet']]);
    return response.json();

json = GetSimilarVideos(videoId);

for i in range(25):
    videoDb.insert(i,
                   {'id': json["items"][i]["id"]["videoId"],
                    'title': json["items"][i]["snippet"]["title"],
                    'channelTitle': json["items"][i]["snippet"]["channelTitle"],
                    'liked':0,
                    'played':0
                   });

