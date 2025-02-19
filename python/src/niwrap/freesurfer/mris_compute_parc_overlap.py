# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_COMPUTE_PARC_OVERLAP_METADATA = Metadata(
    id="d598ee06b2c8bac2b0e66dc28fd526ceb983bfbd.boutiques",
    name="mris_compute_parc_overlap",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisComputeParcOverlapParameters = typing.TypedDict('MrisComputeParcOverlapParameters', {
    "__STYX_TYPE__": typing.Literal["mris_compute_parc_overlap"],
    "subject": str,
    "hemi": str,
    "annot1": typing.NotRequired[InputPathType | None],
    "annot2": typing.NotRequired[InputPathType | None],
    "label1": typing.NotRequired[InputPathType | None],
    "label2": typing.NotRequired[InputPathType | None],
    "subj_dir": typing.NotRequired[str | None],
    "log_file": typing.NotRequired[str | None],
    "label_list": typing.NotRequired[InputPathType | None],
    "nocheck_label1_xyz": bool,
    "nocheck_label2_xyz": bool,
    "nocheck_label_xyz": bool,
    "use_label1_xyz": bool,
    "use_label2_xyz": bool,
    "use_label_xyz": bool,
    "debug_overlap": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "mris_compute_parc_overlap": mris_compute_parc_overlap_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class MrisComputeParcOverlapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_compute_parc_overlap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_compute_parc_overlap_params(
    subject: str,
    hemi: str,
    annot1: InputPathType | None = None,
    annot2: InputPathType | None = None,
    label1: InputPathType | None = None,
    label2: InputPathType | None = None,
    subj_dir: str | None = None,
    log_file: str | None = None,
    label_list: InputPathType | None = None,
    nocheck_label1_xyz: bool = False,
    nocheck_label2_xyz: bool = False,
    nocheck_label_xyz: bool = False,
    use_label1_xyz: bool = False,
    use_label2_xyz: bool = False,
    use_label_xyz: bool = False,
    debug_overlap: bool = False,
) -> MrisComputeParcOverlapParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject to check.
        hemi: Hemisphere: rh or lh.
        annot1: First .annot file.
        annot2: Second .annot file.
        label1: First .label file.
        label2: Second .label file.
        subj_dir: Set SUBJECTS_DIR.
        log_file: Output the overall DICE and minimum distance to filename.
        label_list: File containing labels to check, one per line.
        nocheck_label1_xyz: When loading label1 file, don't check x,y,z coords\
            to surface.
        nocheck_label2_xyz: When loading label2 file, don't check x,y,z coords\
            to surface.
        nocheck_label_xyz: Do not check label1 and label2.
        use_label1_xyz: Replace surface x,y,z coords with those in label1 file.
        use_label2_xyz: Replace surface x,y,z coords with those in label2 file.
        use_label_xyz: Use label1 and label2 coords.
        debug_overlap: Generate ?h.overlap.annot.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_compute_parc_overlap",
        "subject": subject,
        "hemi": hemi,
        "nocheck_label1_xyz": nocheck_label1_xyz,
        "nocheck_label2_xyz": nocheck_label2_xyz,
        "nocheck_label_xyz": nocheck_label_xyz,
        "use_label1_xyz": use_label1_xyz,
        "use_label2_xyz": use_label2_xyz,
        "use_label_xyz": use_label_xyz,
        "debug_overlap": debug_overlap,
    }
    if annot1 is not None:
        params["annot1"] = annot1
    if annot2 is not None:
        params["annot2"] = annot2
    if label1 is not None:
        params["label1"] = label1
    if label2 is not None:
        params["label2"] = label2
    if subj_dir is not None:
        params["subj_dir"] = subj_dir
    if log_file is not None:
        params["log_file"] = log_file
    if label_list is not None:
        params["label_list"] = label_list
    return params


def mris_compute_parc_overlap_cargs(
    params: MrisComputeParcOverlapParameters,
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
    cargs.append("mris_compute_parc_overlap")
    cargs.extend([
        "--s",
        params.get("subject")
    ])
    cargs.extend([
        "--hemi",
        params.get("hemi")
    ])
    if params.get("annot1") is not None:
        cargs.extend([
            "--annot1",
            execution.input_file(params.get("annot1"))
        ])
    if params.get("annot2") is not None:
        cargs.extend([
            "--annot2",
            execution.input_file(params.get("annot2"))
        ])
    if params.get("label1") is not None:
        cargs.extend([
            "--label1",
            execution.input_file(params.get("label1"))
        ])
    if params.get("label2") is not None:
        cargs.extend([
            "--label2",
            execution.input_file(params.get("label2"))
        ])
    if params.get("subj_dir") is not None:
        cargs.extend([
            "--sd",
            params.get("subj_dir")
        ])
    if params.get("log_file") is not None:
        cargs.extend([
            "--log",
            params.get("log_file")
        ])
    if params.get("label_list") is not None:
        cargs.extend([
            "--label-list",
            execution.input_file(params.get("label_list"))
        ])
    if params.get("nocheck_label1_xyz"):
        cargs.append("--nocheck-label1-xyz")
    if params.get("nocheck_label2_xyz"):
        cargs.append("--nocheck-label2-xyz")
    if params.get("nocheck_label_xyz"):
        cargs.append("--nocheck-label-xyz")
    if params.get("use_label1_xyz"):
        cargs.append("--use-label1-xyz")
    if params.get("use_label2_xyz"):
        cargs.append("--use-label2-xyz")
    if params.get("use_label_xyz"):
        cargs.append("--use-label-xyz")
    if params.get("debug_overlap"):
        cargs.append("--debug-overlap")
    return cargs


def mris_compute_parc_overlap_outputs(
    params: MrisComputeParcOverlapParameters,
    execution: Execution,
) -> MrisComputeParcOverlapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisComputeParcOverlapOutputs(
        root=execution.output_file("."),
    )
    return ret


def mris_compute_parc_overlap_execute(
    params: MrisComputeParcOverlapParameters,
    execution: Execution,
) -> MrisComputeParcOverlapOutputs:
    """
    Compares two parcellated (annotated or labeled) surfaces and computes an overall
    Dice coefficient and mean minimum distances (mm).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisComputeParcOverlapOutputs`).
    """
    params = execution.params(params)
    cargs = mris_compute_parc_overlap_cargs(params, execution)
    ret = mris_compute_parc_overlap_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_compute_parc_overlap(
    subject: str,
    hemi: str,
    annot1: InputPathType | None = None,
    annot2: InputPathType | None = None,
    label1: InputPathType | None = None,
    label2: InputPathType | None = None,
    subj_dir: str | None = None,
    log_file: str | None = None,
    label_list: InputPathType | None = None,
    nocheck_label1_xyz: bool = False,
    nocheck_label2_xyz: bool = False,
    nocheck_label_xyz: bool = False,
    use_label1_xyz: bool = False,
    use_label2_xyz: bool = False,
    use_label_xyz: bool = False,
    debug_overlap: bool = False,
    runner: Runner | None = None,
) -> MrisComputeParcOverlapOutputs:
    """
    Compares two parcellated (annotated or labeled) surfaces and computes an overall
    Dice coefficient and mean minimum distances (mm).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject to check.
        hemi: Hemisphere: rh or lh.
        annot1: First .annot file.
        annot2: Second .annot file.
        label1: First .label file.
        label2: Second .label file.
        subj_dir: Set SUBJECTS_DIR.
        log_file: Output the overall DICE and minimum distance to filename.
        label_list: File containing labels to check, one per line.
        nocheck_label1_xyz: When loading label1 file, don't check x,y,z coords\
            to surface.
        nocheck_label2_xyz: When loading label2 file, don't check x,y,z coords\
            to surface.
        nocheck_label_xyz: Do not check label1 and label2.
        use_label1_xyz: Replace surface x,y,z coords with those in label1 file.
        use_label2_xyz: Replace surface x,y,z coords with those in label2 file.
        use_label_xyz: Use label1 and label2 coords.
        debug_overlap: Generate ?h.overlap.annot.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisComputeParcOverlapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COMPUTE_PARC_OVERLAP_METADATA)
    params = mris_compute_parc_overlap_params(subject=subject, hemi=hemi, annot1=annot1, annot2=annot2, label1=label1, label2=label2, subj_dir=subj_dir, log_file=log_file, label_list=label_list, nocheck_label1_xyz=nocheck_label1_xyz, nocheck_label2_xyz=nocheck_label2_xyz, nocheck_label_xyz=nocheck_label_xyz, use_label1_xyz=use_label1_xyz, use_label2_xyz=use_label2_xyz, use_label_xyz=use_label_xyz, debug_overlap=debug_overlap)
    return mris_compute_parc_overlap_execute(params, execution)


__all__ = [
    "MRIS_COMPUTE_PARC_OVERLAP_METADATA",
    "MrisComputeParcOverlapOutputs",
    "MrisComputeParcOverlapParameters",
    "mris_compute_parc_overlap",
    "mris_compute_parc_overlap_params",
]
