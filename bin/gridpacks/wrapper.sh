#! /bin/bash
mkdir tmp
cd tmp
source /cvmfs/cms.cern.ch/cmsset_default.sh
mv ../$1_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz .
tar -axf $1_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz
date
echo $1
echo this is the $2-th job
./runcmsgrid.sh 2000 $2 1
date
mv *lhe ..
rm -rf tmp
