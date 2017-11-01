import telecommand.fs
import response_frames.file_system
from tools.remote_files import RemoteFileTools


class ListFiles(object):
    def __init__(self, path):
        self.path = path

    def send(self, tmtc):
    	frames = tmtc.send_tc_with_multi_response(telecommand.fs.ListFiles, response_frames.file_system.FileListSuccessFrame, self.path)
    	files = []
        for f in frames:
            files.extend(RemoteFileTools.parse_file_list(f))
        return files


class GetFileInfo(object):
    def __init__(self, path, filename):
        self.filename = filename
        self.path = path
        self.lf = ListFiles(path)

    def send(self, tmtc):
    	file_list = self.lf.send(tmtc)
    	
    	try:
    		return (item for item in file_list if item["File"] == self.filename).next()
    	except StopIteration:
        	return None
