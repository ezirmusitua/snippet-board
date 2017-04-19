### Snippet board
一个用于保存来自 `Annotation board` snippets 的站点

主要功能是接收来自 `Annotation board` 的 snippets 请求，并将请求内容保存到数据库中

目前的想法是作为一个本地运行的 server，不开放到外网，通过修改 hosts 让 `Annotation board` 能够连通


### Requirements
初始阶段希望达成的一些需求：
1. 能够接收 snippet 请求
2. 能够将 snippet 保存到数据库中
3. 能够展示 snippet
4. 能够编辑 snippet
5. 能够将编辑后的 snippet 保存到数据库中

### Future
1. 能够抓取原始站点内容并保存到本地数据库中
2. 增加用户系统并作为一个能远程使用的站点

### Techniques
针对初始阶段用到的技术有：
1. flask
2. sqlite3

### TODOs
[x] 初始化 flask 项目

[] 初始化项目结构

[] 初始化数据库

[] 定义 数据 model

[] 设计 路由

[] 设计 templates

[] 实现逻辑

[] 简单测试


