# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

BORDER_FILE_EXPORT_TO_CARET5_METADATA = Metadata(
    id="c6222e815dc12e3246ef1e271032f35ed2201092.boutiques",
    name="border-file-export-to-caret5",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
BorderFileExportToCaret5SurfaceParameters = typing.TypedDict('BorderFileExportToCaret5SurfaceParameters', {
    "__STYX_TYPE__": typing.Literal["surface"],
    "surface_in": InputPathType,
})
BorderFileExportToCaret5Parameters = typing.TypedDict('BorderFileExportToCaret5Parameters', {
    "__STYX_TYPE__": typing.Literal["border-file-export-to-caret5"],
    "border_file": str,
    "output_file_prefix": str,
    "surface": typing.NotRequired[list[BorderFileExportToCaret5SurfaceParameters] | None],
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
        "border-file-export-to-caret5": border_file_export_to_caret5_cargs,
        "surface": border_file_export_to_caret5_surface_cargs,
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


def border_file_export_to_caret5_surface_params(
    surface_in: InputPathType,
) -> BorderFileExportToCaret5SurfaceParameters:
    """
    Build parameters.
    
    Args:
        surface_in: a surface file for unprojection of borders.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "surface",
        "surface_in": surface_in,
    }
    return params


def border_file_export_to_caret5_surface_cargs(
    params: BorderFileExportToCaret5SurfaceParameters,
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
    cargs.append("-surface")
    cargs.append(execution.input_file(params.get("surface_in")))
    return cargs


class BorderFileExportToCaret5Outputs(typing.NamedTuple):
    """
    Output object returned when calling `border_file_export_to_caret5(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def border_file_export_to_caret5_params(
    border_file: str,
    output_file_prefix: str,
    surface: list[BorderFileExportToCaret5SurfaceParameters] | None = None,
) -> BorderFileExportToCaret5Parameters:
    """
    Build parameters.
    
    Args:
        border_file: workbench border file.
        output_file_prefix: prefix for name of output caret5\
            border/borderproj/bordercolor files.
        surface: specify an input surface.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "border-file-export-to-caret5",
        "border_file": border_file,
        "output_file_prefix": output_file_prefix,
    }
    if surface is not None:
        params["surface"] = surface
    return params


def border_file_export_to_caret5_cargs(
    params: BorderFileExportToCaret5Parameters,
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
    cargs.append("wb_command")
    cargs.append("-border-file-export-to-caret5")
    cargs.append(params.get("border_file"))
    cargs.append(params.get("output_file_prefix"))
    if params.get("surface") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("surface")] for a in c])
    return cargs


def border_file_export_to_caret5_outputs(
    params: BorderFileExportToCaret5Parameters,
    execution: Execution,
) -> BorderFileExportToCaret5Outputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = BorderFileExportToCaret5Outputs(
        root=execution.output_file("."),
    )
    return ret


def border_file_export_to_caret5_execute(
    params: BorderFileExportToCaret5Parameters,
    execution: Execution,
) -> BorderFileExportToCaret5Outputs:
    """
    Export border file to caret5 file format.
    
    A Workbench border file may contain borders for multiple structures and
    borders that are both projected and unprojected. It also contains a color
    table for the borders.
    
    Caret5 has both border (unprojected) and border projection (projected)
    files. In addition, each Caret5 border or border projection file typically
    contains data for a single structure. Caret5 also uses a border color file
    that associates colors with the names of the borders.
    
    This command will try to output both Caret5 border and border projection
    files. Each output border/border projection file will contains data for one
    structure so there may be many files created. The structure name is included
    in the name of each border or border projection file that is created.
    
    One Caret5 border color file will also be produced by this command.
    
    Providing surface(s) as input parameters is optional, but recommended.
    Surfaces may be needed to create both projected and/or unprojected
    coordinates of borders. If there is a failure to produce an output border or
    border projection due to a missing surface with the matching structure, an
    error message will be displayed and some output files will not be created.
    
    When writing new files, this command will overwrite a file with the same
    name. .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `BorderFileExportToCaret5Outputs`).
    """
    params = execution.params(params)
    cargs = border_file_export_to_caret5_cargs(params, execution)
    ret = border_file_export_to_caret5_outputs(params, execution)
    execution.run(cargs)
    return ret


def border_file_export_to_caret5(
    border_file: str,
    output_file_prefix: str,
    surface: list[BorderFileExportToCaret5SurfaceParameters] | None = None,
    runner: Runner | None = None,
) -> BorderFileExportToCaret5Outputs:
    """
    Export border file to caret5 file format.
    
    A Workbench border file may contain borders for multiple structures and
    borders that are both projected and unprojected. It also contains a color
    table for the borders.
    
    Caret5 has both border (unprojected) and border projection (projected)
    files. In addition, each Caret5 border or border projection file typically
    contains data for a single structure. Caret5 also uses a border color file
    that associates colors with the names of the borders.
    
    This command will try to output both Caret5 border and border projection
    files. Each output border/border projection file will contains data for one
    structure so there may be many files created. The structure name is included
    in the name of each border or border projection file that is created.
    
    One Caret5 border color file will also be produced by this command.
    
    Providing surface(s) as input parameters is optional, but recommended.
    Surfaces may be needed to create both projected and/or unprojected
    coordinates of borders. If there is a failure to produce an output border or
    border projection due to a missing surface with the matching structure, an
    error message will be displayed and some output files will not be created.
    
    When writing new files, this command will overwrite a file with the same
    name. .
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        border_file: workbench border file.
        output_file_prefix: prefix for name of output caret5\
            border/borderproj/bordercolor files.
        surface: specify an input surface.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderFileExportToCaret5Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_FILE_EXPORT_TO_CARET5_METADATA)
    params = border_file_export_to_caret5_params(border_file=border_file, output_file_prefix=output_file_prefix, surface=surface)
    return border_file_export_to_caret5_execute(params, execution)


__all__ = [
    "BORDER_FILE_EXPORT_TO_CARET5_METADATA",
    "BorderFileExportToCaret5Outputs",
    "BorderFileExportToCaret5Parameters",
    "BorderFileExportToCaret5SurfaceParameters",
    "border_file_export_to_caret5",
    "border_file_export_to_caret5_params",
    "border_file_export_to_caret5_surface_params",
]
