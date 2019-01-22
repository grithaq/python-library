from pathlib import Path
import os

path = Path(os.getcwd())
npath = path.joinpath('zizi')

# print(path)
# print(npath.parts)
# print(npath.name)

# for idx, dirz in enumerate(path.iterdir()):
#     print(idx, dirz)
#
for idx, file in enumerate(path.glob('*.zip')):
    print(idx,file)
#
# pp = list(path.glob('*.py'))
# for line in pp[0].open():
#     print(line)