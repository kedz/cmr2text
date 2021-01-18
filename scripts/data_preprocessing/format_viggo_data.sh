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
VIGGO_TEMPLATES=$VIGGO_OUTPUT/Viggo.templates.jsonl
VIGGO_PHRASES_NOOL=$VIGGO_OUTPUT/Viggo.phrases.no-ol.jsonl
VIGGO_TEMPLATES_NOOL=$VIGGO_OUTPUT/Viggo.templates.no-ol.jsonl

echo "Formatting Viggo training data..."
$SCRIPT_DIR/format_data.py Viggo \
    $VIGGO_TRAIN_ORIG \
    $VIGGO_TRAIN

echo "Formatting Viggo validation data..."
$SCRIPT_DIR/format_data.py Viggo \
    $VIGGO_VALID_ORIG \
    $VIGGO_VALID

echo "Formatting Viggo testing data..."
$SCRIPT_DIR/format_data.py Viggo \
    $VIGGO_TEST_ORIG \
    $VIGGO_TEST \
    --test \

echo "Making Viggo slot filler count data..."
$SCRIPT_DIR/make_slot_filler_frequencies.py \
    Viggo \
    $VIGGO_TRAIN \
    $VIGGO_FREQ

echo "Adding Viggo data derived orders..."
$SCRIPT_DIR/add_simple_orders.py \
    Viggo \
    $VIGGO_FREQ \
    $VIGGO_TRAIN

echo "Adding Viggo validation data derived orders..."
$SCRIPT_DIR/add_simple_orders.py \
    Viggo \
    $VIGGO_FREQ \
    $VIGGO_VALID

echo "Adding Viggo test data derived orders..."
$SCRIPT_DIR/add_simple_orders.py \
    Viggo \
    $VIGGO_FREQ \
    $VIGGO_TEST

echo "Aggregating validation dataset."
$SCRIPT_DIR/aggregate_dataset.py \
    Viggo \
    $VIGGO_VALID \
    $VIGGO_VALID_AGG 
    
echo "Aggregating test dataset."
$SCRIPT_DIR/aggregate_dataset.py \
    Viggo \
    $VIGGO_TEST \
    $VIGGO_TEST_AGG \
    --test 

#  export MRT_DATASET=Viggo
#  export MRT_DELEX=delex 
#  export MRT_TIE_EMB=false 
#  export MRT_ENC_INP=inc_freq
#  #
#  #plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#  #    --hp-MOD "experiments/Viggo/dialog_planner/train/cell=lstm_uni_enc_inp=inc_freq_lr=0.0001_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#  #    --hp-DAT "data/Viggo/Viggo.valid.agg.jsonl"
#  plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#      --hp-MOD "experiments/Viggo/dialog_planner/train/cell=lstm_uni_enc_inp=inc_freq_lr=0.0001_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#      --hp-DAT "data/Viggo/Viggo.test.agg.jsonl"
#  exit
#  echo "Generating random mr data:"
#  MR_SIZES="3 4 5 6 7 8 9 10"
#  for N in $MR_SIZES; do
#      echo "    Generating random mr$N data..."
#      $SCRIPT_DIR/generate_random_data.py Viggo $N \
#          $VIGGO_OUTPUT/Viggo.random.mr$N.jsonl
#  
#      echo "    Adding Viggo data derived orders..."
#          $SCRIPT_DIR/add_simple_orders.py \
#          Viggo \
#          $VIGGO_FREQ \
#          $VIGGO_OUTPUT/Viggo.random.mr$N.jsonl
#  
#      echo "    Adding Viggo NLM derived orders..."
#      plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#          --hp-MOD "experiments/Viggo/dialog_planner/train/cell=lstm_uni_enc_inp=inc_freq_lr=0.0001_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#          --hp-DAT "$VIGGO_OUTPUT/Viggo.random.mr$N.jsonl"
#  done
