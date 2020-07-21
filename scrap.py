from time import sleep, time
import pandas as pd
import string
from web_interaction import web_interaction
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options


inicio = time()        
count = 1
opt = Options()
opt.add_argument('--headless')
url = 'https://www.guiamais.com.br/'
url_init = 'https://www.guiamais.com.br/manaus-am'
dict_contatos = {'Nome' : [],
                 'Endereço' : [],
                 'Telefone' : []}

tipo = input('Qual tipo de estabelecimento?\n')


ff = Firefox(options = opt)
c = web_interaction(ff)

c.navigate(url_init)
sleep(2.5)
c.search(tipo)
sleep(2.5)

while True:
    links = c.get_links()
    current_url = c.current_url()

    for link in links:
        c.navigate(url + link)
        sleep(2.5)
                    
        dict_contatos['Nome'].append(c._get_store_name())
        dict_contatos['Endereço'].append(c._get_store_address())
        dict_contatos['Telefone'].append(c._get_store_phone())
            
    print(count, '-', len(links))
    count += 1
                    
    c.navigate(current_url)
            
    try:
        c.see_more_stores()
        sleep(5)
    except:
        break
    
c.close()
    
df = pd.DataFrame.from_dict(data = dict_contatos)
df.to_csv('database.csv', index = False)

fim = time()
print(round((fim - inicio) / 60, 3))