from web3 import Web3

etherlink_testnet_url = "https://node.ghostnet.etherlink.com/"
web3 = Web3(Web3.HTTPProvider(etherlink_testnet_url))

if web3.is_connected():
    print("Connected to Ether-Link Testnet")
else:
    print("Connection failed")
balance = web3.eth.get_balance('0xAE9919340e9963dAFebA855C13Be6d317B8b672c')
print(f"Balance: {web3.from_wei(balance, 'ether')} Ether")

contract_address = "0x37AbBA3381d74E04EA1C5a0E07688aB559b50c66"
contract_abi = [
    {
				"inputs": [],
				"stateMutability": "nonpayable",
				"type": "constructor"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "videoLink",
						"type": "string"
					}
				],
				"name": "addData",
				"outputs": [],
				"stateMutability": "payable",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "getAdminDetails",
				"outputs": [
					{
						"components": [
							{
								"internalType": "string",
								"name": "userName",
								"type": "string"
							},
							{
								"internalType": "address",
								"name": "adminAddress",
								"type": "address"
							}
						],
						"internalType": "struct CCTV.Admin[]",
						"name": "",
						"type": "tuple[]"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "owner",
				"outputs": [
					{
						"internalType": "address payable",
						"name": "",
						"type": "address"
					}
				],
				"stateMutability": "view",
				"type": "function"
			},
			{
				"inputs": [
					{
						"internalType": "string",
						"name": "_name",
						"type": "string"
					}
				],
				"name": "registerAdmin",
				"outputs": [],
				"stateMutability": "payable",
				"type": "function"
			},
			{
				"inputs": [],
				"name": "viewData",
				"outputs": [
					{
						"components": [
							{
								"internalType": "string",
								"name": "videoClip",
								"type": "string"
							},
							{
								"internalType": "uint256",
								"name": "timeStamp",
								"type": "uint256"
							}
						],
						"internalType": "struct CCTV.Video[]",
						"name": "",
						"type": "tuple[]"
					}
				],
				"stateMutability": "view",
				"type": "function"
			}
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

result = contract.functions.registerAdmin("Sumit").call()
print(f"Result: {result}")

sender_address = "0xAE9919340e9963dAFebA855C13Be6d317B8b672c"
private_key = "8c119a35b1e511d0b22288a0b1784b1b7928a82ae28a05f17bd52d660b33b75b"

nonce = web3.eth.get_transaction_count(sender_address)
gas_price = web3.to_wei('50', 'gwei')

tx = contract.functions.registerAdmin("Sumit").build_transaction({
    'chainId': 	128123,
    'gas': 2000000,
    'gasPrice': gas_price,
    'nonce': nonce
})

signed_tx = web3.eth.account.sign_transaction(tx, private_key)

tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Transaction successful with hash: {web3.to_hex(tx_hash)}")
