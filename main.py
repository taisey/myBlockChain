import module.blockchain as bc

def test():
	#ブロックを作成
	myBlock = bc.Block()
	myBlock.log = "hello world"


	myBC = bc.BlockChain(myBlock)
	
	#ブロックをマイニング 
	myBC.mining()

	print("POW:", myBC.block.pow)

	#POWが正しいか確認
	myBC.validation()
	print("validation:", myBC.validation())

	myBC.view()
if __name__ == '__main__':
	test()
