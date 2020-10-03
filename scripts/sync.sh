#!/bin/bash
cd /content/sequential_sentence_classification/git/allennlp
git pull origin development
cd /content/sequential_sentence_classification
python change_file.py
