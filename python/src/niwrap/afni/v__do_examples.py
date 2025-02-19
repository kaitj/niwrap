# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__DO_EXAMPLES_METADATA = Metadata(
    id="a9216d6bc30f6cf096b83a22a6cc899b517e504e.boutiques",
    name="@DO.examples",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VDoExamplesParameters = typing.TypedDict('VDoExamplesParameters', {
    "__STYX_TYPE__": typing.Literal["@DO.examples"],
    "auto_test": bool,
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
        "@DO.examples": v__do_examples_cargs,
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
        "@DO.examples": v__do_examples_outputs,
    }.get(t)


class VDoExamplesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__do_examples(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_log: OutputPathType
    """Output log file when running in auto test mode"""


def v__do_examples_params(
    auto_test: bool = False,
) -> VDoExamplesParameters:
    """
    Build parameters.
    
    Args:
        auto_test: Run this script in test mode where user prompts are timed\
            out at 2 seconds, and the command output log is preserved in a file\
            called __testlog.txt.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@DO.examples",
        "auto_test": auto_test,
    }
    return params


def v__do_examples_cargs(
    params: VDoExamplesParameters,
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
    cargs.append("@DO.examples")
    if params.get("auto_test"):
        cargs.append("-auto_test")
    return cargs


def v__do_examples_outputs(
    params: VDoExamplesParameters,
    execution: Execution,
) -> VDoExamplesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VDoExamplesOutputs(
        root=execution.output_file("."),
        output_log=execution.output_file("__testlog.txt"),
    )
    return ret


def v__do_examples_execute(
    params: VDoExamplesParameters,
    execution: Execution,
) -> VDoExamplesOutputs:
    """
    A script to illustrate the use of Displayable Objects in SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VDoExamplesOutputs`).
    """
    params = execution.params(params)
    cargs = v__do_examples_cargs(params, execution)
    ret = v__do_examples_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__do_examples(
    auto_test: bool = False,
    runner: Runner | None = None,
) -> VDoExamplesOutputs:
    """
    A script to illustrate the use of Displayable Objects in SUMA.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        auto_test: Run this script in test mode where user prompts are timed\
            out at 2 seconds, and the command output log is preserved in a file\
            called __testlog.txt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VDoExamplesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__DO_EXAMPLES_METADATA)
    params = v__do_examples_params(auto_test=auto_test)
    return v__do_examples_execute(params, execution)


__all__ = [
    "VDoExamplesOutputs",
    "VDoExamplesParameters",
    "V__DO_EXAMPLES_METADATA",
    "v__do_examples",
    "v__do_examples_params",
]
