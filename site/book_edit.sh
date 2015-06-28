#!/bin/bash
pushd . 
cd ~/Documents/Q/docs
cat book_to_merge.txt | mdmerge -o doing_physics.0.md --book -
sed 's|\.\.\/\.\.\/\.\./images|images|g' doing_physics.0.md | tee doing_physics.1.md
sed 's|\.\.\/\.\./images|images|g' doing_physics.1.md | tee doing_physics.2.md
sed 's|\.\./images|images|g' doing_physics.2.md | tee doing_physics.3.md
sed 's|\.\./pdfs|pdfs|g' doing_physics.3.md | tee doing_physics.4.md
perl -ne 'if ($_ =~ /^[\!]/){chomp} print' doing_physics.4.md | tee doing_physics.5.md
perl -ne '$_ =~ s/^[\!]..*\]/\!\[\]/; print' doing_physics.5.md | tee doing_physics.6.md
perl -ne 'if ($_ =~ /^[\!]\[[^\]].*[^\)]/){chomp} print' doing_physics.6.md | tee doing_physics.7.md
perl -ne '$_ =~ s/^[\!]\[[^\]]..*\]/\!\[\]/; print' doing_physics.7.md | tee doing_physics.8.md
perl -ne 'if ($_ =~ /^[\!]\[[^\]].*[^\)]/){chomp} print' doing_physics.8.md | tee doing_physics.9.md
perl -ne '$_ =~ s/^[\!]\[[^\]]..*\]/\!\[\]/; print' doing_physics.9.md | tee doing_physics.10.md
sed '/./,/^$/!d' doing_physics.10.md | tee doing_physics.md
perl -e '@f = 0..10; for $f (@f){unlink("doing_physics.$f.md");}'
popd
