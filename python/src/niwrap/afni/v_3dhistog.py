# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DHISTOG_METADATA = Metadata(
    id="e7bd0d2e8a320bbb6bd63ecc03a72a5a7207b971.boutiques",
    name="3dhistog",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dhistogOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dhistog(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    histogram_output: OutputPathType
    """Histogram output when -prefix option is used"""


def v_3dhistog(
    dataset: InputPathType,
    nbin: float | None = None,
    dind: float | None = None,
    omit: list[float] | None = None,
    mask: InputPathType | None = None,
    roi_mask: InputPathType | None = None,
    doall: bool = False,
    noempty: bool = False,
    notitle: bool = False,
    log10: bool = False,
    pdf: bool = False,
    min_: float | None = None,
    max_: float | None = None,
    igfac: bool = False,
    int_: bool = False,
    float_: bool = False,
    unq: str | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dhistogOutputs:
    """
    Compute histogram of a 3D dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset: Input dataset.
        nbin: Use specified number of bins.
        dind: Use data from specified sub-brick index.
        omit: Omit specified value from the count.
        mask: Use mask dataset to determine which voxels to use.
        roi_mask: Create histogram for each non-zero value in 'r' dataset.
        doall: Include all sub-bricks in the calculation.
        noempty: Only output bins that are not empty.
        notitle: Leave the title line off the output.
        log10: Output log10() of the counts.
        pdf: Output the counts divided by the number of samples.
        min_: Specify minimum (inclusive) of histogram.
        max_: Specify maximum (inclusive) of histogram.
        igfac: Ignore sub-brick scale factors and histogram-ize the 'raw' data.
        int_: Treat data and output as integers.
        float_: Treat data and output as floats.
        unq: Writes out the sorted unique values to file.
        prefix: Write a copy of the histogram into specified file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dhistogOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DHISTOG_METADATA)
    cargs = []
    cargs.append("3dhistog")
    cargs.append(execution.input_file(dataset))
    if nbin is not None:
        cargs.extend([
            "-nbin",
            str(nbin)
        ])
    if dind is not None:
        cargs.extend([
            "-dind",
            str(dind)
        ])
    if omit is not None:
        cargs.extend([
            "-omit",
            *map(str, omit)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if roi_mask is not None:
        cargs.extend([
            "-roi_mask",
            execution.input_file(roi_mask)
        ])
    if doall:
        cargs.append("-doall")
    if noempty:
        cargs.append("-noempty")
    if notitle:
        cargs.append("-notitle")
    if log10:
        cargs.append("-log10")
    if pdf:
        cargs.append("-pdf")
    if min_ is not None:
        cargs.extend([
            "-min",
            str(min_)
        ])
    if max_ is not None:
        cargs.extend([
            "-max",
            str(max_)
        ])
    if igfac:
        cargs.append("-igfac")
    if int_:
        cargs.append("-int")
    if float_:
        cargs.append("-float")
    if unq is not None:
        cargs.extend([
            "-unq",
            unq
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    ret = V3dhistogOutputs(
        root=execution.output_file("."),
        histogram_output=execution.output_file("HOUT.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dhistogOutputs",
    "V_3DHISTOG_METADATA",
    "v_3dhistog",
]
