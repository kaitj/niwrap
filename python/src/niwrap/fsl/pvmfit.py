# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PVMFIT_METADATA = Metadata(
    id="b8d0ef967be4d8b5cbc7c5cc5275de2fe4e76ca6.boutiques",
    name="pvmfit",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class PvmfitOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pvmfit(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """Main output file"""
    bic_file: OutputPathType | None
    """Optional: Saved BIC (Bayesian Information Criterion) for certain
    models"""


def pvmfit(
    data_file: InputPathType,
    mask_file: InputPathType,
    bvec_file: InputPathType,
    bval_file: InputPathType,
    output_basename: str | None = "pvm",
    number_of_fibres: float | None = 1,
    model_type: int | None = None,
    fit_all_models: bool = False,
    constrained_nonlinear: bool = False,
    constrained_nonlinear_f: bool = False,
    grid_search: bool = False,
    include_noise_floor: bool = False,
    save_bic: bool = False,
    verbose: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> PvmfitOutputs:
    """
    Fits diffusion models to multishell DWI data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        data_file: Data file.
        mask_file: Mask file.
        bvec_file: B vectors file.
        bval_file: B values file.
        output_basename: Output basename - default='pvm'.
        number_of_fibres: Number of fibres to fit - default=1.
        model_type: Model type: 1 for Ball-Sticks (single-shell), 2 for\
            Ball-Sticks (multi-shells), 4 for Ball-Binghams.
        fit_all_models: Fit all models from 1 up to N fibres and choose the\
            best using BIC.
        constrained_nonlinear: Model1: Apply constrained nonlinear optimization\
            on the diffusivity, volume fractions and their sum.
        constrained_nonlinear_f: Model1: Apply constrained nonlinear\
            optimization on the diffusivity, volume fractions and their sum. Return\
            n fanning angle estimates, using the Hessian of the cost function.
        grid_search: Use grid search (on the fanning eigenvalues). Default=off.
        include_noise_floor: Include noise floor parameter in the model.
        save_bic: Save BIC for certain models.
        verbose: Switch on diagnostic messages.
        help_: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PvmfitOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PVMFIT_METADATA)
    cargs = []
    cargs.append("pvmfit")
    cargs.append("-k")
    cargs.append(execution.input_file(data_file))
    cargs.append("-m")
    cargs.append(execution.input_file(mask_file))
    cargs.append("-r")
    cargs.append(execution.input_file(bvec_file))
    cargs.append("-b")
    cargs.append(execution.input_file(bval_file))
    if output_basename is not None:
        cargs.extend([
            "-o",
            output_basename
        ])
    if number_of_fibres is not None:
        cargs.extend([
            "-n",
            str(number_of_fibres)
        ])
    if model_type is not None:
        cargs.extend([
            "--model",
            str(model_type)
        ])
    if fit_all_models:
        cargs.append("--all")
    if constrained_nonlinear:
        cargs.append("--cnonlinear")
    if constrained_nonlinear_f:
        cargs.append("--cnonlinear_F")
    if grid_search:
        cargs.append("--gridsearch")
    if include_noise_floor:
        cargs.append("--f0")
    if save_bic:
        cargs.append("--BIC")
    if verbose:
        cargs.append("-V")
    if help_:
        cargs.append("-h")
    ret = PvmfitOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_basename + ".nii.gz") if (output_basename is not None) else None,
        bic_file=execution.output_file(output_basename + "_BIC.nii.gz") if (output_basename is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PVMFIT_METADATA",
    "PvmfitOutputs",
    "pvmfit",
]
