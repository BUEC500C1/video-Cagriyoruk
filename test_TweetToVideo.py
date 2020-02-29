import pytest
from TweetToVideo import *

def test_TTV():
  assert VideoSummary('eys',['lexfridman']) != None
  assert VideoSummary('keys'['lexfridman', 'elonmusk', 'jomaoppa']) != None
  with pytest.raises(FileNotFoundError):
    assert VideoSummary('ky', ['fileNotFound'])

def main():
  test_TTV()

if __name__ == '__main__':
  main()