
import asyncio
import sys
sys.path.insert(0, r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring')
from mx_adapter import PlaidAdapter

async def test():
    plaid = PlaidAdapter()
    try:
        pub = await plaid.create_sandbox_token()
        print("Sandbox token: OK")
        access = await plaid.exchange_token(pub)
        print("Exchange token: OK")
        accounts = await plaid.get_accounts(access)
        print(f"Accounts: {len(accounts)}")
        for a in accounts[:4]:
            bal = a.get("balances", {}).get("current", 0)
            print(f"  {a.get('name', '')} | {a.get('type', '')} | ${bal:,.2f}")
        txs = await plaid.get_transactions(access)
        print(f"Transactions (sync): {len(txs)}")
        if txs:
            t = txs[0]
            print(f"  Sample: {t.get('name', '')} | ${t.get('amount', 0)}")
        print("PLAID SANDBOX: WORKING")
    except Exception as e:
        print(f"ERROR: {e}")

asyncio.run(test())
