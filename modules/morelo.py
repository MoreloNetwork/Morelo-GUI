import subprocess
from modules.timer import *
from modules.api import *
import time
import os

class Morelo():
	def __init__(self, workdir, local = True, d_url = 'http://127.0.0.1:38302', w_url = 'http://127.0.0.1:38340'):
		self.api = API()
		self.daemon = self.Daemon(local, d_url, workdir, self.api)
		#self.wallet = self.Wallet(w_url, workdir)
		
	class Daemon():
		def __init__(self, local, d_url, workdir, api):
			self.api = api
			if local:
				self.process = self.run(workdir)
			self.wait()
			
		def run(self, workdir):
			return subprocess.Popen(os.getcwd() + '/morelod --add-exclusive-node 80.60.19.222 --data-dir "' + workdir, stdout=subprocess.PIPE, shell=True)
			
		def wait(self):
			timeout = Timer()
			while timeout.get() < 15000:
				try:
					nodeInfo = self.api.daemon.get_info()
					if nodeInfo and 'result' in nodeInfo:
						return True
				except:
					pass
				time.sleep(1)
			return False
			
	#class Wallet():
		