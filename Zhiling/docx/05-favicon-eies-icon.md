# 05 — favicon 换成 EIES Lab 三色 icon

状态：done ｜ 标签：favicon,eies-lab,seo ｜ 日期：2026-11-08

## 目标
Google 搜索结果的 favicon 按主机名（`chokurei.github.io`）取，只认根目录个人主页的图标，所以实验室网站 `chokurei.github.io/eies-lab-site/` 在搜索结果里也显示 "GZL"。把个人主页 favicon 换成实验室三色 icon，两边统一。

## 做了什么
1. 源图：`Incubator/Lab-Design/lab-site/assets/media/icon.png`（实验室网站同一张 512px icon），用 PIL 生成 `images/eies_*`：favicon 16/32、`.ico`（16/32/48）、android-chrome 192/512（透明底）、apple-touch-icon 180（白底，iOS 透明会填黑）。
2. 改 3 处引用：`_includes/head.html`、`_includes/head/custom.html`、`images/site.webmanifest`（顺带修正 manifest 原先指向不存在的 `/android-chrome-*.png`）。
3. `head.html` 新增一行 192×192 `rel=icon`：Google 要求 favicon 边长是 48 的倍数，16/32/180 都不是。
4. GZL 原图标文件（`favicon-*` / `apple-touch-icon.png` / `favicon.ico`）保留未删，回退只需改回三处引用。

## 结果
push 后 GitHub Pages 自动部署；Google 搜索结果的图标要等重新抓取（几天到几周），可在 Search Console 请求重新编入首页。
