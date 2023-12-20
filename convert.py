#!/usr/bin/env python3

from pathlib import Path
from fontTools.ttLib import TTFont

# Find all monospace fonts
startdir = Path.cwd() / 'nerd-fonts' / 'patched-fonts'
font_families = [
    'UbuntuMono',
    'RobotoMono',
    'SourceCodePro',
    'DejaVuSansMono',
]

for fam in font_families:
    print(f'Family: {fam}')
    srcfiles = (startdir / fam).rglob('*Mono-*.ttf')
    destdir = Path.cwd() / fam
    destdir.mkdir(exist_ok=True)

    for srcfile in srcfiles:
        print(f'Loading {srcfile.name}')
        font = TTFont(srcfile)
        
        destfile = destdir / f'{srcfile.stem}.woff2'
        print(f'Converting to {destfile}')
        font.flavor = 'woff2'
        font.save(destfile)

