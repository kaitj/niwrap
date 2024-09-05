# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_TCORR_MAP_METADATA = Metadata(
    id="7bd206a1d4a50c204e453541a4d42e8429f33f3a",
    name="3dTcorrMap",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTcorrMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcorr_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_tcorr_map(
    input_: InputPathType,
    seed: InputPathType | None = None,
    mask: InputPathType | None = None,
    automask: bool = False,
    mean: str | None = None,
    zmean: str | None = None,
    qmean: str | None = None,
    pmean: str | None = None,
    thresh: str | None = None,
    varthresh: str | None = None,
    norm_varthresh: str | None = None,
    corrmap: str | None = None,
    corrmask: bool = False,
    aexpr: str | None = None,
    cexpr: str | None = None,
    sexpr: str | None = None,
    hist: str | None = None,
    runner: Runner | None = None,
) -> V3dTcorrMapOutputs:
    """
    3dTcorrMap by AFNI Team.
    
    AFNI program to compute correlation maps of input time series data.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTcorrMap.html
    
    Args:
        input_: Read 3D+time dataset 'dd'. This provides the time series to be\
            correlated en masse. This is a mandatory option.
        seed: Read 3D+time dataset 'bb'. It correlates the -seed voxel time\
            series with every voxel in the -input dataset.
        mask: Read dataset 'mmm' as a voxel mask.
        automask: Create a mask from the input dataset.
        mean: Save average correlations into dataset prefix 'pp'.
        zmean: Save tanh of mean arctanh(correlation) into 'pp'.
        qmean: Save RMS(correlation) into 'pp'.
        pmean: Save average of squared positive correlations into 'pp'.
        thresh: Save the COUNT of how many voxels survived thresholding at\
            level abs(correlation) >= tt.
        varthresh: Save the COUNT of how many voxels survive thresholding at\
            multiple levels abs(correlation) >= tt.
        norm_varthresh: Like '-VarThresh', but the output counts are\
            'Normalized'.
        corrmap: Output at each voxel the entire correlation map, into a\
            dataset with prefix 'pp'.
        corrmask: By default, -CorrMap outputs a sub-brick for EACH input\
            dataset voxel. Eliminates these sub-bricks using this option.
        aexpr: For each correlation 'r', compute the calc-style expression\
            'expr', and average these values to get the output that goes into\
            dataset 'ppp'.
        cexpr: As in '-Aexpr', but only average together nonzero values\
            computed by 'expr'.
        sexpr: As above, but the sum of the expressions is computed rather than\
            the average.
        hist: For each voxel, save a histogram of the correlation coefficients\
            into dataset ppp.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTcorrMapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCORR_MAP_METADATA)
    cargs = []
    cargs.append("3dTcorrMap")
    cargs.append(execution.input_file(input_))
    if seed is not None:
        cargs.extend(["-seed", execution.input_file(seed)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if automask:
        cargs.append("-automask")
    if mean is not None:
        cargs.extend(["-Mean", mean])
    if zmean is not None:
        cargs.extend(["-Zmean", zmean])
    if qmean is not None:
        cargs.extend(["-Qmean", qmean])
    if pmean is not None:
        cargs.extend(["-Pmean", pmean])
    if thresh is not None:
        cargs.extend(["-Thresh", thresh])
    if varthresh is not None:
        cargs.extend(["-VarThresh", varthresh])
    if norm_varthresh is not None:
        cargs.extend(["-VarThreshN", norm_varthresh])
    if corrmap is not None:
        cargs.extend(["-CorrMap", corrmap])
    if corrmask:
        cargs.append("-CorrMask")
    if aexpr is not None:
        cargs.extend(["-Aexpr", aexpr])
    if cexpr is not None:
        cargs.extend(["-Cexpr", cexpr])
    if sexpr is not None:
        cargs.extend(["-Sexpr", sexpr])
    if hist is not None:
        cargs.extend(["-Hist", hist])
    ret = V3dTcorrMapOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTcorrMapOutputs",
    "V_3D_TCORR_MAP_METADATA",
    "v_3d_tcorr_map",
]