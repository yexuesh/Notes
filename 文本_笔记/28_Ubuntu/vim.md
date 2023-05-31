## 下载语法文件

```sh
wget https://raw.githubusercontent.com/vim-scripts/nginx.vim/master/syntax/nginx.vim -O ~/.vim/syntax/nginx.vim

# 创建用于加载 Nginx 语法文件的配置文件
touch ~/.vim/filetype.vim
# 编辑
```

```visual basic
au BufRead,BufNewFile /etc/nginx/*,/usr/local/nginx/*,/usr/local/etc/nginx/*,/usr/local/etc/nginx/conf.d/* if &ft == '' | setfiletype nginx | endif
```

