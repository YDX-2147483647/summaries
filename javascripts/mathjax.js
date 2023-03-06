// https://squidfunk.github.io/mkdocs-material/reference/mathjax/

window.MathJax = {
    loader: {
        load: [
            '[tex]/ams',
            '[tex]/mathtools',
            '[tex]/physics',
        ],
    },
    tex: {
        packages: {
            '[+]': [
                'ams',
                'mathtools',
                'physics',
            ],
        },
        autoload: {
            gensymb: ['degree', 'celsius', 'ohm', 'micro'],
        },
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true,
    },
    options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex",
    },
}

document$.subscribe(() => {
    MathJax.typesetPromise()
})
