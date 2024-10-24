# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SUMA_METADATA = Metadata(
    id="e8bcb13f787fa10a2afe180ac5e247a1f8b299e9.boutiques",
    name="suma",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SumaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `suma(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def suma(
    spec_file: InputPathType | None = None,
    surf_vol: InputPathType | None = None,
    afni_host: str | None = None,
    niml: bool = False,
    noniml: bool = False,
    surface_file: InputPathType | None = None,
    surface_type: str | None = None,
    cifti_dataset: InputPathType | None = None,
    graph_dataset: InputPathType | None = None,
    tractography_dataset: InputPathType | None = None,
    volume: InputPathType | None = None,
    onestate: bool = False,
    anatomical: bool = False,
    linear_depth: float | None = None,
    recursive_depth: float | None = None,
    novolreg: bool = False,
    setenv: str | None = None,
    trace_: bool = False,
    extreme_trace: bool = False,
    nomall: bool = False,
    yesmall: bool = False,
    port_offset: float | None = None,
    port_offset_bloc: float | None = None,
    drive_command: str | None = None,
    clipping_plane_verbose: float | None = None,
    runner: Runner | None = None,
) -> SumaOutputs:
    """
    SUMA: Surface Mapper for visualization and analysis of brain data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        spec_file: Surface specification file.
        surf_vol: Anatomical volume used in creating the surface and registered\
            to the current experiment's anatomical volume.
        afni_host: Name or IP address of the computer running AFNI.
        niml: Start listening for communications with NIML-formatted elements.
        noniml: Do not start listening for communications with NIML-formatted\
            elements.
        surface_file: Path to the surface file.
        surface_type: Specify a surface type (e.g. fs, sf, vec, ply, stl, mni,\
            byu, bv, dx, gii, obj).
        cifti_dataset: CIFTI dataset to display.
        graph_dataset: Graph dataset to display.
        tractography_dataset: Tractography dataset to display.
        volume: Volume to display.
        onestate: Make all -i_* surfaces have the same state.
        anatomical: Label all -i surfaces as anatomically correct.
        linear_depth: Specify a standard-mesh sphere through linear depth.
        recursive_depth: Specify a standard-mesh sphere through recursive\
            depth.
        novolreg: Ignore any Rotate, Volreg, Tagalign, or WarpDrive\
            transformations.
        setenv: Set environment variable.
        trace_: Use debugging options for SUMA.
        extreme_trace: Use extreme debugging options for SUMA.
        nomall: Ignore memory tracing options for SUMA.
        yesmall: Use memory tracing options for SUMA.
        port_offset: Specify the port offset for SUMA.
        port_offset_bloc: Provide port offset bloc for SUMA.
        drive_command: Drive SUMA with a specific command.
        clipping_plane_verbose: Provide verbose output in clipping plane mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SumaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SUMA_METADATA)
    cargs = []
    cargs.append("suma")
    if spec_file is not None:
        cargs.extend([
            "-spec",
            execution.input_file(spec_file)
        ])
    if surf_vol is not None:
        cargs.extend([
            "-sv",
            execution.input_file(surf_vol)
        ])
    if afni_host is not None:
        cargs.extend([
            "-ah",
            afni_host
        ])
    if niml:
        cargs.append("-niml")
    if noniml:
        cargs.append("-noniml")
    if surface_file is not None:
        cargs.extend([
            "-i",
            execution.input_file(surface_file)
        ])
    if surface_type is not None:
        cargs.extend([
            "-i_TYPE",
            surface_type
        ])
    if cifti_dataset is not None:
        cargs.extend([
            "-cdset",
            execution.input_file(cifti_dataset)
        ])
    if graph_dataset is not None:
        cargs.extend([
            "-gdset",
            execution.input_file(graph_dataset)
        ])
    if tractography_dataset is not None:
        cargs.extend([
            "-tract",
            execution.input_file(tractography_dataset)
        ])
    if volume is not None:
        cargs.extend([
            "-vol",
            execution.input_file(volume)
        ])
    if onestate:
        cargs.append("-onestate")
    if anatomical:
        cargs.append("-anatomical")
    if linear_depth is not None:
        cargs.extend([
            "-i ld",
            str(linear_depth)
        ])
    if recursive_depth is not None:
        cargs.extend([
            "-i rd",
            str(recursive_depth)
        ])
    if novolreg:
        cargs.append("-novolreg")
    if setenv is not None:
        cargs.extend([
            "-setenv",
            setenv
        ])
    if trace_:
        cargs.append("-trace")
    if extreme_trace:
        cargs.append("-TRACE")
    if nomall:
        cargs.append("-nomall")
    if yesmall:
        cargs.append("-yesmall")
    if port_offset is not None:
        cargs.extend([
            "-np",
            str(port_offset)
        ])
    if port_offset_bloc is not None:
        cargs.extend([
            "-npb",
            str(port_offset_bloc)
        ])
    if drive_command is not None:
        cargs.extend([
            "-drive_com",
            drive_command
        ])
    if clipping_plane_verbose is not None:
        cargs.extend([
            "-clippingPlaneVerbose",
            str(clipping_plane_verbose)
        ])
    ret = SumaOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SUMA_METADATA",
    "SumaOutputs",
    "suma",
]
