# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CAT_MATVEC_METADATA = Metadata(
    id="ea044673965ec2f3a89f325814e9677a680c6cec.boutiques",
    name="cat_matvec",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
CatMatvecParameters = typing.TypedDict('CatMatvecParameters', {
    "__STYX_TYPE__": typing.Literal["cat_matvec"],
    "four_by_four_format": bool,
    "matvec_spec": list[str],
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
        "cat_matvec": cat_matvec_cargs,
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
    vt = {}
    return vt.get(t)


def cat_matvec_params(
    matvec_spec: list[str],
    four_by_four_format: bool = False,
) -> CatMatvecParameters:
    """
    Build parameters.
    
    Args:
        matvec_spec: Specifies the matrix transformation. Can take forms\
            described in the documentation.
        four_by_four_format: Output matrix in augmented form (last row is 0 0 0\
            1). This option does not work with -MATRIX or -ONELINE.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "cat_matvec",
        "four_by_four_format": four_by_four_format,
        "matvec_spec": matvec_spec,
    }
    return params


def cat_matvec_cargs(
    params: CatMatvecParameters,
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
    cargs.append("cat_matvec")
    if params.get("four_by_four_format"):
        cargs.append("-4x4")
    cargs.extend(params.get("matvec_spec"))
    return cargs


def cat_matvec_outputs(
    params: CatMatvecParameters,
    execution: Execution,
) -> CatMatvecOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = CatMatvecOutputs(
        root=execution.output_file("."),
    )
    return ret


def cat_matvec_execute(
    params: CatMatvecParameters,
    execution: Execution,
) -> CatMatvecOutputs:
    """
    Catenates 3D rotation+shift matrix+vector transformations.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `CatMatvecOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = cat_matvec_cargs(params, execution)
    ret = cat_matvec_outputs(params, execution)
    execution.run(cargs)
    return ret


def cat_matvec(
    matvec_spec: list[str],
    four_by_four_format: bool = False,
    runner: Runner | None = None,
) -> CatMatvecOutputs:
    """
    Catenates 3D rotation+shift matrix+vector transformations.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        matvec_spec: Specifies the matrix transformation. Can take forms\
            described in the documentation.
        four_by_four_format: Output matrix in augmented form (last row is 0 0 0\
            1). This option does not work with -MATRIX or -ONELINE.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CatMatvecOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CAT_MATVEC_METADATA)
    params = cat_matvec_params(four_by_four_format=four_by_four_format, matvec_spec=matvec_spec)
    return cat_matvec_execute(params, execution)


__all__ = [
    "CAT_MATVEC_METADATA",
    "cat_matvec",
    "cat_matvec_params",
]
