# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DWIGRADCHECK_METADATA = Metadata(
    id="640f8310ac9efa10baa6829f1058ce0830fa1f11.boutiques",
    name="dwigradcheck",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DwigradcheckFslgrad:
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


class DwigradcheckExportGradFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `DwigradcheckExportGradFsl | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    bvecs_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""


@dataclasses.dataclass
class DwigradcheckExportGradFsl:
    """
    export the diffusion-weighted gradient table to files in FSL (bvecs / bvals)
    format.
    """
    bvecs_path: str
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: str
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    
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
        cargs.append("-export_grad_fsl")
        cargs.append(self.bvecs_path)
        cargs.append(self.bvals_path)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> DwigradcheckExportGradFslOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `DwigradcheckExportGradFslOutputs`).
        """
        ret = DwigradcheckExportGradFslOutputs(
            root=execution.output_file("."),
            bvecs_path=execution.output_file(self.bvecs_path),
            bvals_path=execution.output_file(self.bvals_path),
        )
        return ret


class DwigradcheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwigradcheck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    export_grad_mrtrix: OutputPathType | None
    """export the diffusion-weighted gradient table to file in MRtrix format """
    export_grad_fsl: OutputPathType | None
    """export the diffusion-weighted gradient table to file in FSL format """
    export_grad_fsl_: DwigradcheckExportGradFslOutputs | None
    """Outputs from `DwigradcheckExportGradFsl`."""


def dwigradcheck(
    input_image: InputPathType,
    grad: InputPathType | None = None,
    fslgrad: DwigradcheckFslgrad | None = None,
    mask_image: InputPathType | None = None,
    number: int | None = None,
    export_grad_mrtrix: str | None = None,
    export_grad_fsl: DwigradcheckExportGradFsl | None = None,
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
    runner: Runner | None = None,
) -> DwigradcheckOutputs:
    """
    Check the orientation of the diffusion gradient table.
    
    Author: Ben Jeurrisen
    
    URL: http://www.mrtrix.org/
    
    Args:
        input_image: The input DWI series to be checked.
        grad: Provide the diffusion gradient table in MRtrix format.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        mask_image: Provide a brain mask image.
        number: Set the number of tracks to generate for each test.
        export_grad_mrtrix: export the diffusion-weighted gradient table to\
            file in MRtrix format.
        export_grad_fsl: export the diffusion-weighted gradient table to files\
            in FSL (bvecs / bvals) format.
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
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DwigradcheckOutputs`).
    """
    if continue_scratch_dir is not None and (len(continue_scratch_dir) != 2): 
        raise ValueError(f"Length of 'continue_scratch_dir' must be 2 but was {len(continue_scratch_dir)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWIGRADCHECK_METADATA)
    cargs = []
    cargs.append("dwigradcorrect")
    cargs.append(execution.input_file(input_image))
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
    if number is not None:
        cargs.extend([
            "-number",
            str(number)
        ])
    if export_grad_mrtrix is not None:
        cargs.extend([
            "-export_grad_mrtrix",
            export_grad_mrtrix
        ])
    if export_grad_fsl is not None:
        cargs.extend(export_grad_fsl.run(execution))
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
    ret = DwigradcheckOutputs(
        root=execution.output_file("."),
        export_grad_mrtrix=execution.output_file(export_grad_mrtrix) if (export_grad_mrtrix is not None) else None,
        export_grad_fsl=execution.output_file(export_grad_mrtrix) if (export_grad_mrtrix is not None) else None,
        export_grad_fsl_=export_grad_fsl.outputs(execution) if export_grad_fsl else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DWIGRADCHECK_METADATA",
    "DwigradcheckExportGradFsl",
    "DwigradcheckExportGradFslOutputs",
    "DwigradcheckFslgrad",
    "DwigradcheckOutputs",
    "dwigradcheck",
]
