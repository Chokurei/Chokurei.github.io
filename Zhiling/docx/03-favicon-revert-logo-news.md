# 03 — favicon 回退 GZL + logo 换黄顶版 + 新增 2026.07 news

状态：done ｜ 标签：favicon,logo,news,about,jekyll ｜ 日期：2026-08-02

## 目标
承接 task 02，用户后续三项微调：①favicon 换回原 GZL；②logo 换成新黄顶版；③News 加 3 条 2026.07。

## 做了什么
1. **favicon 回退 GZL**：把 `head.html`、`head/custom.html`、`site.webmanifest` 三处引用改回原始文件名（`favicon-*.png` / `apple-touch-icon.png` / `favicon.ico` / `android-chrome-*`）。task 02 生成的 `digienergy_*` 图标文件保留未删。侧栏 + about 行内的 logo 保持不变。push `51a7088..4dd653f`。
2. **logo 换黄顶版**：用户更新源图 `logo/未命名作品 4.png`（DE 立方体，顶面橙→黄）。用 PIL 裁边+缩放重生成 `images/digienergy_logo.png`（512px），**同名覆盖**，主页两处引用自动更新，无需改 HTML。push `4dd653f..030d0ea`。
3. **新增 3 条 2026.07 news**（`_pages/about.md` News 区顶部）：
   - 🎤 "Enchanting Beautiful China, Beautiful HK" Experience Day 代表发言（HK）
   - 🏆 Nexus High Citation Award（牛津）— global BIPV facade/rooftop 论文
   - 🎤 Harbin Ice and Snow World（冰雪大世界）AI & Data Science 演讲
   用户随后两轮在 IDE 里自行精简措辞。push `030d0ea..3e22b36` → `3e22b36..c447c0d`。

## 结果
全部已 push origin/main（最新 `c447c0d`），GitHub Pages 自动部署。
