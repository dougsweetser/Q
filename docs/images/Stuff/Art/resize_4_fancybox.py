#!/usr/bin/env python
"""
Outmatically makes 3 file sizes.

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
file_root = file_name[:-4].replace('_big', '')
file_ext = file_name[-3:]
id_out = sp.check_output(["identify", file_name])
match = re.search(r'\d\d+', str(id_out))
image_width = float(match.group(0))

widths = {'small': ARGS['--small_width'], 'big': ARGS['--big_width'], 
          'nine':900}
new_file = {}

for name, width in widths.items():
    scale = float(width) / float(image_width) * 100

    if file_ext == 'gif':
        new_file.update({name: "{fr}_{w}.gif".format(fr=file_root, w=width)})

    else:
        new_file.update({name: "{fr}_{w}.png".format(fr=file_root, w=width)})

    sp.run(["convert", file_name, "-resize", "{s}%".format(s=scale),
           new_file[name]])

fancy = '''
<a class="fancybox-button" rel="fancybox-button" 
    href="../../images/Stuff/Art/{bf}"> 
<img src="../../images/Stuff/Art/{sf}" /> </a>'''.format(bf=new_file['big'],
                                                         sf=new_file['small'])
print(fancy)
