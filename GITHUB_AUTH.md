# 🔐 GitHub 认证设置

## 问题
推送代码时需要 GitHub 认证。

## 解决方案（2 选 1）

### 方案 A：使用 Personal Access Token（推荐）

**步骤 1：创建 Token**
1. 打开 https://github.com/settings/tokens/new
2. 填写：
   - **Note:** `homework-grader-app`
   - **Expiration:** 选择 `90 days` 或 `No expiration`
   - **Scopes:** 勾选 `repo` (Full control of private repositories)
3. 点击 **Generate token**
4. **复制生成的 token**（以 `ghp_` 开头，只显示一次！）

**步骤 2：用 Token 推送**
打开终端，执行：
```bash
cd ~/Desktop/homework_grader_app
git push -u origin main
```
当提示输入密码时：
- **Username:** `bay552`
- **Password:** 粘贴刚才复制的 token（不会显示字符，正常）

---

### 方案 B：用 GitHub Desktop（最简单）

1. 打开 GitHub Desktop（如果没有，下载：https://desktop.github.com）
2. 登录你的 GitHub 账号
3. File → Add Local Repository → 选择 `~/Desktop/homework_grader_app`
4. 如果提示 "This directory does not appear to be a Git repository"，点击 **Create a repository**
5. 点击顶部 **Publish repository**
6. 点击 **Publish**
7. Done！✅

---

**推荐用方案 B**，图形化界面更简单，以后更新代码也方便！
