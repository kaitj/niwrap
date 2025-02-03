# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_DTTO_NOISY_DWI_METADATA = Metadata(
    id="0ef5fe03a8b952b27e737adb59a395ac94790601.boutiques",
    name="3dDTtoNoisyDWI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dDttoNoisyDwiParameters = typing.TypedDict('V3dDttoNoisyDwiParameters', {
    "__STYX_TYPE__": typing.Literal["3dDTtoNoisyDWI"],
    "dt_file": InputPathType,
    "grad_file": InputPathType,
    "noise_dwi": float,
    "noise_b0": typing.NotRequired[float | None],
    "prefix": str,
    "mask": typing.NotRequired[InputPathType | None],
    "bval": typing.NotRequired[float | None],
    "s0": typing.NotRequired[float | None],
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
        "3dDTtoNoisyDWI": v_3d_dtto_noisy_dwi_cargs,
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
        "3dDTtoNoisyDWI": v_3d_dtto_noisy_dwi_outputs,
    }
    return vt.get(t)


class V3dDttoNoisyDwiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dtto_noisy_dwi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dwi: OutputPathType
    """Synthetic set of DWI measures with noise. Contains N+1 bricks mimicking
    B0+DWI data."""


def v_3d_dtto_noisy_dwi_params(
    dt_file: InputPathType,
    grad_file: InputPathType,
    noise_dwi: float,
    prefix: str,
    noise_b0: float | None = None,
    mask: InputPathType | None = None,
    bval: float | None = None,
    s0: float | None = None,
) -> V3dDttoNoisyDwiParameters:
    """
    Build parameters.
    
    Args:
        dt_file: Diffusion tensor file with six bricks of DT components ordered\
            in the AFNI manner: Dxx,Dxy,Dyy,Dxz,Dyz,Dzz.
        grad_file: Text file of gradients arranged in three columns. There\
            should be no row of all zeros representing the b=0 line.
        noise_dwi: Fractional value of noise in DWIs. FF = sigma/S0 = 1/SNR0.\
            For example, FF=0.05 corresponds to SNR0=20.
        prefix: Output file name prefix. Will have N+1 bricks when GRADFILE has\
            N rows of gradients.
        noise_b0: Optional fraction of Rician noise in the b=0 reference image.\
            If not provided, FF2=FF.
        mask: Optional mask within which to calculate uncertainty. Data should\
            be masked already otherwise.
        bval: Optional DW factor to use if DT values are scaled to something\
            physical. Default is BB=1.
        s0: Optional reference b=0 signal strength. Default value is SS=1000.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dDTtoNoisyDWI",
        "dt_file": dt_file,
        "grad_file": grad_file,
        "noise_dwi": noise_dwi,
        "prefix": prefix,
    }
    if noise_b0 is not None:
        params["noise_b0"] = noise_b0
    if mask is not None:
        params["mask"] = mask
    if bval is not None:
        params["bval"] = bval
    if s0 is not None:
        params["s0"] = s0
    return params


def v_3d_dtto_noisy_dwi_cargs(
    params: V3dDttoNoisyDwiParameters,
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
    cargs.append("3dDTtoNoisyDWI")
    cargs.append(execution.input_file(params.get("dt_file")))
    cargs.append(execution.input_file(params.get("grad_file")))
    cargs.extend([
        "-noise_DWI",
        str(params.get("noise_dwi"))
    ])
    if params.get("noise_b0") is not None:
        cargs.extend([
            "-noise_B0",
            str(params.get("noise_b0"))
        ])
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("bval") is not None:
        cargs.extend([
            "-bval",
            str(params.get("bval"))
        ])
    if params.get("s0") is not None:
        cargs.extend([
            "-S0",
            str(params.get("s0"))
        ])
    return cargs


def v_3d_dtto_noisy_dwi_outputs(
    params: V3dDttoNoisyDwiParameters,
    execution: Execution,
) -> V3dDttoNoisyDwiOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dDttoNoisyDwiOutputs(
        root=execution.output_file("."),
        output_dwi=execution.output_file(params.get("prefix") + "+orig"),
    )
    return ret


def v_3d_dtto_noisy_dwi_execute(
    params: V3dDttoNoisyDwiParameters,
    execution: Execution,
) -> V3dDttoNoisyDwiOutputs:
    """
    Generate a synthetic set of DWI measures with a given SNR from an AFNI-style DT
    file and a set of gradients. This can be useful for simulations and testing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dDttoNoisyDwiOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3d_dtto_noisy_dwi_cargs(params, execution)
    ret = v_3d_dtto_noisy_dwi_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3d_dtto_noisy_dwi(
    dt_file: InputPathType,
    grad_file: InputPathType,
    noise_dwi: float,
    prefix: str,
    noise_b0: float | None = None,
    mask: InputPathType | None = None,
    bval: float | None = None,
    s0: float | None = None,
    runner: Runner | None = None,
) -> V3dDttoNoisyDwiOutputs:
    """
    Generate a synthetic set of DWI measures with a given SNR from an AFNI-style DT
    file and a set of gradients. This can be useful for simulations and testing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dt_file: Diffusion tensor file with six bricks of DT components ordered\
            in the AFNI manner: Dxx,Dxy,Dyy,Dxz,Dyz,Dzz.
        grad_file: Text file of gradients arranged in three columns. There\
            should be no row of all zeros representing the b=0 line.
        noise_dwi: Fractional value of noise in DWIs. FF = sigma/S0 = 1/SNR0.\
            For example, FF=0.05 corresponds to SNR0=20.
        prefix: Output file name prefix. Will have N+1 bricks when GRADFILE has\
            N rows of gradients.
        noise_b0: Optional fraction of Rician noise in the b=0 reference image.\
            If not provided, FF2=FF.
        mask: Optional mask within which to calculate uncertainty. Data should\
            be masked already otherwise.
        bval: Optional DW factor to use if DT values are scaled to something\
            physical. Default is BB=1.
        s0: Optional reference b=0 signal strength. Default value is SS=1000.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDttoNoisyDwiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DTTO_NOISY_DWI_METADATA)
    params = v_3d_dtto_noisy_dwi_params(dt_file=dt_file, grad_file=grad_file, noise_dwi=noise_dwi, noise_b0=noise_b0, prefix=prefix, mask=mask, bval=bval, s0=s0)
    return v_3d_dtto_noisy_dwi_execute(params, execution)


__all__ = [
    "V3dDttoNoisyDwiOutputs",
    "V_3D_DTTO_NOISY_DWI_METADATA",
    "v_3d_dtto_noisy_dwi",
    "v_3d_dtto_noisy_dwi_params",
]
