# 🚀 作业批改 APP - 5 分钟部署指南

## 第一步：在 GitHub 创建仓库

1. 打开 **https://github.com/new**
2. 填写：
   - **Repository name:** `homework-grader-app`
   - **Description:** 作业批改助手 - Kivy Android APP
   - **Public** 或 **Private**（随你）
   - ❌ **不要勾选** "Add a README file"
   - ❌ **不要勾选** ".gitignore"  
   - ❌ **不要勾选** "Choose a license"
3. 点击 **Create repository**

---

## 第二步：运行部署命令

打开 **终端**（Terminal），复制粘贴以下命令：

```bash
# 1. 进入项目目录
cd ~/Desktop/homework_grader_app

# 2. 设置 Git 用户信息（替换成你的）
git config user.name "你的 GitHub 用户名"
git config user.email "你的 GitHub 邮箱"

# 3. 初始化并提交
git init
git branch -M main
git add .
git commit -m "Initial commit: 作业批改 APP"

# 4. 连接 GitHub 仓库（替换成你的用户名）
git remote add origin https://github.com/你的用户名/homework-grader-app.git

# 5. 推送代码
git push -u origin main
```

---

## 第三步：等待编译完成

1. 推送成功后，打开你的仓库页面
2. 点击 **Actions** 标签
3. 你会看到 **"Build Android APK"** 正在运行（黄色圆圈）
4. 等待 **20-30 分钟**（首次需要下载 Android SDK）
5. 绿灯 ✅ 后，点击构建记录
6. 在页面底部找到 **Artifacts** → 点击 `homework-grader-apk` 下载

---

## 第四步：安装到手机

1. 解压下载的 ZIP 文件，得到 `.apk` 文件
2. 通过微信/QQ/数据线传到手机
3. 打开 APK 安装
4. 如果提示"未知来源"，允许安装
5. 启动 APP！🎉

---

## 📋 常见问题

### Q: Git 提示 "Permission denied"？
```bash
# 用 HTTPS 方式（推荐）
git remote set-url origin https://github.com/你的用户名/homework-grader-app.git
```

### Q: 编译失败怎么办？
- 点击 Actions 中失败的构建
- 查看日志，截图发给我
- 我来帮你解决

### Q: 如何更新 APP？
```bash
# 修改代码后
cd ~/Desktop/homework_grader_app
git add .
git commit -m "修复 XXX"
git push

# 云端会自动重新编译！
```

---

**搞定！开始上传吧！** 🚀

遇到问题随时告诉我～
