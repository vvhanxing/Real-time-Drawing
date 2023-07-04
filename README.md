# Real-time-Drawing
Real-time Drawing


   #https://www.pinzixing.com/1160.html
 4  bash <(curl -s -L https://git.io/v2ray.sh)
    5  v2ray bbr
    6  history



 地址 (Address) = 104.168.194.140

 端口 (Port) = 65162

 用户ID (User ID / UUID) = 34878c97-c06c-43b6-8e06-c01927db8b92

 额外ID (Alter Id) = 0

 传输协议 (Network) = tcp

 伪装类型 (header type) = none





apt install nginx       sudo yum install -y nginx     https://developer.aliyun.com/article/1165954
cd //etc/nginx/
vim nginx.conf
################################################

pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 4096;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        listen       80;
        listen       [::]:80;
        server_name  139.224.116.216;
        root         /usr/share/nginx/html;
        location / {
            proxy_pass    http://127.0.0.1:5000;      # 本机:启动端口（此处端口与项目端口一致）
            proxy_set_header Host $host;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;


           proxy_http_version 1.1; # fixwebsocket connect error
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

        }


        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }
    }

############################################
   76  systemctl start nginx
   77  nginx -s reload


关闭后可以继续服务
yum -y install tmux

在线运行gpt
vim nginx.conf进入会话
先按下 ctrl+b 再按下 d。要恢复之前的会话，只需要执行 tmux attach

http://127.0.0.1:7860

df -h
  698  free
  699  ls -la
          swapoff -a
  700  fallocate -l 8G /swapfile
  701  mkswap /swapfile
  702  swapon /swapfile



安装conda 
conda config --append channels conda-forge
netstat -tunlp
kill -9 [pid]
