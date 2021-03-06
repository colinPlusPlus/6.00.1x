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
        text = text.lower().replace("'", " ").strip(punctuation)
        text = text.split()
        text = sorted(text)
        mid = len(text)/2
        
        while(True):
            if text == []:
                return False
            elif self.word == text[mid].strip(punctuation): 
                return True
            elif text[mid].strip(punctuation) > self.word:
                text = text[:mid]
                mid = len(text[:mid])/2
            else:
                text = text[mid+1:]
                mid = len(text[mid:])/2
                
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        story = story.getTitle()
        return self.isWordIn(story)
            
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        story = story.getSubject()
        return self.isWordIn(story)

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        story = story.getSummary()
        return self.isWordIn(story)                
        
# Composite Triggers
# Problems 6-8

class NotTrigger(Trigger):
    def __init__(self, trig):
        self.trig = trig
    
    def evaluate(self, story):
        story = self.trig.evaluate(story)
        if story == True:
            return False
        else:
            return True

class AndTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
    
    def evaluate(self, story):
        story1 = self.trig1.evaluate(story)
        story2 = self.trig2.evaluate(story)
        if story1 == True and story2 == True:
            return True
        else:
            return False

class OrTrigger(Trigger):
    def __init__(self, trig1, trig2):
        self.trig1 = trig1
        self.trig2 = trig2
    
    def evaluate(self, story):
        story1 = self.trig1.evaluate(story)
        story2 = self.trig2.evaluate(story)
        if story1 == True or story2 == True:
            return True
        else:
            return False

# Phrase Trigger
# Question 9

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase
    
    def evaluate(self, story):
        if self.phrase in story.getTitle():
            return True
        elif self.phrase in story.getSubject():
            return True
        elif self.phrase in story.getSummary():
            return True
        else:
            return False

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    
    print triggerMap
    print params
    print name
    if triggerType == 'TITLE':
        triggerMap[name] = TitleTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'SUBJECT':
        triggerMap[name] = SubjectTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'SUMMARY':
        triggerMap[name] = SummaryTrigger(' '.join(params))
        return triggerMap[name]
    elif triggerType == 'PHRASE':
        triggerMap[name] = PhraseTrigger(' '.join(params))
        return triggerMap[name] 
    elif triggerType == 'AND':
        triggerMap[name] = AndTrigger(triggerMap[params[0]] ,triggerMap[params[1]])
        return triggerMap[name]
    elif triggerType == 'OR':
        triggerMap[name] = OrTrigger(triggerMap[params[0]] ,triggerMap[params[1]])
        return triggerMap[name]
    elif triggerType == 'NOT':
            triggerMap[name] = OrTrigger(triggerMap[params[0]])
            return triggerMap[name]
        
    
        
        
    
def readTriggerConfig():
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open("/Users/newuser/Documents/6.00/ProblemSet7/triggers.txt", "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers