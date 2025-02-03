# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3_DROIMAKER_METADATA = Metadata(
    id="52994e672a5f137f27dbb8bbd59f66cee7093ffe.boutiques",
    name="3DROIMaker",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3DroimakerParameters = typing.TypedDict('V3DroimakerParameters', {
    "__STYX_TYPE__": typing.Literal["3DROIMaker"],
    "inset": InputPathType,
    "thresh": float,
    "prefix": str,
    "refset": typing.NotRequired[InputPathType | None],
    "volthr": typing.NotRequired[float | None],
    "only_conn_top": typing.NotRequired[float | None],
    "inflate": typing.NotRequired[float | None],
    "trim_off_wm": bool,
    "wm_skel": typing.NotRequired[InputPathType | None],
    "skel_thr": typing.NotRequired[float | None],
    "skel_stop": bool,
    "skel_stop_strict": bool,
    "csf_skel": typing.NotRequired[InputPathType | None],
    "mask": typing.NotRequired[InputPathType | None],
    "neigh_upto_vert": bool,
    "nifti": bool,
    "preinfl_inset": typing.NotRequired[InputPathType | None],
    "preinfl_inflate": typing.NotRequired[float | None],
    "dump_no_labtab": bool,
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
        "3DROIMaker": v_3_droimaker_cargs,
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
        "3DROIMaker": v_3_droimaker_outputs,
    }
    return vt.get(t)


class V3DroimakerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3_droimaker(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    gm_map: OutputPathType
    """GM map of ROIs based on value- and volume-thresholding, corresponding to
    gray matter regions of activation."""
    gmi_map: OutputPathType
    """Map of inflated GM ROIs based on GM map, with ROIs inflated either by
    user-design or WM skeleton."""


def v_3_droimaker_params(
    inset: InputPathType,
    thresh: float,
    prefix: str,
    refset: InputPathType | None = None,
    volthr: float | None = None,
    only_conn_top: float | None = None,
    inflate: float | None = None,
    trim_off_wm: bool = False,
    wm_skel: InputPathType | None = None,
    skel_thr: float | None = None,
    skel_stop: bool = False,
    skel_stop_strict: bool = False,
    csf_skel: InputPathType | None = None,
    mask: InputPathType | None = None,
    neigh_upto_vert: bool = False,
    nifti: bool = False,
    preinfl_inset: InputPathType | None = None,
    preinfl_inflate: float | None = None,
    dump_no_labtab: bool = False,
) -> V3DroimakerParameters:
    """
    Build parameters.
    
    Args:
        inset: 3D volume(s) of values, especially functionally-derived\
            quantities like correlation values or ICA Z-scores.
        thresh: Threshold for values in INSET, used to create ROI islands from\
            the 3D volume's sea of values.
        prefix: Prefix of output name, with output files being: PREFIX_GM* and\
            PREFIX_GMI*.
        refset: 3D (or multi-subbrick) volume containing integer values with\
            which to label specific GM ROIs after thresholding.
        volthr: Minimum size a cluster of voxels must have in order to remain a\
            GM ROI after thresholding. Can reduce 'noisy' clusters.
        only_conn_top: Select N max contiguous voxels in a region starting from\
            peak voxel and expanding.
        inflate: Number of voxels to pad each found ROI in order to turn GM\
            ROIs into inflated (GMI) ROIs.
        trim_off_wm: Trim the INSET to exclude voxels in WM by excluding those\
            which overlap an input WM skeleton.
        wm_skel: 3D volume containing info of WM, as might be defined from an\
            FA map or anatomical segmentation.
        skel_thr: Threshold value for WM skeleton if it is not a mask.
        skel_stop: Stop inflation at locations which are already on WM\
            skeleton.
        skel_stop_strict: Do not allow any inflation into the skel-region.
        csf_skel: 3D volume containing info of CSF. Info must be a binary mask\
            already.
        mask: Mask within which to apply threshold. Useful if the MINTHR is a\
            negative value.
        neigh_upto_vert: Define neighbors loosely so that voxels can be grouped\
            into the same ROI if they share at least one vertex.
        nifti: Switch to output *.nii.gz GM and GMI files.
        preinfl_inset: Start with a WM ROI, inflate it to find the nearest GM,\
            then expand that GM and subtract away the WM+CSF parts.
        preinfl_inflate: Number of voxels for initial inflation of PSET.
        dump_no_labtab: Switch for turning off labeltable attachment to the\
            output GM and GMI files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3DROIMaker",
        "inset": inset,
        "thresh": thresh,
        "prefix": prefix,
        "trim_off_wm": trim_off_wm,
        "skel_stop": skel_stop,
        "skel_stop_strict": skel_stop_strict,
        "neigh_upto_vert": neigh_upto_vert,
        "nifti": nifti,
        "dump_no_labtab": dump_no_labtab,
    }
    if refset is not None:
        params["refset"] = refset
    if volthr is not None:
        params["volthr"] = volthr
    if only_conn_top is not None:
        params["only_conn_top"] = only_conn_top
    if inflate is not None:
        params["inflate"] = inflate
    if wm_skel is not None:
        params["wm_skel"] = wm_skel
    if skel_thr is not None:
        params["skel_thr"] = skel_thr
    if csf_skel is not None:
        params["csf_skel"] = csf_skel
    if mask is not None:
        params["mask"] = mask
    if preinfl_inset is not None:
        params["preinfl_inset"] = preinfl_inset
    if preinfl_inflate is not None:
        params["preinfl_inflate"] = preinfl_inflate
    return params


def v_3_droimaker_cargs(
    params: V3DroimakerParameters,
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
    cargs.append("3dROIMaker")
    cargs.append(execution.input_file(params.get("inset")))
    cargs.extend([
        "-thresh",
        str(params.get("thresh"))
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("refset") is not None:
        cargs.extend([
            "-refset",
            execution.input_file(params.get("refset"))
        ])
    if params.get("volthr") is not None:
        cargs.extend([
            "-volthr",
            str(params.get("volthr"))
        ])
    if params.get("only_conn_top") is not None:
        cargs.extend([
            "-only_conn_top",
            str(params.get("only_conn_top"))
        ])
    if params.get("inflate") is not None:
        cargs.extend([
            "-inflate",
            str(params.get("inflate"))
        ])
    if params.get("trim_off_wm"):
        cargs.append("-trim_off_wm")
    if params.get("wm_skel") is not None:
        cargs.extend([
            "-wm_skel",
            execution.input_file(params.get("wm_skel"))
        ])
    if params.get("skel_thr") is not None:
        cargs.extend([
            "-skel_thr",
            str(params.get("skel_thr"))
        ])
    if params.get("skel_stop"):
        cargs.append("-skel_stop")
    if params.get("skel_stop_strict"):
        cargs.append("-skel_stop_strict")
    if params.get("csf_skel") is not None:
        cargs.extend([
            "-csf_skel",
            execution.input_file(params.get("csf_skel"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("neigh_upto_vert"):
        cargs.append("-neigh_upto_vert")
    if params.get("nifti"):
        cargs.append("-nifti")
    if params.get("preinfl_inset") is not None:
        cargs.extend([
            "-preinfl_inset",
            execution.input_file(params.get("preinfl_inset"))
        ])
    if params.get("preinfl_inflate") is not None:
        cargs.extend([
            "-preinfl_inflate",
            str(params.get("preinfl_inflate"))
        ])
    if params.get("dump_no_labtab"):
        cargs.append("-dump_no_labtab")
    return cargs


def v_3_droimaker_outputs(
    params: V3DroimakerParameters,
    execution: Execution,
) -> V3DroimakerOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3DroimakerOutputs(
        root=execution.output_file("."),
        gm_map=execution.output_file(params.get("prefix") + "_GM+orig.*.HEAD"),
        gmi_map=execution.output_file(params.get("prefix") + "_GMI+orig.*.HEAD"),
    )
    return ret


def v_3_droimaker_execute(
    params: V3DroimakerParameters,
    execution: Execution,
) -> V3DroimakerOutputs:
    """
    Create a labelled set of ROIs from input data, useful in combining functional
    and tractographic/structural data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3DroimakerOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3_droimaker_cargs(params, execution)
    ret = v_3_droimaker_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3_droimaker(
    inset: InputPathType,
    thresh: float,
    prefix: str,
    refset: InputPathType | None = None,
    volthr: float | None = None,
    only_conn_top: float | None = None,
    inflate: float | None = None,
    trim_off_wm: bool = False,
    wm_skel: InputPathType | None = None,
    skel_thr: float | None = None,
    skel_stop: bool = False,
    skel_stop_strict: bool = False,
    csf_skel: InputPathType | None = None,
    mask: InputPathType | None = None,
    neigh_upto_vert: bool = False,
    nifti: bool = False,
    preinfl_inset: InputPathType | None = None,
    preinfl_inflate: float | None = None,
    dump_no_labtab: bool = False,
    runner: Runner | None = None,
) -> V3DroimakerOutputs:
    """
    Create a labelled set of ROIs from input data, useful in combining functional
    and tractographic/structural data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        inset: 3D volume(s) of values, especially functionally-derived\
            quantities like correlation values or ICA Z-scores.
        thresh: Threshold for values in INSET, used to create ROI islands from\
            the 3D volume's sea of values.
        prefix: Prefix of output name, with output files being: PREFIX_GM* and\
            PREFIX_GMI*.
        refset: 3D (or multi-subbrick) volume containing integer values with\
            which to label specific GM ROIs after thresholding.
        volthr: Minimum size a cluster of voxels must have in order to remain a\
            GM ROI after thresholding. Can reduce 'noisy' clusters.
        only_conn_top: Select N max contiguous voxels in a region starting from\
            peak voxel and expanding.
        inflate: Number of voxels to pad each found ROI in order to turn GM\
            ROIs into inflated (GMI) ROIs.
        trim_off_wm: Trim the INSET to exclude voxels in WM by excluding those\
            which overlap an input WM skeleton.
        wm_skel: 3D volume containing info of WM, as might be defined from an\
            FA map or anatomical segmentation.
        skel_thr: Threshold value for WM skeleton if it is not a mask.
        skel_stop: Stop inflation at locations which are already on WM\
            skeleton.
        skel_stop_strict: Do not allow any inflation into the skel-region.
        csf_skel: 3D volume containing info of CSF. Info must be a binary mask\
            already.
        mask: Mask within which to apply threshold. Useful if the MINTHR is a\
            negative value.
        neigh_upto_vert: Define neighbors loosely so that voxels can be grouped\
            into the same ROI if they share at least one vertex.
        nifti: Switch to output *.nii.gz GM and GMI files.
        preinfl_inset: Start with a WM ROI, inflate it to find the nearest GM,\
            then expand that GM and subtract away the WM+CSF parts.
        preinfl_inflate: Number of voxels for initial inflation of PSET.
        dump_no_labtab: Switch for turning off labeltable attachment to the\
            output GM and GMI files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3DroimakerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3_DROIMAKER_METADATA)
    params = v_3_droimaker_params(inset=inset, thresh=thresh, prefix=prefix, refset=refset, volthr=volthr, only_conn_top=only_conn_top, inflate=inflate, trim_off_wm=trim_off_wm, wm_skel=wm_skel, skel_thr=skel_thr, skel_stop=skel_stop, skel_stop_strict=skel_stop_strict, csf_skel=csf_skel, mask=mask, neigh_upto_vert=neigh_upto_vert, nifti=nifti, preinfl_inset=preinfl_inset, preinfl_inflate=preinfl_inflate, dump_no_labtab=dump_no_labtab)
    return v_3_droimaker_execute(params, execution)


__all__ = [
    "V3DroimakerOutputs",
    "V_3_DROIMAKER_METADATA",
    "v_3_droimaker",
    "v_3_droimaker_params",
]
