#!/bin/bash
# 🚀 一键部署作业批改 APP 到 GitHub

set -e

echo "======================================"
echo "📱 作业批改 APP - GitHub 部署脚本"
echo "======================================"
echo ""

cd ~/Desktop/homework_grader_app

# 1. 检查 git 配置
echo "📋 检查 Git 配置..."
if [ -z "$(git config user.email)" ]; then
    echo "⚠️  请设置 Git 邮箱："
    read -p "输入你的 GitHub 邮箱：" email
    git config user.email "$email"
fi

if [ -z "$(git config user.name)" ]; then
    echo "⚠️  请设置 Git 用户名："
    read -p "输入你的 GitHub 用户名：" name
    git config user.name "$name"
fi

echo "✅ Git 配置完成"
echo ""

# 2. 创建 .gitignore（如果不存在）
if [ ! -f .gitignore ]; then
    echo "📝 创建 .gitignore..."
    cat > .gitignore << 'EOF'
.buildozer/
bin/
*.pyc
__pycache__/
*.spec
.env
*.log
.DS_Store
EOF
fi

# 3. 初始化 Git（如果还没初始化）
if [ ! -d .git ]; then
    echo "🔄 初始化 Git 仓库..."
    git init
    git branch -M main
fi

# 4. 添加所有文件
echo "📦 准备文件..."
git add .

# 5. 提交
if ! git diff-index --quiet HEAD --; then
    echo "💾 提交更改..."
    git commit -m "Update: 作业批改 APP $(date +%Y-%m-%d)"
else
    echo "✅ 没有新的更改"
fi

# 6. 创建 GitHub 仓库
echo ""
echo "🌐 接下来请在 GitHub 上创建仓库："
echo "   1. 打开 https://github.com/new"
echo "   2. 仓库名称：homework-grader-app"
echo "   3. 选择 Public 或 Private"
echo "   4. ❌ 不要勾选 'Add a README file'"
echo "   5. 点击 'Create repository'"
echo ""
read -p "✅ 创建完成后，按回车继续..."

# 7. 获取远程仓库地址
echo "📎 输入仓库地址（从 GitHub 页面复制）："
echo "   格式：https://github.com/你的用户名/homework-grader-app.git"
read -p "仓库地址：" repo_url

echo "🔗 添加远程仓库..."
git remote add origin "$repo_url" || git remote set-url origin "$repo_url"

# 8. 推送
echo "🚀 推送到 GitHub..."
git push -u origin main

echo ""
echo "======================================"
echo "🎉 部署成功！"
echo "======================================"
echo ""
echo "📍 接下来："
echo "   1. 打开 https://github.com/你的用户名/homework-grader-app/actions"
echo "   2. 你会看到 'Build Android APK' 正在运行"
echo "   3. 等待 20-30 分钟，绿灯后下载 APK"
echo ""
echo "📚 详细说明请查看 DEPLOYMENT.md"
echo ""
