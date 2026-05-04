# 📱 作业批改 APP - GitHub Actions 云端编译指南

## 🚀 快速开始

### 步骤 1: 创建 GitHub 仓库

```bash
cd ~/Desktop/homework_grader_app

# 初始化 git（如果还没初始化）
git init

# 创建 .gitignore
cat > .gitignore << EOF
.buildozer/
bin/
*.pyc
__pycache__/
*.spec
.env
EOF

# 添加所有文件
git add .

# 首次提交
git commit -m "Initial commit: Homework Grader App"
```

### 步骤 2: 推送到 GitHub

**方式 A: 使用 GitHub Desktop（推荐新手）**
1. 打开 GitHub Desktop
2. File → Add Local Repository → 选择 `homework_grader_app` 文件夹
3. Publish repository → 命名为 `homework-grader-app`
4. 点击 Publish

**方式 B: 使用命令行**
```bash
# 在 GitHub.com 创建一个新仓库（不要初始化 README）
# 然后执行：
git remote add origin https://github.com/你的用户名/homework-grader-app.git
git branch -M main
git push -u origin main
```

### 步骤 3: 触发云端编译

推送代码后，GitHub Actions 会**自动开始编译**！

1. 打开你的仓库页面
2. 点击 **Actions** 标签
3. 你会看到 "Build Android APK" 正在运行
4. 等待约 **20-30 分钟**（首次需要下载 Android SDK）

### 步骤 4: 下载 APK

编译完成后：

**方式 A: 从 Actions 下载**
1. 点击绿色 ✓ 的构建记录
2. 在页面底部找到 **Artifacts**
3. 点击 `homework-grader-apk` 下载
4. 解压后得到 `.apk` 文件

**方式 B: 手动触发（后续更新）**
1. Actions → Build Android APK → Run workflow
2. 选择分支 → 点击 Run workflow

### 步骤 5: 安装到手机

1. 将 APK 传到手机（微信文件传输助手 / 数据线）
2. 手机上打开 APK 安装
3. 如果提示"未知来源"，允许安装

---

## 📋 文件清单

```
homework_grader_app/
├── main.py              # 应用主界面
├── ai_grader.py         # AI 批改引擎
├── buildozer.spec       # Android 打包配置
├── requirements.txt     # Python 依赖
├── .github/
│   └── workflows/
│       └── build-apk.yml  # GitHub Actions 配置文件
└── .gitignore           # Git 忽略文件
```

---

## 🔧 常见问题

### Q1: 编译失败怎么办？
- 检查 Actions 日志，找到红色错误
- 常见原因：
  - `buildozer.spec` 配置问题
  - 依赖包版本冲突
  - Android SDK 下载超时（重试即可）

### Q2: 如何更新 APP？
```bash
# 修改代码后
git add .
git commit -m "修复 XXX 问题"
git push

# 云端会自动重新编译！
```

### Q3: 可以自定义 APP 名称和图标吗？
可以！编辑 `buildozer.spec`:
```spec
title = 作业批改助手
icon.filename = icon.png  # 把你的图标放进来
```

### Q4: 编译需要多久？
- 首次：**20-40 分钟**（下载 Android SDK）
- 后续：**10-15 分钟**（有缓存）

### Q5: APK 有多大？
约 **20-30 MB**（包含 Python 运行时和 Kivy）

---

## 📞 需要帮助？

遇到问题时：
1. 截图 Actions 的错误日志
2. 告诉我具体哪一步失败了
3. 我来帮你解决！

---

**编译成功后，你就有专属的 Android APP 啦！🎉**
