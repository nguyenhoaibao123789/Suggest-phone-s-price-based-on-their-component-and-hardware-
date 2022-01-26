
# Library
import time # cho load day du trang
from selenium import webdriver # driver dung de crawl du lieu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from html_table_parser.parser import HTMLTableParser

# Setup cac thanh phan co ban cho viec crawl
pd.set_option("display.max_columns", 30)
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--headless")
chrome_options.page_load_strategy = 'normal' # to wait for the entire page is loaded
prefs={"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\\chromedriver.exe")

# Bat dau crawl
url = "https://cellphones.com.vn/mobile.html?dir=desc&order=price"
driver.get(url)
#time.sleep(5) #doi load trang
"""
for i in range(22):
    newURl = driver.window_handles[0]
    driver.switch_to.window(newURl)
    button_view_more = driver.find_element_by_class_name('btn-show-more.btn-load-more')
    button_view_more.click()
    """
while (len(driver.find_element_by_class_name('btn-show-more.btn-load-more').text)>0):
    button_view_more = driver.find_element_by_class_name('btn-show-more.btn-load-more')
    button_view_more.click()
    time.sleep(3)
# product_list la danh sach dien thoai tren trang 
elements = driver.find_elements_by_xpath('//div[@class="item-product__box-name"]/a')
# elements = driver.find_elements(By.CLASS_NAME, 'item-product')
# sites la list chua tat ca link dien thoai da crawl duoc
sites = [el.get_attribute("href") for el in elements]
#sites = [el.find_elements_by_xpath('//div[@class="item-product__box-name"]/a').get_attribute("href") for el in elements if el.find_elements_by_xpath('//div[@class="item-product__more-info.text-stock"]/p') != "Sắp về hàng"]
#sites = [el.get_attribute("href") for el in elements if el.find_elements_by_xpath('//div[@class="item-product__more-info.text-stock"]/p') != "Sắp về hàng"]
print("Tổng cộng có", len(sites), "điện thoại trên web này.")

count = 0
data = []
# Truy cap vao tung san pham de crawl
for phone_url in sites:
    driver.get(phone_url)
    count += 1
    print(count, '\n')
    #time.sleep(5) # Doi 5s load trang
    if count in [181,204]:
        print("skip")
        pass
    try:
        newURl = driver.window_handles[0]
        driver.switch_to.window(newURl)
        close_button = driver.find_element_by_id("close-button-1545222288830")
        close_button.click()
    except Exception:
        pass 
    name = driver.find_element(By.XPATH, '//div[@class="box-name__box-product-name"]/h1')
    name = name.text # Crawl ten dien thoai
    try:
        price = driver.find_element(By.XPATH, '//p[@class="old-price"]').text
    except Exception:
        try:
            price = driver.find_element(By.XPATH, '//p[@class="special-price"]').text
        except:
            pass
    print("Ten:",name)
    price = price.replace('.', '').replace('₫', '')
    print("Gia: ", price)
    button_cau_hinh = driver.find_element_by_class_name("box-btn-show-more")
    
    button_cau_hinh.click() # click truy cap cau hinh chi tiet 
    # https://www.thegioididong.com/dtdd/samsung-galaxy-z-fold3-5g-512gb?src=osp#top-tskt
    #wait = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "parameter-all")))
    # driver.getPageSource()
    newURl = driver.window_handles[0]
    driver.switch_to.window(newURl)

    p = HTMLTableParser()
    p.feed(driver.page_source)
    table = p.tables[0]
    for i in range(1,len(p.tables)):
        table.extend(p.tables[i])
    df = pd.DataFrame(table)
    df.replace(to_replace=['',None, np.nan], value=None)
    df = df.dropna().T
    new_header = df.iloc[0]
    try:
        df = df.iloc[[1]]
    except:
        print("skip again")
        pass
    df.columns = new_header
    df=df.T.drop_duplicates().T
    df.insert(0, 'Tên',[name])
    df.insert(1, "Giá", [price])
    #df.to_excel('dienthoai_'+str(count)+'.xlsx', index = False)
    print(df)
    #print("df_col_toDelete: ", df_col_toDelete)
    #df.drop([df.columns[i] for i in range(len(df.columns)) if df_col_toDelete[i] == True], axis=1, inplace=True)
    #df.drop(df.columns[[i for i in range(len(df.columns)) if df.columns[i] in (None, '', np.nan)]], axis=1, inplace=True)
    if count <= 1:
        data = df
    else:
        try:
        #data=data.reset_index(drop=True)
            data = pd.concat([data, df],axis=0, ignore_index=True)
            data = data.T.drop_duplicates().T
            data.to_excel('dienthoai_CellPhones.xlsx', index = False)
        except:
            print("error")

data.to_excel('dienthoai_CellPhones.xlsx', index = False)
driver.close()
