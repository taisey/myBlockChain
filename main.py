import module.blockchain as bc

#ブロックを1つ作成
def test1():
	myBC = bc.BlockChain()

	#ブロックを作成
	myBlock = myBC.make_new_block()
	myBlock.transactions = "hello world"
	myBlock.name = "Block1"

	
	#マイニング 前
	print("\nbefore mining")
	myBC.view(myBlock)
	print("validation:", myBC.validation(myBlock))
	#ブロックのPOWをマイニング 
	myBC.set_correct_pow(myBlock)
	#POWが正しいか確認
	print("\nafter mining")
	myBC.view(myBlock)
	#POWが正しいか確認
	print("validation:", myBC.validation(myBlock))

	print("\nblock hash:",myBC.get_hash_by_block(myBlock))

def test2():
	myBC = bc.BlockChain()

	#ブロック1を作成
	myBlock1 = myBC.make_new_block()
	myBlock1.transactions = "hello world"
	myBlock1.name = "Block1"

	#ブロック2を作成
	myBlock2 = myBC.make_new_block()
	myBlock2.transactions = "goobye world"
	myBlock2.name = "Block2"	

	#ブロック1のマイニング 
	myBC.set_correct_pow(myBlock1)
	myBC.view(myBlock1)

	myBC.connect_blocks(myBlock2, myBlock1)
	myBC.view(myBlock2)
	

if __name__ == '__main__':
	print("***"* 10, "test1", "***"* 10)
	test1()
	print("\n\n\n\n")


	print("***"* 10, "test2", "***"* 10)
	test2()
	print("\n\n\n\n")

