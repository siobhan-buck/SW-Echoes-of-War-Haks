import os
import subprocess

nwsyncDir = 'nwsync'
if not os.path.exists(nwsyncDir):
    os.mkdir(nwsyncDir)

targetDir = '.'
targetDirs = []
for path in os.listdir(targetDir):
    if path.startswith('sw_'):
        targetDirs.append(os.path.join(targetDir, path))

p = subprocess.Popen(['nwn_nwsync_write', '--limit-file-size', '64', nwsyncDir] + targetDirs)
p.wait()
