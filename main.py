import module.blockchain as bc

def test():
	myBC = bc.BlockChain()

	#ブロックを作成
	myBlock = myBC.make_new_block()
	myBlock.log = "hello world"

	myBC = bc.BlockChain()
	
	#ブロックのPOWをマイニング 
	myBC.mining(myBlock)

	print("POW:", myBlock.pow)

	#POWが正しいか確認
	print("validation:", myBC.validation(myBlock))

	myBC.view(myBlock)
if __name__ == '__main__':
	test()
