# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__FAT_TRACT_COLORIZE_METADATA = Metadata(
    id="08df2223341e8a3953edfe06cc72302451f3e2c8.boutiques",
    name="@fat_tract_colorize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VFatTractColorizeParameters = typing.TypedDict('VFatTractColorizeParameters', {
    "__STYX_TYPE__": typing.Literal["@fat_tract_colorize"],
    "in_fa": InputPathType,
    "in_v1": InputPathType,
    "in_tracts": str,
    "prefix": str,
    "in_ulay": typing.NotRequired[InputPathType | None],
    "no_view": bool,
    "only_view": bool,
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
        "@fat_tract_colorize": v__fat_tract_colorize_cargs,
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
        "@fat_tract_colorize": v__fat_tract_colorize_outputs,
    }
    return vt.get(t)


class VFatTractColorizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__fat_tract_colorize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_hue_volume: OutputPathType
    """HSL coloration volume file with four bricks from the V1 and FA volumes:
    Hue, Saturation, Luminosity, and Brightness"""
    output_iso_surface: OutputPathType
    """Slightly smoothed isosurface file made by IsoSurface"""
    output_iso_spec: OutputPathType
    """Spec file made by quickspec"""
    output_proj_surface: OutputPathType
    """Projection of appropriate coloration onto the surface"""


def v__fat_tract_colorize_params(
    in_fa: InputPathType,
    in_v1: InputPathType,
    in_tracts: str,
    prefix: str,
    in_ulay: InputPathType | None = None,
    no_view: bool = False,
    only_view: bool = False,
) -> VFatTractColorizeParameters:
    """
    Build parameters.
    
    Args:
        in_fa: FA values of the DT fitting, used to modulate the brightness of\
            the RGB coloration.
        in_v1: First eigenvector of the DT fitting. A unit vector volume with 3\
            components (0-1 range).
        in_tracts: The INDIMAP or PAIRMAP file output by 3dTrackID, specifying\
            the subbrick if >1 (e.g., NAME_INDIMAP+orig'[0]').
        prefix: Prefix for all output files.
        in_ulay: Optional underlay dataset for AFNI/SUMA viewing. Default is to\
            use the FA dataset.
        no_view: Turn off auto-running of AFNI_SUMA commands to view the output\
            immediately.
        only_view: Only view the data with AFNI+SUMA, assuming the command has\
            been run before.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@fat_tract_colorize",
        "in_fa": in_fa,
        "in_v1": in_v1,
        "in_tracts": in_tracts,
        "prefix": prefix,
        "no_view": no_view,
        "only_view": only_view,
    }
    if in_ulay is not None:
        params["in_ulay"] = in_ulay
    return params


def v__fat_tract_colorize_cargs(
    params: VFatTractColorizeParameters,
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
    cargs.append("@fat_tract_colorize")
    cargs.extend([
        "-in_fa",
        execution.input_file(params.get("in_fa"))
    ])
    cargs.extend([
        "-in_v1",
        execution.input_file(params.get("in_v1"))
    ])
    cargs.extend([
        "-in_tracts",
        params.get("in_tracts")
    ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("in_ulay") is not None:
        cargs.extend([
            "-in_ulay",
            execution.input_file(params.get("in_ulay"))
        ])
    if params.get("no_view"):
        cargs.append("-no_view")
    if params.get("only_view"):
        cargs.append("-only_view")
    return cargs


def v__fat_tract_colorize_outputs(
    params: VFatTractColorizeParameters,
    execution: Execution,
) -> VFatTractColorizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VFatTractColorizeOutputs(
        root=execution.output_file("."),
        output_hue_volume=execution.output_file(params.get("prefix") + "_RGB_HUE.nii.gz"),
        output_iso_surface=execution.output_file(params.get("prefix") + "_RGB_iso.ply"),
        output_iso_spec=execution.output_file(params.get("prefix") + "_RGB_iso.spec"),
        output_proj_surface=execution.output_file(params.get("prefix") + "_RGB.niml.dset"),
    )
    return ret


def v__fat_tract_colorize_execute(
    params: VFatTractColorizeParameters,
    execution: Execution,
) -> VFatTractColorizeOutputs:
    """
    Visualize tractographic output from 3dTrackID, particularly in probabilistic
    mode.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VFatTractColorizeOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__fat_tract_colorize_cargs(params, execution)
    ret = v__fat_tract_colorize_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__fat_tract_colorize(
    in_fa: InputPathType,
    in_v1: InputPathType,
    in_tracts: str,
    prefix: str,
    in_ulay: InputPathType | None = None,
    no_view: bool = False,
    only_view: bool = False,
    runner: Runner | None = None,
) -> VFatTractColorizeOutputs:
    """
    Visualize tractographic output from 3dTrackID, particularly in probabilistic
    mode.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_fa: FA values of the DT fitting, used to modulate the brightness of\
            the RGB coloration.
        in_v1: First eigenvector of the DT fitting. A unit vector volume with 3\
            components (0-1 range).
        in_tracts: The INDIMAP or PAIRMAP file output by 3dTrackID, specifying\
            the subbrick if >1 (e.g., NAME_INDIMAP+orig'[0]').
        prefix: Prefix for all output files.
        in_ulay: Optional underlay dataset for AFNI/SUMA viewing. Default is to\
            use the FA dataset.
        no_view: Turn off auto-running of AFNI_SUMA commands to view the output\
            immediately.
        only_view: Only view the data with AFNI+SUMA, assuming the command has\
            been run before.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VFatTractColorizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__FAT_TRACT_COLORIZE_METADATA)
    params = v__fat_tract_colorize_params(in_fa=in_fa, in_v1=in_v1, in_tracts=in_tracts, prefix=prefix, in_ulay=in_ulay, no_view=no_view, only_view=only_view)
    return v__fat_tract_colorize_execute(params, execution)


__all__ = [
    "VFatTractColorizeOutputs",
    "V__FAT_TRACT_COLORIZE_METADATA",
    "v__fat_tract_colorize",
    "v__fat_tract_colorize_params",
]
