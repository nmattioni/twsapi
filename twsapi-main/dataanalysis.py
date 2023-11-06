import pandas as pd

data = {
    'Code': ['F10451695', 'U10355581', 'U10375548', 'U10393335', 'U11071406', 'U11086471', 'U11239176', 'U11424382', 
            'U11821945', 'U12156732', 'U12167071', 'U12192213', 'U12216291', 'U12236925', 'U12277193', 'U12294610', 
            'U12320396', 'U12321651', 'U12351347', 'U12471035', 'U12631300', 'U12666466', 'U12691955', 'U12843298',
            'U12997920', 'U4031188', 'U5453084', 'U9578694', 'U9624456', 'U9665342'],
    'Short Name': ['PLENO GESTAO DE INVESTIMENTOS', 'HIGH DEFINITION ASSET HOLDING', 'LFSS CAPITAL', 'CORSAGE ORCHID', 
                   'NIMAO', '', 'DAVI ANDRADE', 'SUNFLOWERS GLOBAL CAPITAL', '', '', '', '', '', '', '', '', '', '', '', 
                   '', '', '', '', '', 'VALLE CORPORATE GROUP (JT)', 'THEOS CAPITAL (JT)', '', '', ''],
    'Full Name': ['Pleno Gestao de Investimentos e Consultoria Ltda', 'HIGH DEFINITION ASSET HOLDING INC.', 
                  'LFSS CAPITAL LTD.', 'CORSAGE ORCHID LTD.', 'NIMAO LTD.', 'RRL INTERNATIONAL INVESTING INC.', 
                  'Davi Oliveira Serrano de Andrade', 'SUNFLOWERS GLOBAL CAPITAL INC.', 'Fabio M Rigueira', 
                  'Caio K Amaral and Ana paulla Vasconcelos', 'Guilherme C Nunes', 'Douglas B Thomaz', 
                  'Ghabriel G Ferreira', 'Igor E Sousa', 'Eduardo S Miranda and Dayana K Toledo', 
                  'Pablo E Billard Pacheco De Toledo', 'Alvaro Rodrigues Moreno Junior', 'CAMILO DELFINO', 
                  'GATZZ HOLDING LTD', 'Nata M Franco Sr.', 'Filipe Thomas Steger', 'Alexandre R Cardoso', 
                  'Rodrigo A Azevedo', 'Miguel P de Rezende', 'Carlos H Albertoni', 'VALLE CORPORATE GROUP INC', 
                  'THEOS CAPITAL LTD', 'Lucas Ferreira de Araujo', 'EMILIO TRADE AND INVEST CORP.', 
                  'Paradise Bay Business INC']
}

df = pd.DataFrame(data)
