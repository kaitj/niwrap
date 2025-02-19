# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_GROUP_IN_CORR_METADATA = Metadata(
    id="c0af4482aaede4b9a649dd7f0c784cb42a8b0eb7.boutiques",
    name="3dGroupInCorr",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dGroupInCorrParameters = typing.TypedDict('V3dGroupInCorrParameters', {
    "__STYX_TYPE__": typing.Literal["3dGroupInCorr"],
    "set_a": InputPathType,
    "set_b": typing.NotRequired[InputPathType | None],
    "apair": bool,
    "label_a": typing.NotRequired[str | None],
    "label_b": typing.NotRequired[str | None],
    "pooled": bool,
    "unpooled": bool,
    "paired": bool,
    "nosix": bool,
    "covariates_file": typing.NotRequired[InputPathType | None],
    "center": typing.NotRequired[str | None],
    "seed_radius": typing.NotRequired[float | None],
    "sendall": bool,
    "donocov": bool,
    "dospcov": bool,
    "cluster": typing.NotRequired[str | None],
    "read": bool,
    "ztest": bool,
    "ah": typing.NotRequired[str | None],
    "port_offset": typing.NotRequired[float | None],
    "port_offset_quiet": typing.NotRequired[float | None],
    "port_bloc": typing.NotRequired[float | None],
    "suma": bool,
    "quiet": bool,
    "verbose": bool,
    "very_verbose": bool,
    "debug": bool,
    "batch": typing.NotRequired[str | None],
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
        "3dGroupInCorr": v_3d_group_in_corr_cargs,
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
        "3dGroupInCorr": v_3d_group_in_corr_outputs,
    }.get(t)


class V3dGroupInCorrOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_group_in_corr(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Results from analysis"""


def v_3d_group_in_corr_params(
    set_a: InputPathType,
    set_b: InputPathType | None = None,
    apair: bool = False,
    label_a: str | None = None,
    label_b: str | None = None,
    pooled: bool = False,
    unpooled: bool = False,
    paired: bool = False,
    nosix: bool = False,
    covariates_file: InputPathType | None = None,
    center: str | None = None,
    seed_radius: float | None = None,
    sendall: bool = False,
    donocov: bool = False,
    dospcov: bool = False,
    cluster: str | None = None,
    read: bool = False,
    ztest: bool = False,
    ah: str | None = None,
    port_offset: float | None = None,
    port_offset_quiet: float | None = None,
    port_bloc: float | None = None,
    suma: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    very_verbose: bool = False,
    debug: bool = False,
    batch: str | None = None,
) -> V3dGroupInCorrParameters:
    """
    Build parameters.
    
    Args:
        set_a: Setup file describing the first dataset collection.
        set_b: Setup file describing the second dataset collection for\
            two-sample t-test analysis.
        apair: Use -setA collection again but with different seed locations;\
            produce paired t-test.
        label_a: Label for sub-bricks corresponding to setA.
        label_b: Label for sub-bricks corresponding to setB.
        pooled: Use pooled variance estimator for two-sample un-paired t-test.
        unpooled: Use unpooled variance estimator for two-sample un-paired\
            t-test.
        paired: Use a two-sample paired t-test.
        nosix: Suppress the individual 1-sample t-tests and only return the\
            difference 2-sample t-test.
        covariates_file: File containing covariate values for each dataset.
        center: Option for centering covariates.
        seed_radius: Radius for seed voxel time series averaging (mm).
        sendall: Send all individual subject results to AFNI along with group\
            statistics.
        donocov: Compute results both with and without covariates.
        dospcov: Compute Spearman (rank) correlation coefficient of subject\
            correlation results vs each covariate.
        cluster: Input results from a 3dClustSim run to interface with AFNI.
        read: Force program to read data into memory instead of memory mapping.
        ztest: Debugging option to test if input data is all zero.
        ah: Connect to AFNI/SUMA on a remote host.
        port_offset: Provide a port offset.
        port_offset_quiet: Provide a port offset, with less verbose output.
        port_bloc: Provide a port offset bloc.
        suma: Talk to SUMA instead of AFNI.
        quiet: Suppress informational messages.
        verbose: Print extra informational messages.
        very_verbose: Print even more detailed informational messages.
        debug: Enable internal testing.
        batch: Run program in batch mode with specified METHOD and command\
            file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dGroupInCorr",
        "set_a": set_a,
        "apair": apair,
        "pooled": pooled,
        "unpooled": unpooled,
        "paired": paired,
        "nosix": nosix,
        "sendall": sendall,
        "donocov": donocov,
        "dospcov": dospcov,
        "read": read,
        "ztest": ztest,
        "suma": suma,
        "quiet": quiet,
        "verbose": verbose,
        "very_verbose": very_verbose,
        "debug": debug,
    }
    if set_b is not None:
        params["set_b"] = set_b
    if label_a is not None:
        params["label_a"] = label_a
    if label_b is not None:
        params["label_b"] = label_b
    if covariates_file is not None:
        params["covariates_file"] = covariates_file
    if center is not None:
        params["center"] = center
    if seed_radius is not None:
        params["seed_radius"] = seed_radius
    if cluster is not None:
        params["cluster"] = cluster
    if ah is not None:
        params["ah"] = ah
    if port_offset is not None:
        params["port_offset"] = port_offset
    if port_offset_quiet is not None:
        params["port_offset_quiet"] = port_offset_quiet
    if port_bloc is not None:
        params["port_bloc"] = port_bloc
    if batch is not None:
        params["batch"] = batch
    return params


def v_3d_group_in_corr_cargs(
    params: V3dGroupInCorrParameters,
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
    cargs.append("3dGroupInCorr")
    cargs.extend([
        "-setA",
        execution.input_file(params.get("set_a"))
    ])
    if params.get("set_b") is not None:
        cargs.extend([
            "-setB",
            execution.input_file(params.get("set_b"))
        ])
    if params.get("apair"):
        cargs.append("-Apair")
    if params.get("label_a") is not None:
        cargs.extend([
            "-labelA",
            params.get("label_a")
        ])
    if params.get("label_b") is not None:
        cargs.extend([
            "-labelB",
            params.get("label_b")
        ])
    if params.get("pooled"):
        cargs.append("-pooled")
    if params.get("unpooled"):
        cargs.append("-unpooled")
    if params.get("paired"):
        cargs.append("-paired")
    if params.get("nosix"):
        cargs.append("-nosix")
    if params.get("covariates_file") is not None:
        cargs.extend([
            "-covariates",
            execution.input_file(params.get("covariates_file"))
        ])
    if params.get("center") is not None:
        cargs.extend([
            "-center",
            params.get("center")
        ])
    if params.get("seed_radius") is not None:
        cargs.extend([
            "-seedrad",
            str(params.get("seed_radius"))
        ])
    if params.get("sendall"):
        cargs.append("-sendall")
    if params.get("donocov"):
        cargs.append("-donocov")
    if params.get("dospcov"):
        cargs.append("-dospcov")
    if params.get("cluster") is not None:
        cargs.extend([
            "-clust",
            params.get("cluster")
        ])
    if params.get("read"):
        cargs.append("-read")
    if params.get("ztest"):
        cargs.append("-ztest")
    if params.get("ah") is not None:
        cargs.extend([
            "-ah",
            params.get("ah")
        ])
    if params.get("port_offset") is not None:
        cargs.extend([
            "-np",
            str(params.get("port_offset"))
        ])
    if params.get("port_offset_quiet") is not None:
        cargs.extend([
            "-npq",
            str(params.get("port_offset_quiet"))
        ])
    if params.get("port_bloc") is not None:
        cargs.extend([
            "-npb",
            str(params.get("port_bloc"))
        ])
    if params.get("suma"):
        cargs.append("-suma")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("verbose"):
        cargs.append("-verb")
    if params.get("very_verbose"):
        cargs.append("-VERB")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("batch") is not None:
        cargs.extend([
            "-batch",
            params.get("batch")
        ])
    return cargs


def v_3d_group_in_corr_outputs(
    params: V3dGroupInCorrParameters,
    execution: Execution,
) -> V3dGroupInCorrOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dGroupInCorrOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(pathlib.Path(params.get("set_a")).name + ".results.nii"),
    )
    return ret


def v_3d_group_in_corr_execute(
    params: V3dGroupInCorrParameters,
    execution: Execution,
) -> V3dGroupInCorrOutputs:
    """
    Functional connectivity analysis in group of subjects.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dGroupInCorrOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_group_in_corr_cargs(params, execution)
    ret = v_3d_group_in_corr_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_group_in_corr(
    set_a: InputPathType,
    set_b: InputPathType | None = None,
    apair: bool = False,
    label_a: str | None = None,
    label_b: str | None = None,
    pooled: bool = False,
    unpooled: bool = False,
    paired: bool = False,
    nosix: bool = False,
    covariates_file: InputPathType | None = None,
    center: str | None = None,
    seed_radius: float | None = None,
    sendall: bool = False,
    donocov: bool = False,
    dospcov: bool = False,
    cluster: str | None = None,
    read: bool = False,
    ztest: bool = False,
    ah: str | None = None,
    port_offset: float | None = None,
    port_offset_quiet: float | None = None,
    port_bloc: float | None = None,
    suma: bool = False,
    quiet: bool = False,
    verbose: bool = False,
    very_verbose: bool = False,
    debug: bool = False,
    batch: str | None = None,
    runner: Runner | None = None,
) -> V3dGroupInCorrOutputs:
    """
    Functional connectivity analysis in group of subjects.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        set_a: Setup file describing the first dataset collection.
        set_b: Setup file describing the second dataset collection for\
            two-sample t-test analysis.
        apair: Use -setA collection again but with different seed locations;\
            produce paired t-test.
        label_a: Label for sub-bricks corresponding to setA.
        label_b: Label for sub-bricks corresponding to setB.
        pooled: Use pooled variance estimator for two-sample un-paired t-test.
        unpooled: Use unpooled variance estimator for two-sample un-paired\
            t-test.
        paired: Use a two-sample paired t-test.
        nosix: Suppress the individual 1-sample t-tests and only return the\
            difference 2-sample t-test.
        covariates_file: File containing covariate values for each dataset.
        center: Option for centering covariates.
        seed_radius: Radius for seed voxel time series averaging (mm).
        sendall: Send all individual subject results to AFNI along with group\
            statistics.
        donocov: Compute results both with and without covariates.
        dospcov: Compute Spearman (rank) correlation coefficient of subject\
            correlation results vs each covariate.
        cluster: Input results from a 3dClustSim run to interface with AFNI.
        read: Force program to read data into memory instead of memory mapping.
        ztest: Debugging option to test if input data is all zero.
        ah: Connect to AFNI/SUMA on a remote host.
        port_offset: Provide a port offset.
        port_offset_quiet: Provide a port offset, with less verbose output.
        port_bloc: Provide a port offset bloc.
        suma: Talk to SUMA instead of AFNI.
        quiet: Suppress informational messages.
        verbose: Print extra informational messages.
        very_verbose: Print even more detailed informational messages.
        debug: Enable internal testing.
        batch: Run program in batch mode with specified METHOD and command\
            file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dGroupInCorrOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_GROUP_IN_CORR_METADATA)
    params = v_3d_group_in_corr_params(set_a=set_a, set_b=set_b, apair=apair, label_a=label_a, label_b=label_b, pooled=pooled, unpooled=unpooled, paired=paired, nosix=nosix, covariates_file=covariates_file, center=center, seed_radius=seed_radius, sendall=sendall, donocov=donocov, dospcov=dospcov, cluster=cluster, read=read, ztest=ztest, ah=ah, port_offset=port_offset, port_offset_quiet=port_offset_quiet, port_bloc=port_bloc, suma=suma, quiet=quiet, verbose=verbose, very_verbose=very_verbose, debug=debug, batch=batch)
    return v_3d_group_in_corr_execute(params, execution)


__all__ = [
    "V3dGroupInCorrOutputs",
    "V3dGroupInCorrParameters",
    "V_3D_GROUP_IN_CORR_METADATA",
    "v_3d_group_in_corr",
    "v_3d_group_in_corr_params",
]
