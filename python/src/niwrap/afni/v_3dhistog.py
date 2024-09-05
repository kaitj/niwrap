# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DHISTOG_METADATA = Metadata(
    id="2279c1786ad69d2a883d24cf0ff51ee859b209c3",
    name="3dhistog",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    nbin: float | int | None = None,
    dind: float | int | None = None,
    omit: list[float | int] | None = None,
    mask: InputPathType | None = None,
    roi_mask: InputPathType | None = None,
    doall: bool = False,
    noempty: bool = False,
    notitle: bool = False,
    log10: bool = False,
    pdf: bool = False,
    min_: float | int | None = None,
    max_: float | int | None = None,
    igfac: bool = False,
    int_: bool = False,
    float_: bool = False,
    unq: str | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dhistogOutputs:
    """
    3dhistog by AFNI Team.
    
    Compute histogram of a 3D dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dhistog.html
    
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
    if omit is not None and not (len(omit) <= 100): 
        raise ValueError(f"Length of 'omit' must be less than 100 but was {len(omit)}")
    execution = runner.start_execution(V_3DHISTOG_METADATA)
    cargs = []
    cargs.append("3dhistog")
    cargs.append("[EDITING_OPTIONS]")
    cargs.append("[HISTOGRAM_OPTIONS]")
    cargs.append(execution.input_file(dataset))
    ret = V3dhistogOutputs(
        root=execution.output_file("."),
        histogram_output=execution.output_file(f"HOUT.1D", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dhistogOutputs",
    "V_3DHISTOG_METADATA",
    "v_3dhistog",
]