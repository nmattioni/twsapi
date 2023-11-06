from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.common import *
import time

class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        
    def error(self, reqId, errorCode, errorString):
        print(f"Error. Id: {reqId}, Code: {errorCode}, Msg: {errorString}")

    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
    
        print("AccountSummary. Account:", account, "Tag: ", tag, "Value: ", value, "Currency: ", currency)
    
    def position(self, account: str, contract, pos: int, avgCost: float):
        print("Position. Account:", account, "Contract:", contract, "Position:", pos, "Avg cost:", avgCost)
    
def main():
    app = TestApp()
    app.connect("127.0.0.1", 7496, 0) # informações gateway
    time.sleep(2) #temporizador para não sobrecarregar o servidor

    account_codes = [
        "U12236925"
    ]
        
    for idx, account_code in enumerate(account_codes):
        app.reqAccountSummary(idx + 1, "All", "$LEDGER:" + account_code)
        time.sleep(1)  # Adiciona um atraso de 1 segundo entre cada solicitação
    
    # Solicitando posições (você pode modificar isso para solicitar posições para contas específicas)

    app.reqPositions()
    
    app.run()
    
if __name__ == "__main__": # para permitir exportação das funções 
    main()