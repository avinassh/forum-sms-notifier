#! /usr/bin/python2.7

import os
import sys
import time
import requests
from requests import session
import re
from bs4 import BeautifulSoup
from config import *

def sendSMS(pmAuthor):
	fosLogin = 'http://fullonsms.com/login.php' #fos = full on SMS >.<
	fosPost = 'http://fullonsms.com/home.php'
	payload = { 
				"MobileNoLogin" : myFullOnSMSUserName, 
				"LoginPassword" : myFullOnSMSPassword 
	}
	smsText = 'You have a PM from '+pmAuthor+'!'
	with session() as sms:
	    sms.post(fosLogin, data=payload)
	    payload = {
	    			'MobileNos' : myMobileNo,
	    			'Message' : smsText
	    }
	    sms.post(fosPost,data=payload)

def processConvoPage(convoPage):
	soup = BeautifulSoup(convoPage)
	unreadPMs = soup.find_all('li', class_='unread')
	if len(unreadPMs) == 0:
		print 'no new sms'
		sys.exit()
	for pm in unreadPMs:	
		sendSMS(str(pm['data-author']))
		time.sleep(5)

def forumScrappy():
	forumLogin = forumLink+'/login/login'
	forumConvoPage = forumLink+'/conversations/'
	payload = { 
				'login': myForumUserName,
				'password': myForumPassword
	}
	with session() as forum:
	    forum.post(forumLogin, data=payload)
	    forumConversations = forum.get(forumConvoPage).text
	    processConvoPage(forumConversations)

if __name__ == "__main__":
	forumScrappy()