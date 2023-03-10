# ð[Summaries](https://ydx-2147483647.github.io/summaries/)

åç§è¯¾ç¨çæ»ç»ãéè®°ç­ã

[![ci](https://github.com/YDX-2147483647/summaries/actions/workflows/ci.yml/badge.svg)](https://github.com/YDX-2147483647/summaries/actions/workflows/ci.yml)
[![RSS](https://img.shields.io/badge/RSS-valid-orange?logo=rss)](http://validator.w3.org/feed/check.cgi?url=https%3A//ydx-2147483647.github.io/summaries/feed_rss_updated.xml)

## ð¤æ¹è¿æ­¤é¡¹ç®

### âç®åä¿®æ¹

æ»å¨å°é¡µé¢æä¸æ¹ï¼å¯ç´æ¥è¯è®ºã

è¥æ³ä¿®æ¹åå®¹ï¼è¯·æä»¥ä¸æä½ã

1. åå»é¡µé¢å³ä¸è§çâç¼è¾æ­¤é¡µâðæé®ï¼è¿å¥ GitHub ç¸åºæºæä»¶ã
2. åå»å³ä¸è§âEdit this fileâðæé®ï¼ææ<kbd>E</kbd>ã
3. æç§æç¤º forkãç¼è¾ãæäº¤ pull requestã

### ð¤å¤æä¿®æ¹

1. åéæ¬ä»åºã

2. å®è£ä¾èµã

   ```shell
   $ just bootstrap
   ```

   è¿ä¼ä½¿ç¨`python -m pip`å®è£ä¸äºåã

   > **Note**
   >
   > [`just`](https://just.systems/man/en/chapter_1.html)æ¯ä¸ªå½ä»¤è¿è¡å¨ãè¥æ æ³å®è£ï¼å¯æå¨åè®¸`justfile`ä¸­çå½ä»¤ã

   > **Note**
   >
   > è¥æ³æå®ç¨åªä¸`python`ï¼è¯·åå»º[`.env`æä»¶](https://just.systems/man/en/chapter_26.html)ï¼åå¥`PYTHON = "/path/to/python"`ï¼ä¾å¦`PYTHON = "py -3.11"`æ`PYTHON = "./.venv/Scripts/python.exe"`ã

3. ç¼è¾ã

4. æ¬å°é¢è§ã

   ```shell
   $ just serve
   ```

   è¥ä½¿ç¨ VS Codeï¼è¿å¯ä»¥æ<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>è°ç¨ä»»å¡ã

## âå¯¼å¥ Markdown æ³¨æäºé¡¹

- `just normalize +FILES`.
- MathJax: `\N`, `\Z`, `\Q`, `\R`, `\C`.

  TeX/LaTeX â  (canonical) MathJax â  Typora. Not all commands are [supported](https://docs.mathjax.org/en/latest/input/tex/macros/).

  > **Note**
  >
  > Add the following to `window.MathJax.tex.packages` in [`mathjax.js`](./docs/javascripts/mathjax.js), then [undefined control sequences will generate error messages](https://docs.mathjax.org/en/latest/input/tex/extensions/noundefined.html).
  >
  > ```javascript
  > '[-]': ['noundefined']
  > ```

- Ordered list: 3 spaces â 2-space indent.
- `:material-eye-arrow-right:`, etc.
- assets

## ðè´è°¢

- [Python-Markdown](https://python-markdown.github.io/)
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [giscus](https://giscus.app/)
- [Mdx Truly Sane Lists](https://github.com/radude/mdx_truly_sane_lists)
- [MkDocs RSS plugin](https://guts.github.io/mkdocs-rss-plugin/)
- [Graphviz](https://www.graphviz.org/)
