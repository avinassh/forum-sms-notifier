forum-sms-notifier
==================

Sends sms notification whenever you receive a new Private Message on your favorite forum!

Instructions :
  - Currently this supports only forums running with Xenforo. And also requires little manual effort also. Yeah, that sucks.
  - Visit your favourite Xenforo forum and find out the login page. Something like this : http://xenforo.com/community/login
  - Or it could be http://example.com/login
  - Make note of that URL, copy it somewhere and remove the trailing '/login' part. So your URL mostly could be http://example.com/community for former case or just http://example.com/login for latter. I know this is boring, till I figure out some better way.
  - Now you need a account on http://fullonsms.com. Using this service you are gonna recieve sms alerts.
  - Open up config.py in your favorite text editor. Enter all the data. Don't worry, I am not sending these data to NSA.
  - That'all!

How to :
  - So everytime you run the sendMeSMSonPM.py it checks for unread private messages on the forum and sends you a sms.

Note :
  - This a stateless script, so everytime the script is run it will send you an alert for every unread messages.
  - As of now you will just receive the name of the sender.


Future plans : 
  - Make more readable code with comments and stuff
  - Lil conversation description in the SMS.
  - Errors and exceptions handling
  - Ability to add more than one forum
  - To support various types of forum softwares (vBulletin and myBB next!)
  - Fallback if one sms provider fails
  - Better way of specifying frequency to check for new private message
  - Persistance. So that you don't keep on getting alerts for unread messages.

Known bugs :
  - None as of now. Sweet.
  
  
  
