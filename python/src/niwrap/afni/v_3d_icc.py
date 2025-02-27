# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3D_ICC_METADATA = Metadata(
    id="6b7ec5c6de013c42d47420ebf12a564c200ff8a3.boutiques",
    name="3dICC",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


V3dIccParameters = typing.TypedDict('V3dIccParameters', {
    "__STYX_TYPE__": typing.Literal["3dICC"],
    "model": str,
    "prefix": str,
    "mask": typing.NotRequired[InputPathType | None],
    "data_table": str,
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
        "3dICC": v_3d_icc_cargs,
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
        "3dICC": v_3d_icc_outputs,
    }.get(t)


class V3dIccOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_icc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Name of the output file"""


def v_3d_icc_params(
    model: str,
    prefix: str,
    data_table: str,
    mask: InputPathType | None = None,
) -> V3dIccParameters:
    """
    Build parameters.
    
    Args:
        model: Model structure for all the variables. The expression FORMULA\
            with more than one variable has to be surrounded within quotes.\
            Variable names should be consistent with the ones used in the header of\
            -dataTable.
        prefix: Name of output file. For AFNI format, provide prefix only, with\
            no view+suffix needed. Filename for NIfTI format should have .nii\
            attached, while file name for surface data is expected to end with\
            .niml.dset.
        data_table: List the data structure with a header as the first line.\
            The first column is reserved with label 'Subj', and the last is\
            reserved for 'InputFile'.
        mask: Path to mask file. Only process voxels inside this mask.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dICC",
        "model": model,
        "prefix": prefix,
        "data_table": data_table,
    }
    if mask is not None:
        params["mask"] = mask
    return params


def v_3d_icc_cargs(
    params: V3dIccParameters,
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
    cargs.append("3dICC")
    cargs.append(params.get("model"))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    cargs.extend([
        "-dataTable",
        params.get("data_table")
    ])
    cargs.append("[OPTIONS]")
    return cargs


def v_3d_icc_outputs(
    params: V3dIccParameters,
    execution: Execution,
) -> V3dIccOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dIccOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix")),
    )
    return ret


def v_3d_icc_execute(
    params: V3dIccParameters,
    execution: Execution,
) -> V3dIccOutputs:
    """
    AFNI Program for IntraClass Correlatin (ICC) Analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dIccOutputs`).
    """
    params = execution.params(params)
    cargs = v_3d_icc_cargs(params, execution)
    ret = v_3d_icc_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_icc(
    model: str,
    prefix: str,
    data_table: str,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dIccOutputs:
    """
    AFNI Program for IntraClass Correlatin (ICC) Analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        model: Model structure for all the variables. The expression FORMULA\
            with more than one variable has to be surrounded within quotes.\
            Variable names should be consistent with the ones used in the header of\
            -dataTable.
        prefix: Name of output file. For AFNI format, provide prefix only, with\
            no view+suffix needed. Filename for NIfTI format should have .nii\
            attached, while file name for surface data is expected to end with\
            .niml.dset.
        data_table: List the data structure with a header as the first line.\
            The first column is reserved with label 'Subj', and the last is\
            reserved for 'InputFile'.
        mask: Path to mask file. Only process voxels inside this mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dIccOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ICC_METADATA)
    params = v_3d_icc_params(
        model=model,
        prefix=prefix,
        mask=mask,
        data_table=data_table,
    )
    return v_3d_icc_execute(params, execution)


__all__ = [
    "V3dIccOutputs",
    "V3dIccParameters",
    "V_3D_ICC_METADATA",
    "v_3d_icc",
    "v_3d_icc_params",
]
