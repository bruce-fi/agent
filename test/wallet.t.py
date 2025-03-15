import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from wallet import AgentWallet
import asyncio

agent = AgentWallet()

async def main():
    await agent.create_wallet("0x0000000000000000000000000000000000000002")
    # await agent.fetch_data("0x0000000000000000000000000000000000000002")

    # await agent._check_address("0x0000000000000000000000000000000000000002")
    # await agent._fund_wallet("0x0000000000000000000000000000000000000002")
    # await agent._transfer(user_address="0x0000000000000000000000000000000000000002", amount=1, asset_id='usdc', destination="0x82273B356C8c882371a4CbD276f666D8efb6745F")\
        
    # # Mint tokens
    # await agent.mint(user_address="0x0000000000000000000000000000000000000002", asset_id='usdc', amount=100)
    # await agent.mint(user_address="0x0000000000000000000000000000000000000002", asset_id='usdt', amount=100)
    # await agent.mint(user_address="0x0000000000000000000000000000000000000002", asset_id='uni', amount=100)
    # await agent.mint(user_address="0x0000000000000000000000000000000000000002", asset_id='weth', amount=100)
    # await agent.mint(user_address="0x0000000000000000000000000000000000000002", asset_id='dai', amount=100)
    
    # # Swap from USDC
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", token_out="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", token_out="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", token_out="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", token_out="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", amount=5)
    
    # # Swap from UNI
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", token_out="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", token_out="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", token_out="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", token_out="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", amount=5)
    
    # # Swap from WETH
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", token_out="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", token_out="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", token_out="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", token_out="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", amount=5)

    # # Swap from DAI
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", token_out="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", token_out="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", token_out="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", token_out="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", amount=5)
    
    # # Swap from DAI
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", token_out="0x0E8Ac3cc5183A243FcbA007136135A14831fDA99", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", token_out="0x1eaC9BB63f8673906dBb75874356E33Ab7d5D780", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", token_out="0xbF1876d7643a1d7DA52C7B8a67e7D86aeeAA12A6", amount=5)
    # await agent.swap(user_address="0x0000000000000000000000000000000000000002", spender="0x9F7b08e2365BFf594C4227752741Cb696B9b6E71", token_in="0x134C06B12eA6b1c7419a08085E0de6bDA9A16dA2", token_out="0xD1d25fc5faC3cd5EE2daFE6292C5DFC16057D4d1", amount=5)

    # # Stake
    # await agent.stake(user_address="0x0000000000000000000000000000000000000002", asset_id='uni', protocol='uniswap', spender="0xa42A86906D3FDfFE7ccc1a4E143e5Ddd8dF0Cf83", amount=10)
    # await agent.stake(user_address="0x0000000000000000000000000000000000000002", asset_id='usdt', protocol='compound', spender="0xD1b1954896009800dF01b197A6E8E1d98FF44ae8", amount=10)
    # await agent.stake(user_address="0x0000000000000000000000000000000000000002", asset_id='weth', protocol='usdxmoney', spender="0x6c36eD76d3FF0A7C0309aef473052b487895Fadf", amount=10)
    # await agent.stake(user_address="0x0000000000000000000000000000000000000002", asset_id='dai', protocol='stargate', spender="0x0CAf83Ef2BA9242F174FCE98E30B9ceba299aaa3", amount=10)
    # await agent.stake(user_address="0x0000000000000000000000000000000000000002", asset_id='usdc', protocol='aave', spender="0x5dC10711C60dd5174306aEC6Fb1c78b895C9fA5A", amount=10)

    print("All operations completed successfully!")

asyncio.run(main())