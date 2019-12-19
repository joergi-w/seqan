#!/usr/bin/env python
"""Execute the tests for snp_store.

The golden test outputs are generated by the script generate_outputs.sh.

You have to give the root paths to the source and the binaries as arguments to
the program.  These are the paths to the directory that contains the 'projects'
directory.

Usage:  run_tests.py SOURCE_ROOT_PATH BINARY_ROOT_PATH
"""
import logging
import os.path
import sys

# Automagically add util/py_lib to PYTHONPATH environment variable.
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                    '..', '..', 'util', 'py_lib'))
sys.path.insert(0, path)

import seqan.app_tests as app_tests

def main(source_base, binary_base):
    """Main entry point of the script."""

    print('Executing test for snp_store')
    print('=========================')
    print()

    ph = app_tests.TestPathHelper(
        source_base, binary_base,
        'apps/snp_store/tests')  # tests dir

    # ============================================================
    # Auto-detect the binary path.
    # ============================================================

    path_to_program = app_tests.autolocateBinary(
      binary_base, 'apps/snp_store', 'snp_store')

    # ============================================================
    # Built TestConf list.
    # ============================================================

    # Build list with TestConf objects, analoguely to how the output
    # was generated in generate_outputs.sh.
    conf_list = []

    # We prepare a list of transforms to apply to the output files.  This is
    # used to strip the input/output paths from the programs' output to
    # make it more canonical and host independent.
    ph.outFile('-')  # To ensure that the out path is set.
    transforms = [
        app_tests.RegexpReplaceTransform("#.*snp_store.exe", "#snp_store"),
        app_tests.RegexpReplaceTransform("#[^ ]+snp_store", "#snp_store"),
        app_tests.ReplaceTransform(ph.inFile(''), ''),
        app_tests.ReplaceTransform(ph.outFile(''), ''),
        ]

    # ============================================================
    # First Section.
    # ============================================================

    # App TestConf objects to conf_list, just like this for each
    # test you want to run.
    # default
    conf = app_tests.TestConf(
        program=path_to_program,
        redir_stdout=ph.outFile('snp_store_default.stdout'),
        args=[ph.inFile('human-chr22-inf2.fa'),
              ph.inFile('human-reads2.gff'),
              '-o', ph.outFile('snps_default.vcf'),
              '-id', ph.outFile('indels_default.gff'),],
        to_diff=[(ph.inFile('snp_store_default.stdout'),
                  ph.outFile('snp_store_default.stdout')),
                 (ph.inFile('snps_default.vcf'),
                  ph.outFile('snps_default.vcf'),
                  transforms),
                 (ph.inFile('indels_default.gff'),
                  ph.outFile('indels_default.gff',))])
    conf_list.append(conf)

    # test 2
    conf = app_tests.TestConf(
        program=path_to_program,
        redir_stdout=ph.outFile('snp_store_realign.stdout'),
        args=[ph.inFile('human-chr22-inf2.fa'),
              ph.inFile('human-reads2.sam'),
              '-re',
              '-o', ph.outFile('snps_realign.vcf'),
              '-id', ph.outFile('indels_realign.gff')],
        to_diff=[(ph.inFile('snp_store_realign.stdout'),
                  ph.outFile('snp_store_realign.stdout')),
                 (ph.inFile('snps_realign.vcf'),
                  ph.outFile('snps_realign.vcf'),
                  transforms),
                 (ph.inFile('indels_realign.gff'),
                  ph.outFile('indels_realign.gff'))])
    conf_list.append(conf)

    # test 3
    conf = app_tests.TestConf(
        program=path_to_program,
        redir_stdout=ph.outFile('snp_store_realign_m1mp1oa.stdout'),
        args=[ph.inFile('human-chr22-inf2.fa'),
              ph.inFile('human-reads2.sam'),
              '-it', str(1), '-re', '-oa', '-mp', str(1), '-m', 'maq', '-hq',
              '-o', ph.outFile('snps_realign_m1mp1oa.vcf'),
              '-id', ph.outFile('indels_realign_m1mp1oa.gff')],
        to_diff=[(ph.inFile('snp_store_realign_m1mp1oa.stdout'),
                  ph.outFile('snp_store_realign_m1mp1oa.stdout')),
                 (ph.inFile('snps_realign_m1mp1oa.vcf'),
                  ph.outFile('snps_realign_m1mp1oa.vcf'),
                  transforms),
                 (ph.inFile('indels_realign_m1mp1oa.gff'),
                  ph.outFile('indels_realign_m1mp1oa.gff'))])
    conf_list.append(conf)

    # test 4
    conf = app_tests.TestConf(
        program=path_to_program,
        redir_stdout=ph.outFile('snp_store_realign_m0mp1oa.stdout'),
        args=[ph.inFile('human-chr22-inf2.fa'),
              ph.inFile('human-reads2.gff'),
              '-it', str(2), '-re', '-oa', '-mp', str(1), '-hq',
              '-o', ph.outFile('snps_realign_m0mp1oa.vcf'),
              '-id', ph.outFile('indels_realign_m0mp1oa.gff')],
        to_diff=[(ph.inFile('snp_store_realign_m0mp1oa.stdout'),
                  ph.outFile('snp_store_realign_m0mp1oa.stdout')),
                 (ph.inFile('snps_realign_m0mp1oa.vcf'),
                  ph.outFile('snps_realign_m0mp1oa.vcf'),
                  transforms),
                 (ph.inFile('indels_realign_m0mp1oa.gff'),
                  ph.outFile('indels_realign_m0mp1oa.gff'))])
    conf_list.append(conf)

    # test 5
    conf = app_tests.TestConf(
        program=path_to_program,
        redir_stdout=ph.outFile('snp_store_realign_m0mp1oa_it1ipt01.stdout'),
        args=[ph.inFile('human-chr22-inf2.fa'),
              ph.inFile('human-reads2.sam'),
              '-it', str(1), '-ipt', str(0.1), '-osc', '-re', '-oa', '-hq',
              '-o', ph.outFile('snps_realign_m0mp1oa_it1ipt01.vcf'),
              '-id', ph.outFile('indels_realign_m0mp1oa_it1ipt01.gff')],
        to_diff=[(ph.inFile('snp_store_realign_m0mp1oa_it1ipt01.stdout'),
                  ph.outFile('snp_store_realign_m0mp1oa_it1ipt01.stdout')),
                 (ph.inFile('snps_realign_m0mp1oa_it1ipt01.vcf'),
                  ph.outFile('snps_realign_m0mp1oa_it1ipt01.vcf'),
                  transforms),
                 (ph.inFile('indels_realign_m0mp1oa_it1ipt01.gff'),
                  ph.outFile('indels_realign_m0mp1oa_it1ipt01.gff'))])
    conf_list.append(conf)



    # ============================================================
    # Execute the tests.
    # ============================================================
    failures = 0
    for conf in conf_list:
        res = app_tests.runTest(conf)
        # Output to the user.
        print(' '.join(['snp_store'] + conf.args), end=' ')
        if res:
             print('OK')
        else:
            failures += 1
            print('FAILED')

    # Cleanup.
    ph.deleteTempDir()

    print('==============================')
    print('     total tests: %d' % len(conf_list))
    print('    failed tests: %d' % failures)
    print('successful tests: %d' % (len(conf_list) - failures))
    print('==============================')
    # Compute and return return code.
    return failures != 0


if __name__ == '__main__':
    sys.exit(app_tests.main(main))
