#!/bin/bash
pushd . 
cd ~/workspace/Q/docs
cat book_to_merge.txt | ~/venv-gh/bin/mdmerge -o doing_physics.md --book -
popd
