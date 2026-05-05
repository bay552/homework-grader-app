#!/bin/bash
# 本地打包 Android APK 脚本
# 使用 Docker 确保环境一致性

set -e

echo "🚀 开始打包 APK..."

# 1. 进入项目目录
cd ~/homework-grader-app

# 2. 检查 buildozer.spec 是否存在
if [ ! -f buildozer.spec ]; then
    echo "❌ buildozer.spec 不存在!"
    exit 1
fi

# 3. 使用 Docker 运行 buildozer（推荐方式）
echo "📦 使用 Docker 运行 buildozer..."

docker run --rm -v $(pwd):/home/user/hostcwd \
    -v $(pwd)/.buildozer:/home/user/.buildozer \
    -v $(pwd)/.gradle:/home/user/.gradle \
    kivy/buildozer:latest \
    buildozer -v android debug

# 4. 检查 APK 是否生成
if [ -f bin/*.apk ]; then
    echo "✅ APK 打包成功!"
    ls -lh bin/*.apk
    echo ""
    echo "📱 APK 位置：$(pwd)/bin/"
else
    echo "❌ APK 生成失败"
    exit 1
fi
