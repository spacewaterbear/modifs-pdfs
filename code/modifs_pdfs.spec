# -*- mode: python ; coding: utf-8 -*-
import sys

icon = 'src/main/icons/Icon.ico' if sys.platform == 'win32' else 'src/main/icons/linux/128.png'

a = Analysis(
    ['src/main/python/main.py'],
    pathex=['src/main/python'],
    datas=[
        ('src/main/resources/base', 'resources'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Modifs PDFs',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    icon=icon,
)
