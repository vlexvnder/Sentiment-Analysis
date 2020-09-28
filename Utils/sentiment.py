class Sentiment:
  response = {}
  sentences = {}
  ConfidenceScores = {}
  sentiment = ""

  def __init__(self, response):
    self.response = response
    self.sentences = response['documents'][0]['sentences']
    self.confidenceScores= response['documents'][0]['confidenceScores']
    self.sentiment = response['documents'][0]['sentiment']
  
  def getSentence(self, n):
    return Sentence(self.sentences[n])

class Sentence:
  response = {}
  sentiment = ""
  confidenceScores = {}
  offset = ""
  length = 0
  text = ""
  def __init__(self, response):
    self.response=response
    self.sentiment = response['sentiment']
    self.confidenceScores=response['confidenceScores']
    self.offset=response['offset']
    self.length = response['length']
    self.text = response['text']
  def __str__(self):
     return str(self.response)


  



    