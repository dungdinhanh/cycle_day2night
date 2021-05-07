#!/bin/bash

name=$1

cmd="python sift_compare.py --input_gr results/kovan/${name}/test_latest/images/real_A/ \
--input_gen results/kovan/${name}/test_latest/images/real_B --output_file results/kovan/realA_realB.csv"

echo $cmd
eval $cmd

cmd="python sift_compare.py --input_gr results/kovan/${name}/test_latest/images/fake_B/ \
--input_gen results/kovan/${name}/test_latest/images/real_B --output_file results/kovan/fakeB_realB.csv"

echo $cmd
eval $cmd

cmd="python sift_compare.py --input_gr results/kovan/${name}/test_latest/images/fake_B/ \
--input_gen results/kovan/${name}/test_latest/images/real_A --output_file results/kovan/fakeB_realA.csv"

echo $cmd
eval $cmd

