# 07 — 全称改为 Digital and Embodied，侧栏换新 logo

状态：本地已改，待用户确认后 push ｜ 标签：digienergy-lab,about,logo,narrative ｜ 日期：2026-11-13

## 背景
实验室站 11-13 晚又改了 3 个提交（`5f2e7e5` logo 与首页大标题、`ad5caed` 使命/thrust/场景文案、`e2ddb34` 页脚标语）：叙事从 "Embodied" 变成 "Digital & Embodied"，首页大标题是 "From Digital to Embodied Intelligence"，使命改为 "Intelligence is moving from digital perception and prediction to embodied decision and action"。logo 副标题改成两行 "Digital & Embodied Intelligence / in Energy Systems"，三色条缩放 0.66657。三个 thrust 的名字没变。

## 做了什么
1. about.md 实验室行全称改为 **Laboratory for Digital and Embodied Intelligence in Energy Systems**（正文写 "and"，logo 里才用 "&"）
2. 侧栏 logo `images/digienergy_lab_logo.svg` 换成 `Lab-Design/site/logo_vector/DigiEnergy_Lab_logo_on-light.svg`（转曲版，坐标与实验室站 logo.svg 一致），viewBox 改成和 logo.svg 一样裁到墨迹：`71.0 66.25 1092.75 259.5`；alt/title 改为 "Digital & Embodied Intelligence in Energy Systems"
3. 用户要求 logo 与上方 "The Hong Kong Polytechnic University" 左右对齐：logo 宽度从 100% 改为 `12.06em`（= 15px Trebuchet MS 下 "The Hong Kong Polytechnic" 墨迹宽 180.9px），保留 `max-width: 100%`。1400 宽 3x 截图逐列比对：文字与 logo 墨迹左右边缘同为第 225/767 列
4. 研究陈述第一句改为 "Digital and Embodied Intelligence in Energy Systems: how intelligence moves from digital perception and prediction to embodied decision and action, and how energy dynamics and physical constraints shape this transition."；Research Thrusts 引言补 "from digital perception and modeling to embodied action"（与实验室站一致，用户已认可）

## 已知未处理
- 1024–1279px 宽度时侧栏只有 136px，学校名折成 3 行（最宽 99px），logo 受 max-width 限制为 136px，这一档不对齐（太窄再缩字就看不清了）
- 窄屏（<1024）侧栏横排，logo 紧贴 "University" 没有间距（之前就有，原先 logo 宽到 598px）
