# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_SIGNATURES_METADATA = Metadata(
    id="2b341af415f403aafe08628a486de9e313d26e1f.boutiques",
    name="3dSignatures",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dSignaturesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_signatures(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    results_file: OutputPathType
    """Main analysis results file"""


def v_3d_signatures(
    infile: InputPathType,
    outfile: str,
    segmentation: bool = False,
    filter_: bool = False,
    threshold: float | None = None,
    smoothing: float | None = None,
    runner: Runner | None = None,
) -> V3dSignaturesOutputs:
    """
    3dSignatures analysis tool for 3D genome organization.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dSignatures.html
    
    Args:
        infile: Input file containing 3D genome data (e.g. genome_data.txt).
        outfile: Output file to store analysis results (e.g.\
            analysis_results.txt).
        segmentation: Flag to apply genome segmentation.
        filter_: Flag to apply data filtering.
        threshold: Threshold level for data filtering; default=0.5.
        smoothing: Apply smoothing with specified kernel size.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSignaturesOutputs`).
    """
    if threshold is not None and not (0 <= threshold <= 1): 
        raise ValueError(f"'threshold' must be between 0 <= x <= 1 but was {threshold}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SIGNATURES_METADATA)
    cargs = []
    cargs.append("3dSignatures")
    cargs.append(execution.input_file(infile))
    cargs.append(outfile)
    if segmentation:
        cargs.append("--segmentation")
    if filter_:
        cargs.append("--filter")
    if threshold is not None:
        cargs.extend([
            "--threshold",
            str(threshold)
        ])
    if smoothing is not None:
        cargs.extend([
            "--smoothing",
            str(smoothing)
        ])
    ret = V3dSignaturesOutputs(
        root=execution.output_file("."),
        results_file=execution.output_file(outfile + ".txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSignaturesOutputs",
    "V_3D_SIGNATURES_METADATA",
    "v_3d_signatures",
]