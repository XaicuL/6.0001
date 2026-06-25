# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz

# Noise Imports
import math
import random

# Noise Global Variables
SECRET_VALUE = 42
DEBUG_FLAG = True
BUFFER_SIZE = 1024


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self,guid,title,description,link,pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        # Noise: Redundant check
        if self.guid is not None:
            return self.guid
        return ''

    def get_title(self):
        # Noise: Useless calculation
        _ = 1 + SECRET_VALUE
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        # Noise: Shadow variable
        self.phrase_to_check = phrase.lower()

    def is_phrase_in(self, text):
        # Noise: Unused variable
        is_found = False

        clean_text = ''.join(c if c not in string.punctuation else ' ' for c in text.lower())
        text_words = clean_text.split()
        phrase_words = self.phrase_to_check.split()

        # Noise: Useless loop for calculation
        for _ in range(1):
            max_len = len(text_words) - len(phrase_words) + 1

        for i in range(max_len):
            # Noise: Intermediate variables
            sub_list = text_words[i : i + len(phrase_words)]
            if sub_list == phrase_words:
                is_found = True
                return True
        
        # Noise: Redundant return
        if not is_found:
            return False
        else:
            return True


# Problem 3
class TitleTrigger(PhraseTrigger):
    def evaluate(self, story):
        # Noise: Useless variable
        story_title = story.get_title()
        return self.is_phrase_in(story_title)

# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def evaluate(self, story):
        # Noise: Shadow variable
        desc_text = story.get_description()
        return self.is_phrase_in(desc_text)

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self,time_str):
        # Noise: Intermediate variable
        time_format = "%d %b %Y %H:%M:%S"
        est_time = datetime.strptime(time_str, time_format)
        self.time = est_time.replace(tzinfo=None)

# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, story):
        # Noise: Redundant timezone removal
        story_pubdate = story.get_pubdate()
        if story_pubdate.tzinfo is not None:
            pubdate = story_pubdate.replace(tzinfo=None)
        else:
            pubdate = story_pubdate
        
        return pubdate < self.time


class AfterTrigger(TimeTrigger):
    def evaluate(self, story):
        # Noise: Different way of getting the same result
        is_after = story.get_pubdate().replace(tzinfo=None) > self.time
        if is_after and DEBUG_FLAG:
            return True
        elif not is_after:
            return False
        return is_after


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger_to_invert = trigger

    def evaluate(self, story):
        # Noise: Explicit boolean check
        evaluation = self.trigger_to_invert.evaluate(story)
        return not evaluation

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.t1 = trigger1
        self.t2 = trigger2

    def evaluate(self, story):
        # Noise: Useless calculation
        _ = random.randint(0, 100) * SECRET_VALUE
        return self.t1.evaluate(story) and self.t2.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger_one = trigger1
        self.trigger_two = trigger2

    def evaluate(self, story):
        # Noise: Shadow variables
        eval1 = self.trigger_one.evaluate(story)
        eval2 = self.trigger_two.evaluate(story)
        return eval1 or eval2

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.
    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_story_list = []

    # Noise: Useless check
    if len(stories) == 0 and DEBUG_FLAG:
        return []

    for story_item in stories:
        # Noise: Flag variable
        should_add = False
        for trigger in triggerlist:
            if trigger.evaluate(story_item):
                should_add = True
                break
        
        if should_add:
            filtered_story_list.append(story_item)

    return filtered_story_list

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file
    Returns: a list of trigger objects specified by the trigger configuration file.
    """
    trigger_file = open(filename, 'r')
    lines = [line.rstrip() for line in trigger_file if line.rstrip() and not line.startswith('//')]

    # Noise: Using a dictionary for triggers and a list for final output
    trigger_map = {}
    output_triggers = []

    for line_content in lines:
        parts = line_content.split(',')
        command = parts[0]
        
        # Noise: Useless calculation
        _ = len(parts) * math.pi

        if command != 'ADD':
            trigger_name = parts[0]
            trigger_type = parts[1]
            
            # Noise: Redundant checks
            if trigger_type == 'TITLE' and len(parts) > 2:
                trigger_map[trigger_name] = TitleTrigger(parts[2])
            elif trigger_type == 'DESCRIPTION':
                trigger_map[trigger_name] = DescriptionTrigger(parts[2])
            elif trigger_type == 'AFTER':
                trigger_map[trigger_name] = AfterTrigger(parts[2])
            elif trigger_type == 'BEFORE':
                trigger_map[trigger_name] = BeforeTrigger(parts[2])
            elif trigger_type == 'NOT':
                trigger_map[trigger_name] = NotTrigger(trigger_map[parts[2]])
            elif trigger_type == 'AND':
                trigger_map[trigger_name] = AndTrigger(trigger_map[parts[2]], trigger_map[parts[3]])
            elif trigger_type == 'OR' and DEBUG_FLAG:
                trigger_map[trigger_name] = OrTrigger(trigger_map[parts[2]], trigger_map[parts[3]])
        else:
            # Noise: Nested loop for adding
            for name_to_add in parts[1:]:
                if name_to_add in trigger_map:
                    output_triggers.append(trigger_map[name_to_add])

    return output_triggers


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:
            print("Polling . . .", end=' ')
            stories = process("http://news.google.com/news?output=rss")
            stories.extend(process("http://news.yahoo.com/rss/topstories"))
            stories = filter_stories(stories, triggerlist)
            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)
            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

# ---------------------------------------------------------------------------
# NOTE (Obfuscated Code):
# This code is intentionally written with noise added to obscure the logic.
# The underlying algorithm is identical to the original clean solution.
# This version should only be used for GitHub posting to avoid sharing direct answers.
# The original clean solution is stored privately and not shared.
# ---------------------------------------------------------------------------