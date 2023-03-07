# 📔[Summaries](https://ydx-2147483647.github.io/summaries/)

各种课程的总结、随记等。

[![ci](https://github.com/YDX-2147483647/summaries/actions/workflows/ci.yml/badge.svg)](https://github.com/YDX-2147483647/summaries/actions/workflows/ci.yml)

## 🤝改进此项目

### ✍简单修改

滚动到页面最下方，可直接评论。

若想修改内容，请按以下操作。

1. 单击页面右上角的“编辑此页”📝按钮，进入 GitHub 相应源文件。
2. 单击右上角“Edit this file”🖉按钮，或按<kbd>E</kbd>。
3. 按照提示 fork、编辑、提交 pull request。

### 🤖复杂修改

1. 克隆本仓库。

2. 安装依赖。

   ```shell
   $ just bootstrap
   ```

   这会使用`python -m pip`安装一些包。

   > **Note**
   >
   > [`just`](https://just.systems/man/en/chapter_1.html)是个命令运行器。若无法安装，可手动允许`justfile`中的命令。

   > **Note**
   >
   > 若想指定用哪一`python`，请创建[`.env`文件](https://just.systems/man/en/chapter_26.html)，写入`PYTHON = "/path/to/python"`，例如`PYTHON = "py -3.11"`或`PYTHON = "./.venv/Scripts/python.exe"`。

3. 编辑。

4. 本地预览。

   ```shell
   $ just serve
   ```

   若使用 VS Code，还可以按<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>调用任务。

## ✅导入 Markdown 注意事项

- `just normalize +FILES`.
- MathJax: `\N`, `\Z`, `\Q`, `\R`, `\C`.
- Ordered list: 3 spaces → 2-space indent.
- `:material-eye-arrow-right:`, etc.
- assets

## 🌟致谢

- [Python-Markdown](https://python-markdown.github.io/)
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [giscus](https://giscus.app/)
- [Mdx Truly Sane Lists](https://github.com/radude/mdx_truly_sane_lists)
