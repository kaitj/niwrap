# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TCORR_MAP_METADATA = Metadata(
    id="197d89aea57496a500d08e514c10454efb723051.boutiques",
    name="3dTcorrMap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dTcorrMapParameters = typing.TypedDict('V3dTcorrMapParameters', {
    "__STYX_TYPE__": typing.Literal["3dTcorrMap"],
    "input": InputPathType,
    "seed": typing.NotRequired[InputPathType | None],
    "mask": typing.NotRequired[InputPathType | None],
    "automask": bool,
    "mean": typing.NotRequired[str | None],
    "zmean": typing.NotRequired[str | None],
    "qmean": typing.NotRequired[str | None],
    "pmean": typing.NotRequired[str | None],
    "thresh": typing.NotRequired[str | None],
    "varthresh": typing.NotRequired[str | None],
    "norm_varthresh": typing.NotRequired[str | None],
    "corrmap": typing.NotRequired[str | None],
    "corrmask": bool,
    "aexpr": typing.NotRequired[str | None],
    "cexpr": typing.NotRequired[str | None],
    "sexpr": typing.NotRequired[str | None],
    "hist": typing.NotRequired[str | None],
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "3dTcorrMap": v_3d_tcorr_map_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {}
    return vt.get(t)


def v_3d_tcorr_map_params(
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
) -> V3dTcorrMapParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dTcorrMap",
        "input": input_,
        "automask": automask,
        "corrmask": corrmask,
    }
    if seed is not None:
        params["seed"] = seed
    if mask is not None:
        params["mask"] = mask
    if mean is not None:
        params["mean"] = mean
    if zmean is not None:
        params["zmean"] = zmean
    if qmean is not None:
        params["qmean"] = qmean
    if pmean is not None:
        params["pmean"] = pmean
    if thresh is not None:
        params["thresh"] = thresh
    if varthresh is not None:
        params["varthresh"] = varthresh
    if norm_varthresh is not None:
        params["norm_varthresh"] = norm_varthresh
    if corrmap is not None:
        params["corrmap"] = corrmap
    if aexpr is not None:
        params["aexpr"] = aexpr
    if cexpr is not None:
        params["cexpr"] = cexpr
    if sexpr is not None:
        params["sexpr"] = sexpr
    if hist is not None:
        params["hist"] = hist
    return params


def v_3d_tcorr_map_cargs(
    params: V3dTcorrMapParameters,
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
    cargs.append("3dTcorrMap")
    cargs.append(execution.input_file(params.get("input")))
    if params.get("seed") is not None:
        cargs.extend([
            "-seed",
            execution.input_file(params.get("seed"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("automask"):
        cargs.append("-automask")
    if params.get("mean") is not None:
        cargs.extend([
            "-Mean",
            params.get("mean")
        ])
    if params.get("zmean") is not None:
        cargs.extend([
            "-Zmean",
            params.get("zmean")
        ])
    if params.get("qmean") is not None:
        cargs.extend([
            "-Qmean",
            params.get("qmean")
        ])
    if params.get("pmean") is not None:
        cargs.extend([
            "-Pmean",
            params.get("pmean")
        ])
    if params.get("thresh") is not None:
        cargs.extend([
            "-Thresh",
            params.get("thresh")
        ])
    if params.get("varthresh") is not None:
        cargs.extend([
            "-VarThresh",
            params.get("varthresh")
        ])
    if params.get("norm_varthresh") is not None:
        cargs.extend([
            "-VarThreshN",
            params.get("norm_varthresh")
        ])
    if params.get("corrmap") is not None:
        cargs.extend([
            "-CorrMap",
            params.get("corrmap")
        ])
    if params.get("corrmask"):
        cargs.append("-CorrMask")
    if params.get("aexpr") is not None:
        cargs.extend([
            "-Aexpr",
            params.get("aexpr")
        ])
    if params.get("cexpr") is not None:
        cargs.extend([
            "-Cexpr",
            params.get("cexpr")
        ])
    if params.get("sexpr") is not None:
        cargs.extend([
            "-Sexpr",
            params.get("sexpr")
        ])
    if params.get("hist") is not None:
        cargs.extend([
            "-Hist",
            params.get("hist")
        ])
    return cargs


def v_3d_tcorr_map_outputs(
    params: V3dTcorrMapParameters,
    execution: Execution,
) -> V3dTcorrMapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dTcorrMapOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3d_tcorr_map_execute(
    params: V3dTcorrMapParameters,
    execution: Execution,
) -> V3dTcorrMapOutputs:
    """
    AFNI program to compute correlation maps of input time series data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dTcorrMapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_tcorr_map_cargs(params, execution)
    ret = v_3d_tcorr_map_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    AFNI program to compute correlation maps of input time series data.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
    params = v_3d_tcorr_map_params(input_=input_, seed=seed, mask=mask, automask=automask, mean=mean, zmean=zmean, qmean=qmean, pmean=pmean, thresh=thresh, varthresh=varthresh, norm_varthresh=norm_varthresh, corrmap=corrmap, corrmask=corrmask, aexpr=aexpr, cexpr=cexpr, sexpr=sexpr, hist=hist)
    return v_3d_tcorr_map_execute(params, execution)


__all__ = [
    "V_3D_TCORR_MAP_METADATA",
    "v_3d_tcorr_map",
    "v_3d_tcorr_map_params",
]
