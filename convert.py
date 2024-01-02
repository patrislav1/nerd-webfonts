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
    'Iosevka',
    'Terminus',
    'Hack',
    'Monofur',
    'LiberationMono',
    'Go-Mono',
]

wfmd = open(Path.cwd() / 'webfonts.md', 'w')
baseurl = 'https://cdn.jsdelivr.net/gh/patrislav1/nerd-webfonts/'

for fam in font_families:
    print(f'Family: {fam}')
    wfmd.write(f'# {fam}\n\n')

    srcfiles = (startdir / fam).rglob('*Mono-*.ttf')
    destdir = Path.cwd() / fam
    destdir.mkdir(exist_ok=True)

    for srcfile in srcfiles:
        print(f'Loading {srcfile.name}')
        font = TTFont(srcfile)
        destfile = destdir / f'{srcfile.stem}.woff2'

        style = srcfile.stem.split('-')[-1]
        url = baseurl + str(destfile.relative_to(Path.cwd()))
        wfmd.write(f'  * [{style}]({url})\n')

        print(f'Converting to {destfile}')
        font.flavor = 'woff2'
        font.save(destfile)
    wfmd.write('\n')

wfmd.close()
