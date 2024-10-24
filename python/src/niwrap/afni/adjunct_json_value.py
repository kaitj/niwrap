# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_JSON_VALUE_METADATA = Metadata(
    id="4c1f70aedb2c31842eee295cd6c5e57c03f44033.boutiques",
    name="adjunct_json_value",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctJsonValueOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_json_value(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    modified_json_file: OutputPathType
    """Modified JSON file"""


def adjunct_json_value(
    json_file: InputPathType,
    key: str,
    value: str,
    runner: Runner | None = None,
) -> AdjunctJsonValueOutputs:
    """
    A supplementary tool for manipulating JSON values in conjunction with AFNI's
    apqc_py.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        json_file: Input JSON file.
        key: Key in the JSON object to be modified.
        value: Value to be set for the given key.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctJsonValueOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_JSON_VALUE_METADATA)
    cargs = []
    cargs.append("adjunct_json_value")
    cargs.append(execution.input_file(json_file))
    cargs.append(key)
    cargs.append(value)
    ret = AdjunctJsonValueOutputs(
        root=execution.output_file("."),
        modified_json_file=execution.output_file(pathlib.Path(json_file).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_JSON_VALUE_METADATA",
    "AdjunctJsonValueOutputs",
    "adjunct_json_value",
]
