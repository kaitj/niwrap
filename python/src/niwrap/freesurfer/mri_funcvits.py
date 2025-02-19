# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_FUNCVITS_METADATA = Metadata(
    id="a906844e0fb427ee5992ebd3da45e1f05aaf100a.boutiques",
    name="mri-funcvits",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriFuncvitsParameters = typing.TypedDict('MriFuncvitsParameters', {
    "__STYX_TYPE__": typing.Literal["mri-funcvits"],
    "stem": str,
    "outdir": str,
    "reg": typing.NotRequired[str | None],
    "paintsurf": typing.NotRequired[str | None],
    "sphere": typing.NotRequired[str | None],
    "icosize": typing.NotRequired[int | None],
    "hemi": typing.NotRequired[list[str] | None],
    "svitdir": typing.NotRequired[str | None],
    "icodir": typing.NotRequired[str | None],
    "umask": typing.NotRequired[str | None],
    "mail": typing.NotRequired[str | None],
    "noforce": bool,
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
        "mri-funcvits": mri_funcvits_cargs,
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


class MriFuncvitsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_funcvits(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_funcvits_params(
    stem: str,
    outdir: str,
    reg: str | None = None,
    paintsurf: str | None = "white",
    sphere: str | None = "sphere",
    icosize: int | None = 10242,
    hemi: list[str] | None = ["lh", "rh"],
    svitdir: str | None = None,
    icodir: str | None = "/usr/local/freesurfer/lib/bem",
    umask: str | None = None,
    mail: str | None = None,
    noforce: bool = False,
) -> MriFuncvitsParameters:
    """
    Build parameters.
    
    Args:
        stem: Template stem.
        outdir: Output directory.
        reg: Registration file.
        paintsurf: Surface upon which to paint.
        sphere: Spherical surface.
        icosize: Icosahedron size.
        hemi: Hemifield(s).
        svitdir: SVIT directory.
        icodir: ICO directory.
        umask: New umask.
        mail: User email for notifications.
        noforce: Do not create if output already exists.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri-funcvits",
        "stem": stem,
        "outdir": outdir,
        "noforce": noforce,
    }
    if reg is not None:
        params["reg"] = reg
    if paintsurf is not None:
        params["paintsurf"] = paintsurf
    if sphere is not None:
        params["sphere"] = sphere
    if icosize is not None:
        params["icosize"] = icosize
    if hemi is not None:
        params["hemi"] = hemi
    if svitdir is not None:
        params["svitdir"] = svitdir
    if icodir is not None:
        params["icodir"] = icodir
    if umask is not None:
        params["umask"] = umask
    if mail is not None:
        params["mail"] = mail
    return params


def mri_funcvits_cargs(
    params: MriFuncvitsParameters,
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
    cargs.append("mri-funcvits")
    cargs.extend([
        "--stem",
        params.get("stem")
    ])
    cargs.extend([
        "--outdir",
        params.get("outdir")
    ])
    if params.get("reg") is not None:
        cargs.extend([
            "--reg",
            params.get("reg")
        ])
    if params.get("paintsurf") is not None:
        cargs.extend([
            "--paintsurf",
            params.get("paintsurf")
        ])
    if params.get("sphere") is not None:
        cargs.extend([
            "--sphere",
            params.get("sphere")
        ])
    if params.get("icosize") is not None:
        cargs.extend([
            "--icosize",
            str(params.get("icosize"))
        ])
    if params.get("hemi") is not None:
        cargs.extend([
            "--hemi",
            *params.get("hemi")
        ])
    if params.get("svitdir") is not None:
        cargs.extend([
            "--svitdir",
            params.get("svitdir")
        ])
    if params.get("icodir") is not None:
        cargs.extend([
            "--icodir",
            params.get("icodir")
        ])
    if params.get("umask") is not None:
        cargs.extend([
            "--umask",
            params.get("umask")
        ])
    if params.get("mail") is not None:
        cargs.extend([
            "--mail",
            params.get("mail")
        ])
    if params.get("noforce"):
        cargs.append("--noforce")
    return cargs


def mri_funcvits_outputs(
    params: MriFuncvitsParameters,
    execution: Execution,
) -> MriFuncvitsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriFuncvitsOutputs(
        root=execution.output_file("."),
    )
    return ret


def mri_funcvits_execute(
    params: MriFuncvitsParameters,
    execution: Execution,
) -> MriFuncvitsOutputs:
    """
    Tool for functional volume to surface conversion in neuroimaging analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriFuncvitsOutputs`).
    """
    params = execution.params(params)
    cargs = mri_funcvits_cargs(params, execution)
    ret = mri_funcvits_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_funcvits(
    stem: str,
    outdir: str,
    reg: str | None = None,
    paintsurf: str | None = "white",
    sphere: str | None = "sphere",
    icosize: int | None = 10242,
    hemi: list[str] | None = ["lh", "rh"],
    svitdir: str | None = None,
    icodir: str | None = "/usr/local/freesurfer/lib/bem",
    umask: str | None = None,
    mail: str | None = None,
    noforce: bool = False,
    runner: Runner | None = None,
) -> MriFuncvitsOutputs:
    """
    Tool for functional volume to surface conversion in neuroimaging analysis.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        stem: Template stem.
        outdir: Output directory.
        reg: Registration file.
        paintsurf: Surface upon which to paint.
        sphere: Spherical surface.
        icosize: Icosahedron size.
        hemi: Hemifield(s).
        svitdir: SVIT directory.
        icodir: ICO directory.
        umask: New umask.
        mail: User email for notifications.
        noforce: Do not create if output already exists.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriFuncvitsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_FUNCVITS_METADATA)
    params = mri_funcvits_params(stem=stem, outdir=outdir, reg=reg, paintsurf=paintsurf, sphere=sphere, icosize=icosize, hemi=hemi, svitdir=svitdir, icodir=icodir, umask=umask, mail=mail, noforce=noforce)
    return mri_funcvits_execute(params, execution)


__all__ = [
    "MRI_FUNCVITS_METADATA",
    "MriFuncvitsOutputs",
    "MriFuncvitsParameters",
    "mri_funcvits",
    "mri_funcvits_params",
]
