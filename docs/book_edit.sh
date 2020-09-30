#!/bin/bash
pushd . 
cd ~/workspace/Q/docs
cat book_to_merge.txt | /home/doug/anaconda3/bin/mdmerge -o doing_physics.md --book -
popd
