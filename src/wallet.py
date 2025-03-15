import os
import orjson
from cdp import Cdp, Wallet, WalletData
from src.utils import get_env_variable

class AgentWallet:
    def __init__(self):
        self.api_key = get_env_variable("CDP_API_KEY_NAME")
        self.private_key = get_env_variable("CDP_API_KEY_PRIVATE_KEY")
        self.file_path = "./data/wallet.json"
        Cdp.configure(self.api_key, self.private_key)

    async def create_wallet(self, user_address):
        existing_data = await self._load_existing_data()
        
        for entry in existing_data:
            if entry["user_address"] == user_address:
                print(f"Wallet already exists for user address: {user_address}")
                return
        
        wallet = Wallet.create(network_id="base-sepolia")
        wallet_data = wallet.export_data()
        await self.save_wallet_data(wallet_data, user_address)
        

    async def save_wallet_data(self, wallet_data, user_address):
        wallet_data_dict = wallet_data.to_dict()
        output_data = {
            "user_address": user_address,
            "data": wallet_data_dict
        }

        existing_data = await self._load_existing_data()
        existing_data.append(output_data)
        await self._save_data(existing_data)
        print("Wallet data saved successfully.")

    async def fetch_data(self, user_address):
        existing_data = await self._load_existing_data()

        for entry in existing_data:
            if entry["user_address"] == user_address:
                wallet_data_dict = entry["data"]
                wallet_data = WalletData.from_dict(wallet_data_dict)
                wallet = Wallet.import_wallet(wallet_data)
                
                return wallet

        print(f"No wallet data found for user address: {user_address}")
        return None
    
    async def _check_address(self, user_address):
        wallet = await self.fetch_data(user_address)
        address = wallet.default_address
        return address.address_id
    
    # Fund wallet via mpc
    async def _fund_wallet(self, user_address):
        wallet = await self.fetch_data(user_address)
        faucet = wallet.faucet(asset_id='eth')
        faucet.wait()
        return faucet.transaction_hash
    
    async def _transfer(self, user_address, amount, asset_id, destination):
        wallet = await self.fetch_data(user_address)
        transaction = wallet.transfer(amount, asset_id, destination)
        transaction.wait()
        return transaction.transaction_hash
    
    async def _get_token_ca(self, asset_id):
        match asset_id:
            case "usdc":
                return "0x9a53dbaaCCbBFf2721168673aC7738422bD4d1E9"
            case "uni":
                return "0x40199Df02e052bE29bBf289FbB7717CD0BE8eE80"
            case "weth":
                return "0x0D36746783656989F8D7c03F6bFB80910D32f778"
            case "usdt":
                return "0xe7ba244c2597ADA3e6181577b9758c90f5802F13"
            case "dai":
                return "0xDb5B12196f4195DB9f0a03536CCb217deDF79C0a"
    
    async def _get_protocol_ca(self, protocol):
        match protocol:
            case "pendle":
                return "0x32ecd5f7442ae3b4257557D696c6D68722000008"
            case "compoundv3":
                return "0x67D9572A17C8d7cCfe4d45972d96d6462640b931"
            case "moonwell":
                return "0x80e6A5e648E97FF1dA61c4484d1f41b068c737D3"
            case "stargatev3":
                return "0xE3e657Ae4d01343E74050B73f4Bc4D434431D228"
            case "aavev3":
                return "0x5C2c580bC9A9f7C7C3E7c768b77c6a34510606CC"
    
    async def mint(self, user_address, asset_id, amount):
        amount = int(amount) * (10 ** 6)
        abi = await self._read_abi("./abi/MockToken.json")
        
        wallet = await self.fetch_data(user_address)
        address = wallet.default_address.address_id
        
        invocation = wallet.invoke_contract(
            contract_address=await self._get_token_ca(asset_id),
            abi=abi,
            method="mint",
            args={"to": address, "amount": str(int(amount))}
        )

        invocation.wait()
        
        return invocation.transaction_hash
    
    async def transfer(self, user_address, contract_address, to, amount):
        amount = int(amount) * (10 ** 6)
        abi = await self._read_abi("./abi/MockToken.json")
        
        wallet = await self.fetch_data(user_address)
        
        invocation = wallet.invoke_contract(
            contract_address=contract_address,
            abi=abi,
            method="transfer",
            args={"to": str(to), "value": str(int(amount))}
        )

        invocation.wait()
        
        return invocation.transaction_hash
    
    async def swap(self, user_address, spender, token_in, token_out, amount):
        approve_abi = await self._read_abi("./abi/MockToken.json")
        amount = int(amount) * (10 ** 6)
        
        wallet = await self.fetch_data(user_address)
        approve_incovation = wallet.invoke_contract(
            contract_address=token_in,
            abi=approve_abi,
            method="approve",
            args={"spender": spender, "amount": str(int(amount + 10))}
        )
        approve_incovation.wait()
        
        abi = await self._read_abi("./abi/BruceFi.json")
        
        invocation = wallet.invoke_contract(
            contract_address="0x0e8d24364eb713268566a80F7595780376B6dFC7",
            abi=abi,
            method="swap",
            args={"tokenIn": token_in, "tokenOut": token_out, "amountIn": str(int(amount))}
        )

        invocation.wait()
        
        return invocation.transaction_hash
    
    async def stake(self, user_address, asset_id, protocol, spender, amount):
        approve_abi = await self._read_abi("./abi/MockToken.json")
        amount = int(amount) * (10 ** 6)
        
        wallet = await self.fetch_data(user_address)
        approve_incovation = wallet.invoke_contract(
            contract_address=await self._get_token_ca(asset_id),
            abi=approve_abi,
            method="approve",
            args={"spender": spender, "amount": str(int(amount + 10))}
        )
        approve_incovation.wait()
        
        abi = await self._read_abi("./abi/MockStake.json")
        
        invocation = wallet.invoke_contract(
            contract_address=await self._get_protocol_ca(protocol),
            abi=abi,
            method="stake",
            args={"_days": str(0), "_amount": str(int(amount))}
        )

        invocation.wait()
        
        return invocation.transaction_hash
    
    
    async def unstake(self, user_address, protocol):        
        abi = await self._read_abi("./abi/MockStake.json")
        wallet = await self.fetch_data(user_address)
        invocation = wallet.invoke_contract(
            contract_address=await self._get_protocol_ca(protocol),
            abi=abi,
            method="withdrawAll"
        )

        invocation.wait()
        
        return invocation.transaction_hash


    async def _read_abi(self, abi_path):
        with open(abi_path, 'r') as file:
            return orjson.loads(file.read())


    async def _load_existing_data(self):
        if not os.path.exists(self.file_path):
            return []

        with open(self.file_path, 'rb') as file:
            return orjson.loads(file.read())

    async def _save_data(self, data):
        with open(self.file_path, 'wb') as file:
            file.write(orjson.dumps(data, option=orjson.OPT_INDENT_2))
