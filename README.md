stream - livestreaming controller
===

Based on the work from
[Ben Wilber](https://benwilber.github.io/streamboat.tv/nginx/rtmp/streaming/2016/10/22/implementing-stream-keys-with-nginx-rtmp-and-django.html)

Quick-start
---
1. Add "stream" to your INSTALLED\_APPS setting
2. Run `./manage.py migrate` to update the databases
3. Access [the admin panel](http://127.0.0.1:8000/admin/)
4. Add a stream key to a user
