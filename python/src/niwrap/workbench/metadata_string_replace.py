# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

METADATA_STRING_REPLACE_METADATA = Metadata(
    id="c5101a74a82c5e31a6a055c1295c99ce1b69c5f2.boutiques",
    name="metadata-string-replace",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
MetadataStringReplaceParameters = typing.TypedDict('MetadataStringReplaceParameters', {
    "__STYX_TYPE__": typing.Literal["metadata-string-replace"],
    "input_file": str,
    "find_string": str,
    "replace_string": str,
    "output_file": str,
    "opt_case_insensitive": bool,
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
        "metadata-string-replace": metadata_string_replace_cargs,
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
    vt = {}
    return vt.get(t)


def metadata_string_replace_params(
    input_file: str,
    find_string: str,
    replace_string: str,
    output_file: str,
    opt_case_insensitive: bool = False,
) -> MetadataStringReplaceParameters:
    """
    Build parameters.
    
    Args:
        input_file: the file to replace metadata in.
        find_string: the string to find.
        replace_string: the string to replace <find-string> with.
        output_file: output - the name to save the modified file as.
        opt_case_insensitive: match with case variation also.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "metadata-string-replace",
        "input_file": input_file,
        "find_string": find_string,
        "replace_string": replace_string,
        "output_file": output_file,
        "opt_case_insensitive": opt_case_insensitive,
    }
    return params


def metadata_string_replace_cargs(
    params: MetadataStringReplaceParameters,
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
    cargs.append("-metadata-string-replace")
    cargs.append(params.get("input_file"))
    cargs.append(params.get("find_string"))
    cargs.append(params.get("replace_string"))
    cargs.append(params.get("output_file"))
    if params.get("opt_case_insensitive"):
        cargs.append("-case-insensitive")
    return cargs


def metadata_string_replace_outputs(
    params: MetadataStringReplaceParameters,
    execution: Execution,
) -> MetadataStringReplaceOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MetadataStringReplaceOutputs(
        root=execution.output_file("."),
    )
    return ret


def metadata_string_replace_execute(
    params: MetadataStringReplaceParameters,
    execution: Execution,
) -> MetadataStringReplaceOutputs:
    """
    Replace a string in all metadata of a file.
    
    Replaces all occurrences of <find-string> in the metadata and map names of
    <input-file> with <replace-string>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MetadataStringReplaceOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = metadata_string_replace_cargs(params, execution)
    ret = metadata_string_replace_outputs(params, execution)
    execution.run(cargs)
    return ret


def metadata_string_replace(
    input_file: str,
    find_string: str,
    replace_string: str,
    output_file: str,
    opt_case_insensitive: bool = False,
    runner: Runner | None = None,
) -> MetadataStringReplaceOutputs:
    """
    Replace a string in all metadata of a file.
    
    Replaces all occurrences of <find-string> in the metadata and map names of
    <input-file> with <replace-string>.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_file: the file to replace metadata in.
        find_string: the string to find.
        replace_string: the string to replace <find-string> with.
        output_file: output - the name to save the modified file as.
        opt_case_insensitive: match with case variation also.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MetadataStringReplaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(METADATA_STRING_REPLACE_METADATA)
    params = metadata_string_replace_params(input_file=input_file, find_string=find_string, replace_string=replace_string, output_file=output_file, opt_case_insensitive=opt_case_insensitive)
    return metadata_string_replace_execute(params, execution)


__all__ = [
    "METADATA_STRING_REPLACE_METADATA",
    "metadata_string_replace",
    "metadata_string_replace_params",
]
