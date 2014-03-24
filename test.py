''' def isWordIn(self, text):
        punctuation = string.punctuation
        text = text.lower()
        text = text.split()
        for i in text:
            if "'" in i.strip(punctuation):
                i = i[:-1].replace("'", '')
            if self.word == i.strip(punctuation):
                return True
        return False'''
import string

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
        
    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title
    
    def getSubject(self):
        return self.subject
    
    def getSummary(self):
        return self.summary
    
    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()
    
    def isWordIn(self, text):
        punctuation = string.punctuation
        text = text.lower()
        text = text.replace("'", " ")
        text = text.strip(punctuation)
        text = text.split()
        
        text = sorted(text)
        mid = len(text)/2
        
        while(True):
            print text
            if text == []:
                return False
            elif self.word == text[mid].strip(punctuation): 
                return True
            elif text[mid] > self.word:
                mid = len(text[:mid])/2
                text = text[:mid-1]
            else:
                
                mid = len(text[mid:])/2
                text = text[mid+1:]
            
        
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        story = story.getTitle()
        return self.isWordIn(story)
            
koala     = NewsStory('', 'Koala bears are soft and cuddly', '', '', '')
pillow    = NewsStory('', 'I prefer pillows that are soft.', '', '', '')
soda      = NewsStory('', 'Soft drinks are great', '', '', '')
pink      = NewsStory('', "Soft's the new pink!", '', '', '')
football  = NewsStory('', '"Soft!" he exclaimed as he threw the football', '', '', '')
microsoft = NewsStory('', 'Microsoft announced today that pillows are bad', '', '', '')
nothing   = NewsStory('', 'Reuters reports something really boring', '', '' ,'')
caps      = NewsStory('', 'soft things are soft', '', '', '')