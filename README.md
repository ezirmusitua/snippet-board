### Snippet board
一个用于保存来自 `Annotation board` snippets 的站点

主要功能是接收来自 `Annotation board` 的 snippets 请求，并将请求内容保存到数据库中

目前的想法是作为一个本地运行的 server，不开放到外网 ~~，通过修改 hosts 让 `Annotation board` 能够连通~~

### Version log
v0.1.0 - 完成基本架构，实现最简单的功能

### Requirements
初始阶段希望达成的一些需求：
1. 能够接收 snippet 请求
2. 能够将 snippet 保存到数据库中
3. 能够展示 snippet
4. 能够编辑 snippet
5. 能够将编辑后的 snippet 保存到数据库中
6. 能够手动添加新的内容
7. 能够搜索存在的内容
8. 能够抓取原始站点内容并保存到本地数据库中
10. 增加用户系统并作为一个能远程使用的站点

### Model
#### Snippet
| id | link\_hash | create\_at | raw\_content | create\_by |
| :------: | :------:| :------: | :------: | :------: |
| INTEGER | TEXT | INREGER | TEXT | TEXT |

### Routes
#### Post a new snippet
```
url: /snippet/api/v0.1.0
method: POST
body: {
    link: string,
    raw_content: string
}
action: return {status: int}
```

#### Display snippet list
```
url: /snippet
method: GET
action: render snippet list template with [{
    id: int,
    link_hash: string,
    create_at: int,
    create_by: string
}]
```

### Techniques
针对初始阶段用到的技术有：
1. flask
2. sqlalchemy

### TODOs
- [x] 初始化 flask 项目
- [x] 初始化项目结构
- [x] 定义 数据 models
- [x] 初始化数据库
- [x] 设计 路由
- [x] 设计 templates
- [x] 实现 单例 Database
- [x] 实现 snippet list 静态 template render
- [x] 实现 snippet list logic
- [x] 实现 post API
- [x] 简单测试
- [x] 和 Monkey Script 通信

### Bugs to fix
- [x] 使用 SQLAlchemy 进行数据库操作
- [x] 使用 蓝本 管理 路由
- [x] 复制文本中无法包含 `'` 的问题


