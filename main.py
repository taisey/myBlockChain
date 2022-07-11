import module.blockchain as bc

def test():
	myBlock = bc.Block()
	myBlock.log = "hello world"

	myBC = bc.BlockChain(myBlock)
	myBC.mining()
	print("mining run:", myBC.block.pow)
	myBC.validation()
	print("validation:", myBC.validation())

	myBC.view()
if __name__ == '__main__':
	test()
