# Etsy Listing Researcher 批量使用说明

这个技能适合一次处理多款 Etsy 产品：每个产品单独放在一个文件夹里，文件夹名称作为产品简称，图片作为该产品的输入资料。

## 一、文件夹准备

建议建立这样的目录：

```text
etsy-products/
├── floral-wristlet/
│   ├── front.jpg
│   ├── phone-use.webp
│   └── colors.png
├── pearl-phone-strap/
│   ├── product-1.jpg
│   └── detail.png
└── canvas-bag-charm/
    ├── main.jpg
    └── variants.webp
```

规则：

- 一个文件夹代表一款产品。
- 一个文件夹里的多张图片代表同一款产品的不同角度、颜色或细节。
- 支持 `.jpg`、`.jpeg`、`.png`、`.webp`、`.avif`、`.heic` 和 `.heif`。
- 文件夹名称就是产品简称，建议使用英文或中英结合，例如 `floral-wristlet`、`珍珠手机挂绳`。
- 不要把不同产品放在同一个文件夹里。

## 二、在另一台电脑拉取仓库

仓库地址：

<https://github.com/Even9111/ETSY->

在终端运行：

```bash
git clone https://github.com/Even9111/ETSY-.git
```

然后用 Codex 打开克隆后的 `ETSY-` 文件夹。技能位于：

```text
.agents/skills/etsy-listing-researcher
```

如果 Codex 没有立即识别技能，重启 Codex 后再试。

## 三、批量调用方法

在 Codex 聊天窗口输入 `$etsy-listing-researcher`，然后粘贴多个产品文件夹的绝对路径，例如：

```text
使用 $etsy-listing-researcher 批量处理以下产品文件夹：

/Users/你的用户名/etsy-products/floral-wristlet
/Users/你的用户名/etsy-products/pearl-phone-strap
/Users/你的用户名/etsy-products/canvas-bag-charm

每款产品都请进行 Etsy 公开竞品研究，并把完整上架资料表格保存回对应文件夹。
```

Windows 示例：

```text
使用 $etsy-listing-researcher 批量处理：

C:\Users\你的用户名\etsy-products\floral-wristlet
C:\Users\你的用户名\etsy-products\pearl-phone-strap
```

也可以一次粘贴多个路径，路径之间用换行分隔即可。不要只粘贴父文件夹，除非你明确要求技能扫描其中的产品子文件夹。

## 四、生成结果

每个产品的资料会保存回对应图片文件夹：

```text
floral-wristlet/
├── front.jpg
├── phone-use.webp
└── floral-wristlet_etsy_listing.xlsx
```

Excel 表格通常包含：

- `上架资料`：产品定位、标题、核心字段和完整概览
- `英文描述`：分段的可复制 Etsy 描述
- `13 Tags`：13 个搜索词、字符数和证据状态
- `SKU变体`：颜色、五金、图案和 SKU
- `竞品依据`：公开 Etsy 竞品链接、搜索词、公开信号、详情页观察和限制
- `发布检查`：尺寸、材质、标题长度、Tags、SKU 和图片检查

标题会控制在 135–140 个英文字符；Tags 固定 13 个且每个不超过 20 个英文字符；SKU 按实际颜色、图案和五金生成，通常不超过 20 个字符。

## 五、批量处理时的注意事项

- 技能会逐个文件夹独立分析，不会把不同产品的颜色、材质或尺寸混在一起。
- 如果某个文件夹没有图片，会跳过该文件夹并在聊天窗口报告原因。
- 已存在的 Excel 不会被覆盖，通常会生成 `_v2`、`_v3` 等版本。
- 图片不会被删除、重命名或移动。
- 竞品后台真实 Tags 和单品精确销量不公开，输出会明确区分 `verified`、`observed` 和 `recommended`。
- 如果材料、尺寸、手机兼容性或包装内容无法从图片确认，发布前需要人工核对。

## 六、推荐的批量提示词

```text
使用 $etsy-listing-researcher 批量处理以下文件夹：

把每个文件夹视为一个独立产品，读取其中所有产品图片，识别颜色、图案、结构、五金、用途和尺寸信息。

对每款产品进行 Etsy 公开搜索和详情页研究，综合长期高表现样本与近期活跃信号，生成：
1. 135–140 字符英文标题
2. 13 个 Etsy Tags，每个不超过 20 个英文字符
3. 按图片变体生成的 SKU
4. 带表情元素、并根据产品颜色和图案调整的英文描述
5. 类目和属性
6. 完整竞品链接依据
7. 发布前检查清单

资料表格分别保存回对应产品文件夹，不要覆盖原图片。

产品文件夹路径：
/Users/你的用户名/etsy-products/product-a
/Users/你的用户名/etsy-products/product-b
/Users/你的用户名/etsy-products/product-c
```
