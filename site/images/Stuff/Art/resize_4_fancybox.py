#!/usr/bin/env python
"""
usage: resize_4_fancybox.py -f FILE [-s SMALL] [-b BIG]

optional arguments:
 -f FILENAME --file_name FILENAME   image file to resize
 -s SMALL --small_width SMALL       [default: 150]
 -b BIG --big_width BIG         [default: 750]
"""

import re
import subprocess as sp
from docopt import docopt

if __name__ == "__main__":
    ARGS = docopt(__doc__)

file_name = ARGS['--file_name']
small_width = float(ARGS['--small_width'])
big_width = float(ARGS['--big_width'])

id_out = sp.check_output(["identify", file_name])
match = re.search(r'\d\d+', str(id_out))
image_width = float(match.group(0))

small_scale = small_width / image_width * 100
big_scale = big_width / image_width * 100

file_root = file_name[:-4]
file_ext = file_name[-3:]

if file_ext == 'gif':
    small_file = "{fr}_{sw}.gif".format(fr=file_root, sw=small_width)
    big_file = "{fr}_{bw}.gif".format(fr=file_root, bw=big_width)

else:
    small_file = "{fr}_{sw}.png".format(fr=file_root, sw=small_width)
    big_file = "{fr}_{bw}.png".format(fr=file_root, bw=big_width)

sp.run(["convert", file_name, "-resize", "{ss}%".format(ss=small_scale),
        small_file])
sp.run(["convert", file_name, "-resize", "{bs}%".format(bs=big_scale),
        big_file])

fancy = '''
<a class="fancybox-button" rel="fancybox-button" 
    href="../../images/Stuff/Art/{bf}"> 
<img src="../../images/Stuff/Art/{sf}" /> </a>'''.format(bf=big_file,
                                                         sf=small_file)
print(fancy)
