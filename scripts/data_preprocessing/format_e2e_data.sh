#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

if [ $# -eq 0 ]
  then
    DATA_DIR=`pwd`/data
  else
    DATA_DIR=$1
fi
echo "Using default location: $DATA_DIR"

if [ -z ${NPROCS+x} ]; then 
    NPROCS=4 
fi
echo "Using $NPROCS processes."

E2E_ORIG=$DATA_DIR/orig/e2e
E2E_TRAIN_ORIG=$E2E_ORIG/train-fixed.no-ol.csv
E2E_VALID_ORIG=$E2E_ORIG/devel-fixed.no-ol.csv
E2E_TEST_ORIG=$E2E_ORIG/test-fixed.csv

E2E_OUTPUT=$DATA_DIR/E2E
E2E_TRAIN=$E2E_OUTPUT/E2E.train.jsonl
E2E_VALID=$E2E_OUTPUT/E2E.valid.jsonl
E2E_TRAIN_NOOL=$E2E_OUTPUT/E2E.train.no-ol.jsonl
E2E_VALID_NOOL=$E2E_OUTPUT/E2E.valid.no-ol.jsonl
E2E_VALID_NOOL_AGG=$E2E_OUTPUT/E2E.valid.no-ol.agg.jsonl

E2E_TEST_DHR=$E2E_OUTPUT/E2E.test.dhr19.jsonl
E2E_TEST_DHR_AGG=$E2E_OUTPUT/E2E.test.agg.dhr19.jsonl
E2E_TEST_OG=$E2E_OUTPUT/E2E.test.og.jsonl
E2E_TEST_OG_AGG=$E2E_OUTPUT/E2E.test.agg.og.jsonl

E2E_FREQ=$E2E_OUTPUT/E2E.slot_filler.freqs.json
E2E_PHRASES=$E2E_OUTPUT/E2E.phrases.jsonl
E2E_PHRASES_NOOL=$E2E_OUTPUT/E2E.phrases.no-ol.jsonl

echo "Formatting E2E training dataset..."
$SCRIPT_DIR/format_data.py E2E \
    $E2E_TRAIN_ORIG \
    $E2E_TRAIN \
    --procs $NPROCS

echo "Formatting E2E validation dataset..."
  $SCRIPT_DIR/format_data.py E2E \
      $E2E_VALID_ORIG \
      $E2E_VALID \
      --procs $NPROCS
  
  echo "Formatting E2E test dataset..."
  $SCRIPT_DIR/format_data.py E2E \
      $E2E_TEST_ORIG \
      $E2E_TEST_DHR \
      --procs $NPROCS \
      --test
  
  echo "Formatting E2E test dataset..."
  $SCRIPT_DIR/format_data.py E2E \
      $E2E_TEST_ORIG \
      $E2E_TEST_OG \
      --e2e-og \
      --procs $NPROCS \
      --test
  
  
  
  echo "Making E2E slot filler count data..."
  $SCRIPT_DIR/make_slot_filler_frequencies.py \
      E2E \
      $E2E_TRAIN \
      $E2E_FREQ
  
  echo "Adding E2E data derived orders (TRAIN) ..."
  $SCRIPT_DIR/add_simple_orders.py \
      E2E \
      $E2E_FREQ \
      $E2E_TRAIN 
  
  echo "Adding E2E data derived orders (VALID) ..."
  $SCRIPT_DIR/add_simple_orders.py \
      E2E \
      $E2E_FREQ \
      $E2E_VALID
  
  echo "Adding E2E data derived orders (TEST OG) ..."
  $SCRIPT_DIR/add_simple_orders.py \
      E2E \
      $E2E_FREQ \
      $E2E_TEST_OG --test
  
  echo "Adding E2E data derived orders (TEST DHR19) ..."
  $SCRIPT_DIR/add_simple_orders.py \
      E2E \
      $E2E_FREQ \
      $E2E_TEST_DHR --test
  
  echo "Remove test set overlap..."
  $SCRIPT_DIR/remove_overlap.py \
      E2E \
      $E2E_TRAIN \
      $E2E_TRAIN_NOOL \
      $E2E_VALID \
      $E2E_VALID_NOOL \
      $E2E_TEST_DHR
   
  echo "Aggregating validation dataset."
  $SCRIPT_DIR/aggregate_dataset.py \
      E2E \
      $E2E_VALID_NOOL \
      $E2E_VALID_NOOL_AGG
      
  echo "Aggregating test dataset."
  $SCRIPT_DIR/aggregate_dataset.py \
      E2E \
      $E2E_TEST_OG \
      $E2E_TEST_OG_AGG \
      --test 
  
  echo "Aggregating test dataset."
  $SCRIPT_DIR/aggregate_dataset.py \
      E2E \
      $E2E_TEST_DHR \
      $E2E_TEST_DHR_AGG \
      --test 
#    #
#    ##?echo "Generate E2E Phrase Data"
#    ##?$SCRIPT_DIR/generate_phrases.py \
#    ##?    E2E \
#    ##?    $E2E_FREQ \
#    ##?    $E2E_TRAIN \
#    ##?    $E2E_PHRASES \
#    ##?    --procs 32
#    ##?
#    ##?echo "Generate E2E Templates Data"
#    ##?$SCRIPT_DIR/generate_templates.py \
#    ##?    E2E \
#    ##?    $E2E_FREQ \
#    ##?    $E2E_TEMPLATES 
#    ##?
#    ##echo "Remove test set overlap..."
#    ##$SCRIPT_DIR/remove_overlap.py \
#    ##    E2E \
#    ##    $E2E_PHRASES \
#    ##    $E2E_PHRASES_NOOL \
#    ##    $E2E_TEMPLATES \
#    ##    $E2E_TEMPLATES_NOOL \
#    ##    $E2E_TEST_DHR
#    #
#    #  export MRT_DATASET=E2E
#    #  export MRT_DELEX=delex 
#    #  export MRT_TIE_EMB=false 
#    #  export MRT_ENC_INP=inc_freq
#    #  
#    #  plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#    #      --hp-MOD "dialog_planner_hps/E2E/train/cell=lstm_bi_enc_inp=inc_freq_lr=1e-05_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#    #      --hp-DAT $E2E_VALID_NOOL_AGG
#    #  
#    #  plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#    #      --hp-MOD "dialog_planner_hps/E2E/train/cell=lstm_bi_enc_inp=inc_freq_lr=1e-05_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#    #      --hp-DAT $E2E_TEST_OG_AGG
#    #  
#    #  plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#    #      --hp-MOD "dialog_planner_hps/E2E/train/cell=lstm_bi_enc_inp=inc_freq_lr=1e-05_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#    #      --hp-DAT $E2E_TEST_DHR_AGG
#    #  
#    #  exit
#    #  echo "Generating random mr data:"
#    #  MR_SIZES="3 4 5 6 7 8 9 10"
#    #  for N in $MR_SIZES; do
#    #      echo "    Generating random mr$N data..."
#    #      $SCRIPT_DIR/generate_random_data.py E2E $N \
#    #          $E2E_OUTPUT/E2E.random.mr$N.jsonl
#    #  
#    #      echo "    Adding E2E data derived orders..."
#    #          $SCRIPT_DIR/add_simple_orders.py \
#    #          E2E \
#    #          $E2E_FREQ \
#    #          $E2E_OUTPUT/E2E.random.mr$N.jsonl
#    #  
#    #      echo "    Adding E2E NLM derived orders..."
#    #      plumr $SCRIPT_DIR/dialog_planner.config.py run generate \
#    #          --hp-MOD "dialog_planner_hps/E2E/train/cell=lstm_bi_enc_inp=inc_freq_lr=1e-05_layers=1_ls=0.1/model_checkpoints/optimal.pkl" \
#    #          --hp-DAT "$E2E_OUTPUT/E2E.random.mr$N.jsonl"
#    #  done
