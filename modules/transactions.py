class Transactions():
	def __init__(self):
		self.transactions = []
		
	def add(self, tx):
		self.transactions.append(self.Transaction(tx))
		
	def get(self, txid):
		for tx in self.transactions:
			if tx['txid'] == txid:
				return tx
		return False
		
	def remove(self, txid):
		for tx in self.transactions:
			if tx['txid'] == txid:
				self.transactions.remove(tx)
		
	class Transaction():
		def __init__(self, data):
			self.data = data
			
		def get_hash(self):
			return self.data['result']['txid']
			
		def get_transfers(self):
			return self.data['result']['transfers']
		
		def get_transfer(self, i):
			return self.data['result']['transfers'][i]
			
		def get_fee(self):
			fee = 0
			for fee in self.data['result']['transfers']:
				fee += fee['fee']
			
		def get_amount(self):
			amount = 0
			for transfer in self.data['result']['transfers']:
				if transfer['type'] == 'in':
					amount += transfer['amount']
				elif transfer['type'] == 'out':
					amount -= transfer['amount']
			return amount
		