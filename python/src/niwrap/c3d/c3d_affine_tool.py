# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

C3D_AFFINE_TOOL_METADATA = Metadata(
    id="4d680bc675d44917986d0a7dc537117e07489d00.boutiques",
    name="c3d_affine_tool",
    package="c3d",
    container_image_tag="pyushkevich/itksnap:v3.8.2",
)
C3dAffineToolParameters = typing.TypedDict('C3dAffineToolParameters', {
    "__STYX_TYPE__": typing.Literal["c3d_affine_tool"],
    "transform_file": typing.NotRequired[InputPathType | None],
    "reference_file": typing.NotRequired[InputPathType | None],
    "source_file": typing.NotRequired[InputPathType | None],
    "sform_file": typing.NotRequired[InputPathType | None],
    "invert": bool,
    "determinant": bool,
    "multiply": bool,
    "sqrt": bool,
    "itk_transform": typing.NotRequired[InputPathType | None],
    "irtk_transform": typing.NotRequired[InputPathType | None],
    "fsl2ras": bool,
    "ras2fsl": bool,
    "out_itk_transform": typing.NotRequired[str | None],
    "out_irtk_transform": typing.NotRequired[str | None],
    "out_matfile": typing.NotRequired[str | None],
    "info": bool,
    "info_full": bool,
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
        "c3d_affine_tool": c3d_affine_tool_cargs,
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
        "c3d_affine_tool": c3d_affine_tool_outputs,
    }
    return vt.get(t)


class C3dAffineToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `c3d_affine_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    itk_transform_outfile: OutputPathType | None
    """Output ITK transform file."""
    irtk_transform_outfile: OutputPathType | None
    """Output IRTK transform file."""
    matrix_transform_outfile: OutputPathType | None
    """Write output matrix."""


def c3d_affine_tool_params(
    transform_file: InputPathType | None = None,
    reference_file: InputPathType | None = None,
    source_file: InputPathType | None = None,
    sform_file: InputPathType | None = None,
    invert: bool = False,
    determinant: bool = False,
    multiply: bool = False,
    sqrt: bool = False,
    itk_transform: InputPathType | None = None,
    irtk_transform: InputPathType | None = None,
    fsl2ras: bool = False,
    ras2fsl: bool = False,
    out_itk_transform: str | None = None,
    out_irtk_transform: str | None = None,
    out_matfile: str | None = None,
    info: bool = False,
    info_full: bool = False,
) -> C3dAffineToolParameters:
    """
    Build parameters.
    
    Args:
        transform_file: file or string representing the transform.
        reference_file: Set reference (fixed) image - only for -fsl2ras and\
            -ras2fsl.
        source_file: Set source (moving) image - only for -fsl2ras and\
            -ras2fsl.
        sform_file: Read matrix from NifTI sform.
        invert: Invert matrix.
        determinant: Print the determinant.
        multiply: Multiply matrices.
        sqrt: Matrix square root (i.e., Q s.t. A = Q * Q).
        itk_transform: Import ITK transform.
        irtk_transform: Import IRTK .dof format transform.
        fsl2ras: Convert FSL to RAS.
        ras2fsl: Convert RAS to FSL.
        out_itk_transform: Export ITK transform.
        out_irtk_transform: Export IRTK .dof format transform.
        out_matfile: Write output matrix.
        info: Print matrix.
        info_full: Print matrix and more detail about the transform.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "c3d_affine_tool",
        "invert": invert,
        "determinant": determinant,
        "multiply": multiply,
        "sqrt": sqrt,
        "fsl2ras": fsl2ras,
        "ras2fsl": ras2fsl,
        "info": info,
        "info_full": info_full,
    }
    if transform_file is not None:
        params["transform_file"] = transform_file
    if reference_file is not None:
        params["reference_file"] = reference_file
    if source_file is not None:
        params["source_file"] = source_file
    if sform_file is not None:
        params["sform_file"] = sform_file
    if itk_transform is not None:
        params["itk_transform"] = itk_transform
    if irtk_transform is not None:
        params["irtk_transform"] = irtk_transform
    if out_itk_transform is not None:
        params["out_itk_transform"] = out_itk_transform
    if out_irtk_transform is not None:
        params["out_irtk_transform"] = out_irtk_transform
    if out_matfile is not None:
        params["out_matfile"] = out_matfile
    return params


def c3d_affine_tool_cargs(
    params: C3dAffineToolParameters,
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
    cargs.append("c3d_affine_tool")
    if params.get("transform_file") is not None:
        cargs.append(execution.input_file(params.get("transform_file")))
    if params.get("reference_file") is not None:
        cargs.extend([
            "-ref",
            execution.input_file(params.get("reference_file"))
        ])
    if params.get("source_file") is not None:
        cargs.extend([
            "-src",
            execution.input_file(params.get("source_file"))
        ])
    if params.get("sform_file") is not None:
        cargs.extend([
            "-sform",
            execution.input_file(params.get("sform_file"))
        ])
    if params.get("invert"):
        cargs.append("-inv")
    if params.get("determinant"):
        cargs.append("-det")
    if params.get("multiply"):
        cargs.append("-mult")
    if params.get("sqrt"):
        cargs.append("-sqrt")
    if params.get("itk_transform") is not None:
        cargs.extend([
            "-itk",
            execution.input_file(params.get("itk_transform"))
        ])
    if params.get("irtk_transform") is not None:
        cargs.extend([
            "-irtk",
            execution.input_file(params.get("irtk_transform"))
        ])
    if params.get("fsl2ras"):
        cargs.append("-fsl2ras")
    if params.get("ras2fsl"):
        cargs.append("-ras2fsl")
    if params.get("out_itk_transform") is not None:
        cargs.extend([
            "-oitk",
            params.get("out_itk_transform")
        ])
    if params.get("out_irtk_transform") is not None:
        cargs.extend([
            "-oirtk",
            params.get("out_irtk_transform")
        ])
    if params.get("out_matfile") is not None:
        cargs.extend([
            "-o",
            params.get("out_matfile")
        ])
    if params.get("info"):
        cargs.append("-info")
    if params.get("info_full"):
        cargs.append("-info-full")
    return cargs


def c3d_affine_tool_outputs(
    params: C3dAffineToolParameters,
    execution: Execution,
) -> C3dAffineToolOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = C3dAffineToolOutputs(
        root=execution.output_file("."),
        itk_transform_outfile=execution.output_file(params.get("out_itk_transform")) if (params.get("out_itk_transform") is not None) else None,
        irtk_transform_outfile=execution.output_file(params.get("out_irtk_transform")) if (params.get("out_irtk_transform") is not None) else None,
        matrix_transform_outfile=execution.output_file(params.get("out_matfile")) if (params.get("out_matfile") is not None) else None,
    )
    return ret


def c3d_affine_tool_execute(
    params: C3dAffineToolParameters,
    execution: Execution,
) -> C3dAffineToolOutputs:
    """
    RAS affine transform tool.
    
    Author: Convert3D Developers
    
    URL: http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `C3dAffineToolOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = c3d_affine_tool_cargs(params, execution)
    ret = c3d_affine_tool_outputs(params, execution)
    execution.run(cargs)
    return ret


def c3d_affine_tool(
    transform_file: InputPathType | None = None,
    reference_file: InputPathType | None = None,
    source_file: InputPathType | None = None,
    sform_file: InputPathType | None = None,
    invert: bool = False,
    determinant: bool = False,
    multiply: bool = False,
    sqrt: bool = False,
    itk_transform: InputPathType | None = None,
    irtk_transform: InputPathType | None = None,
    fsl2ras: bool = False,
    ras2fsl: bool = False,
    out_itk_transform: str | None = None,
    out_irtk_transform: str | None = None,
    out_matfile: str | None = None,
    info: bool = False,
    info_full: bool = False,
    runner: Runner | None = None,
) -> C3dAffineToolOutputs:
    """
    RAS affine transform tool.
    
    Author: Convert3D Developers
    
    URL: http://www.itksnap.org/pmwiki/pmwiki.php?n=Convert3D.Convert3D
    
    Args:
        transform_file: file or string representing the transform.
        reference_file: Set reference (fixed) image - only for -fsl2ras and\
            -ras2fsl.
        source_file: Set source (moving) image - only for -fsl2ras and\
            -ras2fsl.
        sform_file: Read matrix from NifTI sform.
        invert: Invert matrix.
        determinant: Print the determinant.
        multiply: Multiply matrices.
        sqrt: Matrix square root (i.e., Q s.t. A = Q * Q).
        itk_transform: Import ITK transform.
        irtk_transform: Import IRTK .dof format transform.
        fsl2ras: Convert FSL to RAS.
        ras2fsl: Convert RAS to FSL.
        out_itk_transform: Export ITK transform.
        out_irtk_transform: Export IRTK .dof format transform.
        out_matfile: Write output matrix.
        info: Print matrix.
        info_full: Print matrix and more detail about the transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `C3dAffineToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(C3D_AFFINE_TOOL_METADATA)
    params = c3d_affine_tool_params(transform_file=transform_file, reference_file=reference_file, source_file=source_file, sform_file=sform_file, invert=invert, determinant=determinant, multiply=multiply, sqrt=sqrt, itk_transform=itk_transform, irtk_transform=irtk_transform, fsl2ras=fsl2ras, ras2fsl=ras2fsl, out_itk_transform=out_itk_transform, out_irtk_transform=out_irtk_transform, out_matfile=out_matfile, info=info, info_full=info_full)
    return c3d_affine_tool_execute(params, execution)


__all__ = [
    "C3D_AFFINE_TOOL_METADATA",
    "C3dAffineToolOutputs",
    "c3d_affine_tool",
    "c3d_affine_tool_params",
]
