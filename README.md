# Tweet To Video
## Main Exercise
Using the twitter feed, construct a daily video summarizing a twitter handle day.
## Process
  * Convert text into an image in a frame
  * Do a sequence of all texts and images in chronological order.
  * Display each video frame for 3 seconds

## Exercises
This exercise involves couple different concepts which are:
 * Queue's
 
![image](https://user-images.githubusercontent.com/55101879/75595723-8948e100-5a5b-11ea-822a-4f07b05317d0.png)

 * Multiprocessing and Threading
 
![image](https://user-images.githubusercontent.com/55101879/75595802-cc0ab900-5a5b-11ea-8445-a91eb18c6ae6.png)

 * FFMPEG
 
 ![image](https://user-images.githubusercontent.com/55101879/75595853-096f4680-5a5c-11ea-98c5-3fbf6f224d60.png)

## How to Use this API

The API object take 2 input arguments. The first one is the key. And the second one is the list of user_handles that we want to get the twitter feed from. The 'keys' file is the path to the api keys of the twitter.

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/With_Stub/Screenshots/How_TO.png)

The 'keys' file looks like this:

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/With_Stub/Screenshots/Auth.png)

The Keys can be obtained through tweepy api. In order to use this API, you need keys.

To be precise, we need to put user_handles in to a list. If we want to check only one person, still we need to put it into a list like ['Cagri_yoruk'].

## Examples
### Frame of a Video

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/master/Screenshots/Example.png)

### Processing the Que

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/master/Screenshots/Processing.png)

### Image Folder

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/master/Screenshots/example_images.png)

### Video Folder

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/master/Screenshots/example_video.png)

### Working Directory

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/master/Screenshots/example_wd.png)


