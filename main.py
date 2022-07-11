import module.blockchain as bc

def test():
	myBC = bc.BlockChain()

	#ブロックを作成
	myBlock = myBC.make_new_block()
	myBlock.log = "hello world"

	myBC = bc.BlockChain()
	
	#マイニング 前
	print("\nbefore mining")
	myBC.view(myBlock)
	print("validation:", myBC.validation(myBlock))
	#ブロックのPOWをマイニング 
	myBC.mining(myBlock)
	#POWが正しいか確認
	print("\nafter mining")
	myBC.view(myBlock)
	#POWが正しいか確認
	print("validation:", myBC.validation(myBlock))

	print("\nblock hash:",myBC.get_hash_by_block(myBlock))

if __name__ == '__main__':
	test()
