# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_SURF2_VOL_METADATA = Metadata(
    id="d846efb04834ca6fcc9a5960307e8d15eacf8fd2.boutiques",
    name="3dSurf2Vol",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dSurf2VolParameters = typing.TypedDict('V3dSurf2VolParameters', {
    "__STYX_TYPE__": typing.Literal["3dSurf2Vol"],
    "spec": InputPathType,
    "surface_volume": InputPathType,
    "surf_a": str,
    "surf_b": typing.NotRequired[str | None],
    "grid_parent": InputPathType,
    "map_func": str,
    "prefix": str,
    "surf_xyz_1d": typing.NotRequired[InputPathType | None],
    "sdata_1d": typing.NotRequired[InputPathType | None],
    "sdata": typing.NotRequired[InputPathType | None],
    "f_steps": typing.NotRequired[float | None],
    "f_index": typing.NotRequired[str | None],
    "f_p1_fr": typing.NotRequired[float | None],
    "f_pn_fr": typing.NotRequired[float | None],
    "f_p1_mm": typing.NotRequired[float | None],
    "f_pn_mm": typing.NotRequired[float | None],
    "stop_gap": bool,
    "cmask": typing.NotRequired[str | None],
    "data_expr": typing.NotRequired[str | None],
    "datum": typing.NotRequired[str | None],
    "debug": typing.NotRequired[int | None],
    "dnode": typing.NotRequired[int | None],
    "dvoxel": typing.NotRequired[int | None],
    "noscale": bool,
    "sxyz_orient_as_gpar": bool,
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
        "3dSurf2Vol": v_3d_surf2_vol_cargs,
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
        "3dSurf2Vol": v_3d_surf2_vol_outputs,
    }
    return vt.get(t)


class V3dSurf2VolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_surf2_vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset"""


def v_3d_surf2_vol_params(
    spec: InputPathType,
    surface_volume: InputPathType,
    surf_a: str,
    grid_parent: InputPathType,
    map_func: str,
    prefix: str,
    surf_b: str | None = None,
    surf_xyz_1d: InputPathType | None = None,
    sdata_1d: InputPathType | None = None,
    sdata: InputPathType | None = None,
    f_steps: float | None = None,
    f_index: str | None = None,
    f_p1_fr: float | None = None,
    f_pn_fr: float | None = None,
    f_p1_mm: float | None = None,
    f_pn_mm: float | None = None,
    stop_gap: bool = False,
    cmask: str | None = None,
    data_expr: str | None = None,
    datum: str | None = None,
    debug: int | None = None,
    dnode: int | None = None,
    dvoxel: int | None = None,
    noscale: bool = False,
    sxyz_orient_as_gpar: bool = False,
) -> V3dSurf2VolParameters:
    """
    Build parameters.
    
    Args:
        spec: SUMA spec file.
        surface_volume: AFNI surface volume dataset.
        surf_a: Specify surface A from spec file.
        grid_parent: AFNI grid parent dataset.
        map_func: Surface to dataset function.
        prefix: Prefix for the output dataset.
        surf_b: Specify surface B from spec file.
        surf_xyz_1d: 1D coordinate file.
        sdata_1d: 1D sub-surface data file.
        sdata: NIML or GIFTI formatted dataset.
        f_steps: Partition segments into this many steps.
        f_index: Index by points or voxels.
        f_p1_fr: Offset p1 by a fraction of the length.
        f_pn_fr: Offset pn by a fraction of the length.
        f_p1_mm: Offset p1 by a distance in mm.
        f_pn_mm: Offset pn by a distance in mm.
        stop_gap: Stop when a zero gap has been hit.
        cmask: Command for dataset mask.
        data_expr: Apply expression to surface input.
        datum: Set data type in output dataset.
        debug: Verbose output level.
        dnode: Extra output for specified node.
        dvoxel: Extra output for specified voxel.
        noscale: No scale factor in output dataset.
        sxyz_orient_as_gpar: Assume grid parent orientation for surface xyz.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dSurf2Vol",
        "spec": spec,
        "surface_volume": surface_volume,
        "surf_a": surf_a,
        "grid_parent": grid_parent,
        "map_func": map_func,
        "prefix": prefix,
        "stop_gap": stop_gap,
        "noscale": noscale,
        "sxyz_orient_as_gpar": sxyz_orient_as_gpar,
    }
    if surf_b is not None:
        params["surf_b"] = surf_b
    if surf_xyz_1d is not None:
        params["surf_xyz_1d"] = surf_xyz_1d
    if sdata_1d is not None:
        params["sdata_1d"] = sdata_1d
    if sdata is not None:
        params["sdata"] = sdata
    if f_steps is not None:
        params["f_steps"] = f_steps
    if f_index is not None:
        params["f_index"] = f_index
    if f_p1_fr is not None:
        params["f_p1_fr"] = f_p1_fr
    if f_pn_fr is not None:
        params["f_pn_fr"] = f_pn_fr
    if f_p1_mm is not None:
        params["f_p1_mm"] = f_p1_mm
    if f_pn_mm is not None:
        params["f_pn_mm"] = f_pn_mm
    if cmask is not None:
        params["cmask"] = cmask
    if data_expr is not None:
        params["data_expr"] = data_expr
    if datum is not None:
        params["datum"] = datum
    if debug is not None:
        params["debug"] = debug
    if dnode is not None:
        params["dnode"] = dnode
    if dvoxel is not None:
        params["dvoxel"] = dvoxel
    return params


