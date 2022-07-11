import module.blockchain as bc

def test():
	#ブロックを作成
	myBlock = bc.Block()
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
