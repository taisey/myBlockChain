import hashlib

DEBUG = 0
class Block:
	def __init__(self):
		self.id = 1
		self.log = ""
		#Proof of Work
		self.pow = "Not Registerd"

class BlockChain(Block):
	def __init__(self, block):
		self.digit = 3
		self.block = block
		self.mining_limit = 100000
	
	def sha256(self, target):
		target_hash = str(hashlib.sha256(target.encode('utf-8')).hexdigest())
		return target_hash
	
	def check_hash(self, target_hash):
		required_head = "0" * self.digit
		return target_hash.startswith(required_head)
	
	def make_target_hash(self, id, log, pow):
		target = str(id) + str(log) + str(pow)
		target_hash = self.sha256(target)
		return target_hash

	def make_pow(self, id, log):
		mining_limit = self.mining_limit
		for i in range(mining_limit):
			target_hash = self.make_target_hash(id, log, i)
			if(DEBUG):
				print("target_hash {:<3}: {}".format(i, target_hash))
			if(self.check_hash(target_hash)):
				return i
		
	def mining(self):
		block = self.block
		id = block.id
		log = block.log
		pow = self.make_pow(id, log)
		block.pow = pow
	
	def validation(self):
		block = self.block
		id = block.id
		log = block.log
		pow = block.pow
		target_hash = self.make_target_hash(id, log, pow)
		valid_f = self.check_hash(target_hash)
		return valid_f

	def view(self):
		block = self.block
		id = block.id
		log = block.log
		pow = block.pow
		print("--------------------------------------")
		print("|{:<12}:{:>20}   |".format("id", id))
		print("|{:<12}:{:>20}   |".format("log", log))
		print("|{:<12}:{:>20}   |".format("pow", pow))
		print("--------------------------------------")
