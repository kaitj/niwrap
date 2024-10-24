# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_MVM_METADATA = Metadata(
    id="41e1dd222d8dc8d40a7419dbf4444dad608de47a.boutiques",
    name="3dMVM",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


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
    cargs = []
    cargs.append("3dMVM")
    if dbg_args is not None:
        cargs.append(dbg_args)
    cargs.append("-prefix")
    cargs.append(prefix)
    cargs.append("-jobs")
    if jobs is not None:
        cargs.append(str(jobs))
    cargs.append("-mask")
    if mask is not None:
        cargs.append(execution.input_file(mask))
    cargs.append("-bsVars")
    cargs.append(bs_vars)
    cargs.append("-wsVars")
    if ws_vars is not None:
        cargs.append(ws_vars)
    cargs.append("-qVars")
    if q_vars is not None:
        cargs.append(q_vars)
    cargs.append("-qVarCenters")
    if q_var_centers is not None:
        cargs.append(q_var_centers)
    cargs.append("-num_glt")
    if num_glt is not None:
        cargs.append(str(num_glt))
    cargs.append("-gltLabel")
    if glt_label is not None:
        cargs.append(glt_label)
    cargs.append("-gltCode")
    if glt_code is not None:
        cargs.append(glt_code)
    cargs.append("-num_glf")
    if num_glf is not None:
        cargs.append(str(num_glf))
    cargs.append("-glfLabel")
    if glf_label is not None:
        cargs.append(glf_label)
    cargs.append("-glfCode")
    if glf_code is not None:
        cargs.append(glf_code)
    cargs.append("-dataTable")
    cargs.append(data_table)
    ret = V3dMvmOutputs(
        root=execution.output_file("."),
        outfile_head=execution.output_file(prefix + "+tlrc.HEAD"),
        outfile_brik=execution.output_file(prefix + "+tlrc.BRIK"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dMvmOutputs",
    "V_3D_MVM_METADATA",
    "v_3d_mvm",
]
