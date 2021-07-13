#!/bin/bash
pushd . 
cd ~/workspace/Q/docs
cat book_to_merge.txt | /home/doug/anaconda3/bin/mdmerge -o doing_physics.md --book -
sed -i s'/^[#] /\\newpage\n\# /' doing_physics.md
sed -i s'/\.\.\/\.\.\/.\.\/images/images/' doing_physics.md
sed -i s'/\.\.\/\.\.\/images/images/' doing_physics.md
sed -i s'/\.\.\/images/images/g' doing_physics.md
popd
