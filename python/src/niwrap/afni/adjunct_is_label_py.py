# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_IS_LABEL_PY_METADATA = Metadata(
    id="eafecccdb4a8d1c355d24efe255d4120da84d75c.boutiques",
    name="adjunct_is_label.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctIsLabelPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_is_label_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_is_label_py(
    infile: InputPathType,
    label: str,
    runner: Runner | None = None,
) -> AdjunctIsLabelPyOutputs:
    """
    A subsidiary script of the chauffeur_afni suite for label functionalities.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/adjunct_is_label.py.html
    
    Args:
        infile: Input file for the adjunct_is_label script.
        label: Output label generated by the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctIsLabelPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_IS_LABEL_PY_METADATA)
    cargs = []
    cargs.append("adjunct_is_label.py")
    cargs.append(execution.input_file(infile))
    cargs.append(label)
    ret = AdjunctIsLabelPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_IS_LABEL_PY_METADATA",
    "AdjunctIsLabelPyOutputs",
    "adjunct_is_label_py",
]