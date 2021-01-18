# cmr2text
Repository for EMNLP paper in progress. Data preprocessing is almost finished.
Model code to come.

## Install source and external data.
```
pip install .  
# or if you want to edit the source code without rebuilding:
# pip install --editable .
python -c "import nltk; nltk.download('punkt')"
```

## Download preprocessed data or run preprocessing:
You can download the preprocessed data here: 
Alternatively you can run the following scripts.

### Install Stanford CoreNLP (for data augmentation) and start server.
We used version 3.9.2 but you could probably use a later version.
```
curl https://nlp.stanford.edu/software/stanford-corenlp-full-2018-10-05.zip \
  > /some/where/stanford-corenlp-full-2018-10-05.zip
unzip  /some/where/stanford-corenlp-full-2018-10-05.zip \
  -d /some/where/
```

The phrase-based data augmentation scheme described in the paper uses the
English constituent parser in the CoreNLP library. In order for the data
augmentations scripts to run successfully, the CoreNLP server must be running
on its default port. To do this, in another shell run:
```
cd /some/where/stanford-corenlp-full-2018-10-05
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer
```

### Download and Preprocess Data
```
./scripts/data_preprocessing/download.sh
# ViGGO data
./scripts/data_preprocessing/format_viggo_data.sh
./scripts/data_preprocessing/dataaug_viggo_data.sh
# E2E Challenge Data, set NPROCS to the number of processes you want to 
# use. E2E is large and the preprocessing takes a while.
NPROCS=12 ./scripts/data_preprocessing/format_e2e_data.sh
``` 
