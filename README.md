# ⚙ qndxx_auto_srcipt

### 1. 简介 📃

cqupt qndxx 自动学习脚本，每周自动学习一次。

### 2.使用方式 📖

#### a. Github Action运行

使用 Github Action 实现 CI/CD，实现每周打卡

1. fork本仓库
2. 自行对微信重庆共青团的qnddx程序进行抓包，获取`OPENID`
3. 给本仓库secrets环境变量添加字段`OPENID`
4. 已默认设置Github Action每周UTC时间周二点打卡，如需更改，请自行给改action配置文件中的schedule中的cron字段，注意时间单位为UTC。

*注：没写时间随机扰动，因为GitHub Action的这个定时执行是不准时的，经常延迟2-3h以上，相当于扰动了。*