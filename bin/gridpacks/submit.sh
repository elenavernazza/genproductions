#! /bin/bash
sed -i "14s/.*/Queue 300 proc in ($1)/g" submit.jdl
mkdir -p $1_results/log
mkdir -p $1_results/lhe
chmod +x submit.jdl
chmod +x wrapper.sh
condor_submit submit.jdl 
