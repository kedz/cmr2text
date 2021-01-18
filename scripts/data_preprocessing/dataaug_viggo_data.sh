#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ $# -eq 0 ]
  then
    DATA_DIR=`pwd`/data
  else
    DATA_DIR=$1
fi
echo "Using default location: $DATA_DIR"

VIGGO_ORIG=$DATA_DIR/orig/Viggo
VIGGO_TRAIN_ORIG=$VIGGO_ORIG/viggo-train.csv
VIGGO_VALID_ORIG=$VIGGO_ORIG/viggo-valid.csv
VIGGO_TEST_ORIG=$VIGGO_ORIG/viggo-test.csv

VIGGO_OUTPUT=$DATA_DIR/Viggo
VIGGO_TRAIN=$VIGGO_OUTPUT/Viggo.train.jsonl
VIGGO_VALID=$VIGGO_OUTPUT/Viggo.valid.jsonl
VIGGO_VALID_AGG=$VIGGO_OUTPUT/Viggo.valid.agg.jsonl
VIGGO_TEST=$VIGGO_OUTPUT/Viggo.test.jsonl
VIGGO_TEST_AGG=$VIGGO_OUTPUT/Viggo.test.agg.jsonl
VIGGO_FREQ=$VIGGO_OUTPUT/Viggo.slot_filler.freqs.json
VIGGO_PHRASES=$VIGGO_OUTPUT/Viggo.phrases.jsonl
VIGGO_PHRASES_NOOL=$VIGGO_OUTPUT/Viggo.phrases.no-ol.jsonl

echo "Generate Viggo Phrase Data"
$SCRIPT_DIR/generate_phrases.py \
    Viggo \
    $VIGGO_FREQ \
    $VIGGO_TRAIN \
    $VIGGO_PHRASES \
    --procs 8

echo "Remove test set overlap..."
$SCRIPT_DIR/remove_overlap.py \
    Viggo \
    $VIGGO_PHRASES \
    $VIGGO_PHRASES_NOOL \
    $VIGGO_TEST


