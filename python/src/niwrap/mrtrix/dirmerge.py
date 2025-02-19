# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

DIRMERGE_METADATA = Metadata(
    id="92c50a190c4f14115f8c861044c931f1316999ca.boutiques",
    name="dirmerge",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
DirmergeConfigParameters = typing.TypedDict('DirmergeConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
DirmergeParameters = typing.TypedDict('DirmergeParameters', {
    "__STYX_TYPE__": typing.Literal["dirmerge"],
    "unipolar_weight": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[DirmergeConfigParameters] | None],
    "help": bool,
    "version": bool,
    "subsets": int,
    "bvalue_files": list[str],
    "out": str,
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
        "dirmerge": dirmerge_cargs,
        "config": dirmerge_config_cargs,
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
        "dirmerge": dirmerge_outputs,
    }.get(t)


def dirmerge_config_params(
    key: str,
    value: str,
) -> DirmergeConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def dirmerge_config_cargs(
    params: DirmergeConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class DirmergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dirmerge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output directions file, with each row listing the X Y Z gradient
    directions, the b-value, and an index representing the phase encode
    direction"""


def dirmerge_params(
    subsets: int,
    bvalue_files: list[str],
    out: str,
    unipolar_weight: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirmergeConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> DirmergeParameters:
    """
    Build parameters.
    
    Args:
        subsets: the number of subsets (eg. phase encoding directions) per\
            b-value.
        bvalue_files: the b-value and sets of corresponding files, in order.
        out: the output directions file, with each row listing the X Y Z\
            gradient directions, the b-value, and an index representing the phase\
            encode direction.
        unipolar_weight: set the weight given to the unipolar electrostatic\
            repulsion model compared to the bipolar model (default: 0.2).
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dirmerge",
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "subsets": subsets,
        "bvalue_files": bvalue_files,
        "out": out,
    }
    if unipolar_weight is not None:
        params["unipolar_weight"] = unipolar_weight
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def dirmerge_cargs(
    params: DirmergeParameters,
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
    cargs.append("dirmerge")
    if params.get("unipolar_weight") is not None:
        cargs.extend([
            "-unipolar_weight",
            str(params.get("unipolar_weight"))
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
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(str(params.get("subsets")))
    cargs.extend(params.get("bvalue_files"))
    cargs.append(params.get("out"))
    return cargs


def dirmerge_outputs(
    params: DirmergeParameters,
    execution: Execution,
) -> DirmergeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DirmergeOutputs(
        root=execution.output_file("."),
        out=execution.output_file(params.get("out")),
    )
    return ret


def dirmerge_execute(
    params: DirmergeParameters,
    execution: Execution,
) -> DirmergeOutputs:
    """
    Splice / merge multiple sets of directions in such a way as to maintain
    near-optimality upon truncation.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DirmergeOutputs`).
    """
    params = execution.params(params)
    cargs = dirmerge_cargs(params, execution)
    ret = dirmerge_outputs(params, execution)
    execution.run(cargs)
    return ret


def dirmerge(
    subsets: int,
    bvalue_files: list[str],
    out: str,
    unipolar_weight: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DirmergeConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> DirmergeOutputs:
    """
    Splice / merge multiple sets of directions in such a way as to maintain
    near-optimality upon truncation.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        subsets: the number of subsets (eg. phase encoding directions) per\
            b-value.
        bvalue_files: the b-value and sets of corresponding files, in order.
        out: the output directions file, with each row listing the X Y Z\
            gradient directions, the b-value, and an index representing the phase\
            encode direction.
        unipolar_weight: set the weight given to the unipolar electrostatic\
            repulsion model compared to the bipolar model (default: 0.2).
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DirmergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DIRMERGE_METADATA)
    params = dirmerge_params(unipolar_weight=unipolar_weight, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, subsets=subsets, bvalue_files=bvalue_files, out=out)
    return dirmerge_execute(params, execution)


__all__ = [
    "DIRMERGE_METADATA",
    "DirmergeConfigParameters",
    "DirmergeOutputs",
    "DirmergeParameters",
    "dirmerge",
    "dirmerge_config_params",
    "dirmerge_params",
]
