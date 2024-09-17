# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_PYTHON_WRAPPER_PY_METADATA = Metadata(
    id="6e37d281f01fec906968b21057c716629cd8edc8.boutiques",
    name="afni_python_wrapper.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AfniPythonWrapperPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_python_wrapper_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_python_wrapper_py(
    runner: Runner | None = None,
) -> AfniPythonWrapperPyOutputs:
    """
    Python wrapper to call AFNI functions from the shell.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_python_wrapper.py.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniPythonWrapperPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_PYTHON_WRAPPER_PY_METADATA)
    cargs = []
    cargs.append("afni_python_wrapper.py")
    cargs.append("[FLAGS]")
    cargs.append("[ARGUMENTS]")
    ret = AfniPythonWrapperPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_PYTHON_WRAPPER_PY_METADATA",
    "AfniPythonWrapperPyOutputs",
    "afni_python_wrapper_py",
]