# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V_3DNEWID_METADATA = Metadata(
    id="acbbcc60d614fe39bf285beddcf6984090e82ecf.boutiques",
    name="3dnewid",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dnewidParameters = typing.TypedDict('V3dnewidParameters', {
    "__STYX_TYPE__": typing.Literal["3dnewid"],
    "datasets": list[InputPathType],
    "fun": typing.NotRequired[float | None],
    "fun11": bool,
    "int": bool,
    "hash": typing.NotRequired[str | None],
    "MD5": typing.NotRequired[str | None],
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
        "3dnewid": v_3dnewid_cargs,
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
    }.get(t)


class V3dnewidOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dnewid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3dnewid_params(
    datasets: list[InputPathType],
    fun: float | None = None,
    fun11: bool = False,
    int_: bool = False,
    hash_: str | None = None,
    md5: str | None = None,
) -> V3dnewidParameters:
    """
    Build parameters.
    
    Args:
        datasets: Input datasets to assign new ID codes.
        fun: Generate n randomly generated ID codes. If n is not present, 1 ID\
            code is printed.
        fun11: Generate an 11 character ID code for use in scripting.
        int_: Generate a random positive integer between 1 million and 1\
            billion.
        hash_: Generate a unique hash code of the provided string. The same\
            string produces the same hash code.
        md5: Generate the MD5 hash of the provided string. Output should be the\
            same as the -hash output without the prefix and without the + and /\
            char substitutions.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dnewid",
        "datasets": datasets,
        "fun11": fun11,
        "int": int_,
    }
    if fun is not None:
        params["fun"] = fun
    if hash_ is not None:
        params["hash"] = hash_
    if md5 is not None:
        params["MD5"] = md5
    return params


def v_3dnewid_cargs(
    params: V3dnewidParameters,
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
    cargs.append("3dnewid")
    cargs.extend([execution.input_file(f) for f in params.get("datasets")])
    if params.get("fun") is not None:
        cargs.extend([
            "-fun",
            str(params.get("fun"))
        ])
    if params.get("fun11"):
        cargs.append("-fun11")
    if params.get("int"):
        cargs.append("-int")
    if params.get("hash") is not None:
        cargs.extend([
            "-hash",
            params.get("hash")
        ])
    if params.get("MD5") is not None:
        cargs.extend([
            "-MD5",
            params.get("MD5")
        ])
    return cargs


def v_3dnewid_outputs(
    params: V3dnewidParameters,
    execution: Execution,
) -> V3dnewidOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dnewidOutputs(
        root=execution.output_file("."),
    )
    return ret


def v_3dnewid_execute(
    params: V3dnewidParameters,
    execution: Execution,
) -> V3dnewidOutputs:
    """
    Assigns a new ID code to a dataset, ensuring internal ID codes remain unique.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dnewidOutputs`).
    """
    params = execution.params(params)
    cargs = v_3dnewid_cargs(params, execution)
    ret = v_3dnewid_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dnewid(
    datasets: list[InputPathType],
    fun: float | None = None,
    fun11: bool = False,
    int_: bool = False,
    hash_: str | None = None,
    md5: str | None = None,
    runner: Runner | None = None,
) -> V3dnewidOutputs:
    """
    Assigns a new ID code to a dataset, ensuring internal ID codes remain unique.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        datasets: Input datasets to assign new ID codes.
        fun: Generate n randomly generated ID codes. If n is not present, 1 ID\
            code is printed.
        fun11: Generate an 11 character ID code for use in scripting.
        int_: Generate a random positive integer between 1 million and 1\
            billion.
        hash_: Generate a unique hash code of the provided string. The same\
            string produces the same hash code.
        md5: Generate the MD5 hash of the provided string. Output should be the\
            same as the -hash output without the prefix and without the + and /\
            char substitutions.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dnewidOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DNEWID_METADATA)
    params = v_3dnewid_params(datasets=datasets, fun=fun, fun11=fun11, int_=int_, hash_=hash_, md5=md5)
    return v_3dnewid_execute(params, execution)


__all__ = [
    "V3dnewidOutputs",
    "V3dnewidParameters",
    "V_3DNEWID_METADATA",
    "v_3dnewid",
    "v_3dnewid_params",
]
