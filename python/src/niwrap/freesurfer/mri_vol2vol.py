# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_VOL2VOL_METADATA = Metadata(
    id="77d3504583fc4d7f61c4962c2cc361faf9664a7d.boutiques",
    name="mri_vol2vol",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MriVol2volParameters = typing.TypedDict('MriVol2volParameters', {
    "__STYX_TYPE__": typing.Literal["mri_vol2vol"],
    "movvol": InputPathType,
    "targvol": InputPathType,
    "outvol": InputPathType,
    "dispvol": typing.NotRequired[InputPathType | None],
    "downsample": typing.NotRequired[list[float] | None],
    "register_dat": typing.NotRequired[InputPathType | None],
    "lta": typing.NotRequired[InputPathType | None],
    "lta_inv": typing.NotRequired[InputPathType | None],
    "fsl": typing.NotRequired[InputPathType | None],
    "xfm": typing.NotRequired[InputPathType | None],
    "inv": bool,
    "tal": bool,
    "talres": typing.NotRequired[float | None],
    "talxfm": typing.NotRequired[InputPathType | None],
    "m3z": typing.NotRequired[InputPathType | None],
    "inv_morph": bool,
    "fstarg": typing.NotRequired[str | None],
    "crop": typing.NotRequired[float | None],
    "slice_crop": typing.NotRequired[list[float] | None],
    "slice_reverse": bool,
    "slice_bias": typing.NotRequired[float | None],
    "interp": typing.NotRequired[str | None],
    "fill_average": bool,
    "fill_conserve": bool,
    "fill_up": typing.NotRequired[float | None],
    "mul": typing.NotRequired[float | None],
    "precision": typing.NotRequired[str | None],
    "keep_precision": bool,
    "kernel": bool,
    "copy_ctab": bool,
    "gcam": typing.NotRequired[str | None],
    "spm_warp": typing.NotRequired[str | None],
    "map_point": typing.NotRequired[str | None],
    "map_point_inv_lta": typing.NotRequired[str | None],
    "no_resample": bool,
    "rot": typing.NotRequired[list[float] | None],
    "trans": typing.NotRequired[list[float] | None],
    "shear": typing.NotRequired[list[float] | None],
    "reg_final": typing.NotRequired[InputPathType | None],
    "synth": bool,
    "seed": typing.NotRequired[float | None],
    "save_reg": bool,
    "debug": bool,
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
        "mri_vol2vol": mri_vol2vol_cargs,
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
        "mri_vol2vol": mri_vol2vol_outputs,
    }
    return vt.get(t)


class MriVol2volOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_vol2vol(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Resampled output volume."""


def mri_vol2vol_params(
    movvol: InputPathType,
    targvol: InputPathType,
    outvol: InputPathType,
    dispvol: InputPathType | None = None,
    downsample: list[float] | None = None,
    register_dat: InputPathType | None = None,
    lta: InputPathType | None = None,
    lta_inv: InputPathType | None = None,
    fsl: InputPathType | None = None,
    xfm: InputPathType | None = None,
    inv: bool = False,
    tal: bool = False,
    talres: float | None = None,
    talxfm: InputPathType | None = None,
    m3z: InputPathType | None = None,
    inv_morph: bool = False,
    fstarg: str | None = None,
    crop: float | None = None,
    slice_crop: list[float] | None = None,
    slice_reverse: bool = False,
    slice_bias: float | None = None,
    interp: str | None = None,
    fill_average: bool = False,
    fill_conserve: bool = False,
    fill_up: float | None = None,
    mul: float | None = None,
    precision: str | None = None,
    keep_precision: bool = False,
    kernel: bool = False,
    copy_ctab: bool = False,
    gcam: str | None = None,
    spm_warp: str | None = None,
    map_point: str | None = None,
    map_point_inv_lta: str | None = None,
    no_resample: bool = False,
    rot: list[float] | None = None,
    trans: list[float] | None = None,
    shear: list[float] | None = None,
    reg_final: InputPathType | None = None,
    synth: bool = False,
    seed: float | None = None,
    save_reg: bool = False,
    debug: bool = False,
    version: bool = False,
) -> MriVol2volParameters:
    """
    Build parameters.
    
    Args:
        movvol: Input volume (or output template with --inv).
        targvol: Output template (or input with --inv).
        outvol: Output volume.
        dispvol: Displacement volume.
        downsample: Downsample factor (e.g., 2) (do not include a targ or\
            registration).
        register_dat: tkRAS-to-tkRAS matrix (tkregister2 format).
        lta: Linear Transform Array (usually only 1 transform).
        lta_inv: LTA, invert (may not be the same as --lta --inv with --fstal).
        fsl: fslRAS-to-fslRAS matrix (FSL format).
        xfm: ScannerRAS-to-ScannerRAS matrix (MNI format).
        inv: Sample from targ to mov.
        tal: Map to a sub FOV of MNI305 (with --reg only).
        talres: Set voxel size 1mm or 2mm (default is 1).
        talxfm: Path to the talairach transformation file. Default is\
            talairach.xfm (looks in mri/transforms).
        m3z: Non-linear morph encoded in the m3z format.
        inv_morph: Compute and use the inverse of the m3z morph.
        fstarg: Optionally use the specified volume from the subject in --reg\
            as target. Default is orig.mgz.
        crop: Crop and change voxel size.
        slice_crop: Crop output slices to be within specified start and end\
            indices.
        slice_reverse: Reverse order of slices, update vox2ras.
        slice_bias: Apply half-cosine bias field.
        interp: Interpolation method: cubic, trilin, or nearest (default is\
            trilin).
        fill_average: Compute mean of all source voxels in a given target voxel.
        fill_conserve: Compute sum of all source voxels in a given target voxel.
        fill_up: Source upsampling factor for --fill-{avg,cons} (default is 2).
        mul: Multiply output by the specified value.
        precision: Output precision (default is float).
        keep_precision: Set output precision to that of the input.
        kernel: Save the trilinear interpolation kernel at each voxel instead\
            of the interpolated image.
        copy_ctab: Setenv FS_COPY_HEADER_CTAB to copy any ctab in the mov\
            header.
        gcam: GCAM warp procedure.
        spm_warp: SPM warp procedure.
        map_point: Standalone option to map a point to another space.
        map_point_inv_lta: Same as --map-point but inverts the LTA.
        no_resample: Do not resample, just change vox2ras matrix.
        rot: Rotation angles (degrees) to apply to registration matrix.
        trans: Translation (mm) to apply to registration matrix.
        shear: Shearing factors. Sxy Sxz Syz with xz as in-plane.
        reg_final: Final registration matrix after rotation and translation\
            (but not inversion).
        synth: Replace input with white Gaussian noise.
        seed: Seed for synth (default is to set from time of day).
        save_reg: Write out output volume registration matrix.
        debug: Turn on debugging output.
        version: Print out version string and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_vol2vol",
        "movvol": movvol,
        "targvol": targvol,
        "outvol": outvol,
        "inv": inv,
        "tal": tal,
        "inv_morph": inv_morph,
        "slice_reverse": slice_reverse,
        "fill_average": fill_average,
        "fill_conserve": fill_conserve,
        "keep_precision": keep_precision,
        "kernel": kernel,
        "copy_ctab": copy_ctab,
        "no_resample": no_resample,
        "synth": synth,
        "save_reg": save_reg,
        "debug": debug,
        "version": version,
    }
    if dispvol is not None:
        params["dispvol"] = dispvol
    if downsample is not None:
        params["downsample"] = downsample
    if register_dat is not None:
        params["register_dat"] = register_dat
    if lta is not None:
        params["lta"] = lta
    if lta_inv is not None:
        params["lta_inv"] = lta_inv
    if fsl is not None:
        params["fsl"] = fsl
    if xfm is not None:
        params["xfm"] = xfm
    if talres is not None:
        params["talres"] = talres
    if talxfm is not None:
        params["talxfm"] = talxfm
    if m3z is not None:
        params["m3z"] = m3z
    if fstarg is not None:
        params["fstarg"] = fstarg
    if crop is not None:
        params["crop"] = crop
    if slice_crop is not None:
        params["slice_crop"] = slice_crop
    if slice_bias is not None:
        params["slice_bias"] = slice_bias
    if interp is not None:
        params["interp"] = interp
    if fill_up is not None:
        params["fill_up"] = fill_up
    if mul is not None:
        params["mul"] = mul
    if precision is not None:
        params["precision"] = precision
    if gcam is not None:
        params["gcam"] = gcam
    if spm_warp is not None:
        params["spm_warp"] = spm_warp
    if map_point is not None:
        params["map_point"] = map_point
    if map_point_inv_lta is not None:
        params["map_point_inv_lta"] = map_point_inv_lta
    if rot is not None:
        params["rot"] = rot
    if trans is not None:
        params["trans"] = trans
    if shear is not None:
        params["shear"] = shear
    if reg_final is not None:
        params["reg_final"] = reg_final
    if seed is not None:
        params["seed"] = seed
    return params


def mri_vol2vol_cargs(
    params: MriVol2volParameters,
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
    cargs.append("mri_vol2vol")
    cargs.append(execution.input_file(params.get("movvol")))
    cargs.append(execution.input_file(params.get("targvol")))
    cargs.append(execution.input_file(params.get("outvol")))
    if params.get("dispvol") is not None:
        cargs.extend([
            "--disp",
            execution.input_file(params.get("dispvol"))
        ])
    if params.get("downsample") is not None:
        cargs.extend([
            "--downsample",
            *map(str, params.get("downsample"))
        ])
    if params.get("register_dat") is not None:
        cargs.extend([
            "--reg",
            execution.input_file(params.get("register_dat"))
        ])
    if params.get("lta") is not None:
        cargs.extend([
            "--lta",
            execution.input_file(params.get("lta"))
        ])
    if params.get("lta_inv") is not None:
        cargs.extend([
            "--lta-inv",
            execution.input_file(params.get("lta_inv"))
        ])
    if params.get("fsl") is not None:
        cargs.extend([
            "--fsl",
            execution.input_file(params.get("fsl"))
        ])
    if params.get("xfm") is not None:
        cargs.extend([
            "--xfm",
            execution.input_file(params.get("xfm"))
        ])
    if params.get("inv"):
        cargs.append("--inv")
    if params.get("tal"):
        cargs.append("--tal")
    if params.get("talres") is not None:
        cargs.extend([
            "--talres",
            str(params.get("talres"))
        ])
    if params.get("talxfm") is not None:
        cargs.extend([
            "--talxfm",
            execution.input_file(params.get("talxfm"))
        ])
    if params.get("m3z") is not None:
        cargs.extend([
            "--m3z",
            execution.input_file(params.get("m3z"))
        ])
    if params.get("inv_morph"):
        cargs.append("--inv-morph")
    if params.get("fstarg") is not None:
        cargs.extend([
            "--fstarg",
            params.get("fstarg")
        ])
    if params.get("crop") is not None:
        cargs.extend([
            "--crop",
            str(params.get("crop"))
        ])
    if params.get("slice_crop") is not None:
        cargs.extend([
            "--slice-crop",
            *map(str, params.get("slice_crop"))
        ])
    if params.get("slice_reverse"):
        cargs.append("--slice-reverse")
    if params.get("slice_bias") is not None:
        cargs.extend([
            "--slice-bias",
            str(params.get("slice_bias"))
        ])
    if params.get("interp") is not None:
        cargs.extend([
            "--interp",
            params.get("interp")
        ])
    if params.get("fill_average"):
        cargs.append("--fill-average")
    if params.get("fill_conserve"):
        cargs.append("--fill-conserve")
    if params.get("fill_up") is not None:
        cargs.extend([
            "--fill-upsample",
            str(params.get("fill_up"))
        ])
    if params.get("mul") is not None:
        cargs.extend([
            "--mul",
            str(params.get("mul"))
        ])
    if params.get("precision") is not None:
        cargs.extend([
            "--precision",
            params.get("precision")
        ])
    if params.get("keep_precision"):
        cargs.append("--keep-precision")
    if params.get("kernel"):
        cargs.append("--kernel")
    if params.get("copy_ctab"):
        cargs.append("--copy-ctab")
    if params.get("gcam") is not None:
        cargs.extend([
            "--gcam",
            params.get("gcam")
        ])
    if params.get("spm_warp") is not None:
        cargs.extend([
            "--spm-warp",
            params.get("spm_warp")
        ])
    if params.get("map_point") is not None:
        cargs.extend([
            "--map-point",
            params.get("map_point")
        ])
    if params.get("map_point_inv_lta") is not None:
        cargs.extend([
            "--map-point-inv-lta",
            params.get("map_point_inv_lta")
        ])
    if params.get("no_resample"):
        cargs.append("--no-resample")
    if params.get("rot") is not None:
        cargs.extend([
            "--rot",
            *map(str, params.get("rot"))
        ])
    if params.get("trans") is not None:
        cargs.extend([
            "--trans",
            *map(str, params.get("trans"))
        ])
    if params.get("shear") is not None:
        cargs.extend([
            "--shear",
            *map(str, params.get("shear"))
        ])
    if params.get("reg_final") is not None:
        cargs.extend([
            "--reg-final",
            execution.input_file(params.get("reg_final"))
        ])
    if params.get("synth"):
        cargs.append("--synth")
    if params.get("seed") is not None:
        cargs.extend([
            "--seed",
            str(params.get("seed"))
        ])
    if params.get("save_reg"):
        cargs.append("--save-reg")
    if params.get("debug"):
        cargs.append("--debug")
    if params.get("version"):
        cargs.append("--version")
    return cargs


def mri_vol2vol_outputs(
    params: MriVol2volParameters,
    execution: Execution,
) -> MriVol2volOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriVol2volOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(pathlib.Path(params.get("outvol")).name),
    )
    return ret


def mri_vol2vol_execute(
    params: MriVol2volParameters,
    execution: Execution,
) -> MriVol2volOutputs:
    """
    Resamples a volume into another field-of-view using various types of matrices
    (FreeSurfer, FSL, SPM, and MNI).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriVol2volOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = mri_vol2vol_cargs(params, execution)
    ret = mri_vol2vol_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_vol2vol(
    movvol: InputPathType,
    targvol: InputPathType,
    outvol: InputPathType,
    dispvol: InputPathType | None = None,
    downsample: list[float] | None = None,
    register_dat: InputPathType | None = None,
    lta: InputPathType | None = None,
    lta_inv: InputPathType | None = None,
    fsl: InputPathType | None = None,
    xfm: InputPathType | None = None,
    inv: bool = False,
    tal: bool = False,
    talres: float | None = None,
    talxfm: InputPathType | None = None,
    m3z: InputPathType | None = None,
    inv_morph: bool = False,
    fstarg: str | None = None,
    crop: float | None = None,
    slice_crop: list[float] | None = None,
    slice_reverse: bool = False,
    slice_bias: float | None = None,
    interp: str | None = None,
    fill_average: bool = False,
    fill_conserve: bool = False,
    fill_up: float | None = None,
    mul: float | None = None,
    precision: str | None = None,
    keep_precision: bool = False,
    kernel: bool = False,
    copy_ctab: bool = False,
    gcam: str | None = None,
    spm_warp: str | None = None,
    map_point: str | None = None,
    map_point_inv_lta: str | None = None,
    no_resample: bool = False,
    rot: list[float] | None = None,
    trans: list[float] | None = None,
    shear: list[float] | None = None,
    reg_final: InputPathType | None = None,
    synth: bool = False,
    seed: float | None = None,
    save_reg: bool = False,
    debug: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriVol2volOutputs:
    """
    Resamples a volume into another field-of-view using various types of matrices
    (FreeSurfer, FSL, SPM, and MNI).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        movvol: Input volume (or output template with --inv).
        targvol: Output template (or input with --inv).
        outvol: Output volume.
        dispvol: Displacement volume.
        downsample: Downsample factor (e.g., 2) (do not include a targ or\
            registration).
        register_dat: tkRAS-to-tkRAS matrix (tkregister2 format).
        lta: Linear Transform Array (usually only 1 transform).
        lta_inv: LTA, invert (may not be the same as --lta --inv with --fstal).
        fsl: fslRAS-to-fslRAS matrix (FSL format).
        xfm: ScannerRAS-to-ScannerRAS matrix (MNI format).
        inv: Sample from targ to mov.
        tal: Map to a sub FOV of MNI305 (with --reg only).
        talres: Set voxel size 1mm or 2mm (default is 1).
        talxfm: Path to the talairach transformation file. Default is\
            talairach.xfm (looks in mri/transforms).
        m3z: Non-linear morph encoded in the m3z format.
        inv_morph: Compute and use the inverse of the m3z morph.
        fstarg: Optionally use the specified volume from the subject in --reg\
            as target. Default is orig.mgz.
        crop: Crop and change voxel size.
        slice_crop: Crop output slices to be within specified start and end\
            indices.
        slice_reverse: Reverse order of slices, update vox2ras.
        slice_bias: Apply half-cosine bias field.
        interp: Interpolation method: cubic, trilin, or nearest (default is\
            trilin).
        fill_average: Compute mean of all source voxels in a given target voxel.
        fill_conserve: Compute sum of all source voxels in a given target voxel.
        fill_up: Source upsampling factor for --fill-{avg,cons} (default is 2).
        mul: Multiply output by the specified value.
        precision: Output precision (default is float).
        keep_precision: Set output precision to that of the input.
        kernel: Save the trilinear interpolation kernel at each voxel instead\
            of the interpolated image.
        copy_ctab: Setenv FS_COPY_HEADER_CTAB to copy any ctab in the mov\
            header.
        gcam: GCAM warp procedure.
        spm_warp: SPM warp procedure.
        map_point: Standalone option to map a point to another space.
        map_point_inv_lta: Same as --map-point but inverts the LTA.
        no_resample: Do not resample, just change vox2ras matrix.
        rot: Rotation angles (degrees) to apply to registration matrix.
        trans: Translation (mm) to apply to registration matrix.
        shear: Shearing factors. Sxy Sxz Syz with xz as in-plane.
        reg_final: Final registration matrix after rotation and translation\
            (but not inversion).
        synth: Replace input with white Gaussian noise.
        seed: Seed for synth (default is to set from time of day).
        save_reg: Write out output volume registration matrix.
        debug: Turn on debugging output.
        version: Print out version string and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriVol2volOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_VOL2VOL_METADATA)
    params = mri_vol2vol_params(movvol=movvol, targvol=targvol, outvol=outvol, dispvol=dispvol, downsample=downsample, register_dat=register_dat, lta=lta, lta_inv=lta_inv, fsl=fsl, xfm=xfm, inv=inv, tal=tal, talres=talres, talxfm=talxfm, m3z=m3z, inv_morph=inv_morph, fstarg=fstarg, crop=crop, slice_crop=slice_crop, slice_reverse=slice_reverse, slice_bias=slice_bias, interp=interp, fill_average=fill_average, fill_conserve=fill_conserve, fill_up=fill_up, mul=mul, precision=precision, keep_precision=keep_precision, kernel=kernel, copy_ctab=copy_ctab, gcam=gcam, spm_warp=spm_warp, map_point=map_point, map_point_inv_lta=map_point_inv_lta, no_resample=no_resample, rot=rot, trans=trans, shear=shear, reg_final=reg_final, synth=synth, seed=seed, save_reg=save_reg, debug=debug, version=version)
    return mri_vol2vol_execute(params, execution)


__all__ = [
    "MRI_VOL2VOL_METADATA",
    "MriVol2volOutputs",
    "mri_vol2vol",
    "mri_vol2vol_params",
]
