## 教學測試專案
* 此專案的目的是將會用到的工具進行整理，主要結合以下常見的內容
  * `djangorestframework`
  * `djnago`
  * `mysql`
  * `redis`
  * `mongodb`: `upcommimg`

## 初始化專案

### 安裝套件管理工具`poetry`
```bash=
pip3 install poetry
poetry install
```

### 啟動由`poetry`管理的虛擬環境
```bash
poetry shell
```

### 環境變數管理方式
* 使用`django-env`進行環境變數管理，`.env`檔案編寫很重要
* 主要相關內容會在`settings.py`中引入，更細節的部分請參考`django-env`的[官方文件](https://django-environ.readthedocs.io/en/latest/getting-started.html)

### 撰寫`.env`檔案
```text=
# 可以根據需要進行擴充
# 要注意觀察settings.py用到哪些
DEBUG=True
DATABASE_URL='mysql://root:root@127.0.0.1:3306/testdb'
REDIS_URL=redis://127.0.0.1:6379/1?client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
SECRET_KEY='l(k$cn#2j572iw+f#&2)n^#38zk^ul31bilhp&z+obd$m@s-w&'
REDIS_HOST='localhost'
REDIS_PORT=6379
REDIS_DB=0
```

### 針對資料庫做遷移
* 執行以下命令
```bash
python manage.py showmigrations
python manage.py mkaemigrations 
python manage.py migrate
```
* 以下為命令幫助
```bash
python manage.py -h
python manage.py makemigrations -h
python manage.py migrate -h
```

### 啟動專案
```python=
python manage.py 8000
```

## API文件

### 使用swagger生成API文件
* 訪問`/swaggerui/`，可以查看API文件


## 文件參考整理

* [django-environ 官方文件](https://django-environ.readthedocs.io/en/latest/getting-started.html)
* [poetry 官方文件](https://python-poetry.org/docs/)
* [django rest framework](https://www.django-rest-framework.org/)