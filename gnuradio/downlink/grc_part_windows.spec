# -*- mode: python -*-

block_cipher = None

added_files = [
         ( 'pyinstaller_hack', 'tk'),
         ( 'pyinstaller_hack', 'tcl')
         ]

a = Analysis(['grc_part.py'],
             pathex=['D:\\Documents\\GitHub\\GSControl\\gnuradio\\downlink'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='grc_part',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='grc_part')