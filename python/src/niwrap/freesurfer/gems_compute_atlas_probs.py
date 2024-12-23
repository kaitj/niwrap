# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

GEMS_COMPUTE_ATLAS_PROBS_METADATA = Metadata(
    id="e4708282a3cd6c2187910866f5c82a92aef1d963.boutiques",
    name="gems_compute_atlas_probs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class GemsComputeAtlasProbsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gems_compute_atlas_probs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gems_compute_atlas_probs(
    subjects_dir: str,
    mesh_collections: list[str],
    out_dir: str,
    segmentations_dir: str | None = None,
    gt_from_fs: bool = False,
    segmentation_name: str | None = None,
    multi_structure: bool = False,
    labels: list[str] | None = None,
    from_samseg: bool = False,
    em_iterations: float | None = None,
    show_figs: bool = False,
    save_figs: bool = False,
    save_average_figs: bool = False,
    subjects_file: str | None = None,
    labels_file: str | None = None,
    samseg_subdir: str | None = None,
    runner: Runner | None = None,
) -> GemsComputeAtlasProbsOutputs:
    """
    Tool to compute atlas probabilities using SAMSEG results.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subjects_dir: Directory with saved SAMSEG runs with --history flag.
        mesh_collections: Mesh collection file(s).
        out_dir: Output directory.
        segmentations_dir: Directory with GT segmentations.
        gt_from_fs: GT from FreeSurfer segmentations.
        segmentation_name: Filename of the segmentations, assumed to be the\
            same for each subject.
        multi_structure: Estimate alphas from more than 1 structure.
        labels: Label numbers for multi-structure estimation.
        from_samseg: SAMSEG runs obtained from command samseg instead of\
            run_samseg.
        em_iterations: Number of EM iterations.
        show_figs: Show figures during the run.
        save_figs: Save rasterized prior of each subject.
        save_average_figs: Save average rasterized prior.
        subjects_file: Text file with list of subjects.
        labels_file: Text file with list of labels (instead of --labels).
        samseg_subdir: Name of samseg subdir in subject/mri folder.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GemsComputeAtlasProbsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GEMS_COMPUTE_ATLAS_PROBS_METADATA)
    cargs = []
    cargs.append("gems_compute_atlas_probs")
    cargs.extend([
        "--subjects-dir",
        subjects_dir
    ])
    cargs.extend([
        "--mesh-collections",
        *mesh_collections
    ])
    cargs.extend([
        "--out-dir",
        out_dir
    ])
    if segmentations_dir is not None:
        cargs.extend([
            "--segmentations-dir",
            segmentations_dir
        ])
    if gt_from_fs:
        cargs.append("--gt-from-FS")
    if segmentation_name is not None:
        cargs.extend([
            "--segmentation-name",
            segmentation_name
        ])
    if multi_structure:
        cargs.append("--multi-structure")
    if labels is not None:
        cargs.extend([
            "--labels",
            *labels
        ])
    if from_samseg:
        cargs.append("--from-samseg")
    if em_iterations is not None:
        cargs.extend([
            "--EM-iterations",
            str(em_iterations)
        ])
    if show_figs:
        cargs.append("--show-figs")
    if save_figs:
        cargs.append("--save-figs")
    if save_average_figs:
        cargs.append("--save-average-figs")
    if subjects_file is not None:
        cargs.extend([
            "--subjects_file",
            subjects_file
        ])
    if labels_file is not None:
        cargs.extend([
            "--labels_file",
            labels_file
        ])
    if samseg_subdir is not None:
        cargs.extend([
            "--samseg-subdir",
            samseg_subdir
        ])
    ret = GemsComputeAtlasProbsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GEMS_COMPUTE_ATLAS_PROBS_METADATA",
    "GemsComputeAtlasProbsOutputs",
    "gems_compute_atlas_probs",
]
