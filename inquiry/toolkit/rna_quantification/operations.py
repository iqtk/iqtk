# Copyright 2017 The Regents of the University of California
#
# Licensed under the BSD-3-clause license (the "License"); you may not
# use this file except in compliance with the License.
# You are provided a copy of the license in LICENSE.md at the root of
# this project.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import apache_beam as beam
import logging

from inquiry.framework import task
from inquiry.framework import util
from inquiry.framework.util import localize
from inquiry.framework.util import localize_set


class TopHat(task.ContainerTask):
    """Run the TopHat spliced read aligner.

    Given a collection of read pairs, performs split-read alignment using
    bowtie in a manner conducive to detecting indels and splice isoforms.

    Example:

        reads_a = fc_create(p, args.cond_a_pairs)

        th_a = tophat(reads_a,
                      args=args,
                      tag='cond_b')

    Args:
        pc (PCollection): The input collection of FASTQ reads.
        args (dict): The argument context.
        label (str): The operation label.
        tag (str): The sub-operation tag to distinguish operations of same type
        debug (bool): Whether to run in debug mode.
        ref_fasta (str): The reference fasta file.
        genes_gtf (str): The reference gene annotation.


    Returns:
        bool: The return value. True for success, False otherwise.

    Todo:
        * Refactor

    .. _TopHat documentation
       https://cole-trapnell-lab.github.io/projects/tophat/
    """

    def __init__(self, args, ref_fasta, genes_gtf, tag=None):
        """Initialize a containerized task."""
        self.ref_fasta = ref_fasta
        self.genes_gtf = genes_gtf
        container = task.ContainerTaskResources(
            disk=60, cpu_cores=4, ram=8,
            image='gcr.io/jbei-cloud/tophat:0.0.1')
        super(TopHat, self).__init__(task_label='tophat',
                                     args=args,
                                     container=container)

    def process(self, read_pair):

        ref_local_stem = localize(self.ref_fasta).split('.')[0]
        ref_gs_stem = self.ref_fasta.split('.fa')[0]
        ref_files = util.gsutil_expand_stem(ref_gs_stem)

        inputs = list(set().union([self.genes_gtf, read_pair[0], read_pair[1]],
                                  ref_files))

        # If the bowtie2 reference indexes are not present, generate them.
        logging.info([thing for thing in ref_files if thing.endswith('.bt2l')])
        if len([thing for thing in ref_files if thing.endswith('.bt2l')]) == 0:
            logging.error('The provided reference must be accompanied by '
                          'bowtie2 index files sharing the same stem '
                          'as the provided reference path, i.e. '
                          '%s' % ref_gs_stem)
            # TODO: Conditionally perform the indexing if the right indexes
            # are not present.

        cmd = util.Command(['tophat',
                          '-p', self.container.cpu_cores,
                          '-G', localize(self.genes_gtf),
                          '-o', self.out_path,
                          ref_local_stem,
                          localize(read_pair[0]),
                          localize(read_pair[1])])

        yield self.submit(cmd.txt, inputs=inputs,
                          expected_outputs=[{'name': 'accepted_hits.bam',
                                             'file_type': 'bam'},
                                            {'name': 'align_summary.txt',
                                             'file_type': 'txt'},
                                            {'name': 'deletions.bed',
                                             'file_type': 'bed'},
                                            {'name': 'insertions.bed',
                                             'file_type': 'bed'},
                                            {'name': 'junctions.bed',
                                             'file_type': 'bed'},
                                            {'name': 'prep_reads.info',
                                             'file_type': 'info'}])


class Cufflinks(task.ContainerTask):
    """Run the cufflinks gene isoform assembler.

    Example:

        cuff = cufflinks(align, args=args)

    Args:
        pc (PCollection): The input collection of aligned bams.
        args (dict): The argument context.
        label (str): The operation label.
        tag (str): The sub-operation tag to distinguish operations of same type
        debug (bool): Whether to run in debug mode.

    Returns:
        PCollection: A collection of files generated by this operation.

    Todo:
        * Refactor

    .. _Google Python Style Guide:
       http://google.github.io/styleguide/pyguide.html
    """

    def __init__(self, args):
        """Initialize a containerized task."""
        container = task.ContainerTaskResources(
            disk=60, cpu_cores=4, ram=8,
            image='gcr.io/jbei-cloud/cufflinks:0.0.1')
        super(Cufflinks, self).__init__(task_label='cufflinks',
                                        args=args,
                                        container=container)

    def process(self, file_path):

        cmd = util.Command(['cufflinks',
                       '-p', self.container.cpu_cores,
                       '-o', self.out_path,
                       util.localize(file_path)])

        inputs = list(set().union(file_path))

        yield self.submit(cmd.txt, inputs=inputs,
                          expected_outputs=[{'name': 'genes.fpkm_tracking',
                                             'file_type': 'fpkm'},
                                            {'name': 'genes.fpkm_tracking',
                                             'file_type': 'fpkm'},
                                            {'name': 'skipped.gtf',
                                             'file_type': 'skipped.gtf'},
                                            {'name': 'transcripts.gtf',
                                             'file_type': 'transcripts.gtf'}])

