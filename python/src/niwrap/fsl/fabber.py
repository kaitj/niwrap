# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_METADATA = Metadata(
    id="7b30d160c8a5a0d761389119c4ba88f3aec8bd00.boutiques",
    name="fabber",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FabberOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    paramnames_file: OutputPathType
    """File containing the names of the model parameters"""
    model_fit_file: OutputPathType
    """The model fit output file"""
    residuals_file: OutputPathType
    """The residuals output file"""
    model_extras_file: OutputPathType
    """The model extras output file"""
    mvn_file: OutputPathType
    """The MVN distributions output file"""
    mean_file: OutputPathType
    """The parameter means output file"""
    std_file: OutputPathType
    """The parameter standard deviations output file"""
    var_file: OutputPathType
    """The parameter variances output file"""
    zstat_file: OutputPathType
    """The parameter Zstats output file"""
    noise_mean_file: OutputPathType
    """The noise means output file"""
    noise_std_file: OutputPathType
    """The noise standard deviations output file"""
    free_energy_file: OutputPathType
    """The free energy output file"""


def fabber(
    runner: Runner | None = None,
) -> FabberOutputs:
    """
    Fabber is a tool for model-based Bayesian analysis of time-series data.
    
    Author: FSL Community
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fabber
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_METADATA)
    cargs = []
    cargs.append("fabber")
    cargs.append("[OPTIONS]")
    ret = FabberOutputs(
        root=execution.output_file("."),
        paramnames_file=execution.output_file("[OUTPUT_DIRECTORY]/paramnames.txt"),
        model_fit_file=execution.output_file("[OUTPUT_DIRECTORY]/model_fit.nii.gz"),
        residuals_file=execution.output_file("[OUTPUT_DIRECTORY]/residuals.nii.gz"),
        model_extras_file=execution.output_file("[OUTPUT_DIRECTORY]/model_extras.nii.gz"),
        mvn_file=execution.output_file("[OUTPUT_DIRECTORY]/mvn.nii.gz"),
        mean_file=execution.output_file("[OUTPUT_DIRECTORY]/mean.nii.gz"),
        std_file=execution.output_file("[OUTPUT_DIRECTORY]/std.nii.gz"),
        var_file=execution.output_file("[OUTPUT_DIRECTORY]/var.nii.gz"),
        zstat_file=execution.output_file("[OUTPUT_DIRECTORY]/zstat.nii.gz"),
        noise_mean_file=execution.output_file("[OUTPUT_DIRECTORY]/noise_mean.nii.gz"),
        noise_std_file=execution.output_file("[OUTPUT_DIRECTORY]/noise_std.nii.gz"),
        free_energy_file=execution.output_file("[OUTPUT_DIRECTORY]/free_energy.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_METADATA",
    "FabberOutputs",
    "fabber",
]