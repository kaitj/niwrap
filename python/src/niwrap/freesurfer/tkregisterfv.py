# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TKREGISTERFV_METADATA = Metadata(
    id="5ebc1a63857c8578925dcc917e8e3ae5ac3c4e9b.boutiques",
    name="tkregisterfv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
TkregisterfvParameters = typing.TypedDict('TkregisterfvParameters', {
    "__STYX_TYPE__": typing.Literal["tkregisterfv"],
    "mov": typing.NotRequired[InputPathType | None],
    "targ": typing.NotRequired[InputPathType | None],
    "reg": InputPathType,
    "subject": typing.NotRequired[str | None],
    "fstarg": typing.NotRequired[InputPathType | None],
    "sd": typing.NotRequired[str | None],
    "seg": typing.NotRequired[InputPathType | None],
    "aseg_flag": bool,
    "aparc_aseg_flag": bool,
    "opacity": typing.NotRequired[float | None],
    "surfs_flag": bool,
    "pial_surfs_flag": bool,
    "all_surfs_flag": bool,
    "no_surfs_flag": bool,
    "lh_only_flag": bool,
    "rh_only_flag": bool,
    "surf": typing.NotRequired[InputPathType | None],
    "aux_s": typing.NotRequired[InputPathType | None],
    "plane": typing.NotRequired[str | None],
    "no_config_flag": bool,
    "mov2": typing.NotRequired[InputPathType | None],
    "reg2": typing.NotRequired[InputPathType | None],
    "mov3": typing.NotRequired[InputPathType | None],
    "reg3": typing.NotRequired[InputPathType | None],
    "heat_flag": bool,
    "regheader_flag": bool,
    "params": typing.NotRequired[list[float] | None],
    "flip_x_flag": bool,
    "flip_y_flag": bool,
    "flip_z_flag": bool,
    "fstal": bool,
    "aux": typing.NotRequired[InputPathType | None],
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
        "tkregisterfv": tkregisterfv_cargs,
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


class TkregisterfvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tkregisterfv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tkregisterfv_params(
    reg: InputPathType,
    mov: InputPathType | None = None,
    targ: InputPathType | None = None,
    subject: str | None = None,
    fstarg: InputPathType | None = None,
    sd: str | None = None,
    seg: InputPathType | None = None,
    aseg_flag: bool = False,
    aparc_aseg_flag: bool = False,
    opacity: float | None = None,
    surfs_flag: bool = False,
    pial_surfs_flag: bool = False,
    all_surfs_flag: bool = False,
    no_surfs_flag: bool = False,
    lh_only_flag: bool = False,
    rh_only_flag: bool = False,
    surf: InputPathType | None = None,
    aux_s: InputPathType | None = None,
    plane: str | None = None,
    no_config_flag: bool = False,
    mov2: InputPathType | None = None,
    reg2: InputPathType | None = None,
    mov3: InputPathType | None = None,
    reg3: InputPathType | None = None,
    heat_flag: bool = False,
    regheader_flag: bool = False,
    params: list[float] | None = None,
    flip_x_flag: bool = False,
    flip_y_flag: bool = False,
    flip_z_flag: bool = False,
    fstal: bool = False,
    aux: InputPathType | None = None,
) -> TkregisterfvParameters:
    """
    Build parameters.
    
    Args:
        reg: LTA registration file.
        mov: Moving image volume.
        targ: Target image volume.
        subject: Subject identifier for FreeSurfer directories.
        fstarg: Freesurfer target volume instead of orig.mgz.
        sd: FreeSurfer SUBJECTS_DIR environment variable.
        seg: Segmentation volume to load.
        aseg_flag: Load aseg.mgz as segmentation volume.
        aparc_aseg_flag: Load aparc+aseg.mgz as segmentation volume.
        opacity: Set segmentation volume opacity.
        surfs_flag: Load left and right hemisphere white matter surfaces.
        pial_surfs_flag: Load pial surfaces instead of white matter surfaces.
        all_surfs_flag: Load both pial and white matter surfaces.
        no_surfs_flag: Do not load any surfaces.
        lh_only_flag: Load only left hemisphere surface.
        rh_only_flag: Load only right hemisphere surface.
        surf: Explicit path to surface to load.
        aux_s: Explicit path to auxiliary surface to load.
        plane: Plane view: cor, sag, ax.
        no_config_flag: Do not automatically raise transform config window.
        mov2: Provide a second moving image volume.
        reg2: Provide a second registration file.
        mov3: Provide a third moving image volume.
        reg3: Provide a third registration file.
        heat_flag: Use heat map color tables for all volumes.
        regheader_flag: Create registration file assuming the two volumes share\
            a RAS.
        params: Affine matrix parameters: translations in mm, rotations in\
            degrees.
        flip_x_flag: Regheader with rx=180.
        flip_y_flag: Regheader with ry=180.
        flip_z_flag: Regheader with rz=180.
        fstal: Modify the talairach.xfm with subject.
        aux: Load auxiliary volumes with registration.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tkregisterfv",
        "reg": reg,
        "aseg_flag": aseg_flag,
        "aparc_aseg_flag": aparc_aseg_flag,
        "surfs_flag": surfs_flag,
        "pial_surfs_flag": pial_surfs_flag,
        "all_surfs_flag": all_surfs_flag,
        "no_surfs_flag": no_surfs_flag,
        "lh_only_flag": lh_only_flag,
        "rh_only_flag": rh_only_flag,
        "no_config_flag": no_config_flag,
        "heat_flag": heat_flag,
        "regheader_flag": regheader_flag,
        "flip_x_flag": flip_x_flag,
        "flip_y_flag": flip_y_flag,
        "flip_z_flag": flip_z_flag,
        "fstal": fstal,
    }
    if mov is not None:
        params["mov"] = mov
    if targ is not None:
        params["targ"] = targ
    if subject is not None:
        params["subject"] = subject
    if fstarg is not None:
        params["fstarg"] = fstarg
    if sd is not None:
        params["sd"] = sd
    if seg is not None:
        params["seg"] = seg
    if opacity is not None:
        params["opacity"] = opacity
    if surf is not None:
        params["surf"] = surf
    if aux_s is not None:
        params["aux_s"] = aux_s
    if plane is not None:
        params["plane"] = plane
    if mov2 is not None:
        params["mov2"] = mov2
    if reg2 is not None:
        params["reg2"] = reg2
    if mov3 is not None:
        params["mov3"] = mov3
    if reg3 is not None:
        params["reg3"] = reg3
    if params is not None:
        params["params"] = params
    if aux is not None:
        params["aux"] = aux
    return params


def tkregisterfv_cargs(
    params: TkregisterfvParameters,
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
    cargs.append("tkregisterfv")
    if params.get("mov") is not None:
        cargs.extend([
            "--mov",
            execution.input_file(params.get("mov"))
        ])
    if params.get("targ") is not None:
        cargs.extend([
            "--targ",
            execution.input_file(params.get("targ"))
        ])
    cargs.extend([
        "--reg",
        execution.input_file(params.get("reg"))
    ])
    if params.get("subject") is not None:
        cargs.extend([
            "--s",
            params.get("subject")
        ])
    if params.get("fstarg") is not None:
        cargs.extend([
            "--fstarg",
            execution.input_file(params.get("fstarg"))
        ])
    if params.get("sd") is not None:
        cargs.extend([
            "--sd",
            params.get("sd")
        ])
    if params.get("seg") is not None:
        cargs.extend([
            "--seg",
            execution.input_file(params.get("seg"))
        ])
    if params.get("aseg_flag"):
        cargs.append("--aseg")
    if params.get("aparc_aseg_flag"):
        cargs.append("--aparc+aseg")
    if params.get("opacity") is not None:
        cargs.extend([
            "--opacity",
            str(params.get("opacity"))
        ])
    if params.get("surfs_flag"):
        cargs.append("--surfs")
    if params.get("pial_surfs_flag"):
        cargs.append("--pial-surfs")
    if params.get("all_surfs_flag"):
        cargs.append("--all-surfs")
    if params.get("no_surfs_flag"):
        cargs.append("--no-surfs")
    if params.get("lh_only_flag"):
        cargs.append("--lh-only")
    if params.get("rh_only_flag"):
        cargs.append("--rh-only")
    if params.get("surf") is not None:
        cargs.extend([
            "--surf",
            execution.input_file(params.get("surf"))
        ])
    if params.get("aux_s") is not None:
        cargs.extend([
            "--aux-surf",
            execution.input_file(params.get("aux_s"))
        ])
    if params.get("plane") is not None:
        cargs.extend([
            "--plane",
            params.get("plane")
        ])
    if params.get("no_config_flag"):
        cargs.append("--no-config")
    if params.get("mov2") is not None:
        cargs.extend([
            "--mov2",
            execution.input_file(params.get("mov2"))
        ])
    if params.get("reg2") is not None:
        cargs.extend([
            "--reg2",
            execution.input_file(params.get("reg2"))
        ])
    if params.get("mov3") is not None:
        cargs.extend([
            "--mov3",
            execution.input_file(params.get("mov3"))
        ])
    if params.get("reg3") is not None:
        cargs.extend([
            "--reg3",
            execution.input_file(params.get("reg3"))
        ])
    if params.get("heat_flag"):
        cargs.append("--heat")
    if params.get("regheader_flag"):
        cargs.append("--regheader")
    if params.get("params") is not None:
        cargs.extend([
            "--params",
            *map(str, params.get("params"))
        ])
    if params.get("flip_x_flag"):
        cargs.append("--flip-x")
    if params.get("flip_y_flag"):
        cargs.append("--flip-y")
    if params.get("flip_z_flag"):
        cargs.append("--flip-z")
    if params.get("fstal"):
        cargs.append("--fstal")
    if params.get("aux") is not None:
        cargs.extend([
            "--aux",
            execution.input_file(params.get("aux"))
        ])
    return cargs


def tkregisterfv_outputs(
    params: TkregisterfvParameters,
    execution: Execution,
) -> TkregisterfvOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TkregisterfvOutputs(
        root=execution.output_file("."),
    )
    return ret


def tkregisterfv_execute(
    params: TkregisterfvParameters,
    execution: Execution,
) -> TkregisterfvOutputs:
    """
    A script that runs freeview with arguments like tkregister, focusing on LTA
    files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TkregisterfvOutputs`).
    """
    params = execution.params(params)
    cargs = tkregisterfv_cargs(params, execution)
    ret = tkregisterfv_outputs(params, execution)
    execution.run(cargs)
    return ret


def tkregisterfv(
    reg: InputPathType,
    mov: InputPathType | None = None,
    targ: InputPathType | None = None,
    subject: str | None = None,
    fstarg: InputPathType | None = None,
    sd: str | None = None,
    seg: InputPathType | None = None,
    aseg_flag: bool = False,
    aparc_aseg_flag: bool = False,
    opacity: float | None = None,
    surfs_flag: bool = False,
    pial_surfs_flag: bool = False,
    all_surfs_flag: bool = False,
    no_surfs_flag: bool = False,
    lh_only_flag: bool = False,
    rh_only_flag: bool = False,
    surf: InputPathType | None = None,
    aux_s: InputPathType | None = None,
    plane: str | None = None,
    no_config_flag: bool = False,
    mov2: InputPathType | None = None,
    reg2: InputPathType | None = None,
    mov3: InputPathType | None = None,
    reg3: InputPathType | None = None,
    heat_flag: bool = False,
    regheader_flag: bool = False,
    params: list[float] | None = None,
    flip_x_flag: bool = False,
    flip_y_flag: bool = False,
    flip_z_flag: bool = False,
    fstal: bool = False,
    aux: InputPathType | None = None,
    runner: Runner | None = None,
) -> TkregisterfvOutputs:
    """
    A script that runs freeview with arguments like tkregister, focusing on LTA
    files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        reg: LTA registration file.
        mov: Moving image volume.
        targ: Target image volume.
        subject: Subject identifier for FreeSurfer directories.
        fstarg: Freesurfer target volume instead of orig.mgz.
        sd: FreeSurfer SUBJECTS_DIR environment variable.
        seg: Segmentation volume to load.
        aseg_flag: Load aseg.mgz as segmentation volume.
        aparc_aseg_flag: Load aparc+aseg.mgz as segmentation volume.
        opacity: Set segmentation volume opacity.
        surfs_flag: Load left and right hemisphere white matter surfaces.
        pial_surfs_flag: Load pial surfaces instead of white matter surfaces.
        all_surfs_flag: Load both pial and white matter surfaces.
        no_surfs_flag: Do not load any surfaces.
        lh_only_flag: Load only left hemisphere surface.
        rh_only_flag: Load only right hemisphere surface.
        surf: Explicit path to surface to load.
        aux_s: Explicit path to auxiliary surface to load.
        plane: Plane view: cor, sag, ax.
        no_config_flag: Do not automatically raise transform config window.
        mov2: Provide a second moving image volume.
        reg2: Provide a second registration file.
        mov3: Provide a third moving image volume.
        reg3: Provide a third registration file.
        heat_flag: Use heat map color tables for all volumes.
        regheader_flag: Create registration file assuming the two volumes share\
            a RAS.
        params: Affine matrix parameters: translations in mm, rotations in\
            degrees.
        flip_x_flag: Regheader with rx=180.
        flip_y_flag: Regheader with ry=180.
        flip_z_flag: Regheader with rz=180.
        fstal: Modify the talairach.xfm with subject.
        aux: Load auxiliary volumes with registration.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TkregisterfvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKREGISTERFV_METADATA)
    params = tkregisterfv_params(mov=mov, targ=targ, reg=reg, subject=subject, fstarg=fstarg, sd=sd, seg=seg, aseg_flag=aseg_flag, aparc_aseg_flag=aparc_aseg_flag, opacity=opacity, surfs_flag=surfs_flag, pial_surfs_flag=pial_surfs_flag, all_surfs_flag=all_surfs_flag, no_surfs_flag=no_surfs_flag, lh_only_flag=lh_only_flag, rh_only_flag=rh_only_flag, surf=surf, aux_s=aux_s, plane=plane, no_config_flag=no_config_flag, mov2=mov2, reg2=reg2, mov3=mov3, reg3=reg3, heat_flag=heat_flag, regheader_flag=regheader_flag, params=params, flip_x_flag=flip_x_flag, flip_y_flag=flip_y_flag, flip_z_flag=flip_z_flag, fstal=fstal, aux=aux)
    return tkregisterfv_execute(params, execution)


__all__ = [
    "TKREGISTERFV_METADATA",
    "TkregisterfvOutputs",
    "TkregisterfvParameters",
    "tkregisterfv",
    "tkregisterfv_params",
]
