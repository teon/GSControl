# -*- mode: python -*-

block_cipher = None
added_files = [
         ( 'blank', 'tcl'),
         ( 'blank', 'tk' )
         ]


a = Analysis(['file_source.py'],
             pathex=['D:\\Documents\\GitHub\\GSControl\\gnuradio\\downlink\\source'],
             binaries=added_files,
             datas=[],
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
          name='file_source',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='file_source')
