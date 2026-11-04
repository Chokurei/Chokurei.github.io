# 04 — 主页改用 EIES Lab 新叙事（替换 DigiEnergy）

状态：done（已 push） ｜ 标签：eies-lab,rebrand,about,logo,research,jekyll ｜ 日期：2026-11-04

## 目标
实验室由 DigiEnergy Lab 改名为 EIES Lab（Laboratory for Embodied Intelligence in Energy Systems，能源具身智能实验室），官网 `https://chokurei.github.io/eies-lab-site/`（独立仓库 `Chokurei/eies-lab-site`，源码在 `Incubator/Lab-Design/lab-site/`）。个人主页叙事、logo、链接同步到新实验室。

## 用户决定（11-04 讨论）
- Director 写 **EIES Lab, UEX, PolyU**
- chokurei.net 暂不用，所有实验室链接指向 `https://chokurei.github.io/eies-lab-site/`
- Research Topics 选**方案 A**：旧 T1–T5 收进实验室 3 个 thrust（研究方向），卡片用已发表成果作证据
- 侧栏放带文字的横版 logo；不加"成立实验室"的 news

## 做了什么
1. **logo**（以实验室仓库 `assets/media/logo.svg` 为准，Inter 字体 v2 版）：
   - 侧栏 `images/eies_lab_logo.svg` = `Lab-Design/site/logo_vector/EIES_Lab_logo_on-light.svg`（文字已转路径、纯黑）把 viewBox 裁成与 logo.svg 相同的 `72 72 1260 386`；与 logo.svg 用 Inter 渲染后叠加对比完全重合。用转路径版是因为 logo.svg 的文字靠网页加载 Inter、颜色是 currentColor，作为 `<img>` 会退回系统字体
   - about 行内 `images/eies_lab_symbol.svg` = logo.svg 里的三条色带（`logo_vector/EIES_Lab_symbol.svg` 是旧 v1 比例，不要用）
   - 11-04 初版误用了 `EIES_Lab_logo_transparent.png`（Lato v1 旧版），已删除
2. **侧栏** `_includes/author-profile.html`：换 EIES logo + 链接
3. **about.md**：
   - 研究陈述改为 Embodied Intelligence in Energy Systems / Energy–Information–Action 叙事
   - 实验室行改为 "I direct the EIES Lab … at UEX, PolyU"
   - 招生蓝字加链接到实验室 contact 页 + 方向词
   - `# 📝 Research Topics`（T1–T5）→ `# 📝 Research Thrusts`（T1 Perception / T2 World Models / T3 Decision & Control），措辞对齐实验室 `/research/` 页；配图复用 `topic_detection.png` / `topic_spatio.png` / `topic_resilience.gif`
   - Services：Director → EIES Lab, UEX, PolyU
4. **导航** `_data/navigation.yml`：Research Topics → Research，锚点 `/#-research-thrusts`
5. `_config.yml` description 错字 Assitant → Assistant

## 验证
- 本地 `jekyll build` 通过；生成页面 0 处 digienergy / chokurei.net 残留；新锚点 `-research-thrusts` 生效
- 实验室站 `/`、`/contact/`、`/research/` 线上均 200
- headless Chrome 截图检查首屏、三张卡片、Services 排版正常

## 遗留
- `topic_genai.png`、`topic_visual.gif`、`digienergy_*` 图片已不再被引用，按用户意见保留未删
- T3 只写"在研项目"，没有声称已有发表成果（与实验室文档"不夸大成熟度"原则一致）
