cd /root/zeilou.io/ && python3 main.py && npm run build
cd /root/zeilou.io/docs && cp -rf /root/zeilou.io/docs/.vuepress/dist/* /root/zeilou.io/docs/ && git pull origin master && git add -A && git commit -m "latest" && git push origin master && git push old master
