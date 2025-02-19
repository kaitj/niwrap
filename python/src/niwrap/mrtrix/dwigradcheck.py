# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DWIGRADCHECK_METADATA = Metadata(
    id="bb74671ccd6fa59a51829fa34812108f525873cb.boutiques",
    name="dwigradcheck",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
DwigradcheckFslgradParameters = typing.TypedDict('DwigradcheckFslgradParameters', {
    "__STYX_TYPE__": typing.Literal["fslgrad"],
    "bvecs": InputPathType,
    "bvals": InputPathType,
})
DwigradcheckExportGradFslParameters = typing.TypedDict('DwigradcheckExportGradFslParameters', {
    "__STYX_TYPE__": typing.Literal["export_grad_fsl"],
    "bvecs_path": str,
    "bvals_path": str,
})
DwigradcheckParameters = typing.TypedDict('DwigradcheckParameters', {
    "__STYX_TYPE__": typing.Literal["dwigradcheck"],
    "input_image": InputPathType,
    "grad": typing.NotRequired[InputPathType | None],
    "fslgrad": typing.NotRequired[DwigradcheckFslgradParameters | None],
    "mask_image": typing.NotRequired[InputPathType | None],
    "number": typing.NotRequired[int | None],
    "export_grad_mrtrix": typing.NotRequired[str | None],
    "export_grad_fsl": typing.NotRequired[DwigradcheckExportGradFslParameters | None],
    "nocleanup": bool,
    "scratch_dir": typing.NotRequired[InputPathType | None],
    "continue_scratch_dir": typing.NotRequired[list[InputPathType] | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[float | None],
    "config": typing.NotRequired[list[str] | None],
    "help": bool,
    "version": bool,
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
        "dwigradcheck": dwigradcheck_cargs,
        "fslgrad": dwigradcheck_fslgrad_cargs,
        "export_grad_fsl": dwigradcheck_export_grad_fsl_cargs,
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
        "dwigradcheck": dwigradcheck_outputs,
        "export_grad_fsl": dwigradcheck_export_grad_fsl_outputs,
    }.get(t)


def dwigradcheck_fslgrad_params(
    bvecs: InputPathType,
    bvals: InputPathType,
) -> DwigradcheckFslgradParameters:
    """
    Build parameters.
    
    Args:
        bvecs: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        bvals: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslgrad",
        "bvecs": bvecs,
        "bvals": bvals,
    }
    return params


def dwigradcheck_fslgrad_cargs(
    params: DwigradcheckFslgradParameters,
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
    cargs.append("-fslgrad")
    cargs.append(execution.input_file(params.get("bvecs")))
    cargs.append(execution.input_file(params.get("bvals")))
    return cargs


class DwigradcheckExportGradFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `DwigradcheckExportGradFslParameters | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    bvecs_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""


def dwigradcheck_export_grad_fsl_params(
    bvecs_path: str,
    bvals_path: str,
) -> DwigradcheckExportGradFslParameters:
    """
    Build parameters.
    
    Args:
        bvecs_path: export the diffusion-weighted gradient table to files in\
            FSL (bvecs / bvals) format.
        bvals_path: export the diffusion-weighted gradient table to files in\
            FSL (bvecs / bvals) format.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "export_grad_fsl",
        "bvecs_path": bvecs_path,
        "bvals_path": bvals_path,
    }
    return params


def dwigradcheck_export_grad_fsl_cargs(
    params: DwigradcheckExportGradFslParameters,
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
    cargs.append("-export_grad_fsl")
    cargs.append(params.get("bvecs_path"))
    cargs.append(params.get("bvals_path"))
    return cargs


def dwigradcheck_export_grad_fsl_outputs(
    params: DwigradcheckExportGradFslParameters,
    execution: Execution,
) -> DwigradcheckExportGradFslOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DwigradcheckExportGradFslOutputs(
        root=execution.output_file("."),
        bvecs_path=execution.output_file(params.get("bvecs_path")),
        bvals_path=execution.output_file(params.get("bvals_path")),
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
    """Outputs from `dwigradcheck_export_grad_fsl_outputs`."""


def dwigradcheck_params(
    input_image: InputPathType,
    grad: InputPathType | None = None,
    fslgrad: DwigradcheckFslgradParameters | None = None,
    mask_image: InputPathType | None = None,
    number: int | None = None,
    export_grad_mrtrix: str | None = None,
    export_grad_fsl: DwigradcheckExportGradFslParameters | None = None,
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
) -> DwigradcheckParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dwigradcheck",
        "input_image": input_image,
        "nocleanup": nocleanup,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
    }
    if grad is not None:
        params["grad"] = grad
    if fslgrad is not None:
        params["fslgrad"] = fslgrad
    if mask_image is not None:
        params["mask_image"] = mask_image
    if number is not None:
        params["number"] = number
    if export_grad_mrtrix is not None:
        params["export_grad_mrtrix"] = export_grad_mrtrix
    if export_grad_fsl is not None:
        params["export_grad_fsl"] = export_grad_fsl
    if scratch_dir is not None:
        params["scratch_dir"] = scratch_dir
    if continue_scratch_dir is not None:
        params["continue_scratch_dir"] = continue_scratch_dir
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dwigradcheck_cargs(
    params: DwigradcheckParameters,
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
    cargs.append("dwigradcheck")
    cargs.append(execution.input_file(params.get("input_image")))
    if params.get("grad") is not None:
        cargs.extend([
            "-grad",
            execution.input_file(params.get("grad"))
        ])
    if params.get("fslgrad") is not None:
        cargs.extend(dyn_cargs(params.get("fslgrad")["__STYXTYPE__"])(params.get("fslgrad"), execution))
    if params.get("mask_image") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask_image"))
        ])
    if params.get("number") is not None:
        cargs.extend([
            "-number",
            str(params.get("number"))
        ])
    if params.get("export_grad_mrtrix") is not None:
        cargs.extend([
            "-export_grad_mrtrix",
            params.get("export_grad_mrtrix")
        ])
    if params.get("export_grad_fsl") is not None:
        cargs.extend(dyn_cargs(params.get("export_grad_fsl")["__STYXTYPE__"])(params.get("export_grad_fsl"), execution))
    if params.get("nocleanup"):
        cargs.append("-nocleanup")
    if params.get("scratch_dir") is not None:
        cargs.extend([
            "-scratch",
            execution.input_file(params.get("scratch_dir"))
        ])
    if params.get("continue_scratch_dir") is not None:
        cargs.extend([
            "-continue",
            *[execution.input_file(f) for f in params.get("continue_scratch_dir")]
        ])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([
            "-config",
            *params.get("config")
        ])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    return cargs


def dwigradcheck_outputs(
    params: DwigradcheckParameters,
    execution: Execution,
) -> DwigradcheckOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DwigradcheckOutputs(
        root=execution.output_file("."),
        export_grad_mrtrix=execution.output_file(params.get("export_grad_mrtrix")) if (params.get("export_grad_mrtrix") is not None) else None,
        export_grad_fsl=execution.output_file(params.get("export_grad_mrtrix")) if (params.get("export_grad_mrtrix") is not None) else None,
        export_grad_fsl_=dyn_outputs(params.get("export_grad_fsl")["__STYXTYPE__"])(params.get("export_grad_fsl"), execution) if params.get("export_grad_fsl") else None,
    )
    return ret


def dwigradcheck_execute(
    params: DwigradcheckParameters,
    execution: Execution,
) -> DwigradcheckOutputs:
    """
    Check the orientation of the diffusion gradient table.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DwigradcheckOutputs`).
    """
    params = execution.params(params)
    cargs = dwigradcheck_cargs(params, execution)
    ret = dwigradcheck_outputs(params, execution)
    execution.run(cargs)
    return ret


def dwigradcheck(
    input_image: InputPathType,
    grad: InputPathType | None = None,
    fslgrad: DwigradcheckFslgradParameters | None = None,
    mask_image: InputPathType | None = None,
    number: int | None = None,
    export_grad_mrtrix: str | None = None,
    export_grad_fsl: DwigradcheckExportGradFslParameters | None = None,
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
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
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
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWIGRADCHECK_METADATA)
    params = dwigradcheck_params(input_image=input_image, grad=grad, fslgrad=fslgrad, mask_image=mask_image, number=number, export_grad_mrtrix=export_grad_mrtrix, export_grad_fsl=export_grad_fsl, nocleanup=nocleanup, scratch_dir=scratch_dir, continue_scratch_dir=continue_scratch_dir, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version)
    return dwigradcheck_execute(params, execution)


__all__ = [
    "DWIGRADCHECK_METADATA",
    "DwigradcheckExportGradFslOutputs",
    "DwigradcheckExportGradFslParameters",
    "DwigradcheckFslgradParameters",
    "DwigradcheckOutputs",
    "DwigradcheckParameters",
    "dwigradcheck",
    "dwigradcheck_export_grad_fsl_params",
    "dwigradcheck_fslgrad_params",
    "dwigradcheck_params",
]
