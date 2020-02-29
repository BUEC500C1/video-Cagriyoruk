import pytest
from TweetToVideo import *

def test_TTV():
  assert VideoSummary('eys',['lexfridman']) != None
