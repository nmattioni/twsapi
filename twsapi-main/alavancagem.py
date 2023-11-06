from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.account_summary_tags import AccountSummaryTags
import csv

class IBApi(EWrapper, EClient):
    def __init__(self, accounts):
        EClient.__init__(self, self)
        self.accounts_data = {account: {"equity": 0, "exposure": 0} for account in accounts}
        self.current_account = ''

    def accountSummary(self, reqId, account, tag, value, currency):
        if account not in self.accounts_data:
            return

        if tag == AccountSummaryTags.NetLiquidation:
            self.accounts_data[account]["equity"] = float(value)
        elif tag == "Exposure":
            self.accounts_data[account]["exposure"] = float(value)

    def calculateLeverage(self, account):
        data = self.accounts_data[account]
        if data["equity"] != 0:
            return data["exposure"] / data["equity"]
        else:
            return 0

    def saveToCSV(self):
        with open('accounts_leverage.csv', 'w', newline='') as csvfile:
            fieldnames = ['Account', 'Equity', 'Exposure', 'Leverage']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for account, data in self.accounts_data.items():
                leverage = self.calculateLeverage(account)
                writer.writerow({'Account': account, 'Equity': data["equity"], 'Exposure': data["exposure"], 'Leverage': leverage})

def main():
    accounts_list = ['U10355581', 'U10375548', 'U10393335', 'U11071406', 'U11086471', 'U11239176', 'U11424382', 
            'U11821945', 'U12156732', 'U12167071', 'U12192213', 'U12216291', 'U12236925', 'U12277193', 'U12294610', 
            'U12320396', 'U12321651', 'U12351347', 'U12471035', 'U12631300', 'U12666466', 'U12691955', 'U12843298',
            'U12997920', 'U4031188', 'U5453084', 'U9578694', 'U9624456', 'U9665342']
    
    app = IBApi(accounts_list)
    app.connect("127.0.0.1", 7496, clientId=0)
    
    for account in accounts_list:
        app.reqAccountSummary(1, "All", f"$LEDGER:{account}")
        app.run()  # Esta chamada bloqueia até que todas as contas sejam processadas

    app.saveToCSV()
    print(f"Dados salvos em accounts_leverage.csv")

if __name__ == "__main__":
    main()