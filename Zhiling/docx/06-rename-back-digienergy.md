# 06 — 实验室名改回 DigiEnergy Lab（保留具身智能叙事）

状态：in-progress（本地已改，等用户本地确认后 push） ｜ 标签：digienergy-lab,rebrand,about,logo ｜ 日期：2026-11-13

## 背景
实验室站 `Chokurei/eies-lab-site` 于 11-13 提交 `385a7ba`：实验室改名 DigiEnergy Lab，**研究叙事仍是 Embodied Intelligence in Energy Systems**；logo 换成 "DigiEnergy Lab" 字标 + 原副标题，三色条不变；站点不再用 "Laboratory for ..." 全称。页脚标语用 "Digital intelligence … / 数字智能"（`417b621`）。网址仍是 `https://chokurei.github.io/eies-lab-site/`。

## 用户要求
个人主页回到 DigiEnergy Lab，只做局部调整；括号里的全称改为 **Laboratory for Digital Intelligence in Energy Systems**，中文相应改（取 **能源数字智能实验室**，"数字智能"沿用实验室站页脚译法）。

## 做了什么
1. **侧栏 logo** → `images/digienergy_lab_logo.svg`：以实验室站 `assets/media/logo.svg`（Inter 实时文字）为准。`Lab-Design/site/logo_vector/DigiEnergy_Lab_logo_on-light.svg` 是转路径版，但排版是早一版（标题 x=412.77/字号 111.83，色带缩放 0.75063），按坐标差给 title/line1/line2 加 transform、色带缩放改 0.7511、viewBox 改 `72 72 1153 294` 对齐 logo.svg。2x 渲染逐像素比对：差异只在轮廓边缘 1px 抗锯齿，字形位置/大小一致
2. **about.md**：实验室行改为 "DigiEnergy Lab … (Laboratory for Digital Intelligence in Energy Systems, 能源数字智能实验室) at UEX, PolyU"；招生行、Research Thrusts 引言链接文字、Services Director 行的 EIES Lab → DigiEnergy Lab
3. **未改**：研究陈述与 3 个 thrust（实验室站同样保留具身智能叙事）；行内小图标 `eies_lab_symbol.svg` 与 favicon `eies_*`（三色条与新 logo 相同，只是文件名带 eies）；`eies_lab_logo.svg` 已不引用，保留未删

## 验证
本地 build 后页面 0 处 "EIES"；括号全称正确；侧栏/行内图标引用正确；首屏截图正常。
