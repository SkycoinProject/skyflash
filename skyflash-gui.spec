#!/usr/bin/env python3

import os

block_cipher = None

# datas for windows/linux
extrafiles = [
                ('skyflash/data/skyflash.qml', '.'),
                ('skyflash/data/skyflash.png', '.'),
            ]
if 'nt' in os.name:
    extrafiles.append(('win-build/dist/windows/flash.exe', '.'))

a = Analysis(['skyflash-gui.py'],
             binaries=[],
             datas=extrafiles,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

# Linux build
if 'posix' in os.name:
    exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='skyflash-gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False,
          icon='skyflash/data/skyflash.png'
          )

if 'nt' in os.name:
    exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='skyflash-gui',
          bootloader_ignore_signals=False,
          strip=False,
          console=False,
          debug=False,
          icon='skyflash/data/skyflash.ico',
          uac_admin=True
          )

    coll = COLLECT(exe,
           a.binaries,
           a.zipfiles,
           a.datas,
           strip=False,
           upx=False,
           name='skyflash-gui'
           )
