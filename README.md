# PDF 全文中文翻译 Skill

将 PDF 文档完整翻译为简体中文 Word，保留标题层级、列表、表格、引用、链接和联系方式，并执行逐页渲染质检。

适用于报告、手册、课程说明、政策文件、学术资料等长文档。

## 主要能力

- 按页提取 PDF 文本，并识别可能需要 OCR 的扫描页
- 全文翻译而不是摘要
- 长文档分段处理和断点保存
- 保留标题、列表、表格、脚注、网址和联系方式
- 将复杂横向图表重建为易读的中文表格
- 生成 A4 中文 DOCX
- 渲染全部页面，检查中文缺字、溢出和异常分页

## 安装

将仓库中的 `pdf-translate-zh` 文件夹复制到：

```text
~/.codex/skills/pdf-translate-zh
```

也可以在支持 Skills 的 GitHub CLI 中安装：

```bash
gh skill install <你的GitHub用户名>/pdf-translate-zh pdf-translate-zh --scope user
```

## 使用

在 Codex 中直接提出类似请求：

```text
用 $pdf-translate-zh 把这份 PDF 全文翻译成中文 Word。
```

也可以自然地说：

```text
把这个 PDF 全文翻译成中文，保留表格和章节层级，并做排版质检。
```

## 文件结构

```text
pdf-translate-zh/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── quality-checklist.md
└── scripts/
    ├── extract_pdf.py
    └── build_docx.py
```

## 环境要求

- Python 3
- `pypdf`
- `python-docx`
- 可用的 DOCX 渲染环境，例如 LibreOffice
- Codex 的 Documents Skill，用于最终渲染与视觉检查

## 隐私与版权

本仓库只包含工作流程和通用脚本，不包含用于测试的原始 PDF 或翻译成果。

处理私人或受版权保护的文件时，请确认你有权翻译、存储和分享相关内容。

## 许可证

[MIT License](LICENSE)
