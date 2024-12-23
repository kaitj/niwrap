# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GCATRAIN_METADATA = Metadata(
    id="eee9b89002e0f2e263128edc3af126a1ada69cbf.boutiques",
    name="gcatrain",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class GcatrainOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gcatrain(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gcatrain(
    gcadir: str,
    subjectlistfile: InputPathType,
    init_subject_transform: list[str],
    seg_file: InputPathType,
    source_subjects_dir: str,
    num_iters: float | None = None,
    num_threads: float | None = None,
    exclude_file: InputPathType | None = None,
    exclude_subject: str | None = None,
    symmetric_atlas: bool = False,
    color_table: InputPathType | None = None,
    no_submit: bool = False,
    mail_flag: bool = False,
    no_strict: bool = False,
    gcareg_iters: bool = False,
    prep_only: bool = False,
    nu10_flag: bool = False,
    nu12_flag: bool = False,
    no_emreg: bool = False,
    runner: Runner | None = None,
) -> GcatrainOutputs:
    """
    GCA training tool for building a GCA from a group of manually labeled subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        gcadir: Directory for the new SUBJECTS_DIR.
        subjectlistfile: The list of subjects to include.
        init_subject_transform: Initialization subject and its talairach\
            transform.
        seg_file: Segmentation file (e.g. seg_edited.mgz).
        source_subjects_dir: Source SUBJECTS_DIR for data.
        num_iters: Number of iterations.
        num_threads: Number of threads to use.
        exclude_file: File listing subjects to exclude, useful for jackknifing.
        exclude_subject: Exclude a single subject, useful for jackknifing.
        symmetric_atlas: Create a symmetric atlas.
        color_table: Colortable for segmentation labels (not needed).
        no_submit: Run serially without pbsubmit.
        mail_flag: Mail to user when jobs are pbsubmitted or finished.
        no_strict: Do not require FS build stamps to match across iterations.
        gcareg_iters: Set to 1 for testing.
        prep_only: Execute preparation steps only.
        nu10_flag: Run with nu10 settings.
        nu12_flag: Run with nu12 settings (default).
        no_emreg: Do not use mri_em_register.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GcatrainOutputs`).
    """
    if (len(init_subject_transform) != 2): 
        raise ValueError(f"Length of 'init_subject_transform' must be 2 but was {len(init_subject_transform)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(GCATRAIN_METADATA)
    cargs = []
    cargs.append("gcatrain")
    cargs.extend([
        "--g",
        gcadir
    ])
    cargs.extend([
        "--f",
        execution.input_file(subjectlistfile)
    ])
    cargs.extend([
        "--init",
        *init_subject_transform
    ])
    cargs.extend([
        "--seg",
        execution.input_file(seg_file)
    ])
    cargs.extend([
        "--sd",
        source_subjects_dir
    ])
    if num_iters is not None:
        cargs.extend([
            "--niters",
            str(num_iters)
        ])
    if num_threads is not None:
        cargs.extend([
            "--nthreads",
            str(num_threads)
        ])
    if exclude_file is not None:
        cargs.extend([
            "--x",
            execution.input_file(exclude_file)
        ])
    if exclude_subject is not None:
        cargs.extend([
            "--xs",
            exclude_subject
        ])
    if symmetric_atlas:
        cargs.append("--sym")
    if color_table is not None:
        cargs.extend([
            "--ctab",
            execution.input_file(color_table)
        ])
    if no_submit:
        cargs.append("--no-submit")
    if mail_flag:
        cargs.append("--pb-m")
    if no_strict:
        cargs.append("--no-strict")
    if gcareg_iters:
        cargs.append("--gcareg-iters")
    if prep_only:
        cargs.append("--prep-only")
    if nu10_flag:
        cargs.append("--nu10")
    if nu12_flag:
        cargs.append("--nu12")
    if no_emreg:
        cargs.append("--no-emreg")
    ret = GcatrainOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GCATRAIN_METADATA",
    "GcatrainOutputs",
    "gcatrain",
]
