from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import re

def setup_driver():
    edge_options = Options()
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    
    service = Service("D:\\environment\\edgedriver_win64\\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=edge_options)
    return driver

def get_news_links(driver, url):
    driver.get(url)
    links = []
    while len(links) < 100:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "na_detail"))
        )
        news_elements = driver.find_elements(By.CLASS_NAME, "na_detail")
        for element in news_elements:
            link = element.find_element(By.TAG_NAME, "a").get_attribute("href")
            if link not in links:
                links.append(link)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    return links[:100]

def save_news_content(driver, link):
    driver.get(link)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "post_content"))
    )
    title = driver.find_element(By.CLASS_NAME, "post_title").text
    content = driver.find_element(By.CLASS_NAME, "post_content").text
    
    # 清理文件名
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    filename = f"{title[:50]}.txt"
    
    # 将标题和内容都保存到文件中
    with open(os.path.join("newsLog", filename), "w", encoding="utf-8") as f:
        f.write(f"标题：{title}\n\n")
        f.write(f"内容：\n{content}")

def main():
    try:
        url = "https://news.163.com/domestic/"
        driver = setup_driver()
        
        # 创建 newsLog 文件夹（如果不存在）
        if not os.path.exists("newsLog"):
            os.makedirs("newsLog")
        
        links = get_news_links(driver, url)
        
        for i, link in enumerate(links, 1):
            try:
                save_news_content(driver, link)
                print(f"已保存第 {i} 条新闻")
            except Exception as e:
                print(f"保存第 {i} 条新闻时出错: {str(e)}")
        
        print("爬取完成")
    except Exception as e:
        print(f"程序运行出错: {str(e)}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    main()
