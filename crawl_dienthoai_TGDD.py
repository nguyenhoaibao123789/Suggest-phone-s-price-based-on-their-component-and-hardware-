!pip install pyclipper
# Library
import time # cho load day du trang
from selenium import webdriver # driver dung de crawl du lieu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

# Setup cac thanh phan co ban cho viec crawl
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
prefs={"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="D:\\chromedriver.exe")

# Bat dau crawl
url = "https://www.thegioididong.com/dtdd#c=42&o=9&pi=7"
driver.get(url)
time.sleep(5) #doi load trang
#button_view_more = driver.find_element_by_class_name('view-more')

# product_list la danh sach dien thoai tren trang
product_list = driver.find_element(By.CLASS_NAME, value='listproduct')
elements = product_list.find_elements_by_css_selector("a")
# sites la list chua tat ca link dien thoai da crawl duoc
sites = [el.get_attribute("href") for el in elements if el.get_attribute("data-cate") == "Điện thoại"]
print("Tổng cộng có", len(sites), "điện thoại trên web này.")

count = 1
data = []
# Truy cap vao tung san pham de crawl
for phone_url in sites:
    driver.get(phone_url)
    print(count, '\n')
    count += 1
    time.sleep(5) # Doi 5s load trang
    name = driver.find_element_by_tag_name('h1')
    name = name.text # Crawl ten dien thoai
    try:
        price = driver.find_element_by_class_name('box-price-old')
    except Exception:
        price = driver.find_element_by_class_name('box-price-present')    
    price = price.text.replace('.', '').replace('₫', '')
    button_cau_hinh = driver.find_element_by_class_name("icondetail-thongso")
    button_cau_hinh.click() # click truy cap cau hinh chi tiet 
    # https://www.thegioididong.com/dtdd/samsung-galaxy-z-fold3-5g-512gb?src=osp#top-tskt
    wait = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "parameter-all")))
    # driver.getPageSource()
    newURl = driver.window_handles[0]
    driver.switch_to.window(newURl)
    #img_src = driver.find_element_by_class_name("img").get_attribute('src')
    #cau_hinh_all = driver.find_elements_by_class_name("parameter-all")
    try:
        man_hinh = driver.find_element_by_xpath("//div[@class='parameter-all']/div[@class='parameter-item']/ul[@class='ulist']/li[@data-id='6459']/div[@class='ctRight']").text
    except Exception:
        man_hinh = None
    try:
        do_phan_giai_manHinh = driver.find_element_by_xpath("//div[@class='parameter-all']/div[@class='parameter-item']/ul[@class='ulist']/li[@data-id='78']/div[@class='ctRight']").text
    except Exception:
        do_phan_giai_manHinh= None    
    try:
        man_hinh_rong = driver.find_element_by_xpath("//div[@class='parameter-all']/div[@class='parameter-item']/ul[@class='ulist']/li[@data-id='27278']/div[@class='ctRight']").text
    except Exception:
        man_hinh_rong = None    
    try:
        do_sang_toi_da = driver.find_element_by_xpath("//li[@data-id='27392']/div[@class='ctRight']").text
    except Exception:
        do_sang_toi_da = None    
    try:
        mat_kinh_cam_ung = driver.find_element_by_xpath("//li[@data-id='7799']/div[@class='ctRight']").text
    except Exception:
        mat_kinh_cam_ung = None        
    try:
        do_phan_giai_Camera = driver.find_element_by_xpath("//li[@data-id='27']/div[@class='ctRight']").text
    except Exception:
        do_phan_giai_Camera= None
    try:
        quay_phim = driver.find_element_by_xpath("//li[@data-id='31']/div[@class='ctRight']").text
    except Exception:
        quay_phim = None    
    try:
        den_flash = driver.find_element_by_xpath("//li[@data-id='6460']/div[@class='ctRight']").text
    except Exception:
        den_flash = None
    try:
        tinh_nang_camera = driver.find_element_by_xpath("//li[@data-id='28']/div[@class='ctRight']").text
    except Exception:
        tinh_nang_camera = None    
    try:
        do_phan_giai_CameraTruoc = driver.find_element_by_xpath("//li[@data-id='29']/div[@class='ctRight']").text
    except Exception:
        do_phan_giai_CameraTruoc = None    
    try:
        tinh_nang_cameraTruoc = driver.find_element_by_xpath("//li[@data-id='7801']/div[@class='ctRight']").text
    except Exception:
        tinh_nang_cameraTruoc = None
    try:
        he_dieu_hanh = driver.find_element_by_xpath("//li[@data-id='72']/div[@class='ctRight']").text
    except Exception:
        he_dieu_hanh = None
    try:
        cpu = driver.find_element_by_xpath("//li[@data-id='6059']/div[@class='ctRight']").text
    except Exception:
        cpu = None
    try:
        toc_do_cpu = driver.find_element_by_xpath("//li[@data-id='51']/div[@class='ctRight']").text
    except Exception:
        toc_do_cpu = None
    try:
        chip_do_hoa_GPU = driver.find_element_by_xpath("//li[@data-id='6079']/div[@class='ctRight']").text
    except Exception:
        chip_do_hoa_GPU = None
    try:
        ram = driver.find_element_by_xpath("//li[@data-id='50']/div[@class='ctRight']").text
    except Exception:
        ram = None
    try:
        bo_nho_trong = driver.find_element_by_xpath("//li[@data-id='49']/div[@class='ctRight']").text
    except Exception:
        bo_nho_trong = None
    try:
        bo_nho_con_lai = driver.find_element_by_xpath("//li[@data-id='7803']/div[@class='ctRight']").text
    except Exception:
        bo_nho_con_lai = None    
    try:
        danh_ba = driver.find_element_by_xpath("//li[@data-id='54']/div[@class='ctRight']").text
    except Exception:
        danh_ba = None    
    try:
        sim = driver.find_element_by_xpath("//li[@data-id='6339']/div[@class='ctRight']").text
    except Exception:
        sim=None
    try:
        wifi = driver.find_element_by_xpath("//li[@data-id='66']/div[@class='ctRight']").text
    except Exception:
        wifi = None
    try:
        gps = driver.find_element_by_xpath("//li[@data-id='68']/div[@class='ctRight']").text
    except Exception:
        gps = None      
    try:
        bluetooth = driver.find_element_by_xpath("//li[@data-id='69']/div[@class='ctRight']").text
    except Exception:
        bluetooth = None    
    try:
        cong_sac = driver.find_element_by_xpath("//li[@data-id='71']/div[@class='ctRight']").text 
    except Exception:
        cong_sac = None    
    try:
        ket_noi_khac = driver.find_element_by_xpath("//li[@data-id='5199']/div[@class='ctRight']").text
    except Exception:
        ket_noi_khac = None
    try:
        dung_luong_pin = driver.find_element_by_xpath("//li[@data-id='84']/div[@class='ctRight']").text
    except Exception:
        dung_luong_pin = None    
    try:
        loai_pin = driver.find_element_by_xpath("//li[@data-id='83']/div[@class='ctRight']").text
    except Exception:
        loai_pin = None    
    try:
        cong_nghe_pin = driver.find_element_by_xpath("//li[@data-id='10859']/div[@class='ctRight']").text
    except Exception:
        cong_nghe_pin = None    
    try:
        kichThuoc_khoiLuong = driver.find_element_by_xpath("//li[@data-id='88']/div[@class='ctRight']").text
    except Exception:
        kichThuoc_khoiLuong = None    
    try:
        thoiDiem_raMat = driver.find_element_by_xpath("//li[@data-id='13045']/div[@class='ctRight']").text
    except Exception:
        thoiDiem_raMat = None 
    try:
        the_nho=driver.find_element_by_xpath("//li[@data-id='52']/div[@class='ctRight']").text
    except Exception:
        the_nho = None
    try:
        chat_lieu=driver.find_element_by_xpath("//li[@data-id='7805']/div[@class='ctRight']").text
    except Exception:
        chat_lieu = None
    try:
        khang_nuoc=driver.find_element_by_xpath("//li[@data-id='27511']/div[@class='ctRight']").text
    except Exception:
        khang_nuoc = None
    try:
        cam_bien=driver.find_element_by_xpath("//li[@data-id='10860']/div[@class='ctRight']").text
    except Exception:
        cam_bien = None   
    try:
        tinh_nang_db=driver.find_element_by_xpath("//li[@data-id='43']/div[@class='ctRight']").text
    except Exception:
        tinh_nang_db = None 
    try:
        jack_tai_nghe=driver.find_element_by_xpath("//li[@data-id='48']/div[@class='ctRight']").text
    except Exception:
        jack_tai_nghe = None 
    print("Ten:",name)
    print("Gia: ", price)
    print("Cong nghe man hinh:", man_hinh)
    print("Do phan giai man hinh:", do_phan_giai_manHinh)
    print("Man hinh rong:", man_hinh_rong)
    print("Do sang toi da:", do_sang_toi_da)
    print("Mat kinh cam ung:", mat_kinh_cam_ung)
    print("Do phan giai camera:", do_phan_giai_Camera)
    print("Quay phim:", quay_phim)
    print("Den flash:", den_flash)
    print("Ram:",ram)
    print("bo nho trong:",bo_nho_trong)
    print("Tinh nang camera:", tinh_nang_camera)
    print("do phan giai camera truoc:", do_phan_giai_CameraTruoc)
    print("Tinh nang camera truoc:", tinh_nang_cameraTruoc)
    print("He dieu hanh:", he_dieu_hanh)
    print("Chip xu ly (CPU):", cpu)
    print("Toc do CPU:", toc_do_cpu)
    print("Chip do hoa GPU:", chip_do_hoa_GPU)
    print("Danh Ba:", danh_ba)
    print("Sim:",sim)
    print("Wifi:", wifi)
    print("GPS:", gps)
    print("Bluetooth: ", bluetooth)
    print("Cong sac:", cong_sac)
    print("ket noi khac:", ket_noi_khac)
    print("Dung luong pin:", dung_luong_pin)
    print("Loai pin:", loai_pin)
    print("Cong nghe pin:", cong_nghe_pin)
    print("Kich thuoc, khoi luong:", kichThuoc_khoiLuong)
    print("Thoi diem ra mat:", thoiDiem_raMat)
    print("the nho:",the_nho)
    print("chat lieu", chat_lieu)
    print("khang nuoc", khang_nuoc)
    print("Tinh nang dac biet", tinh_nang_db)
    print("Jack tai nghe",jack_tai_nghe)
    data.append([name, price,man_hinh_rong, man_hinh, do_phan_giai_Camera,
                 do_phan_giai_CameraTruoc,cpu,ram,bo_nho_trong,dung_luong_pin, loai_pin,
                 sim,he_dieu_hanh,do_phan_giai_manHinh, toc_do_cpu,
                 quay_phim, tinh_nang_camera,
                 chip_do_hoa_GPU,the_nho,cong_nghe_pin,
                 cong_sac,wifi, bluetooth,gps,kichThuoc_khoiLuong,
                 chat_lieu,khang_nuoc,cam_bien,
                 tinh_nang_db, jack_tai_nghe])
    
df = pd.DataFrame(data, columns = ['Tên', 'Giá', 'Kích thước màn hình', 'Công nghệ màn hình', 'Camera sau',
       'Camera trước', 'CPU', 'Dung lượng RAM', 'Bộ nhớ trong', 'Dung lượng pin',"Loại pin",
       'Thẻ SIM', 'Hệ điều hành', 'Độ phân giải màn hình', 'Loại CPU',
       'Quay video', 'Tính năng camera',
       'GPU', 'Khe cắm thẻ nhớ', 'Công nghệ sạc',
       'Cổng sạc', 'Wi-Fi', 'Bluetooth', 'GPS', 'Kích thước,khối lượng',   
       'Chất liệu','Chỉ số kháng nước, bụi', 'Cảm biến vân tay',
       'Tính năng đặc biệt','Jack tai nghe 3.5'],
                  index=None)
df.to_excel('dienthoai_TGDD.xlsx')
driver.close()
