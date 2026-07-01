# 02 — 添加 DigiEnergy Lab logo 与 favicon

状态：done ｜ 标签：logo,favicon,about,jekyll ｜ 日期：2026-07-01

## 目标
把实验室 logo（`logo/Image_20260701163357_18306_22.png`，等距 "DE" 立方体）加到主页，并替换网站 favicon。

## 做了什么
1. **侧边栏 logo**：`_includes/author-profile.html` 姓名/机构下方加居中 logo，点击跳 chokurei.net。原图 2.1MB → 压缩为 `images/digienergy_logo.png`（512px, ~104KB）。
2. **favicon 全套**：基于 logo 用 PIL 生成 `images/digienergy_*`（16/32/apple-touch-180/android-192/512/.ico）。为解决"太小看不清"，裁剪时用颜色掩码（排除灰色辅助线与阴影）裁到立方体主体，使 "DE" 填满图标。更新 3 处引用：`_includes/head.html`、`_includes/head/custom.html`、`images/site.webmanifest`。旧 favicon 文件保留未删。
3. **about 页行内图标**：`_pages/about.md` 的 "Visit my DigiEnergy Lab" 行内加小图标（现放在 "Lab" 后面，`height:1.4em`），整段仍为超链接。

## 关键点 / 坑
- 本地 `jekyll build` 报 SCSS `Invalid US-ASCII` → 是本地 locale 问题，构建时加 `LANG=en_US.UTF-8` 解决；线上 GitHub Pages 不受影响。
- `jekyll serve` 的 watch 在本环境不可靠（静态图片和 md 改动都不自动重建），需手动 `bundle exec jekyll build` 或直接 cp 到 `_site/`。
- `git push` 首次 HTTP 400 RPC failed → 设 `http.postBuffer 524288000` + `http.version HTTP/1.1` 后成功。

## 结果
已 push 到 origin/main（`5f69847..51a7088`），GitHub Pages 自动部署。
