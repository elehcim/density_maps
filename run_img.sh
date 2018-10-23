#!/bin/bash

OUT_DIR=$1
DATA_DIR=../dataset/medium

for i in `ls $DATA_DIR/snap*[^.jpg]`; do
  echo $i; python generate_density_map.py -i $i -w 35 -p $OUT_DIR -r 1000 -t "0 -10 0" -d $OUT_DIR
done

python create_mat.py $OUT_DIR