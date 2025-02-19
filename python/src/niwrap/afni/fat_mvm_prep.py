# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

FAT_MVM_PREP_METADATA = Metadata(
    id="90f6bc657de16af423e425320b0789c1d1f1d2eb.boutiques",
    name="fat_mvm_prep",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
FatMvmPrepParameters = typing.TypedDict('FatMvmPrepParameters', {
    "__STYX_TYPE__": typing.Literal["fat_mvm_prep"],
    "prefix": str,
    "csv_file": InputPathType,
    "matrix_files": typing.NotRequired[str | None],
    "list_match": typing.NotRequired[InputPathType | None],
    "unionize_rois": bool,
    "na_warn_off": bool,
    "extern_labels_no": bool,
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
        "fat_mvm_prep": fat_mvm_prep_cargs,
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
        "fat_mvm_prep": fat_mvm_prep_outputs,
    }.get(t)


class FatMvmPrepOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mvm_prep(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mvmtbl: OutputPathType
    """Output tabular text file for 3dMVM."""
    mvmprep_log: OutputPathType
    """Log file detailing subject matching and ROI list."""


def fat_mvm_prep_params(
    prefix: str,
    csv_file: InputPathType,
    matrix_files: str | None = None,
    list_match: InputPathType | None = None,
    unionize_rois: bool = False,
    na_warn_off: bool = False,
    extern_labels_no: bool = False,
) -> FatMvmPrepParameters:
    """
    Build parameters.
    
    Args:
        prefix: Prefix for output files.
        csv_file: Comma-separated variable (CSV) file for input.
        matrix_files: Set of matrix (*.grid or *.netcc) files by searchable\
            path.
        list_match: Text file containing two columns: path to subject matrix\
            file and CSV IDs.
        unionize_rois: Make the ROI list as the union of elements across the\
            group.
        na_warn_off: Turn off the automatic warnings as the data table is\
            created.
        extern_labels_no: Turn off the writing/usage of user-defined labels in\
            the *.grid/*.netcc files.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fat_mvm_prep",
        "prefix": prefix,
        "csv_file": csv_file,
        "unionize_rois": unionize_rois,
        "na_warn_off": na_warn_off,
        "extern_labels_no": extern_labels_no,
    }
    if matrix_files is not None:
        params["matrix_files"] = matrix_files
    if list_match is not None:
        params["list_match"] = list_match
    return params


def fat_mvm_prep_cargs(
    params: FatMvmPrepParameters,
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
    cargs.append("fat_mvm_prep.py")
    cargs.extend([
        "-p",
        params.get("prefix")
    ])
    cargs.extend([
        "-c",
        execution.input_file(params.get("csv_file"))
    ])
    if params.get("matrix_files") is not None:
        cargs.extend([
            "-m",
            params.get("matrix_files")
        ])
    if params.get("list_match") is not None:
        cargs.extend([
            "-l",
            execution.input_file(params.get("list_match"))
        ])
    if params.get("unionize_rois"):
        cargs.append("-u")
    if params.get("na_warn_off"):
        cargs.append("-N")
    if params.get("extern_labels_no"):
        cargs.append("-E")
    return cargs


def fat_mvm_prep_outputs(
    params: FatMvmPrepParameters,
    execution: Execution,
) -> FatMvmPrepOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FatMvmPrepOutputs(
        root=execution.output_file("."),
        mvmtbl=execution.output_file(params.get("prefix") + "_MVMtbl.txt"),
        mvmprep_log=execution.output_file(params.get("prefix") + "_MVMprep.log"),
    )
    return ret


def fat_mvm_prep_execute(
    params: FatMvmPrepParameters,
    execution: Execution,
) -> FatMvmPrepOutputs:
    """
    Combine FATCAT output with CSV data for statistical modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FatMvmPrepOutputs`).
    """
    params = execution.params(params)
    cargs = fat_mvm_prep_cargs(params, execution)
    ret = fat_mvm_prep_outputs(params, execution)
    execution.run(cargs)
    return ret


def fat_mvm_prep(
    prefix: str,
    csv_file: InputPathType,
    matrix_files: str | None = None,
    list_match: InputPathType | None = None,
    unionize_rois: bool = False,
    na_warn_off: bool = False,
    extern_labels_no: bool = False,
    runner: Runner | None = None,
) -> FatMvmPrepOutputs:
    """
    Combine FATCAT output with CSV data for statistical modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for output files.
        csv_file: Comma-separated variable (CSV) file for input.
        matrix_files: Set of matrix (*.grid or *.netcc) files by searchable\
            path.
        list_match: Text file containing two columns: path to subject matrix\
            file and CSV IDs.
        unionize_rois: Make the ROI list as the union of elements across the\
            group.
        na_warn_off: Turn off the automatic warnings as the data table is\
            created.
        extern_labels_no: Turn off the writing/usage of user-defined labels in\
            the *.grid/*.netcc files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMvmPrepOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MVM_PREP_METADATA)
    params = fat_mvm_prep_params(prefix=prefix, csv_file=csv_file, matrix_files=matrix_files, list_match=list_match, unionize_rois=unionize_rois, na_warn_off=na_warn_off, extern_labels_no=extern_labels_no)
    return fat_mvm_prep_execute(params, execution)


__all__ = [
    "FAT_MVM_PREP_METADATA",
    "FatMvmPrepOutputs",
    "FatMvmPrepParameters",
    "fat_mvm_prep",
    "fat_mvm_prep_params",
]
