# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__ATLASIZE_METADATA = Metadata(
    id="5fc4c62439ac62644ef483caa2fc7a4ea1cb35f0.boutiques",
    name="@Atlasize",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VAtlasizeParameters = typing.TypedDict('VAtlasizeParameters', {
    "__STYX_TYPE__": typing.Literal["@Atlasize"],
    "dset": typing.NotRequired[InputPathType | None],
    "space": typing.NotRequired[str | None],
    "lab_file": typing.NotRequired[list[str] | None],
    "lab_file_delim": typing.NotRequired[str | None],
    "longnames": typing.NotRequired[float | None],
    "last_longname_col": typing.NotRequired[float | None],
    "atlas_type": typing.NotRequired[str | None],
    "atlas_description": typing.NotRequired[str | None],
    "atlas_name": typing.NotRequired[str | None],
    "auto_backup": bool,
    "centers": bool,
    "centertype": typing.NotRequired[str | None],
    "centermask": typing.NotRequired[InputPathType | None],
    "skip_novoxels": bool,
    "h_web": bool,
    "h_view": bool,
    "all_opts": bool,
    "h_find": typing.NotRequired[str | None],
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
        "@Atlasize": v__atlasize_cargs,
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
        "@Atlasize": v__atlasize_outputs,
    }.get(t)


class VAtlasizeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__atlasize(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    niml_file: OutputPathType | None
    """Generated NIML file for the atlas"""


def v__atlasize_params(
    dset: InputPathType | None = None,
    space: str | None = None,
    lab_file: list[str] | None = None,
    lab_file_delim: str | None = None,
    longnames: float | None = None,
    last_longname_col: float | None = None,
    atlas_type: str | None = None,
    atlas_description: str | None = None,
    atlas_name: str | None = None,
    auto_backup: bool = False,
    centers: bool = False,
    centertype: str | None = None,
    centermask: InputPathType | None = None,
    skip_novoxels: bool = False,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find: str | None = None,
) -> VAtlasizeParameters:
    """
    Build parameters.
    
    Args:
        dset: Make DSET an atlas.
        space: Mark DSET as being in space SPACE.
        lab_file: Labels and keys are in text file FILE. cLAB is the index of\
            column containing labels, vVAL is the index of column containing keys\
            (1st column is indexed at 0).
        lab_file_delim: Set column delimiter for -lab_file option. Default is '\
            ' (space), but you can set your own. ';' for example.
        longnames: Additionally, allow for another column of long names for\
            regions, e.g., amygdala for AMY. cLONGNAME is the starting column for\
            the long name continuing to the last name of the output.
        last_longname_col: Limit long names to nth column.
        atlas_type: Set the atlas type where TP is 'S' for subject-based and\
            'G' for group-based atlases, respectively.
        atlas_description: A description for the atlas. Default is 'My Atlas'.
        atlas_name: Name for the atlas. Default name is based on prefix of\
            DSET.
        auto_backup: Back up the dataset if it already exists in the custom\
            atlas directory and allows an overwrite.
        centers: Add center of mass coordinates to atlas.
        centertype: Choose Icent, Dcent, or cm for different ways to compute\
            centers.
        centermask: Calculate center of mass locations for each ROI using a\
            subset of voxels. Useful for atlases with identical labels in both\
            hemispheres.
        skip_novoxels: Skip regions without any voxels in the dataset.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find: Search for lines containing WORD in -help output. Search is\
            approximate.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@Atlasize",
        "auto_backup": auto_backup,
        "centers": centers,
        "skip_novoxels": skip_novoxels,
        "h_web": h_web,
        "h_view": h_view,
        "all_opts": all_opts,
    }
    if dset is not None:
        params["dset"] = dset
    if space is not None:
        params["space"] = space
    if lab_file is not None:
        params["lab_file"] = lab_file
    if lab_file_delim is not None:
        params["lab_file_delim"] = lab_file_delim
    if longnames is not None:
        params["longnames"] = longnames
    if last_longname_col is not None:
        params["last_longname_col"] = last_longname_col
    if atlas_type is not None:
        params["atlas_type"] = atlas_type
    if atlas_description is not None:
        params["atlas_description"] = atlas_description
    if atlas_name is not None:
        params["atlas_name"] = atlas_name
    if centertype is not None:
        params["centertype"] = centertype
    if centermask is not None:
        params["centermask"] = centermask
    if h_find is not None:
        params["h_find"] = h_find
    return params


def v__atlasize_cargs(
    params: VAtlasizeParameters,
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
    cargs.append("@Atlasize")
    if params.get("dset") is not None:
        cargs.extend([
            "-dset",
            execution.input_file(params.get("dset"))
        ])
    if params.get("space") is not None:
        cargs.extend([
            "-space",
            params.get("space")
        ])
    if params.get("lab_file") is not None:
        cargs.extend([
            "-lab_file",
            *params.get("lab_file")
        ])
    if params.get("lab_file_delim") is not None:
        cargs.extend([
            "-lab_file_delim",
            params.get("lab_file_delim")
        ])
    if params.get("longnames") is not None:
        cargs.extend([
            "-longnames",
            str(params.get("longnames"))
        ])
    if params.get("last_longname_col") is not None:
        cargs.extend([
            "-last_longname_col",
            str(params.get("last_longname_col"))
        ])
    if params.get("atlas_type") is not None:
        cargs.extend([
            "-atlas_type",
            params.get("atlas_type")
        ])
    if params.get("atlas_description") is not None:
        cargs.extend([
            "-atlas_description",
            params.get("atlas_description")
        ])
    if params.get("atlas_name") is not None:
        cargs.extend([
            "-atlas_name",
            params.get("atlas_name")
        ])
    if params.get("auto_backup"):
        cargs.append("-auto_backup")
    if params.get("centers"):
        cargs.append("-centers")
    if params.get("centertype") is not None:
        cargs.extend([
            "-centertype",
            params.get("centertype")
        ])
    if params.get("centermask") is not None:
        cargs.extend([
            "-centermask",
            execution.input_file(params.get("centermask"))
        ])
    if params.get("skip_novoxels"):
        cargs.append("-skip_novoxels")
    if params.get("h_web"):
        cargs.append("-h_web")
    if params.get("h_view"):
        cargs.append("-h_view")
    if params.get("all_opts"):
        cargs.append("-all_opts")
    if params.get("h_find") is not None:
        cargs.extend([
            "-h_find",
            params.get("h_find")
        ])
    return cargs


def v__atlasize_outputs(
    params: VAtlasizeParameters,
    execution: Execution,
) -> VAtlasizeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAtlasizeOutputs(
        root=execution.output_file("."),
        niml_file=execution.output_file(pathlib.Path(params.get("dset")).name + ".niml") if (params.get("dset") is not None) else None,
    )
    return ret


def v__atlasize_execute(
    params: VAtlasizeParameters,
    execution: Execution,
) -> VAtlasizeOutputs:
    """
    Script to turn a volumetric dataset into an AFNI atlas.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAtlasizeOutputs`).
    """
    params = execution.params(params)
    cargs = v__atlasize_cargs(params, execution)
    ret = v__atlasize_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__atlasize(
    dset: InputPathType | None = None,
    space: str | None = None,
    lab_file: list[str] | None = None,
    lab_file_delim: str | None = None,
    longnames: float | None = None,
    last_longname_col: float | None = None,
    atlas_type: str | None = None,
    atlas_description: str | None = None,
    atlas_name: str | None = None,
    auto_backup: bool = False,
    centers: bool = False,
    centertype: str | None = None,
    centermask: InputPathType | None = None,
    skip_novoxels: bool = False,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find: str | None = None,
    runner: Runner | None = None,
) -> VAtlasizeOutputs:
    """
    Script to turn a volumetric dataset into an AFNI atlas.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dset: Make DSET an atlas.
        space: Mark DSET as being in space SPACE.
        lab_file: Labels and keys are in text file FILE. cLAB is the index of\
            column containing labels, vVAL is the index of column containing keys\
            (1st column is indexed at 0).
        lab_file_delim: Set column delimiter for -lab_file option. Default is '\
            ' (space), but you can set your own. ';' for example.
        longnames: Additionally, allow for another column of long names for\
            regions, e.g., amygdala for AMY. cLONGNAME is the starting column for\
            the long name continuing to the last name of the output.
        last_longname_col: Limit long names to nth column.
        atlas_type: Set the atlas type where TP is 'S' for subject-based and\
            'G' for group-based atlases, respectively.
        atlas_description: A description for the atlas. Default is 'My Atlas'.
        atlas_name: Name for the atlas. Default name is based on prefix of\
            DSET.
        auto_backup: Back up the dataset if it already exists in the custom\
            atlas directory and allows an overwrite.
        centers: Add center of mass coordinates to atlas.
        centertype: Choose Icent, Dcent, or cm for different ways to compute\
            centers.
        centermask: Calculate center of mass locations for each ROI using a\
            subset of voxels. Useful for atlases with identical labels in both\
            hemispheres.
        skip_novoxels: Skip regions without any voxels in the dataset.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find: Search for lines containing WORD in -help output. Search is\
            approximate.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAtlasizeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ATLASIZE_METADATA)
    params = v__atlasize_params(dset=dset, space=space, lab_file=lab_file, lab_file_delim=lab_file_delim, longnames=longnames, last_longname_col=last_longname_col, atlas_type=atlas_type, atlas_description=atlas_description, atlas_name=atlas_name, auto_backup=auto_backup, centers=centers, centertype=centertype, centermask=centermask, skip_novoxels=skip_novoxels, h_web=h_web, h_view=h_view, all_opts=all_opts, h_find=h_find)
    return v__atlasize_execute(params, execution)


__all__ = [
    "VAtlasizeOutputs",
    "VAtlasizeParameters",
    "V__ATLASIZE_METADATA",
    "v__atlasize",
    "v__atlasize_params",
]
