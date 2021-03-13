# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/home/andrei/scripts/dotfiles/backup.py'],
             pathex=['/home/andrei/scripts/dotfiles'],
             binaries=[],
             datas=[],
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

a.datas += [('add.png','/home/andrei/scripts/dotfiles/add.png', "DATA")]      
a.datas += [('remove.png','/home/andrei/scripts/dotfiles/remove.png', "DATA")]     
a.datas += [('save.png','/home/andrei/scripts/dotfiles/save.png', "DATA")]     
a.datas += [('restore.png','/home/andrei/scripts/dotfiles/restore.png', "DATA")]  

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='backup',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
