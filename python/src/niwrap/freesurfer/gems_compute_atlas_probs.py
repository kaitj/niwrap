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
GemsComputeAtlasProbsParameters = typing.TypedDict('GemsComputeAtlasProbsParameters', {
    "__STYX_TYPE__": typing.Literal["gems_compute_atlas_probs"],
    "subjects_dir": str,
    "mesh_collections": list[str],
    "out_dir": str,
    "segmentations_dir": typing.NotRequired[str | None],
    "gt_from_fs": bool,
    "segmentation_name": typing.NotRequired[str | None],
    "multi_structure": bool,
    "labels": typing.NotRequired[list[str] | None],
    "from_samseg": bool,
    "em_iterations": typing.NotRequired[float | None],
    "show_figs": bool,
    "save_figs": bool,
    "save_average_figs": bool,
    "subjects_file": typing.NotRequired[str | None],
    "labels_file": typing.NotRequired[str | None],
    "samseg_subdir": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "gems_compute_atlas_probs": gems_compute_atlas_probs_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


def gems_compute_atlas_probs_params(
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
) -> GemsComputeAtlasProbsParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "gems_compute_atlas_probs",
        "subjects_dir": subjects_dir,
        "mesh_collections": mesh_collections,
        "out_dir": out_dir,
        "gt_from_fs": gt_from_fs,
        "multi_structure": multi_structure,
        "from_samseg": from_samseg,
        "show_figs": show_figs,
        "save_figs": save_figs,
        "save_average_figs": save_average_figs,
    }
    if segmentations_dir is not None:
        params["segmentations_dir"] = segmentations_dir
    if segmentation_name is not None:
        params["segmentation_name"] = segmentation_name
    if labels is not None:
        params["labels"] = labels
    if em_iterations is not None:
        params["em_iterations"] = em_iterations
    if subjects_file is not None:
        params["subjects_file"] = subjects_file
    if labels_file is not None:
        params["labels_file"] = labels_file
    if samseg_subdir is not None:
        params["samseg_subdir"] = samseg_subdir
    return params


def gems_compute_atlas_probs_cargs(
    params: GemsComputeAtlasProbsParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("gems_compute_atlas_probs")
    cargs.extend([
        "--subjects-dir",
        params.get("subjects_dir")
    ])
    cargs.extend([
        "--mesh-collections",
        *params.get("mesh_collections")
    ])
    cargs.extend([
        "--out-dir",
        params.get("out_dir")
    ])
    if params.get("segmentations_dir") is not None:
        cargs.extend([
            "--segmentations-dir",
            params.get("segmentations_dir")
        ])
    if params.get("gt_from_fs"):
        cargs.append("--gt-from-FS")
    if params.get("segmentation_name") is not None:
        cargs.extend([
            "--segmentation-name",
            params.get("segmentation_name")
        ])
    if params.get("multi_structure"):
        cargs.append("--multi-structure")
    if params.get("labels") is not None:
        cargs.extend([
            "--labels",
            *params.get("labels")
        ])
    if params.get("from_samseg"):
        cargs.append("--from-samseg")
    if params.get("em_iterations") is not None:
        cargs.extend([
            "--EM-iterations",
            str(params.get("em_iterations"))
        ])
    if params.get("show_figs"):
        cargs.append("--show-figs")
    if params.get("save_figs"):
        cargs.append("--save-figs")
    if params.get("save_average_figs"):
        cargs.append("--save-average-figs")
    if params.get("subjects_file") is not None:
        cargs.extend([
            "--subjects_file",
            params.get("subjects_file")
        ])
    if params.get("labels_file") is not None:
        cargs.extend([
            "--labels_file",
            params.get("labels_file")
        ])
    if params.get("samseg_subdir") is not None:
        cargs.extend([
            "--samseg-subdir",
            params.get("samseg_subdir")
        ])
    return cargs


def gems_compute_atlas_probs_outputs(
    params: GemsComputeAtlasProbsParameters,
    execution: Execution,
) -> GemsComputeAtlasProbsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = GemsComputeAtlasProbsOutputs(
        root=execution.output_file("."),
    )
    return ret


def gems_compute_atlas_probs_execute(
    params: GemsComputeAtlasProbsParameters,
    execution: Execution,
) -> GemsComputeAtlasProbsOutputs:
    """
    Tool to compute atlas probabilities using SAMSEG results.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `GemsComputeAtlasProbsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = gems_compute_atlas_probs_cargs(params, execution)
    ret = gems_compute_atlas_probs_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    params = gems_compute_atlas_probs_params(subjects_dir=subjects_dir, mesh_collections=mesh_collections, out_dir=out_dir, segmentations_dir=segmentations_dir, gt_from_fs=gt_from_fs, segmentation_name=segmentation_name, multi_structure=multi_structure, labels=labels, from_samseg=from_samseg, em_iterations=em_iterations, show_figs=show_figs, save_figs=save_figs, save_average_figs=save_average_figs, subjects_file=subjects_file, labels_file=labels_file, samseg_subdir=samseg_subdir)
    return gems_compute_atlas_probs_execute(params, execution)


__all__ = [
    "GEMS_COMPUTE_ATLAS_PROBS_METADATA",
    "gems_compute_atlas_probs",
    "gems_compute_atlas_probs_params",
]
