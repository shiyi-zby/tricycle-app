[app]
title = TriApp
package.name = triapp
package.domain = org.tri.app
source.dir = .
# 包含所有用到的资源格式
source.include_exts = py,png,jpg,kv,atlas,ttf,xlsx
# 锁定固定版本，不要用最新版，移动端极易崩溃
requirements = python3,kivy==2.2.0,kivymd==1.1.1,pillow==9.5.0
android.api = 33
android.minapi = 21
android.ndk = 25b
version = 0.1
# 最全存储+网络权限，适配所有安卓10以上机型
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.skip_check = True

[buildozer]
log_level = 2