#!/bin/bash
sed 's|\.\.\/\.\.\/\.\./images|images|g' $1 | tee $1.1.md
sed 's|\.\.\/\.\./images|images|g' $1.1.md | tee $1.2.md
sed 's|\.\./images|images|g' $1.2.md | tee $1.3.md
sed 's|\.\./pdfs|pdfs|g' $1.3.md | tee $1.4.md
perl -ne 'if ($_ =~ /^[\!]/){chomp} print' $1.4.md | tee $1.5.md
perl -ne '$_ =~ s/^[\!]..*\]/\!\[\]/; print' $1.5.md | tee $1.6.md
perl -ne 'if ($_ =~ /^[\!]\[[^\]].*[^\)]/){chomp} print' $1.6.md | tee $1.7.md
perl -ne '$_ =~ s/^[\!]\[[^\]]..*\]/\!\[\]/; print' $1.7.md | tee $1.8.md
perl -ne 'if ($_ =~ /^[\!]\[[^\]].*[^\)]/){chomp} print' $1.8.md | tee $1.9.md
perl -ne '$_ =~ s/^[\!]\[[^\]]..*\]/\!\[\]/; print' $1.9.md | tee $1.10.md
sed '/./,/^$/!d' $1.10.md | tee $1.md
perl -e '@f = 0..10; for $f (@f){unlink("$1.$f.md");}'
