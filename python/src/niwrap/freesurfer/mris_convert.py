# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_CONVERT_METADATA = Metadata(
    id="2935cffb17b5edbbc239ffbc0efa59b1c070ffca.boutiques",
    name="mris_convert",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisConvertParameters = typing.TypedDict('MrisConvertParameters', {
    "__STYX_TYPE__": typing.Literal["mris_convert"],
    "input_file": InputPathType,
    "second_input_file": typing.NotRequired[InputPathType | None],
    "output_file": str,
    "patch": bool,
    "curv_overlay_files": typing.NotRequired[list[str] | None],
    "functional_data_file": typing.NotRequired[InputPathType | None],
    "orig_positions": typing.NotRequired[str | None],
    "scale": typing.NotRequired[float | None],
    "rescale": bool,
    "talairach_xfm": typing.NotRequired[str | None],
    "normals": bool,
    "neighbors": bool,
    "xyz": bool,
    "annotation_file": typing.NotRequired[InputPathType | None],
    "parcstats_file": typing.NotRequired[InputPathType | None],
    "gifti_dataarray_num": typing.NotRequired[float | None],
    "label_file": typing.NotRequired[InputPathType | None],
    "label_stats_file": typing.NotRequired[str | None],
    "combine_surfs": bool,
    "merge_gifti": bool,
    "split_gifti": bool,
    "gifti_outdir": typing.NotRequired[str | None],
    "delete_cmds": bool,
    "center": bool,
    "vol_geom": typing.NotRequired[str | None],
    "remove_vol_geom": bool,
    "to_surf": typing.NotRequired[str | None],
    "to_scanner": bool,
    "to_tkr": bool,
    "userealras": bool,
    "usesurfras": bool,
    "upsample": typing.NotRequired[str | None],
    "volume": typing.NotRequired[str | None],
    "area": typing.NotRequired[str | None],
    "angle": typing.NotRequired[str | None],
    "label_to_mask": typing.NotRequired[str | None],
    "cras_add": bool,
    "cras_subtract": bool,
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
        "mris_convert": mris_convert_cargs,
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
        "mris_convert": mris_convert_outputs,
    }.get(t)


class MrisConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_surface: OutputPathType
    """Output converted surface file"""


def mris_convert_params(
    input_file: InputPathType,
    output_file: str,
    second_input_file: InputPathType | None = None,
    patch: bool = False,
    curv_overlay_files: list[str] | None = None,
    functional_data_file: InputPathType | None = None,
    orig_positions: str | None = None,
    scale: float | None = None,
    rescale: bool = False,
    talairach_xfm: str | None = None,
    normals: bool = False,
    neighbors: bool = False,
    xyz: bool = False,
    annotation_file: InputPathType | None = None,
    parcstats_file: InputPathType | None = None,
    gifti_dataarray_num: float | None = None,
    label_file: InputPathType | None = None,
    label_stats_file: str | None = None,
    combine_surfs: bool = False,
    merge_gifti: bool = False,
    split_gifti: bool = False,
    gifti_outdir: str | None = None,
    delete_cmds: bool = False,
    center: bool = False,
    vol_geom: str | None = None,
    remove_vol_geom: bool = False,
    to_surf: str | None = None,
    to_scanner: bool = False,
    to_tkr: bool = False,
    userealras: bool = False,
    usesurfras: bool = False,
    upsample: str | None = None,
    volume: str | None = None,
    area: str | None = None,
    angle: str | None = None,
    label_to_mask: str | None = None,
    cras_add: bool = False,
    cras_subtract: bool = False,
) -> MrisConvertParameters:
    """
    Build parameters.
    
    Args:
        input_file: Input filename.
        output_file: Output filename.
        second_input_file: Second input filename to be combined, required for\
            --combinesurfs.
        patch: Input file is a patch file, not a full surface.
        curv_overlay_files: Input scalar curv overlay files.
        functional_data_file: Input functional time-series or other multi-frame\
            data.
        orig_positions: Read orig positions.
        scale: Scale vertex xyz by scale.
        rescale: Rescale vertex xyz so total area is same as group average.
        talairach_xfm: Apply talairach xfm of subject to vertex xyz.
        normals: Output ascii file where vertex data is the surface normal\
            vector.
        neighbors: Write out neighbors of a vertex in each row.
        xyz: Print only surface xyz to ascii file.
        annotation_file: Input annotation or gifti label data.
        parcstats_file: Input text file containing label/val pairs for\
            parcellation.
        gifti_dataarray_num: Input gifti dataarray number to use.
        label_file: Input .label file and name for this label.
        label_stats_file: Output gifti file to which label stats will be\
            written.
        combine_surfs: Combine surface files, two input surface files required.
        merge_gifti: Generate combined gifti file with surface and multiple\
            curvature data.
        split_gifti: Separate surface and data array from combined gifti file.
        gifti_outdir: Output directory for generated gifti files.
        delete_cmds: Delete command lines in surface.
        center: Put center of surface at (0,0,0).
        vol_geom: Use MRIVol to set the volume geometry.
        remove_vol_geom: Set the valid flag in vg to 0.
        to_surf: Copy coordinates from surfcoords to output (good for patches).
        to_scanner: Convert coordinates from native FS (tkr) coords to scanner\
            coords.
        to_tkr: Convert coordinates from scanner coords to native FS (tkr)\
            coords.
        userealras: Same as --to-scanner.
        usesurfras: Same as --to-tkr.
        upsample: Upsample N times by splitting edges/faces.
        volume: Compute vertex-wise volume.
        area: Compute vertex-wise area.
        angle: Compute cortical orientation angles.
        label_to_mask: Convert a surface-based label to a binary mask.
        cras_add: Shift center to scanner coordinate center.
        cras_subtract: Shift center from scanner coordinate center.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_convert",
        "input_file": input_file,
        "output_file": output_file,
        "patch": patch,
        "rescale": rescale,
        "normals": normals,
        "neighbors": neighbors,
        "xyz": xyz,
        "combine_surfs": combine_surfs,
        "merge_gifti": merge_gifti,
        "split_gifti": split_gifti,
        "delete_cmds": delete_cmds,
        "center": center,
        "remove_vol_geom": remove_vol_geom,
        "to_scanner": to_scanner,
        "to_tkr": to_tkr,
        "userealras": userealras,
        "usesurfras": usesurfras,
        "cras_add": cras_add,
        "cras_subtract": cras_subtract,
    }
    if second_input_file is not None:
        params["second_input_file"] = second_input_file
    if curv_overlay_files is not None:
        params["curv_overlay_files"] = curv_overlay_files
    if functional_data_file is not None:
        params["functional_data_file"] = functional_data_file
    if orig_positions is not None:
        params["orig_positions"] = orig_positions
    if scale is not None:
        params["scale"] = scale
    if talairach_xfm is not None:
        params["talairach_xfm"] = talairach_xfm
    if annotation_file is not None:
        params["annotation_file"] = annotation_file
    if parcstats_file is not None:
        params["parcstats_file"] = parcstats_file
    if gifti_dataarray_num is not None:
        params["gifti_dataarray_num"] = gifti_dataarray_num
    if label_file is not None:
        params["label_file"] = label_file
    if label_stats_file is not None:
        params["label_stats_file"] = label_stats_file
    if gifti_outdir is not None:
        params["gifti_outdir"] = gifti_outdir
    if vol_geom is not None:
        params["vol_geom"] = vol_geom
    if to_surf is not None:
        params["to_surf"] = to_surf
    if upsample is not None:
        params["upsample"] = upsample
    if volume is not None:
        params["volume"] = volume
    if area is not None:
        params["area"] = area
    if angle is not None:
        params["angle"] = angle
    if label_to_mask is not None:
        params["label_to_mask"] = label_to_mask
    return params


def mris_convert_cargs(
    params: MrisConvertParameters,
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
    cargs.append("mris_convert")
    cargs.append(execution.input_file(params.get("input_file")))
    if params.get("second_input_file") is not None:
        cargs.append(execution.input_file(params.get("second_input_file")))
    cargs.append(params.get("output_file"))
    if params.get("patch"):
        cargs.append("-p")
    if params.get("curv_overlay_files") is not None:
        cargs.extend([
            "-c",
            *params.get("curv_overlay_files")
        ])
    if params.get("functional_data_file") is not None:
        cargs.extend([
            "-f",
            execution.input_file(params.get("functional_data_file"))
        ])
    if params.get("orig_positions") is not None:
        cargs.extend([
            "-o",
            params.get("orig_positions")
        ])
    if params.get("scale") is not None:
        cargs.extend([
            "-s",
            str(params.get("scale"))
        ])
    if params.get("rescale"):
        cargs.append("-r")
    if params.get("talairach_xfm") is not None:
        cargs.extend([
            "-t",
            params.get("talairach_xfm")
        ])
    if params.get("normals"):
        cargs.append("-n")
    if params.get("neighbors"):
        cargs.append("-v")
    if params.get("xyz"):
        cargs.append("-a")
    if params.get("annotation_file") is not None:
        cargs.extend([
            "--annot",
            execution.input_file(params.get("annotation_file"))
        ])
    if params.get("parcstats_file") is not None:
        cargs.extend([
            "--parcstats",
            execution.input_file(params.get("parcstats_file"))
        ])
    if params.get("gifti_dataarray_num") is not None:
        cargs.extend([
            "--da_num",
            str(params.get("gifti_dataarray_num"))
        ])
    if params.get("label_file") is not None:
        cargs.extend([
            "--label",
            execution.input_file(params.get("label_file"))
        ])
    if params.get("label_stats_file") is not None:
        cargs.extend([
            "--labelstats",
            params.get("label_stats_file")
        ])
    if params.get("combine_surfs"):
        cargs.append("--combinesurfs")
    if params.get("merge_gifti"):
        cargs.append("--mergegifti")
    if params.get("split_gifti"):
        cargs.append("--splitgifti")
    if params.get("gifti_outdir") is not None:
        cargs.extend([
            "--giftioutdir",
            params.get("gifti_outdir")
        ])
    if params.get("delete_cmds"):
        cargs.append("--delete-cmds")
    if params.get("center"):
        cargs.append("--center")
    if params.get("vol_geom") is not None:
        cargs.extend([
            "--vol-geom",
            params.get("vol_geom")
        ])
    if params.get("remove_vol_geom"):
        cargs.append("--remove-vol-geom")
    if params.get("to_surf") is not None:
        cargs.extend([
            "--to-surf",
            params.get("to_surf")
        ])
    if params.get("to_scanner"):
        cargs.append("--to-scanner")
    if params.get("to_tkr"):
        cargs.append("--to-tkr")
    if params.get("userealras"):
        cargs.append("--userealras")
    if params.get("usesurfras"):
        cargs.append("--usesurfras")
    if params.get("upsample") is not None:
        cargs.extend([
            "--upsample",
            params.get("upsample")
        ])
    if params.get("volume") is not None:
        cargs.extend([
            "--volume",
            params.get("volume")
        ])
    if params.get("area") is not None:
        cargs.extend([
            "--area",
            params.get("area")
        ])
    if params.get("angle") is not None:
        cargs.extend([
            "--angle",
            params.get("angle")
        ])
    if params.get("label_to_mask") is not None:
        cargs.extend([
            "--label2mask",
            params.get("label_to_mask")
        ])
    if params.get("cras_add"):
        cargs.append("--cras_add")
    if params.get("cras_subtract"):
        cargs.append("--cras_subtract")
    return cargs


def mris_convert_outputs(
    params: MrisConvertParameters,
    execution: Execution,
) -> MrisConvertOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisConvertOutputs(
        root=execution.output_file("."),
        converted_surface=execution.output_file(params.get("output_file")),
    )
    return ret


def mris_convert_execute(
    params: MrisConvertParameters,
    execution: Execution,
) -> MrisConvertOutputs:
    """
    This program will convert MRI-surface data formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisConvertOutputs`).
    """
    params = execution.params(params)
    cargs = mris_convert_cargs(params, execution)
    ret = mris_convert_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_convert(
    input_file: InputPathType,
    output_file: str,
    second_input_file: InputPathType | None = None,
    patch: bool = False,
    curv_overlay_files: list[str] | None = None,
    functional_data_file: InputPathType | None = None,
    orig_positions: str | None = None,
    scale: float | None = None,
    rescale: bool = False,
    talairach_xfm: str | None = None,
    normals: bool = False,
    neighbors: bool = False,
    xyz: bool = False,
    annotation_file: InputPathType | None = None,
    parcstats_file: InputPathType | None = None,
    gifti_dataarray_num: float | None = None,
    label_file: InputPathType | None = None,
    label_stats_file: str | None = None,
    combine_surfs: bool = False,
    merge_gifti: bool = False,
    split_gifti: bool = False,
    gifti_outdir: str | None = None,
    delete_cmds: bool = False,
    center: bool = False,
    vol_geom: str | None = None,
    remove_vol_geom: bool = False,
    to_surf: str | None = None,
    to_scanner: bool = False,
    to_tkr: bool = False,
    userealras: bool = False,
    usesurfras: bool = False,
    upsample: str | None = None,
    volume: str | None = None,
    area: str | None = None,
    angle: str | None = None,
    label_to_mask: str | None = None,
    cras_add: bool = False,
    cras_subtract: bool = False,
    runner: Runner | None = None,
) -> MrisConvertOutputs:
    """
    This program will convert MRI-surface data formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input filename.
        output_file: Output filename.
        second_input_file: Second input filename to be combined, required for\
            --combinesurfs.
        patch: Input file is a patch file, not a full surface.
        curv_overlay_files: Input scalar curv overlay files.
        functional_data_file: Input functional time-series or other multi-frame\
            data.
        orig_positions: Read orig positions.
        scale: Scale vertex xyz by scale.
        rescale: Rescale vertex xyz so total area is same as group average.
        talairach_xfm: Apply talairach xfm of subject to vertex xyz.
        normals: Output ascii file where vertex data is the surface normal\
            vector.
        neighbors: Write out neighbors of a vertex in each row.
        xyz: Print only surface xyz to ascii file.
        annotation_file: Input annotation or gifti label data.
        parcstats_file: Input text file containing label/val pairs for\
            parcellation.
        gifti_dataarray_num: Input gifti dataarray number to use.
        label_file: Input .label file and name for this label.
        label_stats_file: Output gifti file to which label stats will be\
            written.
        combine_surfs: Combine surface files, two input surface files required.
        merge_gifti: Generate combined gifti file with surface and multiple\
            curvature data.
        split_gifti: Separate surface and data array from combined gifti file.
        gifti_outdir: Output directory for generated gifti files.
        delete_cmds: Delete command lines in surface.
        center: Put center of surface at (0,0,0).
        vol_geom: Use MRIVol to set the volume geometry.
        remove_vol_geom: Set the valid flag in vg to 0.
        to_surf: Copy coordinates from surfcoords to output (good for patches).
        to_scanner: Convert coordinates from native FS (tkr) coords to scanner\
            coords.
        to_tkr: Convert coordinates from scanner coords to native FS (tkr)\
            coords.
        userealras: Same as --to-scanner.
        usesurfras: Same as --to-tkr.
        upsample: Upsample N times by splitting edges/faces.
        volume: Compute vertex-wise volume.
        area: Compute vertex-wise area.
        angle: Compute cortical orientation angles.
        label_to_mask: Convert a surface-based label to a binary mask.
        cras_add: Shift center to scanner coordinate center.
        cras_subtract: Shift center from scanner coordinate center.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CONVERT_METADATA)
    params = mris_convert_params(input_file=input_file, second_input_file=second_input_file, output_file=output_file, patch=patch, curv_overlay_files=curv_overlay_files, functional_data_file=functional_data_file, orig_positions=orig_positions, scale=scale, rescale=rescale, talairach_xfm=talairach_xfm, normals=normals, neighbors=neighbors, xyz=xyz, annotation_file=annotation_file, parcstats_file=parcstats_file, gifti_dataarray_num=gifti_dataarray_num, label_file=label_file, label_stats_file=label_stats_file, combine_surfs=combine_surfs, merge_gifti=merge_gifti, split_gifti=split_gifti, gifti_outdir=gifti_outdir, delete_cmds=delete_cmds, center=center, vol_geom=vol_geom, remove_vol_geom=remove_vol_geom, to_surf=to_surf, to_scanner=to_scanner, to_tkr=to_tkr, userealras=userealras, usesurfras=usesurfras, upsample=upsample, volume=volume, area=area, angle=angle, label_to_mask=label_to_mask, cras_add=cras_add, cras_subtract=cras_subtract)
    return mris_convert_execute(params, execution)


__all__ = [
    "MRIS_CONVERT_METADATA",
    "MrisConvertOutputs",
    "MrisConvertParameters",
    "mris_convert",
    "mris_convert_params",
]
