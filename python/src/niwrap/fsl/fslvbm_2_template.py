# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLVBM_2_TEMPLATE_METADATA = Metadata(
    id="07d5c99b1fc70d604c474ae66a112235c4703c8a",
    name="fslvbm_2_template",
    container_image_type="docker",
    container_image_tag="mcin/fsl:6.0.5",
)


class Fslvbm2TemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslvbm_2_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslvbm_2_template(
    arch: str | None = None,
    coprocessor: str | None = None,
    coprocessor_multi: str | None = None,
    coprocessor_class: str | None = None,
    coprocessor_toolkit: str | None = None,
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
    memory_gb: float | int | None = None,
    parallel_env: str | None = None,
    array_task: str | None = None,
    array_native: str | None = None,
    num_tasks: float | int | None = None,
    coprocessor_name: str | None = None,
    project: str | None = None,
    runtime_limit: float | int | None = None,
    job_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> Fslvbm2TemplateOutputs:
    """
    fslvbm_2_template by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    FSL-VBM is a Voxel-Based Morphometry style analysis tool for FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSLVBM
    
    Args:
        arch: Specify architecture.
        coprocessor: Specify coprocessor type.
        coprocessor_multi: Specify multiple coprocessors.
        coprocessor_class: Specify coprocessor class.
        coprocessor_toolkit: Specify coprocessor toolkit.
        jobhold: Hold job until specified job ID is completed.
        array_hold: Hold array job until specified job ID is completed.
        logdir: Specify log directory.
        mailoptions: Specify mail options.
        mailto: Specify email address for notifications.
        name: Specify job name.
        priority: Specify job priority.
        queue_: Specify queue.
        resource_: Specify resources.
        delete_job: Delete specified job.
        memory_gb: Specify memory in GB.
        parallel_env: Specify parallel environment and threads.
        array_task: Specify array task.
        array_native: Specify array native task.
        num_tasks: Specify number of tasks.
        coprocessor_name: Specify coprocessor name.
        project: Specify project.
        runtime_limit: Specify runtime limit in minutes.
        job_file: Specify job script file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Fslvbm2TemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLVBM_2_TEMPLATE_METADATA)
    cargs = []
    cargs.append("fslvbm_2_template")
    if arch is not None:
        cargs.extend(["-a", arch])
    if coprocessor is not None:
        cargs.extend(["-c", coprocessor])
    if coprocessor_multi is not None:
        cargs.extend(["--coprocessor_multi", coprocessor_multi])
    if coprocessor_class is not None:
        cargs.extend(["--coprocessor_class", coprocessor_class])
    if coprocessor_toolkit is not None:
        cargs.extend(["--coprocessor_toolkit", coprocessor_toolkit])
    if jobhold is not None:
        cargs.extend(["-j", jobhold])
    if array_hold is not None:
        cargs.extend(["--array_hold", array_hold])
    if logdir is not None:
        cargs.extend(["-l", logdir])
    if mailoptions is not None:
        cargs.extend(["-m", mailoptions])
    if mailto is not None:
        cargs.extend(["-M", mailto])
    if name is not None:
        cargs.extend(["-N", name])
    if priority is not None:
        cargs.extend(["-p", priority])
    if queue_ is not None:
        cargs.extend(["-q", queue_])
    if resource_ is not None:
        cargs.extend(["-r", resource_])
    if delete_job is not None:
        cargs.extend(["--delete_job", delete_job])
    if memory_gb is not None:
        cargs.extend(["-R", str(memory_gb)])
    cargs.append("[PARALLELENV]")
    cargs.append("[THREADS]")
    if array_task is not None:
        cargs.extend(["-t", array_task])
    if array_native is not None:
        cargs.extend(["--array_native", array_native])
    if num_tasks is not None:
        cargs.extend(["-x", str(num_tasks)])
    if coprocessor_name is not None:
        cargs.extend(["--has_coprocessor", coprocessor_name])
    if project is not None:
        cargs.extend(["--project", project])
    if runtime_limit is not None:
        cargs.extend(["-T", str(runtime_limit)])
    if job_file is not None:
        cargs.extend(["-z", execution.input_file(job_file)])
    ret = Fslvbm2TemplateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLVBM_2_TEMPLATE_METADATA",
    "Fslvbm2TemplateOutputs",
    "fslvbm_2_template",
]