# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ESTIMATE_FIBER_BINGHAMS_METADATA = Metadata(
    id="0cdc134d5bffcca430de60ceed43049ba2d52103.boutiques",
    name="estimate-fiber-binghams",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
EstimateFiberBinghamsParameters = typing.TypedDict('EstimateFiberBinghamsParameters', {
    "__STYX_TYPE__": typing.Literal["estimate-fiber-binghams"],
    "merged_f1samples": InputPathType,
    "merged_th1samples": InputPathType,
    "merged_ph1samples": InputPathType,
    "merged_f2samples": InputPathType,
    "merged_th2samples": InputPathType,
    "merged_ph2samples": InputPathType,
    "merged_f3samples": InputPathType,
    "merged_th3samples": InputPathType,
    "merged_ph3samples": InputPathType,
    "label_volume": InputPathType,
    "cifti_out": str,
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
        "estimate-fiber-binghams": estimate_fiber_binghams_cargs,
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
    vt = {
        "estimate-fiber-binghams": estimate_fiber_binghams_outputs,
    }
    return vt.get(t)


class EstimateFiberBinghamsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `estimate_fiber_binghams(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti fiber distributons file"""


def estimate_fiber_binghams_params(
    merged_f1samples: InputPathType,
    merged_th1samples: InputPathType,
    merged_ph1samples: InputPathType,
    merged_f2samples: InputPathType,
    merged_th2samples: InputPathType,
    merged_ph2samples: InputPathType,
    merged_f3samples: InputPathType,
    merged_th3samples: InputPathType,
    merged_ph3samples: InputPathType,
    label_volume: InputPathType,
    cifti_out: str,
) -> EstimateFiberBinghamsParameters:
    """
    Build parameters.
    
    Args:
        merged_f1samples: fiber 1 strength samples.
        merged_th1samples: fiber 1 theta samples.
        merged_ph1samples: fiber 1 phi samples.
        merged_f2samples: fiber 2 strength samples.
        merged_th2samples: fiber 2 theta samples.
        merged_ph2samples: fiber 2 phi samples.
        merged_f3samples: fiber 3 strength samples.
        merged_th3samples: fiber 3 theta samples.
        merged_ph3samples: fiber 3 phi samples.
        label_volume: volume of cifti structure labels.
        cifti_out: output cifti fiber distributons file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "estimate-fiber-binghams",
        "merged_f1samples": merged_f1samples,
        "merged_th1samples": merged_th1samples,
        "merged_ph1samples": merged_ph1samples,
        "merged_f2samples": merged_f2samples,
        "merged_th2samples": merged_th2samples,
        "merged_ph2samples": merged_ph2samples,
        "merged_f3samples": merged_f3samples,
        "merged_th3samples": merged_th3samples,
        "merged_ph3samples": merged_ph3samples,
        "label_volume": label_volume,
        "cifti_out": cifti_out,
    }
    return params


def estimate_fiber_binghams_cargs(
    params: EstimateFiberBinghamsParameters,
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
    cargs.append("wb_command")
    cargs.append("-estimate-fiber-binghams")
    cargs.append(execution.input_file(params.get("merged_f1samples")))
    cargs.append(execution.input_file(params.get("merged_th1samples")))
    cargs.append(execution.input_file(params.get("merged_ph1samples")))
    cargs.append(execution.input_file(params.get("merged_f2samples")))
    cargs.append(execution.input_file(params.get("merged_th2samples")))
    cargs.append(execution.input_file(params.get("merged_ph2samples")))
    cargs.append(execution.input_file(params.get("merged_f3samples")))
    cargs.append(execution.input_file(params.get("merged_th3samples")))
    cargs.append(execution.input_file(params.get("merged_ph3samples")))
    cargs.append(execution.input_file(params.get("label_volume")))
    cargs.append(params.get("cifti_out"))
    return cargs


def estimate_fiber_binghams_outputs(
    params: EstimateFiberBinghamsParameters,
    execution: Execution,
) -> EstimateFiberBinghamsOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = EstimateFiberBinghamsOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(params.get("cifti_out")),
    )
    return ret


def estimate_fiber_binghams_execute(
    params: EstimateFiberBinghamsParameters,
    execution: Execution,
) -> EstimateFiberBinghamsOutputs:
    """
    Estimate fiber orientation distributions from bedpostx samples.
    
    This command does an estimation of a bingham distribution for each fiber
    orientation in each voxel which is labeled a structure identifier. These
    labelings come from the <label-volume> argument, which must have labels that
    match the following strings:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `EstimateFiberBinghamsOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = estimate_fiber_binghams_cargs(params, execution)
    ret = estimate_fiber_binghams_outputs(params, execution)
    execution.run(cargs)
    return ret


def estimate_fiber_binghams(
    merged_f1samples: InputPathType,
    merged_th1samples: InputPathType,
    merged_ph1samples: InputPathType,
    merged_f2samples: InputPathType,
    merged_th2samples: InputPathType,
    merged_ph2samples: InputPathType,
    merged_f3samples: InputPathType,
    merged_th3samples: InputPathType,
    merged_ph3samples: InputPathType,
    label_volume: InputPathType,
    cifti_out: str,
    runner: Runner | None = None,
) -> EstimateFiberBinghamsOutputs:
    """
    Estimate fiber orientation distributions from bedpostx samples.
    
    This command does an estimation of a bingham distribution for each fiber
    orientation in each voxel which is labeled a structure identifier. These
    labelings come from the <label-volume> argument, which must have labels that
    match the following strings:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        merged_f1samples: fiber 1 strength samples.
        merged_th1samples: fiber 1 theta samples.
        merged_ph1samples: fiber 1 phi samples.
        merged_f2samples: fiber 2 strength samples.
        merged_th2samples: fiber 2 theta samples.
        merged_ph2samples: fiber 2 phi samples.
        merged_f3samples: fiber 3 strength samples.
        merged_th3samples: fiber 3 theta samples.
        merged_ph3samples: fiber 3 phi samples.
        label_volume: volume of cifti structure labels.
        cifti_out: output cifti fiber distributons file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EstimateFiberBinghamsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ESTIMATE_FIBER_BINGHAMS_METADATA)
    params = estimate_fiber_binghams_params(merged_f1samples=merged_f1samples, merged_th1samples=merged_th1samples, merged_ph1samples=merged_ph1samples, merged_f2samples=merged_f2samples, merged_th2samples=merged_th2samples, merged_ph2samples=merged_ph2samples, merged_f3samples=merged_f3samples, merged_th3samples=merged_th3samples, merged_ph3samples=merged_ph3samples, label_volume=label_volume, cifti_out=cifti_out)
    return estimate_fiber_binghams_execute(params, execution)


__all__ = [
    "ESTIMATE_FIBER_BINGHAMS_METADATA",
    "EstimateFiberBinghamsOutputs",
    "estimate_fiber_binghams",
    "estimate_fiber_binghams_params",
]