class CuffMerge(task.ContainerTask):
    """Run CuffMerge

    Merges a set of cufflinks-assembled gene annotations into a single
    annotation.

    Example:

        cm = cuffmerge(fc_match(cuff, {'file_type': 'transcripts.gtf'}),
                       ref_fasta=args.ref_fasta,
                       args=args,
                       genes_gtf=args.genes_gtf)

    Args:
        pc (PCollection): The input collection of files to process.
        args (dict): The argument context.
        label (str): The operation label.
        tag (str): The sub-operation tag to distinguish operations of same type
        debug (bool): Whether to run in debug mode.
        ref_fasta (str): The reference fasta file.
        genes_gtf (str): The reference gene annotation.

    Returns:
        PCollection: A collection of files generated by this operation.

    Todo:
        * Refactor

    .. _CuffMerge documentation:
       https://cole-trapnell-lab.github.io/cufflinks/cuffmerge/
    """

    def __init__(self, args, ref_fasta, genes_gtf):
        """Initialize a containerized task."""
        self.ref_fasta = ref_fasta
        self.genes_gtf = genes_gtf
        container = task.ContainerTaskResources(
            disk=60, cpu_cores=4, ram=8,
            image='gcr.io/jbei-cloud/cufflinks:0.0.1')
        super(CuffMerge, self).__init__(task_label='cuffmerge',
                                        args=args,
                                        container=container)

    def process(self, assemblies):

        assemblies_txt = '%s/assemblies.txt' % self.out_path

        cmd = util.Command(['cp', localize(self.ref_fasta), self.out_path])

        inputs = list(set().union([self.genes_gtf, self.ref_fasta]))

        for assembly in assemblies:
            cmd.chain(['echo', localize(assembly), '>>',
                                   assemblies_txt])
            inputs.extend([assembly])

        cmd.chain(['cuffmerge',
                   '-g', localize(self.genes_gtf),
                   '-s', localize(self.ref_fasta, local_stem=self.out_path),
                   '-p', 8,
                   '-o', self.out_path,
                   assemblies_txt])

        yield self.submit(cmd.txt, inputs=inputs,
                          expected_outputs=[{'name': 'merged.gtf',
                                             'file_type': 'gtf'}])


class CuffDiff(task.ContainerTask):
    """Diff two read collections in terms of the prevalence of genome features.

    Provided a set of genome features in a genes_gtf file (received from an
    input PCollection) and reads from two conditions, cuffdiff will quantify
    the differential prevalence of these features between conditions.

    Example:

        cd = cuffdiff(fc_match(cm, {'file_type': 'gtf'}),
                      ref_fasta=args.ref_fasta,
                      args=args,
                      cond_a_bams=AsList(align_a),
                      cond_b_bams=AsList(align_b))

    Args:
        pc (PCollection): The input collection of files to process.
        args (dict): The argument context.
        label (str): The operation label.
        tag (str): The sub-operation tag to distinguish operations of same type
        debug (bool): Whether to run in debug mode.
        ref_fasta (str): The reference fasta file.
        genes_gtf (str): The reference gene annotation.
        cond_a_bams (list): A list of BAM alignments for condition A.
        cond_b_bams (list): a list of BAM alignments for condition B.

    Returns:
        PCollection: A collection of files generated by this operation.

    Todo:
        * Refactor

    .. _Documentation:
       https://cole-trapnell-lab.github.io/cufflinks/cuffdiff/
    """

    def __init__(self, args, ref_fasta, genes_gtf, cond_a_bams, cond_b_bams):
        """Initialize a containerized task."""
        self.ref_fasta = ref_fasta
        self.genes_gtf = genes_gtf
        self.cond_a_bams = cond_a_bams
        self.cond_b_bams = cond_b_bams
        container = task.ContainerTaskResources(
            disk=60, cpu_cores=4, ram=8,
            image='gcr.io/jbei-cloud/cufflinks:0.0.1')
        super(CuffDiff, self).__init__(task_label='cuffdiff',
                                       args=args,
                                       container=container)

    def process(self, file_path):

        cond_a = ','.join(localize_set(self.cond_a_bams))
        cond_b = ','.join(localize_set(self.cond_b_bams))

        cmd = util.Command(['cp', localize(self.ref_fasta), self.out_path])

        cmd.chain(['cuffdiff',
                   '-o', self.out_path,
                   '-b', localize(self.ref_fasta, local_stem=self.out_path),
                   '-p', cpu_cores,
                   '-L', 'C1,C2',
                   '-u',  localize(self.genes_gtf),
                   cond_a, cond_b])

        inputs = [util.gsutil_expand_stem(self.ref_fasta),
                  self.cond_a_bams, self.cond_b_bams, self.genes_gtf]

        yield self.submit(cmd.txt, inputs=inputs,
                          expected_outputs=[{'genes.count_tracking'},
                                            {'name': 'genes.fpkm_tracking'},
                                            {'name': 'genes.read_group_tracking'},
                                            {'name': 'read_groups.info'},
                                            {'name': 'run.info'}])
