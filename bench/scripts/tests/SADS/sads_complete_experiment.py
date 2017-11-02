import sys, time, pprint
sys.path.append('../../..')

import tmtc
from tm import TM, Check
from tmtc import Tmtc
from tc.experiments import AbortExperiment, PerformSADSExperiment
from tc.comm import SendBeacon
from tc.fs import GetFileInfo, RemoveFile, RemoveFileIfExists, DownloadFile
from tools.remote_files import RemoteFileTools

tmtc = Tmtc()
checker = Check(tmtc)

# Remove SADS files if present
res = tmtc.send(RemoveFileIfExists('/', 'sads.photo_wing'))
print(res)
res = tmtc.send(RemoveFileIfExists('/', 'sads.exp'))
print(res)

# Be sure that no experiment is currently running
checker.check(TM.Experiments.CurrentExperimentCode, 'None', 0)

# Request SADS experiment and check whether is running
tmtc.send(PerformSADSExperiment())
checker.check(TM.Experiments.CurrentExperimentCode, 'SADS', 300)

# Wait till the experiment is finished
checker.check(TM.Experiments.CurrentExperimentCode, 'None', 1000)


# Get 'sads.exp'
# Request info about particular file
chosen_file = tmtc.send(GetFileInfo('/', 'sads.exp'))
pprint.pprint(chosen_file)

# Download file
chunks = tmtc.send(DownloadFile(chosen_file["File"], chosen_file["Chunks"]))

# Save file
RemoteFileTools.save_chunks('sads.exp.raw', chunks)

# Get 'sads.photo_wing'
# Request info about particular file
chosen_file = tmtc.send(GetFileInfo('/', 'sads.photo_wing'))
pprint.pprint(chosen_file)

# Download file
chunks = tmtc.send(DownloadFile(chosen_file["File"], chosen_file["Chunks"]))

# Save file
RemoteFileTools.save_chunks('sads.photo_wing.raw', chunks)
# Save photo
RemoteFileTools.save_photo('sads.photo_wing.jpg', chunks)
