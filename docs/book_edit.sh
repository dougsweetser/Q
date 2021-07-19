#!/bin/bash
pushd . 
cd ~/workspace/Q/docs
cat book_to_merge.txt | /home/doug/anaconda3/bin/mdmerge -o doing_physics.md --book -
sed -i s'/^[#] /\\newpage\n\# /' doing_physics.md
sed -i s'/\.\.\/\.\.\/.\.\/images/images/' doing_physics.md
sed -i s'/\.\.\/\.\.\/images/images/' doing_physics.md
sed -i s'/\.\.\/images/images/g' doing_physics.md
sed -i s'/\.\.\/\.\.\/Stuff/Stuff/' doing_physics.md
sed -i s'/\.\.\/Stuff/Stuff/g' doing_physics.md
sed -i s'/.Stuff.pdfs.space-times-time_invariance.pdf.//g' doing_physics.md
sed -i s'/.EM_invariants.md.//g' doing_physics.md
sed -i s'/.problem_set_1.md.//g' doing_physics.md
sed -i s'/.*iframe.*//' doing_physics.md
popd
