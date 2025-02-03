# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MKHEADSURF_METADATA = Metadata(
    id="d268c25e144e66d66d451c811baf8b76c969e6ec.boutiques",
    name="mkheadsurf",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MkheadsurfParameters = typing.TypedDict('MkheadsurfParameters', {
    "__STYX_TYPE__": typing.Literal["mkheadsurf"],
    "input_vol": InputPathType,
    "output_vol": str,
    "output_surf": str,
    "subject_id": str,
    "nsmooth": typing.NotRequired[float | None],
    "noseghead": bool,
    "thresh1": typing.NotRequired[float | None],
    "thresh2": typing.NotRequired[float | None],
    "nhitsmin": typing.NotRequired[float | None],
    "ndilate": typing.NotRequired[float | None],
    "nerode": typing.NotRequired[float | None],
    "fillval": typing.NotRequired[float | None],
    "fhi": typing.NotRequired[float | None],
    "no_rescale": bool,
    "no_fill_holes_islands": bool,
    "or_mask": typing.NotRequired[InputPathType | None],
    "tessellation_method": typing.NotRequired[str | None],
    "inflate": bool,
    "curv": bool,
    "srcvol": typing.NotRequired[str | None],
    "headvol": typing.NotRequired[str | None],
    "headsurf": typing.NotRequired[str | None],
    "smheadsurf": typing.NotRequired[str | None],
    "hemi": typing.NotRequired[str | None],
    "subjects_dir": typing.NotRequired[str | None],
    "umask": typing.NotRequired[float | None],
    "logfile": typing.NotRequired[str | None],
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
        "mkheadsurf": mkheadsurf_cargs,
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


def mkheadsurf_params(
    input_vol: InputPathType,
    output_vol: str,
    output_surf: str,
    subject_id: str,
    nsmooth: float | None = None,
    noseghead: bool = False,
    thresh1: float | None = None,
    thresh2: float | None = None,
    nhitsmin: float | None = None,
    ndilate: float | None = None,
    nerode: float | None = None,
    fillval: float | None = None,
    fhi: float | None = None,
    no_rescale: bool = False,
    no_fill_holes_islands: bool = False,
    or_mask: InputPathType | None = None,
    tessellation_method: str | None = None,
    inflate: bool = False,
    curv: bool = False,
    srcvol: str | None = None,
    headvol: str | None = None,
    headsurf: str | None = None,
    smheadsurf: str | None = None,
    hemi: str | None = None,
    subjects_dir: str | None = None,
    umask: float | None = None,
    logfile: str | None = None,
) -> MkheadsurfParameters:
    """
    Build parameters.
    
    Args:
        input_vol: Input volume.
        output_vol: Output volume.
        output_surf: Output surface.
        subject_id: Subject ID.
        nsmooth: Number of smoothing iterations (default 10).
        noseghead: Do not segment the head, only tessellate and smooth existing.
        thresh1: Threshold 1 value (default 20).
        thresh2: Threshold 2 value (default 20).
        nhitsmin: Minimum number of hits (default 2).
        ndilate: Number of dilations (default 0).
        nerode: Number of erosions (default 0).
        fillval: Fill value (default 1).
        fhi: FHI for MRIchangeType; default is to use default in mri_seghead.
        no_rescale: Do not rescale input when converting to uchar.
        no_fill_holes_islands: Do not fill holes and remove islands.
        or_mask: Include all voxels in ormask in the head seg.
        tessellation_method: Tessellation method using mri_tessellate or mri_mc\
            (default is -mc).
        inflate: Inflate and compute sulc.
        curv: Compute curv with smoothing.
        srcvol: Source volume ID (default is T1).
        headvol: Head volume ID (default is seghead).
        headsurf: Head surface ID (default is seghead).
        smheadsurf: Smoothed head surface ID (default is smseghead).
        hemi: Hemisphere (default is lh).
        subjects_dir: Subjects directory (default is SUBJECTS_DIR).
        umask: Umask setting (default is 2).
        logfile: Log file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mkheadsurf",
        "input_vol": input_vol,
        "output_vol": output_vol,
        "output_surf": output_surf,
        "subject_id": subject_id,
        "noseghead": noseghead,
        "no_rescale": no_rescale,
        "no_fill_holes_islands": no_fill_holes_islands,
        "inflate": inflate,
        "curv": curv,
    }
    if nsmooth is not None:
        params["nsmooth"] = nsmooth
    if thresh1 is not None:
        params["thresh1"] = thresh1
    if thresh2 is not None:
        params["thresh2"] = thresh2
    if nhitsmin is not None:
        params["nhitsmin"] = nhitsmin
    if ndilate is not None:
        params["ndilate"] = ndilate
    if nerode is not None:
        params["nerode"] = nerode
    if fillval is not None:
        params["fillval"] = fillval
    if fhi is not None:
        params["fhi"] = fhi
    if or_mask is not None:
        params["or_mask"] = or_mask
    if tessellation_method is not None:
        params["tessellation_method"] = tessellation_method
    if srcvol is not None:
        params["srcvol"] = srcvol
    if headvol is not None:
        params["headvol"] = headvol
    if headsurf is not None:
        params["headsurf"] = headsurf
    if smheadsurf is not None:
        params["smheadsurf"] = smheadsurf
    if hemi is not None:
        params["hemi"] = hemi
    if subjects_dir is not None:
        params["subjects_dir"] = subjects_dir
    if umask is not None:
        params["umask"] = umask
    if logfile is not None:
        params["logfile"] = logfile
    return params


def mkheadsurf_cargs(
    params: MkheadsurfParameters,
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
    cargs.append("mkheadsurf")
    cargs.extend([
        "-i",
        execution.input_file(params.get("input_vol"))
    ])
    cargs.extend([
        "-o",
        params.get("output_vol")
    ])
    cargs.extend([
        "-surf",
        params.get("output_surf")
    ])
    cargs.extend([
        "-s",
        params.get("subject_id")
    ])
    if params.get("nsmooth") is not None:
        cargs.extend([
            "-nsmooth",
            str(params.get("nsmooth"))
        ])
    if params.get("noseghead"):
        cargs.append("-noseghead")
    if params.get("thresh1") is not None:
        cargs.extend([
            "-thresh1",
            str(params.get("thresh1"))
        ])
    if params.get("thresh2") is not None:
        cargs.extend([
            "-thresh2",
            str(params.get("thresh2"))
        ])
    if params.get("nhitsmin") is not None:
        cargs.extend([
            "-nhitsmin",
            str(params.get("nhitsmin"))
        ])
    if params.get("ndilate") is not None:
        cargs.extend([
            "-ndilate",
            str(params.get("ndilate"))
        ])
    if params.get("nerode") is not None:
        cargs.extend([
            "-nerode",
            str(params.get("nerode"))
        ])
    if params.get("fillval") is not None:
        cargs.extend([
            "-fillval",
            str(params.get("fillval"))
        ])
    if params.get("fhi") is not None:
        cargs.extend([
            "-fhi",
            str(params.get("fhi"))
        ])
    if params.get("no_rescale"):
        cargs.append("-no-rescale")
    if params.get("no_fill_holes_islands"):
        cargs.append("-no-fill-holes-islands")
    if params.get("or_mask") is not None:
        cargs.extend([
            "-or-mask",
            execution.input_file(params.get("or_mask"))
        ])
    if params.get("tessellation_method") is not None:
        cargs.extend([
            "-tess",
            params.get("tessellation_method")
        ])
    if params.get("inflate"):
        cargs.append("-inflate")
    if params.get("curv"):
        cargs.append("-curv")
    if params.get("srcvol") is not None:
        cargs.extend([
            "-srcvol",
            params.get("srcvol")
        ])
    if params.get("headvol") is not None:
        cargs.extend([
            "-headvol",
            params.get("headvol")
        ])
    if params.get("headsurf") is not None:
        cargs.extend([
            "-headsurf",
            params.get("headsurf")
        ])
    if params.get("smheadsurf") is not None:
        cargs.extend([
            "-smheadsurf",
            params.get("smheadsurf")
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "-hemi",
            params.get("hemi")
        ])
    if params.get("subjects_dir") is not None:
        cargs.extend([
            "-sd",
            params.get("subjects_dir")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "-umask",
            str(params.get("umask"))
        ])
    if params.get("logfile") is not None:
        cargs.extend([
            "-log",
            params.get("logfile")
        ])
    return cargs


def mkheadsurf_outputs(
    params: MkheadsurfParameters,
    execution: Execution,
) -> MkheadsurfOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MkheadsurfOutputs(
        root=execution.output_file("."),
    )
    return ret


def mkheadsurf_execute(
    params: MkheadsurfParameters,
    execution: Execution,
) -> MkheadsurfOutputs:
    """
    Segment and create a surface representation of the head for visualization and
    further processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MkheadsurfOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mkheadsurf_cargs(params, execution)
    ret = mkheadsurf_outputs(params, execution)
    execution.run(cargs)
    return ret


def mkheadsurf(
    input_vol: InputPathType,
    output_vol: str,
    output_surf: str,
    subject_id: str,
    nsmooth: float | None = None,
    noseghead: bool = False,
    thresh1: float | None = None,
    thresh2: float | None = None,
    nhitsmin: float | None = None,
    ndilate: float | None = None,
    nerode: float | None = None,
    fillval: float | None = None,
    fhi: float | None = None,
    no_rescale: bool = False,
    no_fill_holes_islands: bool = False,
    or_mask: InputPathType | None = None,
    tessellation_method: str | None = None,
    inflate: bool = False,
    curv: bool = False,
    srcvol: str | None = None,
    headvol: str | None = None,
    headsurf: str | None = None,
    smheadsurf: str | None = None,
    hemi: str | None = None,
    subjects_dir: str | None = None,
    umask: float | None = None,
    logfile: str | None = None,
    runner: Runner | None = None,
) -> MkheadsurfOutputs:
    """
    Segment and create a surface representation of the head for visualization and
    further processing.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_vol: Input volume.
        output_vol: Output volume.
        output_surf: Output surface.
        subject_id: Subject ID.
        nsmooth: Number of smoothing iterations (default 10).
        noseghead: Do not segment the head, only tessellate and smooth existing.
        thresh1: Threshold 1 value (default 20).
        thresh2: Threshold 2 value (default 20).
        nhitsmin: Minimum number of hits (default 2).
        ndilate: Number of dilations (default 0).
        nerode: Number of erosions (default 0).
        fillval: Fill value (default 1).
        fhi: FHI for MRIchangeType; default is to use default in mri_seghead.
        no_rescale: Do not rescale input when converting to uchar.
        no_fill_holes_islands: Do not fill holes and remove islands.
        or_mask: Include all voxels in ormask in the head seg.
        tessellation_method: Tessellation method using mri_tessellate or mri_mc\
            (default is -mc).
        inflate: Inflate and compute sulc.
        curv: Compute curv with smoothing.
        srcvol: Source volume ID (default is T1).
        headvol: Head volume ID (default is seghead).
        headsurf: Head surface ID (default is seghead).
        smheadsurf: Smoothed head surface ID (default is smseghead).
        hemi: Hemisphere (default is lh).
        subjects_dir: Subjects directory (default is SUBJECTS_DIR).
        umask: Umask setting (default is 2).
        logfile: Log file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MkheadsurfOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MKHEADSURF_METADATA)
    params = mkheadsurf_params(input_vol=input_vol, output_vol=output_vol, output_surf=output_surf, subject_id=subject_id, nsmooth=nsmooth, noseghead=noseghead, thresh1=thresh1, thresh2=thresh2, nhitsmin=nhitsmin, ndilate=ndilate, nerode=nerode, fillval=fillval, fhi=fhi, no_rescale=no_rescale, no_fill_holes_islands=no_fill_holes_islands, or_mask=or_mask, tessellation_method=tessellation_method, inflate=inflate, curv=curv, srcvol=srcvol, headvol=headvol, headsurf=headsurf, smheadsurf=smheadsurf, hemi=hemi, subjects_dir=subjects_dir, umask=umask, logfile=logfile)
    return mkheadsurf_execute(params, execution)


__all__ = [
    "MKHEADSURF_METADATA",
    "mkheadsurf",
    "mkheadsurf_params",
]
