# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_MVM_METADATA = Metadata(
    id="f66a98f269fed22500c7f8aa62cd43c5d51fda61.boutiques",
    name="3dMVM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dMvmParameters = typing.TypedDict('V3dMvmParameters', {
    "__STYX_TYPE__": typing.Literal["3dMVM"],
    "dbgArgs": typing.NotRequired[str | None],
    "prefix": str,
    "jobs": typing.NotRequired[int | None],
    "mask": typing.NotRequired[InputPathType | None],
    "bsVars": str,
    "wsVars": typing.NotRequired[str | None],
    "qVars": typing.NotRequired[str | None],
    "qVarCenters": typing.NotRequired[str | None],
    "num_glt": typing.NotRequired[int | None],
    "gltLabel": typing.NotRequired[str | None],
    "gltCode": typing.NotRequired[str | None],
    "num_glf": typing.NotRequired[int | None],
    "glfLabel": typing.NotRequired[str | None],
    "glfCode": typing.NotRequired[str | None],
    "dataTable": str,
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
        "3dMVM": v_3d_mvm_cargs,
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
        "3dMVM": v_3d_mvm_outputs,
    }.get(t)


class V3dMvmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_mvm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_head: OutputPathType
    """Output HEAD file in AFNI format"""
    outfile_brik: OutputPathType
    """Output BRIK file in AFNI format"""


