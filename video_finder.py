import argparse
import os


from youtube_transcript_api import YouTubeTranscriptApi
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 

def extract_captions(video_id):

    srt = YouTubeTranscriptApi.get_transcript(video_id)

    captions = ""
    # timings = []
    # count = 0
    # dict_idx = [] 
    for i in srt:
        captions = captions + " "+ i["text"]
        # dict_idx.append[count]
        # count+=1
        # timings.append( [ i["start"] , i["start"]+i["end"] )

    return captions#,timings


def youtube_query(args):

    #path = r"./"
    #dst = os.path.join(path,path,"test.wav")

    video_id = str(args.url)  ##"VUoDXPlBNEU&t=119s"

    video_id = video_id[ video_id.find("=")+1 : ]

    captions = extract_captions(video_id)

    print(len(captions))    

    tokens = word_tokenize(captions)

    key_words = str(args.keys).split(",")

    if(len(key_words) == 0 or args.keys == None):
        print("Please given some key words/ queries to help you find the video")
        return False
    
    lemmatizer = WordNetLemmatizer() 

    for token in tokens:
        token =  lemmatizer.lemmatize(token) 

    for word in key_words:
        word = lemmatizer.lemmatize(word) 

    print(tokens[:50])

    print(key_words)
    queries = key_words.copy()
    count = 0
    for token in tokens:
        if token in queries:
            count+=1
            queries.remove(token)

    if(count==len(key_words)):
        print("This is your Video")

    return True

def main():

    # Initiate the parser
    parser = argparse.ArgumentParser()
    
    parser.add_argument("-t", "--type", 
                        help="Select the type of input - 1 for youtube, 2 for file in the browser/drive")
    parser.add_argument("-u", "--url", help="provide the URL for youtube video")
    parser.add_argument("-k", "--keys", help="provide the queries/ key_words that you are looking for")
    
    # Read arguments from the command line
    args = parser.parse_args()

    print("type: ",args.type)
    print("url: ",args.url)
    print("keys: ",args.keys)

    #if(args.type == "1"):
    youtube_query(args)

    return True
    #else:
        #call folder.py


if __name__ == "__main__":
    a = main()
    if(a):
        print("Done")

else:
    print("Not Executed")
