# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_MAKE_AVERAGE_SURFACE_METADATA = Metadata(
    id="c7c7dc6c877d2ef020d99e894c96f070fb1a71d2.boutiques",
    name="mris_make_average_surface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisMakeAverageSurfaceParameters = typing.TypedDict('MrisMakeAverageSurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["mris_make_average_surface"],
    "hemi": str,
    "outsurfname": str,
    "cansurfname": str,
    "outsubject": str,
    "subjects": list[str],
    "sdir": typing.NotRequired[str | None],
    "sdir_out": typing.NotRequired[str | None],
    "nonorm_flag": bool,
    "icoorder": typing.NotRequired[float | None],
    "xfmname": typing.NotRequired[str | None],
    "templatename": typing.NotRequired[str | None],
    "surfname": typing.NotRequired[str | None],
    "surf2surf_flag": bool,
    "simple": typing.NotRequired[list[str] | None],
    "diagno": typing.NotRequired[float | None],
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
        "mris_make_average_surface": mris_make_average_surface_cargs,
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
    vt = {
        "mris_make_average_surface": mris_make_average_surface_outputs,
    }
    return vt.get(t)


class MrisMakeAverageSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_make_average_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType | None
    """Output averaged surface"""


def mris_make_average_surface_params(
    hemi: str,
    outsurfname: str,
    cansurfname: str,
    outsubject: str,
    subjects: list[str],
    sdir: str | None = None,
    sdir_out: str | None = None,
    nonorm_flag: bool = False,
    icoorder: float | None = None,
    xfmname: str | None = None,
    templatename: str | None = None,
    surfname: str | None = None,
    surf2surf_flag: bool = False,
    simple: list[str] | None = None,
    diagno: float | None = None,
) -> MrisMakeAverageSurfaceParameters:
    """
    Build parameters.
    
    Args:
        hemi: Hemisphere, lh or rh.
        outsurfname: Output surface name (e.g., avg_orig).
        cansurfname: Registration surface (e.g., sphere.reg).
        outsubject: Name of subject to store the results in.
        subjects: List of subjects to average.
        sdir: Use sdir instead of SUBJECTS_DIR.
        sdir_out: Save results in sdirout/outsubject instead of\
            SUBJECTS_DIR/outsubject.
        nonorm_flag: Do not normalize area.
        icoorder: Use given icosahedron order (default is 7).
        xfmname: Use transforms/xfmname instead of talairach.xfm.
        templatename: Volume to use as geometry template for output surfaces.
        surfname: Use surfname instead of orig.
        surf2surf_flag: Use surf2surf transform instead of parametric surface.
        simple: Compute an average surface from the list of surfaces. All\
            surfaces must have same number of vertices.
        diagno: Set Gdiag_no to diagno.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_make_average_surface",
        "hemi": hemi,
        "outsurfname": outsurfname,
        "cansurfname": cansurfname,
        "outsubject": outsubject,
        "subjects": subjects,
        "nonorm_flag": nonorm_flag,
        "surf2surf_flag": surf2surf_flag,
    }
    if sdir is not None:
        params["sdir"] = sdir
    if sdir_out is not None:
        params["sdir_out"] = sdir_out
    if icoorder is not None:
        params["icoorder"] = icoorder
    if xfmname is not None:
        params["xfmname"] = xfmname
    if templatename is not None:
        params["templatename"] = templatename
    if surfname is not None:
        params["surfname"] = surfname
    if simple is not None:
        params["simple"] = simple
    if diagno is not None:
        params["diagno"] = diagno
    return params


def mris_make_average_surface_cargs(
    params: MrisMakeAverageSurfaceParameters,
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
    cargs.append("mris_make_average_surface")
    cargs.append(params.get("hemi"))
    cargs.append(params.get("outsurfname"))
    cargs.append(params.get("cansurfname"))
    cargs.append(params.get("outsubject"))
    cargs.extend(params.get("subjects"))
    if params.get("sdir") is not None:
        cargs.extend([
            "-sdir",
            params.get("sdir")
        ])
    if params.get("sdir_out") is not None:
        cargs.extend([
            "-sdir-out",
            params.get("sdir_out")
        ])
    if params.get("nonorm_flag"):
        cargs.append("-nonorm")
    if params.get("icoorder") is not None:
        cargs.extend([
            "-i",
            str(params.get("icoorder"))
        ])
    if params.get("xfmname") is not None:
        cargs.extend([
            "-x",
            params.get("xfmname")
        ])
    if params.get("templatename") is not None:
        cargs.extend([
            "-t",
            params.get("templatename")
        ])
    if params.get("surfname") is not None:
        cargs.extend([
            "-s",
            params.get("surfname")
        ])
    if params.get("surf2surf_flag"):
        cargs.append("-surf2surf")
    if params.get("simple") is not None:
        cargs.extend([
            "-simple",
            *params.get("simple")
        ])
    if params.get("diagno") is not None:
        cargs.extend([
            "-v",
            str(params.get("diagno"))
        ])
    return cargs


def mris_make_average_surface_outputs(
    params: MrisMakeAverageSurfaceParameters,
    execution: Execution,
) -> MrisMakeAverageSurfaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisMakeAverageSurfaceOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(params.get("sdir_out") + "/" + params.get("outsubject") + "/" + params.get("outsurfname")) if (params.get("sdir_out") is not None) else None,
    )
    return ret


def mris_make_average_surface_execute(
    params: MrisMakeAverageSurfaceParameters,
    execution: Execution,
) -> MrisMakeAverageSurfaceOutputs:
    """
    A program to average the orig surfaces from the given subject list into a single
    surface using Talairach coords and the spherical transform.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisMakeAverageSurfaceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mris_make_average_surface_cargs(params, execution)
    ret = mris_make_average_surface_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_make_average_surface(
    hemi: str,
    outsurfname: str,
    cansurfname: str,
    outsubject: str,
    subjects: list[str],
    sdir: str | None = None,
    sdir_out: str | None = None,
    nonorm_flag: bool = False,
    icoorder: float | None = None,
    xfmname: str | None = None,
    templatename: str | None = None,
    surfname: str | None = None,
    surf2surf_flag: bool = False,
    simple: list[str] | None = None,
    diagno: float | None = None,
    runner: Runner | None = None,
) -> MrisMakeAverageSurfaceOutputs:
    """
    A program to average the orig surfaces from the given subject list into a single
    surface using Talairach coords and the spherical transform.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        hemi: Hemisphere, lh or rh.
        outsurfname: Output surface name (e.g., avg_orig).
        cansurfname: Registration surface (e.g., sphere.reg).
        outsubject: Name of subject to store the results in.
        subjects: List of subjects to average.
        sdir: Use sdir instead of SUBJECTS_DIR.
        sdir_out: Save results in sdirout/outsubject instead of\
            SUBJECTS_DIR/outsubject.
        nonorm_flag: Do not normalize area.
        icoorder: Use given icosahedron order (default is 7).
        xfmname: Use transforms/xfmname instead of talairach.xfm.
        templatename: Volume to use as geometry template for output surfaces.
        surfname: Use surfname instead of orig.
        surf2surf_flag: Use surf2surf transform instead of parametric surface.
        simple: Compute an average surface from the list of surfaces. All\
            surfaces must have same number of vertices.
        diagno: Set Gdiag_no to diagno.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisMakeAverageSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_MAKE_AVERAGE_SURFACE_METADATA)
    params = mris_make_average_surface_params(hemi=hemi, outsurfname=outsurfname, cansurfname=cansurfname, outsubject=outsubject, subjects=subjects, sdir=sdir, sdir_out=sdir_out, nonorm_flag=nonorm_flag, icoorder=icoorder, xfmname=xfmname, templatename=templatename, surfname=surfname, surf2surf_flag=surf2surf_flag, simple=simple, diagno=diagno)
    return mris_make_average_surface_execute(params, execution)


__all__ = [
    "MRIS_MAKE_AVERAGE_SURFACE_METADATA",
    "MrisMakeAverageSurfaceOutputs",
    "mris_make_average_surface",
    "mris_make_average_surface_params",
]
