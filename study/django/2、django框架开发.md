## 创建项目的指令       
* $django-admin startproject 项目名称       
* 如：$django-admin start projectmysite1     
* 运行 ：
```
cd mysite1      
python3 manage.py runserver     
或  
pytthon3 manage.py runserver 5000 #指定只能本机使用     
```
* 项目目录结构解析：        
    * manage.py     
        * 此文件是项目管理的主程序，在开发阶段用于管理整个项目的开发运行调试    
        * manage.py包含项目管理的子命令，如：
            * python3 manage.py runserver启动服务       
            * python3 manage.py startapp创建应用        
            * python3 manage.py migrate数据库迁移       
            * 。。。。
        * 项目文件夹
            * 项目的文件夹（默认与项目名称一致）    
            1. \_\_init__.py
            包初始化文件，当此项目包被导入(import)时此文件会自动运行        
            2. wsgi.py      
            WSGI即Web Server Gateway Interface       
web服务网关接口的配置文件，仅部署项目时使用      
            3. urls.py      
            项目的基础陆游配置文件，素有的动态路径必须先走该文件进行匹配      
        * settings.py文件介绍       
        1. BASE_DIR     
        用于绑定当前项目的绝对路径（动态计算出来的），所有文件都可以依赖此路径      
        2. DEBUG        
        * 用于配置Django项目的启动模式，取值：
        True表示开发环境中使用调试模式（用于开发中）        
False表示低昂钱项目运行在生产环境中（不启用调试）    
        3. ALLOWED_HOSTS        
        * 设置允许访问到本项目的网络地址列表，取值：        
         1、[]空列表，表示只有127.0.0.1，localhost能访问本项目      
2、['*']，表示任何网络地址都能访问当前项目        
3、['192.168.1.3','192.168.3.3']表示只有当前两个主机能访问当前项目      
__注意:__       
如果要在局域网其他主机也能访问此主机，启动方式应使用如下模式：      
`python3 manage.py runserver 0.0.0.0:5000 #指定网络设备所有主机都可以通过5000端口访问（需要加ALLOWED_HOSTS=['*']
        4. INSTALLED_APPS           
        指定当前项目中安装的应用列表     
        5. MIDDLEWARE       
        用于注册中间件      
        6. TEMPLATES        
        用于指定模版的配置信息      
        7. DATABASES        
        用于指定数据的配置信息      
        8. LANGUAGE_CODE        
        用于指定语言配置        
        取值："en-us"英文，"zh-Hans"中文        
        9. TIME_ZONE        
        用于指定当前服务器端时区        
        取值："UTC"世界标准时间，"Asia/Shanghai"中国时区        
        10. ROOT_URLCONF        
        用于配置根级url配置'项目名.url'