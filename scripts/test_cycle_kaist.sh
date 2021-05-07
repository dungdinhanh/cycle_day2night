#!/bin/bash

epochs=(150 170 "latest")
#epochs=(150 )
phases=( "test")
name="kaist1_cycle"

for epoch in "${epochs[@]}"
do
  for phase in "${phases[@]}"
  do
  cmd="python test.py --dataroot datasets/data/kaist1 --name ${name} --phase ${phase} --epoch ${epoch} --num_test 10000 --model cycle_gan"
  echo ${cmd}
  eval ${cmd}

  fideval="python -m pytorch_fid results/${name}/${phase}_${epoch}/images/fake_B results/${name}/${phase}_${epoch}/images/real_B --gpu 0  --batch 5 2> results/${name}/${phase}_${epoch}/fid.txt"
  echo ${fideval}
  eval ${fideval}
done
done
