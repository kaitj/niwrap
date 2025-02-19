# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_MEASURES_METADATA = Metadata(
    id="21378ea7d8b0e920275d5e4fab477aa23c434ab4.boutiques",
    name="SurfMeasures",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
SurfMeasuresParameters = typing.TypedDict('SurfMeasuresParameters', {
    "__STYX_TYPE__": typing.Literal["SurfMeasures"],
    "spec_file": InputPathType,
    "surf_A": str,
    "surf_B": typing.NotRequired[str | None],
    "out_1D": typing.NotRequired[str | None],
    "out_dset": str,
    "func": typing.NotRequired[list[str] | None],
    "surf_volume": typing.NotRequired[InputPathType | None],
    "cmask": typing.NotRequired[str | None],
    "debug": typing.NotRequired[int | None],
    "dnode": typing.NotRequired[float | None],
    "nodes_1D": typing.NotRequired[InputPathType | None],
    "info_all": bool,
    "info_area": bool,
    "info_norms": bool,
    "info_thick": bool,
    "info_vol": bool,
    "info_volg": bool,
    "ver": bool,
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
        "SurfMeasures": surf_measures_cargs,
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
        "SurfMeasures": surf_measures_outputs,
    }.get(t)


class SurfMeasuresOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_measures(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_1_d: OutputPathType | None
    """Output in 1D format"""
    output_dset: OutputPathType
    """Output in specified dataset format"""


def surf_measures_params(
    spec_file: InputPathType,
    surf_a: str,
    out_dset: str,
    surf_b: str | None = None,
    out_1_d: str | None = None,
    func: list[str] | None = None,
    surf_volume: InputPathType | None = None,
    cmask: str | None = None,
    debug: int | None = None,
    dnode: float | None = None,
    nodes_1_d: InputPathType | None = None,
    info_all: bool = False,
    info_area: bool = False,
    info_norms: bool = False,
    info_thick: bool = False,
    info_vol: bool = False,
    info_volg: bool = False,
    ver: bool = False,
) -> SurfMeasuresParameters:
    """
    Build parameters.
    
    Args:
        spec_file: SUMA spec file containing a list of related surfaces.
        surf_a: Surface name (in spec file) for the first surface.
        out_dset: Output filename with dataset format.
        surf_b: Surface name (in spec file) for the second surface.
        out_1_d: Output filename in 1D format.
        func: Measure function to be applied.
        surf_volume: AFNI volume dataset associated with the surface.
        cmask: Restrict nodes with a mask.
        debug: Display extra run-time information with specified debug level\
            (0-5).
        dnode: Display extra information for specified node.
        nodes_1_d: Restrict output to specific nodes listed in a file.
        info_all: Display all final info.
        info_area: Display total area of each triangulated surface.
        info_norms: Display info about the normals.
        info_thick: Display minimum and maximum thickness between surfaces.
        info_vol: Display total computed volume between surfaces.
        info_volg: Display total computed volume estimated via Gauss' theorem.
        ver: Show program version and compile date.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfMeasures",
        "spec_file": spec_file,
        "surf_A": surf_a,
        "out_dset": out_dset,
        "info_all": info_all,
        "info_area": info_area,
        "info_norms": info_norms,
        "info_thick": info_thick,
        "info_vol": info_vol,
        "info_volg": info_volg,
        "ver": ver,
    }
    if surf_b is not None:
        params["surf_B"] = surf_b
    if out_1_d is not None:
        params["out_1D"] = out_1_d
    if func is not None:
        params["func"] = func
    if surf_volume is not None:
        params["surf_volume"] = surf_volume
    if cmask is not None:
        params["cmask"] = cmask
    if debug is not None:
        params["debug"] = debug
    if dnode is not None:
        params["dnode"] = dnode
    if nodes_1_d is not None:
        params["nodes_1D"] = nodes_1_d
    return params


def surf_measures_cargs(
    params: SurfMeasuresParameters,
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
    cargs.append("SurfMeasures")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("spec_file"))
    ])
    cargs.extend([
        "-surf_A",
        params.get("surf_A")
    ])
    if params.get("surf_B") is not None:
        cargs.extend([
            "-surf_B",
            params.get("surf_B")
        ])
    if params.get("out_1D") is not None:
        cargs.extend([
            "-out_1D",
            params.get("out_1D")
        ])
    cargs.extend([
        "-out",
        params.get("out_dset")
    ])
    if params.get("func") is not None:
        cargs.extend([
            "-func",
            *params.get("func")
        ])
    if params.get("surf_volume") is not None:
        cargs.extend([
            "-sv",
            execution.input_file(params.get("surf_volume"))
        ])
    if params.get("cmask") is not None:
        cargs.extend([
            "-cmask",
            params.get("cmask")
        ])
    if params.get("debug") is not None:
        cargs.extend([
            "-debug",
            str(params.get("debug"))
        ])
    if params.get("dnode") is not None:
        cargs.extend([
            "-dnode",
            str(params.get("dnode"))
        ])
    if params.get("nodes_1D") is not None:
        cargs.extend([
            "-nodes_1D",
            execution.input_file(params.get("nodes_1D"))
        ])
    if params.get("info_all"):
        cargs.append("-info_all")
    if params.get("info_area"):
        cargs.append("-info_area")
    if params.get("info_norms"):
        cargs.append("-info_norms")
    if params.get("info_thick"):
        cargs.append("-info_thick")
    if params.get("info_vol"):
        cargs.append("-info_vol")
    if params.get("info_volg"):
        cargs.append("-info_volg")
    if params.get("ver"):
        cargs.append("-ver")
    return cargs


def surf_measures_outputs(
    params: SurfMeasuresParameters,
    execution: Execution,
) -> SurfMeasuresOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfMeasuresOutputs(
        root=execution.output_file("."),
        output_1_d=execution.output_file(params.get("out_1D") + ".1D") if (params.get("out_1D") is not None) else None,
        output_dset=execution.output_file(params.get("out_dset")),
    )
    return ret


def surf_measures_execute(
    params: SurfMeasuresParameters,
    execution: Execution,
) -> SurfMeasuresOutputs:
    """
    Compute measures from surface dataset(s).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfMeasuresOutputs`).
    """
    params = execution.params(params)
    cargs = surf_measures_cargs(params, execution)
    ret = surf_measures_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_measures(
    spec_file: InputPathType,
    surf_a: str,
    out_dset: str,
    surf_b: str | None = None,
    out_1_d: str | None = None,
    func: list[str] | None = None,
    surf_volume: InputPathType | None = None,
    cmask: str | None = None,
    debug: int | None = None,
    dnode: float | None = None,
    nodes_1_d: InputPathType | None = None,
    info_all: bool = False,
    info_area: bool = False,
    info_norms: bool = False,
    info_thick: bool = False,
    info_vol: bool = False,
    info_volg: bool = False,
    ver: bool = False,
    runner: Runner | None = None,
) -> SurfMeasuresOutputs:
    """
    Compute measures from surface dataset(s).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_file: SUMA spec file containing a list of related surfaces.
        surf_a: Surface name (in spec file) for the first surface.
        out_dset: Output filename with dataset format.
        surf_b: Surface name (in spec file) for the second surface.
        out_1_d: Output filename in 1D format.
        func: Measure function to be applied.
        surf_volume: AFNI volume dataset associated with the surface.
        cmask: Restrict nodes with a mask.
        debug: Display extra run-time information with specified debug level\
            (0-5).
        dnode: Display extra information for specified node.
        nodes_1_d: Restrict output to specific nodes listed in a file.
        info_all: Display all final info.
        info_area: Display total area of each triangulated surface.
        info_norms: Display info about the normals.
        info_thick: Display minimum and maximum thickness between surfaces.
        info_vol: Display total computed volume between surfaces.
        info_volg: Display total computed volume estimated via Gauss' theorem.
        ver: Show program version and compile date.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfMeasuresOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_MEASURES_METADATA)
    params = surf_measures_params(spec_file=spec_file, surf_a=surf_a, surf_b=surf_b, out_1_d=out_1_d, out_dset=out_dset, func=func, surf_volume=surf_volume, cmask=cmask, debug=debug, dnode=dnode, nodes_1_d=nodes_1_d, info_all=info_all, info_area=info_area, info_norms=info_norms, info_thick=info_thick, info_vol=info_vol, info_volg=info_volg, ver=ver)
    return surf_measures_execute(params, execution)


__all__ = [
    "SURF_MEASURES_METADATA",
    "SurfMeasuresOutputs",
    "SurfMeasuresParameters",
    "surf_measures",
    "surf_measures_params",
]
