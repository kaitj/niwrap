# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ICA_AROMA_METADATA = Metadata(
    id="068247c1b91b6921a39d631270d137a1e79fb52f.boutiques",
    name="ICA_AROMA",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class IcaAromaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ica_aroma(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    aggr_denoised_file: OutputPathType
    """If generated: aggressively denoised volume."""
    nonaggr_denoised_file: OutputPathType
    """If generated: non aggressively denoised volume."""
    out_dir_outfile: OutputPathType
    """file or string representing an existing directory. Directory contains (in
    addition to the denoised files): melodic.ica + classified_motion_components
    + classification_overview + feature_scores + melodic_ic_mni)."""


def ica_aroma(
    feat_dir: InputPathType,
    in_file: InputPathType,
    motion_parameters: InputPathType,
    out_dir: InputPathType,
    tr: float | None = None,
    denoise_type: typing.Literal["nonaggr", "aggr", "both", "no"] = "nonaggr",
    dim: int | None = None,
    fnirt_warp_file: InputPathType | None = None,
    mask: InputPathType | None = None,
    mat_file: InputPathType | None = None,
    melodic_dir: InputPathType | None = None,
    runner: Runner | None = None,
) -> IcaAromaOutputs:
    """
    
    Interface for the ICA_AROMA.py script.
    ICA-AROMA (i.e. 'ICA-based Automatic Removal Of Motion Artifacts') concerns
    a data-driven method to identify and remove motion-related independent
    components from fMRI data. To that end it exploits a small, but robust set
    of theoretically motivated features, preventing the need for classifier
    re-training and therefore providing direct and easy applicability.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        feat_dir: file or string representing an existing directory. If a feat\
            directory exists and temporal filtering has not been run yet, ica_aroma\
            can use the files in this directory.
        in_file: Volume to be denoised.
        motion_parameters: Motion parameters file.
        out_dir: file or string representing a directory. Output directory.
        tr: Tr in seconds. if this is not specified the tr will be extracted\
            from the header of the fmri nifti file.
        denoise_type: 'nonaggr' or 'aggr' or 'both' or 'no'. Type of denoising\
            strategy:-no: only classification, no denoising-nonaggr (default):\
            non-aggresssive denoising, i.e. partial component regression-aggr:\
            aggressive denoising, i.e. full component regression-both: both\
            aggressive and non-aggressive denoising (two outputs).
        dim: Dimensionality reduction when running melodic (default is\
            automatic estimation).
        fnirt_warp_file: File name of the warp-file describing the non-linear\
            registration (e.g. fsl fnirt) of the structural data to mni152 space\
            (.nii.gz).
        mask: Path/name volume mask.
        mat_file: Path/name of the mat-file describing the affine registration\
            (e.g. fsl flirt) of the functional data to structural space (.mat\
            file).
        melodic_dir: file or string representing an existing directory. Path to\
            melodic directory if melodic has already been run.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `IcaAromaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ICA_AROMA_METADATA)
    cargs = []
    cargs.append("ICA_AROMA")
    if tr is not None:
        cargs.extend([
            "-tr",
            str(tr)
        ])
    cargs.extend([
        "-den",
        denoise_type
    ])
    if dim is not None:
        cargs.extend([
            "-dim",
            str(dim)
        ])
    cargs.extend([
        "-feat",
        execution.input_file(feat_dir)
    ])
    if fnirt_warp_file is not None:
        cargs.extend([
            "-warp",
            execution.input_file(fnirt_warp_file)
        ])
    cargs.extend([
        "-i",
        execution.input_file(in_file)
    ])
    if mask is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask)
        ])
    if mat_file is not None:
        cargs.extend([
            "-affmat",
            execution.input_file(mat_file)
        ])
    if melodic_dir is not None:
        cargs.extend([
            "-meldir",
            execution.input_file(melodic_dir)
        ])
    cargs.extend([
        "-mc",
        execution.input_file(motion_parameters)
    ])
    cargs.extend([
        "-o",
        execution.input_file(out_dir)
    ])
    ret = IcaAromaOutputs(
        root=execution.output_file("."),
        aggr_denoised_file=execution.output_file("out/denoised_func_data_aggr.nii.gz"),
        nonaggr_denoised_file=execution.output_file("out/denoised_func_data_nonaggr.nii.gz"),
        out_dir_outfile=execution.output_file("out"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ICA_AROMA_METADATA",
    "IcaAromaOutputs",
    "ica_aroma",
]
