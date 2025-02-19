# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SWI_PREPROCESS_METADATA = Metadata(
    id="9c092f99975ad21400c19882fe546f899bd6d1ce.boutiques",
    name="swi_preprocess",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
SwiPreprocessParameters = typing.TypedDict('SwiPreprocessParameters', {
    "__STYX_TYPE__": typing.Literal["swi_preprocess"],
    "scanner": typing.Literal["ge", "siemens", "philips"],
    "ge_file": typing.NotRequired[InputPathType | None],
    "philips_file": typing.NotRequired[InputPathType | None],
    "siemens_magnitude": typing.NotRequired[InputPathType | None],
    "siemens_phase": typing.NotRequired[InputPathType | None],
    "out_magnitude": str,
    "out_phase": str,
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
        "swi_preprocess": swi_preprocess_cargs,
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
        "swi_preprocess": swi_preprocess_outputs,
    }.get(t)


class SwiPreprocessOutputs(typing.NamedTuple):
    """
    Output object returned when calling `swi_preprocess(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_magnitude_file: OutputPathType
    """Output magnitude file in NIfTI format."""
    output_phase_file: OutputPathType
    """Output phase file in NIfTI format."""


def swi_preprocess_params(
    scanner: typing.Literal["ge", "siemens", "philips"],
    out_magnitude: str,
    out_phase: str,
    ge_file: InputPathType | None = None,
    philips_file: InputPathType | None = None,
    siemens_magnitude: InputPathType | None = None,
    siemens_phase: InputPathType | None = None,
) -> SwiPreprocessParameters:
    """
    Build parameters.
    
    Args:
        scanner: Name of the scanner (one of ge, siemens or philips).
        out_magnitude: Name of the output magnitude file after preprocessing.\
            Ensure it has a .nii suffix.
        out_phase: Name of the output phase file after preprocessing. Ensure it\
            has a .nii suffix.
        ge_file: Name of the input GE file (only compatible with --scanner ge\
            option).
        philips_file: Name of the input Philips file (only compatible with\
            --scanner philips option).
        siemens_magnitude: Name of the input Siemens magnitude file (only\
            compatible with --scanner siemens option).
        siemens_phase: Name of the input Siemens phase file (only compatible\
            with --scanner siemens option).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "swi_preprocess",
        "scanner": scanner,
        "out_magnitude": out_magnitude,
        "out_phase": out_phase,
    }
    if ge_file is not None:
        params["ge_file"] = ge_file
    if philips_file is not None:
        params["philips_file"] = philips_file
    if siemens_magnitude is not None:
        params["siemens_magnitude"] = siemens_magnitude
    if siemens_phase is not None:
        params["siemens_phase"] = siemens_phase
    return params


def swi_preprocess_cargs(
    params: SwiPreprocessParameters,
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
    cargs.append("swi_preprocess")
    cargs.extend([
        "--scanner",
        params.get("scanner")
    ])
    if params.get("ge_file") is not None:
        cargs.extend([
            "--ge_file",
            execution.input_file(params.get("ge_file"))
        ])
    if params.get("philips_file") is not None:
        cargs.extend([
            "--philips_file",
            execution.input_file(params.get("philips_file"))
        ])
    if params.get("siemens_magnitude") is not None:
        cargs.extend([
            "--siemens_mag",
            execution.input_file(params.get("siemens_magnitude"))
        ])
    if params.get("siemens_phase") is not None:
        cargs.extend([
            "--siemens_phase",
            execution.input_file(params.get("siemens_phase"))
        ])
    cargs.extend([
        "--out_magnitude",
        params.get("out_magnitude")
    ])
    cargs.extend([
        "--out_phase",
        params.get("out_phase")
    ])
    return cargs


def swi_preprocess_outputs(
    params: SwiPreprocessParameters,
    execution: Execution,
) -> SwiPreprocessOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SwiPreprocessOutputs(
        root=execution.output_file("."),
        output_magnitude_file=execution.output_file(params.get("out_magnitude")),
        output_phase_file=execution.output_file(params.get("out_phase")),
    )
    return ret


def swi_preprocess_execute(
    params: SwiPreprocessParameters,
    execution: Execution,
) -> SwiPreprocessOutputs:
    """
    Pre-process the Susceptibility-weighted images and write out nifti files for
    feeding into PRELUDE (Phase Unwrapping Library of FSL).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SwiPreprocessOutputs`).
    """
    params = execution.params(params)
    cargs = swi_preprocess_cargs(params, execution)
    ret = swi_preprocess_outputs(params, execution)
    execution.run(cargs)
    return ret


def swi_preprocess(
    scanner: typing.Literal["ge", "siemens", "philips"],
    out_magnitude: str,
    out_phase: str,
    ge_file: InputPathType | None = None,
    philips_file: InputPathType | None = None,
    siemens_magnitude: InputPathType | None = None,
    siemens_phase: InputPathType | None = None,
    runner: Runner | None = None,
) -> SwiPreprocessOutputs:
    """
    Pre-process the Susceptibility-weighted images and write out nifti files for
    feeding into PRELUDE (Phase Unwrapping Library of FSL).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        scanner: Name of the scanner (one of ge, siemens or philips).
        out_magnitude: Name of the output magnitude file after preprocessing.\
            Ensure it has a .nii suffix.
        out_phase: Name of the output phase file after preprocessing. Ensure it\
            has a .nii suffix.
        ge_file: Name of the input GE file (only compatible with --scanner ge\
            option).
        philips_file: Name of the input Philips file (only compatible with\
            --scanner philips option).
        siemens_magnitude: Name of the input Siemens magnitude file (only\
            compatible with --scanner siemens option).
        siemens_phase: Name of the input Siemens phase file (only compatible\
            with --scanner siemens option).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SwiPreprocessOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SWI_PREPROCESS_METADATA)
    params = swi_preprocess_params(scanner=scanner, ge_file=ge_file, philips_file=philips_file, siemens_magnitude=siemens_magnitude, siemens_phase=siemens_phase, out_magnitude=out_magnitude, out_phase=out_phase)
    return swi_preprocess_execute(params, execution)


__all__ = [
    "SWI_PREPROCESS_METADATA",
    "SwiPreprocessOutputs",
    "SwiPreprocessParameters",
    "swi_preprocess",
    "swi_preprocess_params",
]
