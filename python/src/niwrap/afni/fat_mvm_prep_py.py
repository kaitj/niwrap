# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_MVM_PREP_PY_METADATA = Metadata(
    id="5e09dac2fb0a02ac411b5be7e41be335f325d553.boutiques",
    name="fat_mvm_prep.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatMvmPrepPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mvm_prep_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mvmtbl: OutputPathType
    """Output tabular text file for 3dMVM."""
    mvmprep_log: OutputPathType
    """Log file detailing subject matching and ROI list."""


def fat_mvm_prep_py(
    prefix: str,
    csv_file: InputPathType,
    matrix_files: str | None = None,
    list_match: InputPathType | None = None,
    unionize_rois: bool = False,
    na_warn_off: bool = False,
    extern_labels_no: bool = False,
    runner: Runner | None = None,
) -> FatMvmPrepPyOutputs:
    """
    Combine FATCAT output with CSV data for statistical modeling.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/fat_mvm_prep.py.html
    
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
        NamedTuple of outputs (described in `FatMvmPrepPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MVM_PREP_PY_METADATA)
    cargs = []
    cargs.append("fat_mvm_prep")
    cargs.extend([
        "-p",
        prefix
    ])
    cargs.extend([
        "-c",
        execution.input_file(csv_file)
    ])
    if matrix_files is not None:
        cargs.extend([
            "-m",
            matrix_files
        ])
    if list_match is not None:
        cargs.extend([
            "-l",
            execution.input_file(list_match)
        ])
    if unionize_rois:
        cargs.append("-u")
    if na_warn_off:
        cargs.append("-N")
    if extern_labels_no:
        cargs.append("-E")
    ret = FatMvmPrepPyOutputs(
        root=execution.output_file("."),
        mvmtbl=execution.output_file(prefix + "_MVMtbl.txt"),
        mvmprep_log=execution.output_file(prefix + "_MVMprep.log"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_MVM_PREP_PY_METADATA",
    "FatMvmPrepPyOutputs",
    "fat_mvm_prep_py",
]
