# 网络爬虫作业集

这个仓库用于存储和管理我的一些网络爬虫相关作业和项目。

## 目录
- [网络爬虫作业集](#网络爬虫作业集)
  - [目录](#目录)
  - [项目简介](#项目简介)
  - [文件结构](#文件结构)
  - [如何运行](#如何运行)
  - [注意事项](#注意事项)
  - [贡献指南](#贡献指南)

## 项目简介

本仓库包含了我在学习和实践网络爬虫过程中完成的各种作业和项目，每个子文件夹代表一个独立的爬虫任务或项目。

## 文件结构

- `/NetEaseNews`：网易新闻爬虫
- `/BilibiliHot`：Bilibili热榜爬虫
- ...
- `requirements.txt`: 所有项目共用的基本依赖
- `README.md`: 本文件

## 如何运行

1. 克隆仓库到本地
   ```bash
   git clone https://github.com/peng2132/Spider
   ```

2. 进入特定项目文件夹，安装项目特定依赖，并运行脚本
   ```bash
   cd NetEaseNews
   pip install -r requirements.txt 
   python main.py
   ```

## 注意事项

- 请遵守网站的robots.txt规则
- 注意控制爬取速度，避免对目标网站造成负担
- 遵守相关法律法规，不要爬取敏感或违法内容
- 每个项目可能有特定的依赖要求，请查看项目文件夹中的requirements.txt文件

## 贡献指南

欢迎对本项目进行贡献！如果你有任何改进意见或新的爬虫项目想法，请遵循以下步骤：

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 将你的改动推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