def v_3d_surf2_vol_cargs(
    params: V3dSurf2VolParameters,
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
    cargs.append("3dSurf2Vol")
    cargs.extend([
        "-spec",
        execution.input_file(params.get("spec"))
    ])
    cargs.extend([
        "-sv",
        execution.input_file(params.get("surface_volume"))
    ])
    cargs.extend([
        "-surf_A",
        params.get("surf_a")
    ])
    if params.get("surf_b") is not None:
        cargs.extend([
            "-surf_B",
            params.get("surf_b")
        ])
    cargs.extend([
        "-grid_parent",
        execution.input_file(params.get("grid_parent"))
    ])
    cargs.extend([
        "-map_func",
        params.get("map_func")
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("surf_xyz_1d") is not None:
        cargs.extend([
            "-surf_xyz_1D",
            execution.input_file(params.get("surf_xyz_1d"))
        ])
    if params.get("sdata_1d") is not None:
        cargs.extend([
            "-sdata_1D",
            execution.input_file(params.get("sdata_1d"))
        ])
    if params.get("sdata") is not None:
        cargs.extend([
            "-sdata",
            execution.input_file(params.get("sdata"))
        ])
    if params.get("f_steps") is not None:
        cargs.extend([
            "-f_steps",
            str(params.get("f_steps"))
        ])
    if params.get("f_index") is not None:
        cargs.extend([
            "-f_index",
            params.get("f_index")
        ])
    if params.get("f_p1_fr") is not None:
        cargs.extend([
            "-f_p1_fr",
            str(params.get("f_p1_fr"))
        ])
    if params.get("f_pn_fr") is not None:
        cargs.extend([
            "-f_pn_fr",
            str(params.get("f_pn_fr"))
        ])
    if params.get("f_p1_mm") is not None:
        cargs.extend([
            "-f_p1_mm",
            str(params.get("f_p1_mm"))
        ])
    if params.get("f_pn_mm") is not None:
        cargs.extend([
            "-f_pn_mm",
            str(params.get("f_pn_mm"))
        ])
    if params.get("stop_gap"):
        cargs.append("-stop_gap")
    if params.get("cmask") is not None:
        cargs.extend([
            "-cmask",
            params.get("cmask")
        ])
    if params.get("data_expr") is not None:
        cargs.extend([
            "-data_expr",
            params.get("data_expr")
        ])
    if params.get("datum") is not None:
        cargs.extend([
            "-datum",
            params.get("datum")
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
    if params.get("dvoxel") is not None:
        cargs.extend([
            "-dvoxel",
            str(params.get("dvoxel"))
        ])
    if params.get("noscale"):
        cargs.append("-noscale")
    if params.get("sxyz_orient_as_gpar"):
        cargs.append("-sxyz_orient_as_gpar")
    return cargs


def v_3d_surf2_vol_outputs(
    params: V3dSurf2VolParameters,
    execution: Execution,
) -> V3dSurf2VolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dSurf2VolOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + "+*[gz]"),
    )
    return ret


def v_3d_surf2_vol_execute(
    params: V3dSurf2VolParameters,
    execution: Execution,
) -> V3dSurf2VolOutputs:
    """
    Map data from a surface domain to an AFNI volume domain.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dSurf2VolOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_surf2_vol_cargs(params, execution)
    ret = v_3d_surf2_vol_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_surf2_vol(
    spec: InputPathType,
    surface_volume: InputPathType,
    surf_a: str,
    grid_parent: InputPathType,
    map_func: str,
    prefix: str,
    surf_b: str | None = None,
    surf_xyz_1d: InputPathType | None = None,
    sdata_1d: InputPathType | None = None,
    sdata: InputPathType | None = None,
    f_steps: float | None = None,
    f_index: str | None = None,
    f_p1_fr: float | None = None,
    f_pn_fr: float | None = None,
    f_p1_mm: float | None = None,
    f_pn_mm: float | None = None,
    stop_gap: bool = False,
    cmask: str | None = None,
    data_expr: str | None = None,
    datum: str | None = None,
    debug: int | None = None,
    dnode: int | None = None,
    dvoxel: int | None = None,
    noscale: bool = False,
    sxyz_orient_as_gpar: bool = False,
    runner: Runner | None = None,
) -> V3dSurf2VolOutputs:
    """
    Map data from a surface domain to an AFNI volume domain.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec: SUMA spec file.
        surface_volume: AFNI surface volume dataset.
        surf_a: Specify surface A from spec file.
        grid_parent: AFNI grid parent dataset.
        map_func: Surface to dataset function.
        prefix: Prefix for the output dataset.
        surf_b: Specify surface B from spec file.
        surf_xyz_1d: 1D coordinate file.
        sdata_1d: 1D sub-surface data file.
        sdata: NIML or GIFTI formatted dataset.
        f_steps: Partition segments into this many steps.
        f_index: Index by points or voxels.
        f_p1_fr: Offset p1 by a fraction of the length.
        f_pn_fr: Offset pn by a fraction of the length.
        f_p1_mm: Offset p1 by a distance in mm.
        f_pn_mm: Offset pn by a distance in mm.
        stop_gap: Stop when a zero gap has been hit.
        cmask: Command for dataset mask.
        data_expr: Apply expression to surface input.
        datum: Set data type in output dataset.
        debug: Verbose output level.
        dnode: Extra output for specified node.
        dvoxel: Extra output for specified voxel.
        noscale: No scale factor in output dataset.
        sxyz_orient_as_gpar: Assume grid parent orientation for surface xyz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSurf2VolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SURF2_VOL_METADATA)
    params = v_3d_surf2_vol_params(spec=spec, surface_volume=surface_volume, surf_a=surf_a, surf_b=surf_b, grid_parent=grid_parent, map_func=map_func, prefix=prefix, surf_xyz_1d=surf_xyz_1d, sdata_1d=sdata_1d, sdata=sdata, f_steps=f_steps, f_index=f_index, f_p1_fr=f_p1_fr, f_pn_fr=f_pn_fr, f_p1_mm=f_p1_mm, f_pn_mm=f_pn_mm, stop_gap=stop_gap, cmask=cmask, data_expr=data_expr, datum=datum, debug=debug, dnode=dnode, dvoxel=dvoxel, noscale=noscale, sxyz_orient_as_gpar=sxyz_orient_as_gpar)
    return v_3d_surf2_vol_execute(params, execution)


__all__ = [
    "V3dSurf2VolOutputs",
    "V_3D_SURF2_VOL_METADATA",
    "v_3d_surf2_vol",
    "v_3d_surf2_vol_params",
]
