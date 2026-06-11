
f = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\mx_adapter.py', encoding='utf-8')
content = f.read()
f.close()

# Fix 1: Replace deprecated get_transactions with sync endpoint
old_get_tx = '''    async def get_transactions(self, access_token: str,
                                start_date: str, end_date: str) -> List[dict]:
        body = {
            "access_token": access_token,
            "start_date":   start_date,
            "end_date":     end_date,
            "options":      {"count": 500}
        }
        data = await self._post("/transactions/get", body)
        return data.get("transactions", [])'''

new_get_tx = '''    async def get_transactions(self, access_token: str,
                                start_date: str = None, end_date: str = None) -> List[dict]:
        """Use /transactions/sync — current Plaid API (replaces deprecated /transactions/get)."""
        all_tx = []
        cursor = None
        for _ in range(5):  # max 5 pages
            body = {"access_token": access_token, "count": 500}
            if cursor:
                body["cursor"] = cursor
            try:
                data = await self._post("/transactions/sync", body)
                all_tx.extend(data.get("added", []))
                if not data.get("has_more", False):
                    break
                cursor = data.get("next_cursor")
            except Exception:
                break
        return all_tx'''

# Fix 2: Update pull_and_calculate to use updated method signature
old_pull = '''            plaid_tx   = await self.get_transactions(access_token, start_date, end_date)'''
new_pull = '''            plaid_tx   = await self.get_transactions(access_token)'''

# Fix 3: Remove unused start/end date vars in pull_and_calculate
old_dates = '''            # Pull accounts and transactions
            plaid_accounts = await self.get_accounts(access_token)
            end_date   = datetime.now().strftime("%Y-%m-%d")
            start_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
            plaid_tx   = await self.get_transactions(access_token)'''

new_dates = '''            # Pull accounts and transactions
            plaid_accounts = await self.get_accounts(access_token)
            plaid_tx   = await self.get_transactions(access_token)'''

content = content.replace(old_get_tx, new_get_tx)
content = content.replace(old_pull, new_pull)
content = content.replace(old_dates, new_dates)

g = open(r'C:\Users\alima\Dropbox\Meridia\integra-core\meridia-wiring\mx_adapter.py', 'w', encoding='utf-8')
g.write(content)
g.close()
print("Plaid fix applied")
