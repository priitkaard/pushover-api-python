from lib.notification_provider import NotificationProvider

if __name__ == '__main__':
	np = NotificationProvider()
	print(np.send_message('test message', title='My App', url='www.google.com', url_title='Go to Google'))
