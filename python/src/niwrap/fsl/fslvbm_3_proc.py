# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSLVBM_3_PROC_METADATA = Metadata(
    id="e412ceb5c621d60c9b9b10de2a0a6700c42898c2.boutiques",
    name="fslvbm_3_proc",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
Fslvbm3ProcParameters = typing.TypedDict('Fslvbm3ProcParameters', {
    "__STYX_TYPE__": typing.Literal["fslvbm_3_proc"],
    "arch": typing.NotRequired[str | None],
    "coprocessor": typing.NotRequired[str | None],
    "coprocessor_multi": typing.NotRequired[str | None],
    "coprocessor_class": typing.NotRequired[str | None],
    "coprocessor_class_strict": bool,
    "coprocessor_toolkit": typing.NotRequired[str | None],
    "not_requeueable": bool,
    "jobhold": typing.NotRequired[str | None],
    "array_hold": typing.NotRequired[str | None],
    "logdir": typing.NotRequired[str | None],
    "mailoptions": typing.NotRequired[str | None],
    "mailto": typing.NotRequired[str | None],
    "name": typing.NotRequired[str | None],
    "priority": typing.NotRequired[str | None],
    "queue": typing.NotRequired[str | None],
    "resource": typing.NotRequired[str | None],
    "delete_job": typing.NotRequired[str | None],
    "memory_gb": typing.NotRequired[float | None],
    "parallel_env_threads": typing.NotRequired[str | None],
    "array_task": typing.NotRequired[str | None],
    "array_native": typing.NotRequired[str | None],
    "number_jobscripts": typing.NotRequired[float | None],
    "keep_jobscript": bool,
    "coprocessor_name": typing.NotRequired[str | None],
    "has_queues": bool,
    "project": typing.NotRequired[str | None],
    "submit_scheduler": bool,
    "runtime_limit": typing.NotRequired[float | None],
    "show_config": bool,
    "verbose": bool,
    "version": bool,
    "config_file": typing.NotRequired[InputPathType | None],
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
        "fslvbm_3_proc": fslvbm_3_proc_cargs,
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
        "fslvbm_3_proc": fslvbm_3_proc_outputs,
    }
    return vt.get(t)


class Fslvbm3ProcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslvbm_3_proc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_directory: OutputPathType
    """Output data directory"""


def fslvbm_3_proc_params(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: str | None = None,
    coprocessor_class: str | None = None,
    coprocessor_class_strict: bool = False,
    coprocessor_toolkit: str | None = None,
    not_requeueable: bool = False,
    jobhold: str | None = None,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = None,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    memory_gb: float | None = None,
    parallel_env_threads: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    number_jobscripts: float | None = None,
    keep_jobscript: bool = False,
    coprocessor_name: str | None = None,
    has_queues: bool = False,
    project: str | None = None,
    submit_scheduler: bool = False,
    runtime_limit: float | None = None,
    show_config: bool = False,
    verbose: bool = False,
    version: bool = False,
    config_file: InputPathType | None = None,
) -> Fslvbm3ProcParameters:
    """
    Build parameters.
    
    Args:
        arch: Specify architecture.
        coprocessor: Specify coprocessor.
        coprocessor_multi: Specify multiple coprocessors.
        coprocessor_class: Specify coprocessor class.
        coprocessor_class_strict: Use strict class matching for coprocessor.
        coprocessor_toolkit: Specify coprocessor toolkit.
        not_requeueable: Do not requeue the job.
        jobhold: Job to hold.
        array_hold: Array hold.
        logdir: Specify log directory.
        mailoptions: Specify mail options.
        mailto: Specify mail recipient.
        name: Job name.
        priority: Job priority.
        queue_: Queue to submit to.
        resource_: Resource identifier.
        delete_job: Delete specified job.
        memory_gb: Memory (GB).
        parallel_env_threads: Parallel environment and threads.
        array_task: Array task file.
        array_native: Array native specification.
        number_jobscripts: Keep number of job scripts.
        keep_jobscript: Keep job script.
        coprocessor_name: Specify coprocessor name.
        has_queues: Specify queues.
        project: Specify project name.
        submit_scheduler: Submit to Scheduler.
        runtime_limit: Specify runtime limit in minutes.
        show_config: Show configuration.
        verbose: Verbose output.
        version: Version information.
        config_file: Specify configuration file.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fslvbm_3_proc",
        "coprocessor_class_strict": coprocessor_class_strict,
        "not_requeueable": not_requeueable,
        "keep_jobscript": keep_jobscript,
        "has_queues": has_queues,
        "submit_scheduler": submit_scheduler,
        "show_config": show_config,
        "verbose": verbose,
        "version": version,
    }
    if arch is not None:
        params["arch"] = arch
    if coprocessor is not None:
        params["coprocessor"] = coprocessor
    if coprocessor_multi is not None:
        params["coprocessor_multi"] = coprocessor_multi
    if coprocessor_class is not None:
        params["coprocessor_class"] = coprocessor_class
    if coprocessor_toolkit is not None:
        params["coprocessor_toolkit"] = coprocessor_toolkit
    if jobhold is not None:
        params["jobhold"] = jobhold
    if array_hold is not None:
        params["array_hold"] = array_hold
    if logdir is not None:
        params["logdir"] = logdir
    if mailoptions is not None:
        params["mailoptions"] = mailoptions
    if mailto is not None:
        params["mailto"] = mailto
    if name is not None:
        params["name"] = name
    if priority is not None:
        params["priority"] = priority
    if queue_ is not None:
        params["queue"] = queue_
    if resource_ is not None:
        params["resource"] = resource_
    if delete_job is not None:
        params["delete_job"] = delete_job
    if memory_gb is not None:
        params["memory_gb"] = memory_gb
    if parallel_env_threads is not None:
        params["parallel_env_threads"] = parallel_env_threads
    if array_task is not None:
        params["array_task"] = array_task
    if array_native is not None:
        params["array_native"] = array_native
    if number_jobscripts is not None:
        params["number_jobscripts"] = number_jobscripts
    if coprocessor_name is not None:
        params["coprocessor_name"] = coprocessor_name
    if project is not None:
        params["project"] = project
    if runtime_limit is not None:
        params["runtime_limit"] = runtime_limit
    if config_file is not None:
        params["config_file"] = config_file
    return params


def fslvbm_3_proc_cargs(
    params: Fslvbm3ProcParameters,
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
    cargs.append("fslvbm_3_proc")
    if params.get("arch") is not None:
        cargs.extend([
            "-a",
            params.get("arch")
        ])
    if params.get("coprocessor") is not None:
        cargs.extend([
            "-c",
            params.get("coprocessor")
        ])
    if params.get("coprocessor_multi") is not None:
        cargs.extend([
            "--coprocessor_multi",
            params.get("coprocessor_multi")
        ])
    if params.get("coprocessor_class") is not None:
        cargs.extend([
            "--coprocessor_class",
            params.get("coprocessor_class")
        ])
    if params.get("coprocessor_class_strict"):
        cargs.append("--coprocessor_class_strict")
    if params.get("coprocessor_toolkit") is not None:
        cargs.extend([
            "--coprocessor_toolkit",
            params.get("coprocessor_toolkit")
        ])
    if params.get("not_requeueable"):
        cargs.append("-F")
    if params.get("jobhold") is not None:
        cargs.extend([
            "-j",
            params.get("jobhold")
        ])
    if params.get("array_hold") is not None:
        cargs.extend([
            "--array_hold",
            params.get("array_hold")
        ])
    if params.get("logdir") is not None:
        cargs.extend([
            "-l",
            params.get("logdir")
        ])
    if params.get("mailoptions") is not None:
        cargs.extend([
            "-m",
            params.get("mailoptions")
        ])
    if params.get("mailto") is not None:
        cargs.extend([
            "-M",
            params.get("mailto")
        ])
    if params.get("name") is not None:
        cargs.extend([
            "-N",
            params.get("name")
        ])
    if params.get("priority") is not None:
        cargs.extend([
            "-p",
            params.get("priority")
        ])
    if params.get("queue") is not None:
        cargs.extend([
            "-q",
            params.get("queue")
        ])
    if params.get("resource") is not None:
        cargs.extend([
            "-r",
            params.get("resource")
        ])
    if params.get("delete_job") is not None:
        cargs.extend([
            "--delete_job",
            params.get("delete_job")
        ])
    if params.get("memory_gb") is not None:
        cargs.extend([
            "-R",
            str(params.get("memory_gb"))
        ])
    if params.get("parallel_env_threads") is not None:
        cargs.extend([
            "-s",
            params.get("parallel_env_threads")
        ])
    if params.get("array_task") is not None:
        cargs.extend([
            "-t",
            params.get("array_task")
        ])
    if params.get("array_native") is not None:
        cargs.extend([
            "--array_native",
            params.get("array_native")
        ])
    if params.get("number_jobscripts") is not None:
        cargs.extend([
            "-x",
            str(params.get("number_jobscripts"))
        ])
    if params.get("keep_jobscript"):
        cargs.append("--keep_jobscript")
    if params.get("coprocessor_name") is not None:
        cargs.extend([
            "--has_coprocessor",
            params.get("coprocessor_name")
        ])
    if params.get("has_queues"):
        cargs.append("--has_queues")
    if params.get("project") is not None:
        cargs.extend([
            "--project",
            params.get("project")
        ])
    if params.get("submit_scheduler"):
        cargs.append("-S")
    if params.get("runtime_limit") is not None:
        cargs.extend([
            "-T",
            str(params.get("runtime_limit"))
        ])
    if params.get("show_config"):
        cargs.append("--show_config")
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("version"):
        cargs.append("-V")
    if params.get("config_file") is not None:
        cargs.extend([
            "-z",
            execution.input_file(params.get("config_file"))
        ])
    return cargs


def fslvbm_3_proc_outputs(
    params: Fslvbm3ProcParameters,
    execution: Execution,
) -> Fslvbm3ProcOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Fslvbm3ProcOutputs(
        root=execution.output_file("."),
        output_directory=execution.output_file("fslvbm3a"),
    )
    return ret


def fslvbm_3_proc_execute(
    params: Fslvbm3ProcParameters,
    execution: Execution,
) -> Fslvbm3ProcOutputs:
    """
    Pipeline for voxel-based morphometry analysis using FSL tools.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Fslvbm3ProcOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fslvbm_3_proc_cargs(params, execution)
    ret = fslvbm_3_proc_outputs(params, execution)
    execution.run(cargs)
    return ret


def fslvbm_3_proc(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: str | None = None,
    coprocessor_class: str | None = None,
    coprocessor_class_strict: bool = False,
    coprocessor_toolkit: str | None = None,
    not_requeueable: bool = False,
    jobhold: str | None = None,
    array_hold: str | None = None,
    logdir: str | None = None,
    mailoptions: str | None = None,
    mailto: str | None = None,
    name: str | None = None,
    priority: str | None = None,
    queue_: str | None = None,
    resource_: str | None = None,
    delete_job: str | None = None,
    memory_gb: float | None = None,
    parallel_env_threads: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    number_jobscripts: float | None = None,
    keep_jobscript: bool = False,
    coprocessor_name: str | None = None,
    has_queues: bool = False,
    project: str | None = None,
    submit_scheduler: bool = False,
    runtime_limit: float | None = None,
    show_config: bool = False,
    verbose: bool = False,
    version: bool = False,
    config_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> Fslvbm3ProcOutputs:
    """
    Pipeline for voxel-based morphometry analysis using FSL tools.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        arch: Specify architecture.
        coprocessor: Specify coprocessor.
        coprocessor_multi: Specify multiple coprocessors.
        coprocessor_class: Specify coprocessor class.
        coprocessor_class_strict: Use strict class matching for coprocessor.
        coprocessor_toolkit: Specify coprocessor toolkit.
        not_requeueable: Do not requeue the job.
        jobhold: Job to hold.
        array_hold: Array hold.
        logdir: Specify log directory.
        mailoptions: Specify mail options.
        mailto: Specify mail recipient.
        name: Job name.
        priority: Job priority.
        queue_: Queue to submit to.
        resource_: Resource identifier.
        delete_job: Delete specified job.
        memory_gb: Memory (GB).
        parallel_env_threads: Parallel environment and threads.
        array_task: Array task file.
        array_native: Array native specification.
        number_jobscripts: Keep number of job scripts.
        keep_jobscript: Keep job script.
        coprocessor_name: Specify coprocessor name.
        has_queues: Specify queues.
        project: Specify project name.
        submit_scheduler: Submit to Scheduler.
        runtime_limit: Specify runtime limit in minutes.
        show_config: Show configuration.
        verbose: Verbose output.
        version: Version information.
        config_file: Specify configuration file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslvbm3ProcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVBM_3_PROC_METADATA)
    params = fslvbm_3_proc_params(arch=arch, coprocessor=coprocessor, coprocessor_multi=coprocessor_multi, coprocessor_class=coprocessor_class, coprocessor_class_strict=coprocessor_class_strict, coprocessor_toolkit=coprocessor_toolkit, not_requeueable=not_requeueable, jobhold=jobhold, array_hold=array_hold, logdir=logdir, mailoptions=mailoptions, mailto=mailto, name=name, priority=priority, queue_=queue_, resource_=resource_, delete_job=delete_job, memory_gb=memory_gb, parallel_env_threads=parallel_env_threads, array_task=array_task, array_native=array_native, number_jobscripts=number_jobscripts, keep_jobscript=keep_jobscript, coprocessor_name=coprocessor_name, has_queues=has_queues, project=project, submit_scheduler=submit_scheduler, runtime_limit=runtime_limit, show_config=show_config, verbose=verbose, version=version, config_file=config_file)
    return fslvbm_3_proc_execute(params, execution)


__all__ = [
    "FSLVBM_3_PROC_METADATA",
    "Fslvbm3ProcOutputs",
    "fslvbm_3_proc",
    "fslvbm_3_proc_params",
]
