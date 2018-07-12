"""Pushover API Notification provider."""
from config import config
import requests


class NotificationProvider:
	"""Notification Provider class."""
	
	def __init__(self):
		self.data = {
			'token': config.PUSHOVER_TOKEN, 
			'user': config.PUSHOVER_USER_KEY
		}
	
	def send_message(self, message: str, attachment=None, device=None, title=None, 
					 url=None, url_title=None, priority=None, sound=None, timestamp=None):
		"""
		Method to send a notification via Pushover API.
		
		:param message: 		Message you want to display in notification body.
		:param attachment: 		Binary image attachment.
		:param device: 			Parameter to send to specific device or set on devices (Separated with comma).
		:param title: 			Title you want to display in notification header instead of Application Name.
		:param url: 			Supplementary URL with message.
		:param url_title: 		Supplementary URL label.
		:param priority:		Notification priority.
		:param sound: 			Name of official Pushover notification sounds.
		:param timestamp: 		UNIX Timestamp at what time to display the notification.
		"""
		self.data.update({'message': message})
		if attachment:
			self.data.update({'attachment': attachment})
		if device:
			self.data.update({'device': device})
		if title:
			self.data.update({'title': title})
		if url:
			self.data.update({'url': url})
		if url_title:
			self.data.update({'url_title': url_title})
		if priority:
			self.data.update({'priority': priority})
		if sound:
			self.data.update({'sound': sound})
		if timestamp:
			self.data.update({'timestamp': timestamp})
		
		req = requests.post(config.PUSHOVER_API_ENDPOINT, data=self.data)
		return req.status_code == requests.codes.ok
