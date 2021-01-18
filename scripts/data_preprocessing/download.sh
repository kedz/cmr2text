#!/bin/bash

printf 'Downloading Data \342\230\216 -> \360\237\222\277\n'

if [ $# -eq 0 ]
  then
    DATA_DIR=`pwd`/data
  else
    DATA_DIR=$1
fi
echo "Using default location: $DATA_DIR"

ORIG_VIGGO_DATA_DIR=$DATA_DIR/orig/viggo/
mkdir -p $ORIG_VIGGO_DATA_DIR
curl -s http://nldslab.soe.ucsc.edu/viggo/viggo-v1.zip > $ORIG_VIGGO_DATA_DIR/viggo-v1.zip

unzip $ORIG_VIGGO_DATA_DIR/viggo-v1.zip -d $ORIG_VIGGO_DATA_DIR
rm $ORIG_VIGGO_DATA_DIR/viggo-v1.zip
echo "ViGGO dataset downloaded to: $ORIG_VIGGO_DATA_DIR"

ORIG_E2E_DATA_DIR=$DATA_DIR/orig/e2e
mkdir -p $ORIG_E2E_DATA_DIR

curl -L -s https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/train-fixed.no-ol.csv \
    > $ORIG_E2E_DATA_DIR/train-fixed.no-ol.csv
curl -L -s https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/devel-fixed.no-ol.csv \
    > $ORIG_E2E_DATA_DIR/devel-fixed.no-ol.csv
curl -L -s https://github.com/tuetschek/e2e-cleaning/raw/master/cleaned-data/test-fixed.csv \
    > $ORIG_E2E_DATA_DIR/test-fixed.csv

echo "E2E Challenge (Cleaned) dataset downloaded to: $ORIG_E2E_DATA_DIR"
