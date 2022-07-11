import hashlib
import uuid

DEBUG = 0
class Block:
	def __init__(self):
		self.id = str(uuid.uuid4())
		self.log = ""
		#Proof of Work
		self.pow = "Not Registered"
		self.prev_hash = "Not Registered"
		
		#表示用
		self.name = "None"

class BlockChain(Block):
	def __init__(self):
		self.digit = 4
		self.mining_limit = 1000000
	
	def make_new_block(self):
		return Block()
	
	def sha256(self, target):
		target_hash = str(hashlib.sha256(target.encode('utf-8')).hexdigest())
		return target_hash
	
	def check_hash(self, target_hash):
		required_head = "0" * self.digit
		return target_hash.startswith(required_head)
	
	def get_hash_by_param(self, id, log, prev_hash, pow):
		target_str = str(id) + str(log) + str(prev_hash) + str(pow)
		target_hash = self.sha256(target_str)
		return target_hash

	def make_pow(self, block):
		id = block.id
		log = block.log
		prev_hash = block.prev_hash

		init_pow = 0
		init_target_hash = self.get_hash_by_param(id, log, prev_hash, init_pow)		
		
		pow = init_pow
		target_hash = init_target_hash

		while(not self.check_hash(target_hash)):
			target_hash = self.get_hash_by_param(id, log, prev_hash, pow)
			if(DEBUG):
				print("target_hash {:<3}: {}".format(pow, target_hash))
			pow += 1
		return pow - 1
	def mining(self, block):
		pow = self.make_pow(block)
		return pow
	def set_correct_pow(self, block):
		pow = self.mining(block)
		block.pow = pow
	
	def validation(self, block):
		id = block.id
		log = block.log
		pow = block.pow
		prev_hash = block.prev_hash
		target_hash = self.get_hash_by_param(id, log, prev_hash, pow)
		valid_f = self.check_hash(target_hash)
		return valid_f

	def print_column(self, name, num):
		print("|{:<12}:{:>64}   |".format(name, num))		
	def view(self, block, blockname = "None"):
		id = block.id
		log = block.log
		pow = block.pow
		name = block.name
		prev_hash = block.prev_hash
		print("-" * len("|name:{:>10}   |".format(name)))
		print("|name:{:>10}   |".format(name))

		print("-" * len("|{:<12}:{:>64}   |".format("id", id)))
		self.print_column("prev_hash", prev_hash)
		self.print_column("id", id)
		self.print_column("log", log)
		self.print_column("pow", pow)

		print("-" * len("|{:<12}:{:>64}   |".format("id", id)))

	def get_hash_by_block(self, block):
		id = block.id
		log = block.log
		pow = block.pow
		prev_hash = block.prev_hash
		hash = self.get_hash_by_param(id, log, prev_hash, pow)
		return hash

	def connect_blocks(self, dst, src):
		src_hash = self.get_hash_by_block(src)
		dst.prev_hash = src_hash
		self.set_correct_pow(dst)
		