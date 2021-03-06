import tweepy
import queue
import multiprocessing
import threading
import configparser
import ffmpeg
from PIL import Image
from PIL import ImageDraw
import os
import ffmpeg
import glob
import json

class VideoSummary:

  # Initialize the Object
  def __init__(self,path, process_list):
    self.process_list = process_list
    self.api = self.authentication(path)
    self.que = queue.Queue()
    self.threads = []
    self.thread_amount = 4
    self.threadProcess(process_list)

  # Get the API Calls
  def threadProcess(self, process_list):
    for each in process_list:
      self.que.put(each)
    for i in range(self.thread_amount):
      t = threading.Thread(target = self.processor())
      t.daemon = True
      t.start()
    # Block until all tasks are done
    print('Job is Finished!!!')
    self.que.join()
    for i in range(self.thread_amount):
        self.que.put(None)
    for t in self.threads:
        t.join()

  # Process the calls
  def processor(self):
    while True:
      element = self.que.get()
      if element is None:
        print('Queue is Empty!!!')
        break
      self.getTweets(element)
      self.que.task_done()
      print('Processing the ' + str(self.process_list.index(element) + 1) + ' element out of ' + str(len(self.process_list)) + ' items')

  # Start the authentication process
  def authentication(self,path):
    if not os.path.exists(path):
      return None
    else:   
      config = configparser.ConfigParser()
      config.read(path)
      auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(),
                                 config.get('auth', 'consumer_secret').strip())
      auth.set_access_token(config.get('auth', 'access_token').strip(),
                            config.get('auth', 'access_secret').strip())
      api = tweepy.API(auth)
    return api

  # Get tweets from a specific user handle
  def getTweets(self,user_handle):
    temp = {}
    counter = 0
    tweet_list = []
    if self.api == None:
      return self.go_stub(user_handle)
    tweets = self.api.user_timeline(id = user_handle, count = 30)
    for tweet in reversed(tweets):
      for character in tweet.text:
        if ord(character) > 256:
          tweet.text = tweet.text.replace(character, " ")
      tweet = tweet.user.name + "\n" + tweet.text 
      if user_handle in temp:
        temp[user_handle] += [tweet]
      else:
        temp[user_handle] = []
      tweet_list.append(tweet)
    with open(user_handle, 'w+') as outfile:
      json.dump(temp, outfile)
    return self.text2Image(tweet_list,counter,user_handle)

  def go_stub(self,user_handle):
    with open(user_handle) as json_file:
      data = json.load(json_file)
      return data[user_handle]
    
  # Parse and convert the text to images
  def text2Image(self,tweet_list,counter,user_handle):
    if not os.path.isdir(user_handle + '_tweets'):
      os.mkdir(user_handle + '_tweets')
    while counter < len(tweet_list):
      pre_image = Image.new(mode = 'RGB', size = (960,540), color = (138,43,226))
      image = ImageDraw.Draw(pre_image)
      image.text((20,220), tweet_list[counter], fill = (255,255,255))
      fileName = user_handle + '_tweets/'+ user_handle + str(counter) + '.png'
      pre_image.save(fileName)
      counter += 1
    return self.image2Video(user_handle)

  # Merge all images to create a video
  def image2Video(self,user_handle):
    if not os.path.isdir('VideoSummary'):
      os.mkdir('VideoSummary')
    fileName = os.getcwd() + '/' + user_handle + '_tweets/' + '*.png'
    videoName = 'VideoSummary/' + user_handle + '_daliy.mp4'
    ffmpeg.input(fileName, pattern_type = 'glob', framerate = 0.3).output(videoName).run()

def main():
  letsPlay = VideoSummary('kys',['lexfridman'])

if __name__ == '__main__':
  main()
