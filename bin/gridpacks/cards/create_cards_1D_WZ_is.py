#!/usr/bin/env python

import os

if __name__ == "__main__":

    switchOn = ['21','24','25','28','32','45','46','48','49','53','54','55','56','57','58']

    params = [(' 1', 'ceWPh'),
              (' 2', 'ceBPh'),
              (' 3', 'cuGPh'),
              (' 4', 'cuWPh'),
              (' 5', 'cuBPh'),
              (' 6', 'cdGPh'),
              (' 7', 'cdWPh'),
              (' 8', 'cdBPh'),
              (' 9', 'cHudPh'),
              ('10', 'ceHPh'),
              ('11', 'cuHPh'),
              ('12', 'cdHPh'),
              ('13', 'cledqPh'),
              ('14', 'cquqd1Ph'),
              ('15', 'cquqd8Ph'),
              ('16', 'clequ1Ph'),
              ('17', 'clequ3Ph'),
              ('19', 'cG'),
              ('20', 'cGtil'),
              ('21', 'cW'),
              ('22', 'cWtil'),
              ('23', 'cH'),
              ('24', 'cHbox'),
              ('25', 'cHDD'),
              ('26', 'cHG'),
              ('27', 'cHGtil'),
              ('28', 'cHW'),
              ('29', 'cHWtil'),
              ('30', 'cHB'),
              ('31', 'cHBtil'),
              ('32', 'cHWB'),
              ('33', 'cHWBtil'),
              ('34', 'ceHAbs'),
              ('35', 'cuHAbs'),
              ('36', 'cdHAbs'),
              ('37', 'ceWAbs'),
              ('38', 'ceBAbs'),
              ('39', 'cuGAbs'),
              ('40', 'cuWAbs'),
              ('41', 'cuBAbs'),
              ('42', 'cdGAbs'),
              ('43', 'cdWAbs'),
              ('44', 'cdBAbs'),
              ('45', 'cHl1'),
              ('46', 'cHl3'),
              ('47', 'cHe'),
              ('48', 'cHq1'),
              ('49', 'cHq3'),
              ('50', 'cHu'),
              ('51', 'cHd'),
              ('52', 'cHudAbs'),
              ('53', 'cll'),
              ('54', 'cll1'),
              ('55', 'cqq1'),
              ('56', 'cqq11'),
              ('57', 'cqq3'),
              ('58', 'cqq31'),
              ('59', 'clq1'),
              ('60', 'clq3'),
              ('61', 'cee'),
              ('62', 'cuu'),
              ('63', 'cuu1'),
              ('64', 'cdd'),
              ('65', 'cdd1'),
              ('66', 'ceu'),
              ('67', 'ced'),
              ('68', 'cud1'),
              ('69', 'cud8'),
              ('70', 'cle'),
              ('71', 'clu'),
              ('72', 'cld'),
              ('73', 'cqe'),
              ('74', 'cqu1'),
              ('75', 'cqu8'),
              ('76', 'cqd1'),
              ('77', 'cqd8'),
              ('78', 'cledqAbs'),
              ('79', 'cquqd1Abs'),
              ('80', 'cquqd8Abs'),
              ('81', 'clequ1Abs'),
              ('82', 'clequ3Abs')
              ]

    proc_ID = 'WZeu_is'


    for order in [('LI', 1), ('QU', 2)]:
        for param in params:
            if param[0] not in switchOn: continue
            prefix = '{0}_{1}_{2}'.format(proc_ID, param[1], order[0])
            dirname = './' + prefix + '/'
            if os.path.isdir(dirname):
                os.system('rm -rf ' + dirname)
            os.mkdir(dirname)
            extramodels = dirname + prefix + '_extramodels.dat'
            runcard = dirname + prefix + '_run_card.dat'
            proccard = dirname + prefix + '_proc_card.dat'
            os.system('cp ./extramodels.dat ' + extramodels)
            os.system('cp ./run_card.dat ' + runcard)
            with open(proccard, 'w') as f:
                f.write('set group_subprocesses Auto\n')
                f.write('set ignore_six_quark_processes False\n')
                f.write('set loop_optimized_output True\n')
                f.write('set complex_mass_scheme False\n')
                f.write('define p = g u c d s b u~ c~ d~ s~ b~\n')
                f.write('define j = p\n')
                f.write('define l+ = e+ mu+ ta+\n')
                f.write('define l- = e- mu- ta-\n')
                f.write('define vl = ve vm vt\n')
                f.write('define vl~ = ve~ vm~ vt~\n')
                f.write('import model SMEFTsim_A_U35_MwScheme_UFO_v3_1-{0}_massless\n'.format(param[1]))
                f.write('generate    p p > w+ z > e+ e- mu+ vm  j j QCD=0 NP=1 NP^2=={0} SMHLOOP=0\n'.format(order[1]))
                f.write('add process p p > w- z > e+ e- mu- vm~ j j QCD=0 NP=1 NP^2=={0} SMHLOOP=0\n'.format(order[1]))
                f.write('output ' + prefix)
