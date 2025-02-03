# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_TRAIN_METADATA = Metadata(
    id="918d6285f42340a49fa09c21128213fd2bfe5e71.boutiques",
    name="dmri_train",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DmriTrainParameters = typing.TypedDict('DmriTrainParameters', {
    "__STYX_TYPE__": typing.Literal["dmri_train"],
    "slist": InputPathType,
    "trk_files": list[InputPathType],
    "rois": typing.NotRequired[list[InputPathType] | None],
    "seg": InputPathType,
    "cmask": InputPathType,
    "lmask": list[float],
    "bmask_training": list[InputPathType],
    "outtrk": list[InputPathType],
    "bmask_test": list[InputPathType],
    "fa": typing.NotRequired[list[InputPathType] | None],
    "reg": typing.NotRequired[InputPathType | None],
    "regnl": typing.NotRequired[InputPathType | None],
    "refnl": typing.NotRequired[InputPathType | None],
    "basereg": typing.NotRequired[list[InputPathType] | None],
    "baseref": typing.NotRequired[list[InputPathType] | None],
    "ncpts": list[float],
    "max_streamlines": float,
    "xstr": bool,
    "aprior": bool,
    "sprior": bool,
    "trunc": bool,
    "out_files": list[str],
    "outdir": typing.NotRequired[str | None],
    "cptdir": typing.NotRequired[str | None],
    "debug": bool,
    "checkopts": bool,
    "help": bool,
    "version": bool,
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
        "dmri_train": dmri_train_cargs,
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


def dmri_train_params(
    slist: InputPathType,
    trk_files: list[InputPathType],
    seg: InputPathType,
    cmask: InputPathType,
    lmask: list[float],
    bmask_training: list[InputPathType],
    outtrk: list[InputPathType],
    bmask_test: list[InputPathType],
    ncpts: list[float],
    max_streamlines: float,
    out_files: list[str],
    rois: list[InputPathType] | None = None,
    fa: list[InputPathType] | None = None,
    reg: InputPathType | None = None,
    regnl: InputPathType | None = None,
    refnl: InputPathType | None = None,
    basereg: list[InputPathType] | None = None,
    baseref: list[InputPathType] | None = None,
    xstr: bool = False,
    aprior: bool = False,
    sprior: bool = False,
    trunc: bool = False,
    outdir: str | None = None,
    cptdir: str | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
) -> DmriTrainParameters:
    """
    Build parameters.
    
    Args:
        slist: Text file with list of training subject directories.
        trk_files: Name(s) of input .trk file(s), one per path.
        seg: Name of input aparc+aseg volume.
        cmask: Name of input cortex mask volume.
        lmask: Add a label ID from aparc+aseg to cortex mask, one per path.
        bmask_training: Input brain mask volume(s).
        outtrk: Name(s) of output, pre-sorted .trk file(s), one per path.
        bmask_test: Input brain mask volume(s) for test subject.
        ncpts: Number of control points for initial spline.
        max_streamlines: Maximum number of training streamlines to keep per\
            path.
        out_files: Base name(s) of output(s) for test subject, one per path.
        rois: Optional, names of input tract labeling ROIs, two per path.
        fa: Input FA volume(s) for test subject.
        reg: Affine registration from atlas to base space.
        regnl: Nonlinear registration from atlas to base space.
        refnl: Nonlinear registration source reference volume.
        basereg: Affine registration(s) from base to FA volume(s).
        baseref: Base space reference volume.
        xstr: Exclude previously chosen center streamline(s).
        aprior: Compute priors on underlying anatomy.
        sprior: Compute priors on shape.
        trunc: Use all training streamlines, truncated or not.
        outdir: Output directory.
        cptdir: Output directory for control points in test subject's space.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dmri_train",
        "slist": slist,
        "trk_files": trk_files,
        "seg": seg,
        "cmask": cmask,
        "lmask": lmask,
        "bmask_training": bmask_training,
        "outtrk": outtrk,
        "bmask_test": bmask_test,
        "ncpts": ncpts,
        "max_streamlines": max_streamlines,
        "xstr": xstr,
        "aprior": aprior,
        "sprior": sprior,
        "trunc": trunc,
        "out_files": out_files,
        "debug": debug,
        "checkopts": checkopts,
        "help": help_,
        "version": version,
    }
    if rois is not None:
        params["rois"] = rois
    if fa is not None:
        params["fa"] = fa
    if reg is not None:
        params["reg"] = reg
    if regnl is not None:
        params["regnl"] = regnl
    if refnl is not None:
        params["refnl"] = refnl
    if basereg is not None:
        params["basereg"] = basereg
    if baseref is not None:
        params["baseref"] = baseref
    if outdir is not None:
        params["outdir"] = outdir
    if cptdir is not None:
        params["cptdir"] = cptdir
    return params


def dmri_train_cargs(
    params: DmriTrainParameters,
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
    cargs.append("dmri_train")
    cargs.extend([
        "--slist",
        execution.input_file(params.get("slist"))
    ])
    cargs.extend([
        "--trk",
        *[execution.input_file(f) for f in params.get("trk_files")]
    ])
    if params.get("rois") is not None:
        cargs.extend([
            "--rois",
            *[execution.input_file(f) for f in params.get("rois")]
        ])
    cargs.extend([
        "--seg",
        execution.input_file(params.get("seg"))
    ])
    cargs.extend([
        "--cmask",
        execution.input_file(params.get("cmask"))
    ])
    cargs.extend([
        "--lmask",
        *map(str, params.get("lmask"))
    ])
    cargs.extend([
        "--bmask",
        *[execution.input_file(f) for f in params.get("bmask_training")]
    ])
    cargs.extend([
        "--outtrk",
        *[execution.input_file(f) for f in params.get("outtrk")]
    ])
    cargs.extend([
        "--bmask",
        *[execution.input_file(f) for f in params.get("bmask_test")]
    ])
    if params.get("fa") is not None:
        cargs.extend([
            "--fa",
            *[execution.input_file(f) for f in params.get("fa")]
        ])
    if params.get("reg") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("reg"))
        ])
    if params.get("regnl") is not None:
        cargs.extend([
            "--regnl",
            execution.input_file(params.get("regnl"))
        ])
    if params.get("refnl") is not None:
        cargs.extend([
            "--refnl",
            execution.input_file(params.get("refnl"))
        ])
    if params.get("basereg") is not None:
        cargs.extend([
            "--basereg",
            *[execution.input_file(f) for f in params.get("basereg")]
        ])
    if params.get("baseref") is not None:
        cargs.extend([
            "--baseref",
            *[execution.input_file(f) for f in params.get("baseref")]
        ])
    cargs.extend([
        "--ncpts",
        *map(str, params.get("ncpts"))
    ])
    cargs.extend([
        "--max",
        str(params.get("max_streamlines"))
    ])
    if params.get("xstr"):
        cargs.append("--xstr")
    if params.get("aprior"):
        cargs.append("--aprior")
    if params.get("sprior"):
        cargs.append("--sprior")
    if params.get("trunc"):
        cargs.append("--trunc")
    cargs.extend([
        "--out",
        *params.get("out_files")
    ])
    if params.get("outdir") is not None:
        cargs.extend([
            "--outdir",
            params.get("outdir")
        ])
    if params.get("cptdir") is not None:
        cargs.extend([
            "--cptdir",
            params.get("cptdir")
        ])
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("checkopts"):
        cargs.append("--checkopts")
    if params.get("help"):
        cargs.append("--help")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def dmri_train_outputs(
    params: DmriTrainParameters,
    execution: Execution,
) -> DmriTrainOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DmriTrainOutputs(
        root=execution.output_file("."),
    )
    return ret


def dmri_train_execute(
    params: DmriTrainParameters,
    execution: Execution,
) -> DmriTrainOutputs:
    """
    DMRI training tool for processing diffusion MRI data in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DmriTrainOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dmri_train_cargs(params, execution)
    ret = dmri_train_outputs(params, execution)
    execution.run(cargs)
    return ret


def dmri_train(
    slist: InputPathType,
    trk_files: list[InputPathType],
    seg: InputPathType,
    cmask: InputPathType,
    lmask: list[float],
    bmask_training: list[InputPathType],
    outtrk: list[InputPathType],
    bmask_test: list[InputPathType],
    ncpts: list[float],
    max_streamlines: float,
    out_files: list[str],
    rois: list[InputPathType] | None = None,
    fa: list[InputPathType] | None = None,
    reg: InputPathType | None = None,
    regnl: InputPathType | None = None,
    refnl: InputPathType | None = None,
    basereg: list[InputPathType] | None = None,
    baseref: list[InputPathType] | None = None,
    xstr: bool = False,
    aprior: bool = False,
    sprior: bool = False,
    trunc: bool = False,
    outdir: str | None = None,
    cptdir: str | None = None,
    debug: bool = False,
    checkopts: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DmriTrainOutputs:
    """
    DMRI training tool for processing diffusion MRI data in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        slist: Text file with list of training subject directories.
        trk_files: Name(s) of input .trk file(s), one per path.
        seg: Name of input aparc+aseg volume.
        cmask: Name of input cortex mask volume.
        lmask: Add a label ID from aparc+aseg to cortex mask, one per path.
        bmask_training: Input brain mask volume(s).
        outtrk: Name(s) of output, pre-sorted .trk file(s), one per path.
        bmask_test: Input brain mask volume(s) for test subject.
        ncpts: Number of control points for initial spline.
        max_streamlines: Maximum number of training streamlines to keep per\
            path.
        out_files: Base name(s) of output(s) for test subject, one per path.
        rois: Optional, names of input tract labeling ROIs, two per path.
        fa: Input FA volume(s) for test subject.
        reg: Affine registration from atlas to base space.
        regnl: Nonlinear registration from atlas to base space.
        refnl: Nonlinear registration source reference volume.
        basereg: Affine registration(s) from base to FA volume(s).
        baseref: Base space reference volume.
        xstr: Exclude previously chosen center streamline(s).
        aprior: Compute priors on underlying anatomy.
        sprior: Compute priors on shape.
        trunc: Use all training streamlines, truncated or not.
        outdir: Output directory.
        cptdir: Output directory for control points in test subject's space.
        debug: Turn on debugging.
        checkopts: Don't run anything, just check options and exit.
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriTrainOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_TRAIN_METADATA)
    params = dmri_train_params(slist=slist, trk_files=trk_files, rois=rois, seg=seg, cmask=cmask, lmask=lmask, bmask_training=bmask_training, outtrk=outtrk, bmask_test=bmask_test, fa=fa, reg=reg, regnl=regnl, refnl=refnl, basereg=basereg, baseref=baseref, ncpts=ncpts, max_streamlines=max_streamlines, xstr=xstr, aprior=aprior, sprior=sprior, trunc=trunc, out_files=out_files, outdir=outdir, cptdir=cptdir, debug=debug, checkopts=checkopts, help_=help_, version=version)
    return dmri_train_execute(params, execution)


__all__ = [
    "DMRI_TRAIN_METADATA",
    "dmri_train",
    "dmri_train_params",
]
