# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_COPY_HEADER_METADATA = Metadata(
    id="50aaea9bf37b8cf2e2b611b945681126287cbd83.boutiques",
    name="mris_copy_header",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
MrisCopyHeaderParameters = typing.TypedDict('MrisCopyHeaderParameters', {
    "__STYX_TYPE__": typing.Literal["mris_copy_header"],
    "input_surface": InputPathType,
    "template_surface": InputPathType,
    "output_surface": str,
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
        "mris_copy_header": mris_copy_header_cargs,
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
        "mris_copy_header": mris_copy_header_outputs,
    }.get(t)


class MrisCopyHeaderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_copy_header(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_surface: OutputPathType
    """Output surface file with copied header."""


def mris_copy_header_params(
    input_surface: InputPathType,
    template_surface: InputPathType,
    output_surface: str,
) -> MrisCopyHeaderParameters:
    """
    Build parameters.
    
    Args:
        input_surface: Input surface file whose header will be replaced.
        template_surface: Template surface file from which the header will be\
            copied.
        output_surface: Output surface file with the updated header.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_copy_header",
        "input_surface": input_surface,
        "template_surface": template_surface,
        "output_surface": output_surface,
    }
    return params


def mris_copy_header_cargs(
    params: MrisCopyHeaderParameters,
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
    cargs.append("mris_copy_header")
    cargs.append(execution.input_file(params.get("input_surface")))
    cargs.append(execution.input_file(params.get("template_surface")))
    cargs.append(params.get("output_surface"))
    return cargs


def mris_copy_header_outputs(
    params: MrisCopyHeaderParameters,
    execution: Execution,
) -> MrisCopyHeaderOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisCopyHeaderOutputs(
        root=execution.output_file("."),
        out_surface=execution.output_file(params.get("output_surface")),
    )
    return ret


def mris_copy_header_execute(
    params: MrisCopyHeaderParameters,
    execution: Execution,
) -> MrisCopyHeaderOutputs:
    """
    Tool to copy the header from a template surface to an input surface and save as
    the output surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisCopyHeaderOutputs`).
    """
    params = execution.params(params)
    cargs = mris_copy_header_cargs(params, execution)
    ret = mris_copy_header_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_copy_header(
    input_surface: InputPathType,
    template_surface: InputPathType,
    output_surface: str,
    runner: Runner | None = None,
) -> MrisCopyHeaderOutputs:
    """
    Tool to copy the header from a template surface to an input surface and save as
    the output surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_surface: Input surface file whose header will be replaced.
        template_surface: Template surface file from which the header will be\
            copied.
        output_surface: Output surface file with the updated header.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisCopyHeaderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_COPY_HEADER_METADATA)
    params = mris_copy_header_params(input_surface=input_surface, template_surface=template_surface, output_surface=output_surface)
    return mris_copy_header_execute(params, execution)


__all__ = [
    "MRIS_COPY_HEADER_METADATA",
    "MrisCopyHeaderOutputs",
    "MrisCopyHeaderParameters",
    "mris_copy_header",
    "mris_copy_header_params",
]
