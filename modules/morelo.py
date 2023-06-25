import subprocess
from modules.timer import *
from modules.api import *
import time
import os

class Morelo():
	def __init__(self, workdir, local = True, d_url = 'http://127.0.0.1:38302', w_port = 38340):
		self.api = API()
		self.daemon = self.Daemon(local, d_url, workdir, self.api)
		self.wallet = self.Wallet(workdir, w_port, self.api)
		
	class Daemon():
		def __init__(self, local, d_url, workdir, api):
			self.api = api
			if local:
				self.process = self.run(workdir)
			
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
		
		def get_info(self):
			req1 = json.loads(self.api.daemon.sync_info())
			req2 = json.loads(self.api.daemon.get_connections())
			req3 = json.loads(self.api.daemon.get_info())
			#some shitty mixing responses json
			req1['result']['difficulty'] = 0
			target_height = 0
			if 'connections' in req2['result']:
				for conn in req2['result']['connections']:
					if conn['height'] > target_height:
						target_height = conn['height']
			req1['result']['target_height'] = target_height
			if req3:
				req1['result']['difficulty'] = req3['result']['difficulty']
			return req1
			
	class Wallet():
		def __init__(self, workdir, w_port, api):
			self.api = api
			self.proc = self.run(workdir, w_port)
			
		def run(self, workdir, w_port):
			return subprocess.Popen(os.getcwd() + '/morelo-wallet-rpc --wallet-dir "' + workdir + '" --rpc-bind-port ' + str(w_port) + ' --disable-rpc-login', stdout=subprocess.DEVNULL,  shell=True)#, creationflags = CREATE_NO_WINDOW)
		
		def open(self, file, password = ""):
			self.api.wallet.open(file, password)
			
		