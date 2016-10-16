#!/bin/bash

cd /home/shibhansh/Downloads/apache-opennlp-1.6.0/bin/
./opennlp POSTaggerTrainer -model en-pos-maxent.bin -lang en -data train_data_opennlp -encoding UTF-8
./opennlp POSTaggerEvaluator -model en-pos-maxent.bin -data test_data_opennlp -encoding utf-8