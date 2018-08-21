# -*- mode: python -*-

block_cipher = None
added_files = [
         ( 'blank', 'tcl'),
         ( 'blank', 'tk' )
         ]


a = Analysis(['file_source.py'],
             pathex=['C:\\Users\\begreen\\Documents\\GitHub\\GSControl\\gnuradio\\downlink\\source'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='file_source',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
