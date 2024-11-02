#!/bin/bash

sample=$1
fq1=${sample}_1.fastq.gz
fq2=${sample}_2.fastq.gz

echo "##START: `date`" > ${sample}.log.txt

#PROGRAMS
BWA="/usr/bin/bwa"
SAMTOOLS="/usr/local/bin/samtools"
JAVA="/usr/bin/java"
PICARD="/home/jiu/etc/picard/picard.jar"
GATK="/home/jiu/etc/gatk/gatk-4.5.0.0/gatk-package-4.5.0.0-local.jar"
SNPEFF="/home/jiu/Downloads/snpEff/snpEff.jar"

#RESOURCES
REFERENCE="/home/jiu/etc/reference/chr21.fa.gz"

#FILES
mapped_sam="${sample}.chr21.sam"
mapped_bam="${sample}.chr21.bam"
sorted_bam="${sample}.chr21.sorted.bam"
markdup_bam="${sample}.chr21.markdup.bam"
gvcf="${sample}.chr21.g.vcf.gz"
vcf="${sample}.chr21.vcf.gz"
annotated_vcf="${sample}.ann.vcf.gz"


#MAPPING to REF
${BWA} mem -t 1 -R "@RG\tID:${sample}\tSM:${sample}\tPL:platform" ${REFERENCE} ${fq1} ${fq2} > ${mapped_sam}

#SAM to BAM
${SAMTOOLS} view -Sb ${mapped_sam} > ${mapped_bam}

#BAM sorting
${SAMTOOLS} sort ${mapped_bam} -o ${sorted_bam}

#BAM indexing
${SAMTOOLS} index ${sorted_bam}

#Markduplicate
${JAVA} -jar ${PICARD} MarkDuplicates -I ${sorted_bam} -O ${markdup_bam} -M ${sample}.metrics.txt

#BAM indexing
${SAMTOOLS} index ${markdup_bam}

#Markdup BAM to GVCF
${JAVA} -jar ${GATK} HaplotypeCaller -I ${markdup_bam} -O ${gvcf} -R ${REFERENCE} -ERC GVCF

#GVCF to VCF
${JAVA} -jar ${GATK} GenotypeGVCFs -V ${gvcf} -O ${vcf} -R ${REFERENCE}

#Annotation
${JAVA} -jar ${SNPEFF} -v hg38 ${vcf} > ${annotated_vcf}

echo "##END: `date`" >> ${sample}.log.txt