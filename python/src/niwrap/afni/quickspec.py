# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

QUICKSPEC_METADATA = Metadata(
    id="0a985ab38a04ef53341c98e04d446660dcd3c0c6.boutiques",
    name="quickspec",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class QuickspecOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quickspec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_specfile: OutputPathType | None
    """The spec file output."""


def quickspec(
    tn: list[str],
    tsn: list[str],
    tsnad: list[str] | None = None,
    tsnadm: list[str] | None = None,
    tsnadl: list[str] | None = None,
    spec: str | None = None,
    help_: bool = False,
    runner: Runner | None = None,
) -> QuickspecOutputs:
    """
    A quick and dirty way of loading a surface into SUMA or command line programs
    using a spec file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        tn: Specify surface type and name.
        tsn: Specify surface type, state, and name.
        tsnad: Specify surface type, state, name, anatomical correctness, and\
            Local Domain Parent.
        tsnadm: Specify surface type, state, name, anatomical correctness,\
            Local Domain Parent, and node marker file.
        tsnadl: Specify surface type, state, name, anatomical correctness,\
            Local Domain Parent, and label dataset file.
        spec: Name of spec file output. Default is quick.spec.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuickspecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUICKSPEC_METADATA)
    cargs = []
    cargs.append("quickspec")
    cargs.extend([
        "-tn",
        *tn
    ])
    cargs.extend([
        "-tsn",
        *tsn
    ])
    if tsnad is not None:
        cargs.extend([
            "-tsnad",
            *tsnad
        ])
    if tsnadm is not None:
        cargs.extend([
            "-tsnadm",
            *tsnadm
        ])
    if tsnadl is not None:
        cargs.extend([
            "-tsnadl",
            *tsnadl
        ])
    if spec is not None:
        cargs.extend([
            "-spec",
            spec
        ])
    if help_:
        cargs.append("-h")
    ret = QuickspecOutputs(
        root=execution.output_file("."),
        out_specfile=execution.output_file(spec) if (spec is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QUICKSPEC_METADATA",
    "QuickspecOutputs",
    "quickspec",
]
