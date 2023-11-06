import time
import csv
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import AccountSummaryTags

class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.account_details = {}

    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        if tag == AccountSummaryTags.NetLiquidation:
            self.account_details[account] = value

def main():
    # Lista de contas para as quais você deseja obter o NetLiquidation
    account_list = [ 'U10355581', 'U10375548', 'U10393335', 'U11071406', 'U11086471', 'U11239176', 'U11424382', 'U11821945', 
    'U12156732', 'U12167071', 'U12192213', 'U12216291', 'U12236925', 'U12277193', 'U12294610', 'U12320396', 
    'U12321651', 'U12351347', 'U12471035', 'U12631300', 'U12666466', 'U12691955', 'U12843298', 'U12997920', 
    'U4031188', 'U5453084', 'U9578694', 'U9624456', 'U9665342'] 

    app = IBapi()
    app.connect('127.0.0.1', 7496, 123)  # Seu IP, porta e ID do cliente

    print("Conectando...")
    time.sleep(1)  

    # Solicitar resumos de conta
    app.reqAccountSummary(1, "All", AccountSummaryTags.NetLiquidation)
    time.sleep(3)  # Dê tempo para os dados serem recebidos

    # Desconectar depois de obter os dados
    app.disconnect()

    # Salvar em um arquivo CSV
    with open('netliquidation.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account", "NetLiquidation"])

        for account in account_list:
            if account in app.account_details:
                writer.writerow([account, app.account_details[account]])
            else:
                writer.writerow([account, "Not Received"])

    print("Dados salvos em netliquidation.csv")

if __name__ == "__main__":
    main()
