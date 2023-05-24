
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

def buscar_info(medicamento):
    resultado=medicamento+" cambio hecho"
    return resultado


def buscar_med(dato):
    options = Options()
    options.add_argument('--headless')
    browser=webdriver.Chrome(options=options)
    Urlss=dict()

    Urlss['https://www.farmaciaspasteur.com.co/xx?_q=xx&map=ft']=['//span[@class="vtex-product-summary-2-x-productBrand vtex-product-summary-2-x-brandName t-body"]','//span[@class="vtex-product-price-1-x-sellingPriceValue"]']
    Urlss['https://www.cruzverde.com.co/search?query=xx']=['//a[@class="font-open flex items-center text-main text-16 sm:text-18 leading-20 font-semibold ellipsis hover:text-accent"]','//span[@class="font-bold text-prices"]']


   
    medicamento=dato.replace(" ","%20")
    elementos=[]
    precios=[]
    list_elementos=[]
    list_precios=[]
    farmacias=[]

    for k,v in Urlss.items():
        browser.get(k.replace("xx",medicamento))
        farmacia=k[k.find("www.")+4:k.find(".com")]
        time.sleep(3)
        elementos=browser.find_elements(By.XPATH, v[0])
        precios=browser.find_elements(By.XPATH, v[1])
        for elemento in elementos:
            list_elementos.append(elemento.text)
            farmacias.append(farmacia)
        for precio in precios:
            list_precios.append(int(precio.text.replace("$","").replace(".","")))


    datos={'Elemento':list_elementos,'Precios':list_precios, 'Farmacia':farmacias}

    info=pd.DataFrame(datos)

    info_orden = info.sort_values(by='Precios', ascending=True)


    #print(info)
    #print(info_orden)

    browser.quit()

    return info_orden