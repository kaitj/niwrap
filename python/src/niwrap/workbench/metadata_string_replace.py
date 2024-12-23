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


class MetadataStringReplaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `metadata_string_replace(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


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
    cargs = []
    cargs.append("wb_command")
    cargs.append("-metadata-string-replace")
    cargs.append(input_file)
    cargs.append(find_string)
    cargs.append(replace_string)
    cargs.append(output_file)
    if opt_case_insensitive:
        cargs.append("-case-insensitive")
    ret = MetadataStringReplaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "METADATA_STRING_REPLACE_METADATA",
    "MetadataStringReplaceOutputs",
    "metadata_string_replace",
]
