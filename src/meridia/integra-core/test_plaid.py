
import asyncio
from meridia_wiring.mx_adapter import PlaidAdapter

async def test():
    plaid = PlaidAdapter()
    try:
        pub = await plaid.create_sandbox_token()
        print(f"Sandbox token: {pub[:30]}...")
        access = await plaid.exchange_token(pub)
        print(f"Access token: {access[:30]}...")
        accounts = await plaid.get_accounts(access)
        print(f"Accounts: {len(accounts)}")
        for a in accounts[:3]:
            print(f"  {a.get('name')} — {a.get('type')} — ${a.get('balances',{}).get('current',0):,.2f}")
        txs = await plaid.get_transactions(access)
        print(f"Transactions: {len(txs)}")
        print("Plaid sandbox: WORKING")
    except Exception as e:
        print(f"Plaid error: {e}")

asyncio.run(test())
