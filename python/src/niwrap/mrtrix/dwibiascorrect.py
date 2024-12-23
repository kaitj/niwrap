# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DWIBIASCORRECT_METADATA = Metadata(
    id="e83d9f4b1c64834e7ce4b8084fa8aefaad7cc322.boutiques",
    name="dwibiascorrect",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DwibiascorrectFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used.
    """
    bvecs: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    bvals: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-fslgrad")
        cargs.append(execution.input_file(self.bvecs))
        cargs.append(execution.input_file(self.bvals))
        return cargs


class DwibiascorrectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwibiascorrect(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """File containing the corrected image series"""
    bias_image_file: OutputPathType | None
    """File containing the estimated bias field"""


def dwibiascorrect(
    algorithm: str,
    input_image: InputPathType,
    output_image: str,
    grad: InputPathType | None = None,
    fslgrad: DwibiascorrectFslgrad | None = None,
    mask_image: InputPathType | None = None,
    bias_image: InputPathType | None = None,
    nocleanup: bool = False,
    scratch_dir: InputPathType | None = None,
    continue_scratch_dir: list[InputPathType] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: float | None = None,
    config: list[str] | None = None,
    help_: bool = False,
    version: bool = False,
    ants_b: str | None = None,
    ants_c: str | None = None,
    ants_s: str | None = None,
    runner: Runner | None = None,
) -> DwibiascorrectOutputs:
    """
    Perform B1 field inhomogeneity correction for a DWI volume series using either
    ANTs or FSL.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        algorithm: Select the algorithm to be used for bias correction. Options\
            are: ants, fsl.
        input_image: The input image series to be corrected.
        output_image: The output corrected image series.
        grad: Provide the diffusion gradient table in MRtrix format.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        mask_image: Manually provide a mask image for bias field estimation.
        bias_image: Output the estimated bias field.
        nocleanup: Do not delete intermediate files during script execution,\
            and do not delete scratch directory at script completion.
        scratch_dir: Manually specify the path in which to generate the scratch\
            directory.
        continue_scratch_dir: Continue the script from a previous execution;\
            must provide the scratch directory path.
        info: Display information messages.
        quiet: Do not display information messages or progress status.
        debug: Display debugging messages.
        force: Force overwrite of output files.
        nthreads: Use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: Temporarily set the value of an MRtrix config file entry.
        help_: Display help information and exit.
        version: Display version information and exit.
        ants_b: N4BiasFieldCorrection option -b (initial mesh resolution in mm,\
            spline order).
        ants_c: N4BiasFieldCorrection option -c (number of iterations,\
            convergence threshold).
        ants_s: N4BiasFieldCorrection option -s (shrink-factor applied to\
            spatial dimensions).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DwibiascorrectOutputs`).
    """
    if continue_scratch_dir is not None and (len(continue_scratch_dir) != 2): 
        raise ValueError(f"Length of 'continue_scratch_dir' must be 2 but was {len(continue_scratch_dir)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWIBIASCORRECT_METADATA)
    cargs = []
    cargs.append("dwibiascorrect")
    cargs.append(algorithm)
    cargs.append(execution.input_file(input_image))
    cargs.append(output_image)
    if grad is not None:
        cargs.extend([
            "-grad",
            execution.input_file(grad)
        ])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if mask_image is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask_image)
        ])
    if bias_image is not None:
        cargs.extend([
            "-bias",
            execution.input_file(bias_image)
        ])
    if nocleanup:
        cargs.append("-nocleanup")
    if scratch_dir is not None:
        cargs.extend([
            "-scratch",
            execution.input_file(scratch_dir)
        ])
    if continue_scratch_dir is not None:
        cargs.extend([
            "-continue",
            *[execution.input_file(f) for f in continue_scratch_dir]
        ])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([
            "-config",
            *config
        ])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    if ants_b is not None:
        cargs.extend([
            "-ants.b",
            ants_b
        ])
    if ants_c is not None:
        cargs.extend([
            "-ants.c",
            ants_c
        ])
    if ants_s is not None:
        cargs.extend([
            "-ants.s",
            ants_s
        ])
    ret = DwibiascorrectOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(output_image),
        bias_image_file=execution.output_file(pathlib.Path(bias_image).name) if (bias_image is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DWIBIASCORRECT_METADATA",
    "DwibiascorrectFslgrad",
    "DwibiascorrectOutputs",
    "dwibiascorrect",
]
