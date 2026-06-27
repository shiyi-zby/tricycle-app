[app]
title = TriApp
package.name = triapp
package.domain = org.tri.app
source.dir = .
# 把你用到的所有文件后缀都加上
source.include_exts = py,png,jpg,kv,atlas,ttf,xlsx
# 这里必须把你所有用到的第三方库全部写上，举例：
# 只用kivy就写：python3,kivy
# 如果用了KivyMD、图片处理就写：python3,kivy,kivymd,pillow
requirements = python3,kivy
android.api = 33
android.minapi = 21
android.ndk = 27
version = 0.1
# 加上存储权限，读写文件必备
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.skip_check = True

[buildozer]
log_level = 2