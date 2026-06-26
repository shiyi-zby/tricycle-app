[app]

# 应用名称（英文）
title = 三轮车订货单
# 包名（必须三段英文小写，不能中文）
package.name = myapp
# 公司反向域名格式
package.domain = org.myapp
# 主程序文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
# 用到的依赖库，基础kivy就写kivy，多个用逗号分隔
requirements = python3,kivy
# 安卓SDK版本
android.api = 33
# 最低安卓版本
android.minapi = 21
# 应用版本号
version = 0.1

# 关闭隐私权限默认申请
android.permissions = INTERNET
android.accept_sdk_license = True