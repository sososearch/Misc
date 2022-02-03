#Creating folder structures

import os
base_path = "C:\\Users\\1"
dir_basename = "_"
for index in range (0o1, 101):
  os.makedirs("{}{}{}".format(base_pat, dir_basename, index))
