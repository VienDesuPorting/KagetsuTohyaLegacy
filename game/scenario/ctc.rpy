init -3:
    $ sizes = 30
    image ctc_blink:
        yalign 0.8
        "image/ctc/ctc_blink/cursor-0.png"
        size(sizes, sizes)
        .15
        "image/ctc/ctc_blink/cursor-1.png"
        size(sizes, sizes)
        .15
        "image/ctc/ctc_blink/cursor-2.png"
        size(sizes, sizes)
        .15
        "image/ctc/ctc_blink/cursor-1.png"
        size(sizes, sizes)
        .15
        repeat

    image ctc_clear:
        yalign 0.8
        "image/ctc/ctc_claer/page-0.png"
        size(sizes, sizes)
        .15
        "image/ctc/ctc_claer/page-1.png"
        size(sizes, sizes)
        .15
        "image/ctc/ctc_claer/page-2.png"
        size(sizes, sizes)
        .15
        "image/ctc/ctc_claer/page-1.png"
        size(sizes, sizes)
        .15
        repeat

define config.nvl_page_ctc = "ctc_clear"