def v_3d_mvm_params(
    prefix: str,
    bs_vars: str,
    data_table: str,
    dbg_args: str | None = None,
    jobs: int | None = None,
    mask: InputPathType | None = None,
    ws_vars: str | None = None,
    q_vars: str | None = None,
    q_var_centers: str | None = None,
    num_glt: int | None = None,
    glt_label: str | None = None,
    glt_code: str | None = None,
    num_glf: int | None = None,
    glf_label: str | None = None,
    glf_code: str | None = None,
) -> V3dMvmParameters:
    """
    Build parameters.
    
    Args:
        prefix: Output file name prefix.
        bs_vars: Formula for between-subjects variables.
        data_table: Data table for analysis.
        dbg_args: Enable R to save parameters in a file for debugging.
        jobs: Number of jobs for parallel processing.
        mask: Only process voxels inside this mask.
        ws_vars: Formula for within-subjects variables.
        q_vars: Comma-separated list of quantitative variables (covariates).
        q_var_centers: Comma-separated centering values for quantitative\
            variables.
        num_glt: Number of general linear t-tests (GLTs).
        glt_label: Label for each general linear t-test (GLT).
        glt_code: Coding for each general linear t-test (GLT).
        num_glf: Number of general linear F-tests (GLFs).
        glf_label: Label for each general linear F-test (GLF).
        glf_code: Coding for each general linear F-test (GLF).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dMVM",
        "prefix": prefix,
        "bsVars": bs_vars,
        "dataTable": data_table,
    }
    if dbg_args is not None:
        params["dbgArgs"] = dbg_args
    if jobs is not None:
        params["jobs"] = jobs
    if mask is not None:
        params["mask"] = mask
    if ws_vars is not None:
        params["wsVars"] = ws_vars
    if q_vars is not None:
        params["qVars"] = q_vars
    if q_var_centers is not None:
        params["qVarCenters"] = q_var_centers
    if num_glt is not None:
        params["num_glt"] = num_glt
    if glt_label is not None:
        params["gltLabel"] = glt_label
    if glt_code is not None:
        params["gltCode"] = glt_code
    if num_glf is not None:
        params["num_glf"] = num_glf
    if glf_label is not None:
        params["glfLabel"] = glf_label
    if glf_code is not None:
        params["glfCode"] = glf_code
    return params


def v_3d_mvm_cargs(
    params: V3dMvmParameters,
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
    cargs.append("3dMVM")
    if params.get("dbgArgs") is not None:
        cargs.append(params.get("dbgArgs"))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("jobs") is not None:
        cargs.extend([
            "-jobs",
            str(params.get("jobs"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    cargs.extend([
        "-bsVars",
        params.get("bsVars")
    ])
    if params.get("wsVars") is not None:
        cargs.extend([
            "-wsVars",
            params.get("wsVars")
        ])
    if params.get("qVars") is not None:
        cargs.extend([
            "-qVars",
            params.get("qVars")
        ])
    if params.get("qVarCenters") is not None:
        cargs.extend([
            "-qVarCenters",
            params.get("qVarCenters")
        ])
    if params.get("num_glt") is not None:
        cargs.extend([
            "-num_glt",
            str(params.get("num_glt"))
        ])
    if params.get("gltLabel") is not None:
        cargs.extend([
            "-gltLabel",
            params.get("gltLabel")
        ])
    if params.get("gltCode") is not None:
        cargs.extend([
            "-gltCode",
            params.get("gltCode")
        ])
    if params.get("num_glf") is not None:
        cargs.extend([
            "-num_glf",
            str(params.get("num_glf"))
        ])
    if params.get("glfLabel") is not None:
        cargs.extend([
            "-glfLabel",
            params.get("glfLabel")
        ])
    if params.get("glfCode") is not None:
        cargs.extend([
            "-glfCode",
            params.get("glfCode")
        ])
    cargs.extend([
        "-dataTable",
        params.get("dataTable")
    ])
    return cargs


def v_3d_mvm_outputs(
    params: V3dMvmParameters,
    execution: Execution,
) -> V3dMvmOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dMvmOutputs(
        root=execution.output_file("."),
        outfile_head=execution.output_file(params.get("prefix") + "+tlrc.HEAD"),
        outfile_brik=execution.output_file(params.get("prefix") + "+tlrc.BRIK"),
    )
    return ret


def v_3d_mvm_execute(
    params: V3dMvmParameters,
    execution: Execution,
) -> V3dMvmOutputs:
    """
    AFNI Group Analysis Program with Multi-Variate Modeling Approach.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dMvmOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_mvm_cargs(params, execution)
    ret = v_3d_mvm_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_mvm(
    prefix: str,
    bs_vars: str,
    data_table: str,
    dbg_args: str | None = None,
    jobs: int | None = None,
    mask: InputPathType | None = None,
    ws_vars: str | None = None,
    q_vars: str | None = None,
    q_var_centers: str | None = None,
    num_glt: int | None = None,
    glt_label: str | None = None,
    glt_code: str | None = None,
    num_glf: int | None = None,
    glf_label: str | None = None,
    glf_code: str | None = None,
    runner: Runner | None = None,
) -> V3dMvmOutputs:
    """
    AFNI Group Analysis Program with Multi-Variate Modeling Approach.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file name prefix.
        bs_vars: Formula for between-subjects variables.
        data_table: Data table for analysis.
        dbg_args: Enable R to save parameters in a file for debugging.
        jobs: Number of jobs for parallel processing.
        mask: Only process voxels inside this mask.
        ws_vars: Formula for within-subjects variables.
        q_vars: Comma-separated list of quantitative variables (covariates).
        q_var_centers: Comma-separated centering values for quantitative\
            variables.
        num_glt: Number of general linear t-tests (GLTs).
        glt_label: Label for each general linear t-test (GLT).
        glt_code: Coding for each general linear t-test (GLT).
        num_glf: Number of general linear F-tests (GLFs).
        glf_label: Label for each general linear F-test (GLF).
        glf_code: Coding for each general linear F-test (GLF).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dMvmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_MVM_METADATA)
    params = v_3d_mvm_params(dbg_args=dbg_args, prefix=prefix, jobs=jobs, mask=mask, bs_vars=bs_vars, ws_vars=ws_vars, q_vars=q_vars, q_var_centers=q_var_centers, num_glt=num_glt, glt_label=glt_label, glt_code=glt_code, num_glf=num_glf, glf_label=glf_label, glf_code=glf_code, data_table=data_table)
    return v_3d_mvm_execute(params, execution)


__all__ = [
    "V3dMvmOutputs",
    "V3dMvmParameters",
    "V_3D_MVM_METADATA",
    "v_3d_mvm",
    "v_3d_mvm_params",
]
