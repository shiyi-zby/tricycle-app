[app]
title = TriApp
package.name = triapp
package.domain = org.tri.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,xlsx
requirements = python3,kivy,kivymd,pillow
android.api = 33
android.minapi = 21
android.ndk = 27
version = 0.1
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.skip_check = True

[buildozer]
log_level = 2