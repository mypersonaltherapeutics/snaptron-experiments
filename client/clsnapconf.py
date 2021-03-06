#!/usr/bin/env python2.7

# Copyright 2016, Christopher Wilks <broadsword@gmail.com>
#
# This file is part of Snaptron.
#
# Snaptron is free software: you can redistribute it and/or modify
# it under the terms of the 
# Creative Commons Attribution-NonCommercial 4.0 
# International Public License ("CC BY-NC 4.0").
#
# Snaptron is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# CC BY-NC 4.0 license for more details.
#
# You should have received a copy of the CC BY-NC 4.0 license
# along with Snaptron.  If not, see 
# <https://creativecommons.org/licenses/by-nc/4.0/legalcode>.

DS_SRAV2='srav2'
DS_SRAV1='srav1'
DS_GTEX='gtex'
DS_TCGA='tcga'
DS_SUPERMOUSE='supermouse'
DS_ENCODE='encode1159'
SERVICE_URL='http://snaptron.cs.jhu.edu'
BUFFER_SIZE_BYTES=1024*1024
CACHE_SAMPLE_METADTA=True
#TODO use python tmp
TMPDIR='../snaptron_tmp'
FIELD_ARGS={'region':['"chr#:start-end"',str,None,'either a simple genomic region (e.g. chr1:1-1000) or a gene fusion pair (e.g. EML4-ALK)'],
      'filters':['"coverage_sum>=5&annotated=1"',str,None,'one or more junction specific thresholds/filters'], 
      'metadata':['"design_description: cortex"',str,None,'one or more sample specific filters passed to Lucene (using the Lucene query langage)'],
      'samples':['"0,1,5,200"',str,None,'one or more comma delimited sample IDs filter junctions by'],
      'contains':['1',str,None,'search for only junctions which have both their genomic coordinates within (inclusive) the specified region'],
      'exact':['1',str,None,'search for only junctions which have both their genomic coordinates matching exactly the specified region\'s start/end coordinates'],
      'either':['2',str,None,'search for only junctions which have one or the other of their genomic coordinates within (inclusive) of the specified region, 1=left coordinte;2=right coordinate']}
SAMPLE_IDS_COL=12
SAMPLE_COUNT_COL=13
SAMPLE_SUM_COL=14
SAMPLE_AVG_COL=15
SAMPLE_MED_COL=16
INTRON_ID_COL=1
INTERVAL_CHR_COL=2
INTERVAL_START_COL=3
INTERVAL_END_COL=4
MIN_EXON_SIZE = 1
LEFT_ANNOT_COL=10
RIGHT_ANNOT_COL=11
FULL_ANNOT_COL=7
EXON_COUNT_COL=9
PSI_MIN_READS=20
BULK_LIMIT=50
BULK_QUERY_DELIMITER='|||'
ID_LIMIT=100
JX_ENDPOINT="snaptron"
SAMPLE_ENDPOINT="sample"
GENES_ENDPOINT="genes"
EXONS_ENDPOINT="exons"
#normalization related config parameters
#recount's gene normalization scaling factor
NORMAL_RECOUNT_GENE_TARGET = 40 * 1000000
#our junction scaling factor: 40 million 100-base reads
NORMAL_RECOUNT_JX_TARGET = NORMAL_RECOUNT_GENE_TARGET * 100
#based on average junction coverage across 43332 SRAv2 samples, rounded
NORMAL_JXCOV_TARGET = 3953678
RECOUNT_NORM='recount'
JX_NORM='jxcov'
#map to the various scaling factors we can use depending on 1) normalization type and 2) endpoint (genes, junctions)
RECOUNT_FACTOR_MAP={GENES_ENDPOINT:NORMAL_RECOUNT_GENE_TARGET,JX_ENDPOINT:NORMAL_RECOUNT_JX_TARGET}
JX_FACTOR_MAP={JX_ENDPOINT:NORMAL_JXCOV_TARGET}
NORM_FACTOR_MAP={RECOUNT_NORM:RECOUNT_FACTOR_MAP,JX_NORM:JX_FACTOR_MAP}
#map to the various normalization dividers depending on 1) normalization type and 2) datasource
AUC_COL_MAP={DS_SRAV2:78,DS_GTEX:308,DS_TCGA:11,DS_SUPERMOUSE:55,DS_ENCODE:37}
JXCOV_COL_MAP={DS_SRAV2:90,DS_GTEX:320,DS_TCGA:859,DS_SUPERMOUSE:53,DS_ENCODE:39}
NORM_DIVISOR_COL_MAP={RECOUNT_NORM:AUC_COL_MAP,JX_NORM:JXCOV_COL_MAP}
