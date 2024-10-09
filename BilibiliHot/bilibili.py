from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# 设置Edge驱动
def setup_driver():
    edge_options = Options()
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    
    service = Service("D:\\environment\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=edge_options)
    return driver

# 目标URL
url = "https://www.bilibili.com/v/popular/all"

# 初始化 Selenium 驱动
driver = setup_driver()
driver.get(url)

# 向下滚动页面直至底部
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # 向下滚动页面
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # 等待 5 秒钟

    # 计算新的页面高度
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 获取完整的页面源代码
html_content = driver.page_source

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(html_content, "html.parser")

# 找到所有视频卡片元素
video_cards = soup.find_all("div", class_="video-card")

# 创建 CSV 文件并写入标题行
with open("bilibili_hotlist.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "author", "video_link", "views", "image_link"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # 遍历每个视频卡片,提取所需信息并写入 CSV
    for video_card in video_cards:
        title = video_card.find("p", class_="video-name").text.strip()
        author = video_card.find("span", class_="up-name__text").text.strip()
        video_link = "https://www.bilibili.com" + video_card.find("a")["href"].lstrip("/")
        views = video_card.find("span", class_="play-text").text.strip()
        image_link = video_card.find("img", class_="cover-picture__image")["data-src"]

        writer.writerow({
            "title": title,
            "author": author,
            "video_link": video_link,
            "views": views,
            "image_link": image_link
        })

driver.quit()
print("数据已保存到 bilibili_hotlist.csv 文件中.")