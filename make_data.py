import os

FILE_DIR_GDRIV = "repos"
FULL_PATHS = []
MAX_CHAR_LENGTH = 512
MIN_CHAR_LENGTH = 100
NEWINLINECHAR = "<N>"

for dirpath, dirnames, filenames in os.walk(FILE_DIR_GDRIV):
  for f in filenames:
    fullpath = os.path.join(dirpath, f)
    # print(fullpath)
    FULL_PATHS.append(fullpath)
print(len(FULL_PATHS))

# now read data form FULL_PATHS 
#read single file and replace with new line 

with open("./test.txt","a") as f:
  for fpath in FULL_PATHS:
    try:
      d = open(fpath, "r", encoding="utf8").read()
      fd = d.replace("\n", NEWINLINECHAR)
      print(d)
      if 100  < len(d) <= MAX_CHAR_LENGTH:
        f.write(fd+'\n')
        print(fd)
        # break
      else:
        sd = fd.split(f"{NEWINLINECHAR}{NEWINLINECHAR}")
        substr = ""
        for split in sd:
          substr += split + f"{NEWINLINECHAR}{NEWINLINECHAR}"
          if MIN_CHAR_LENGTH <= len(substr) <= MAX_CHAR_LENGTH:
            f.write(substr+'\n')
            substr=""
        # break
    except Exception as e:
      print(str(e))





# for fPath in FULL_PATHS:

#   d = open(fPath, "r", encoding="utf8").read()
#   forma_data = d.replace("\n", NEWINLINECHAR)
#   if MIN_CHAR_LENGTH < len(d) <= MAX_CHAR_LENGTH:

#         # pass
#     # print(d)
#     # print(len(d))

#     print(forma_data)
#     # f.write(forma_data+'\n')

#     break
#   else:
#     save_data = d.split(f"{NEWINLINECHAR}{NEWINLINECHAR}")
#     substring = ""
#     for split in save_data:
#       print(split)
#       break



# with open("../src/text_.py","a") as f:
#   for fPath in FULL_PATHS:
#       d = open(fPath, "r", encoding="utf8").read()
#       forma_data = d.replace("\n", NEWINLINECHAR)      
#       if 100 < len(d) <= MAX_CHAR_LENGTH:
#         # pass
#         # print(d)
#         # print(len(d))
       
#         # print(forma_data)
#         f.write(forma_data+'\n')


#         break
#       else:
#         save_data = d.split(f"{NEWINLINECHAR}{NEWINLINECHAR}")
#         substring = ""
#         for split in save_data:
#           print(split)
#           break

