from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import TickerId

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        print("Erro: ", reqId, " ", errorCode, " ", errorString)

    def accountSummary(self, reqId:int, account:str, tag:str, value:str, currency:str):
        print("Conta: ", account, ", Tag: ", tag, ", Valor: ", value, ", Moeda: ", currency)

def main():
    app = IBApi()
    app.connect("127.0.0.1", 7496, 0)

    contas_administradas = [
        "DF7428746"
    ] 

    for idx, conta in enumerate(contas_administradas):
        app.reqAccountSummary(idx+1, conta, "$LEDGER:ALL")
        app.reqAccountSummary(idx+2, conta, "Leverage")

    app.run()

if __name__ == "__main__":
    main()