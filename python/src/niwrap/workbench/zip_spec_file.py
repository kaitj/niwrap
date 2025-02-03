# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ZIP_SPEC_FILE_METADATA = Metadata(
    id="990bcafbdd158caacb4567de9823ced2ae25e8d9.boutiques",
    name="zip-spec-file",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)
ZipSpecFileParameters = typing.TypedDict('ZipSpecFileParameters', {
    "__STYX_TYPE__": typing.Literal["zip-spec-file"],
    "spec_file": str,
    "extract_folder": str,
    "zip_file": str,
    "opt_base_dir_directory": typing.NotRequired[str | None],
    "opt_skip_missing": bool,
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
        "zip-spec-file": zip_spec_file_cargs,
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


def zip_spec_file_params(
    spec_file: str,
    extract_folder: str,
    zip_file: str,
    opt_base_dir_directory: str | None = None,
    opt_skip_missing: bool = False,
) -> ZipSpecFileParameters:
    """
    Build parameters.
    
    Args:
        spec_file: the specification file to add to zip file.
        extract_folder: the name of the folder created when the zip file is\
            unzipped.
        zip_file: out - the zip file that will be created.
        opt_base_dir_directory: specify a directory that all data files are\
            somewhere within, this will become the root of the zipfile's directory\
            structure: the directory.
        opt_skip_missing: any missing files will generate only warnings, and\
            the zip file will be created anyway.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "zip-spec-file",
        "spec_file": spec_file,
        "extract_folder": extract_folder,
        "zip_file": zip_file,
        "opt_skip_missing": opt_skip_missing,
    }
    if opt_base_dir_directory is not None:
        params["opt_base_dir_directory"] = opt_base_dir_directory
    return params


def zip_spec_file_cargs(
    params: ZipSpecFileParameters,
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
    cargs.append("wb_command")
    cargs.append("-zip-spec-file")
    cargs.append(params.get("spec_file"))
    cargs.append(params.get("extract_folder"))
    cargs.append(params.get("zip_file"))
    if params.get("opt_base_dir_directory") is not None:
        cargs.extend([
            "-base-dir",
            params.get("opt_base_dir_directory")
        ])
    if params.get("opt_skip_missing"):
        cargs.append("-skip-missing")
    return cargs


def zip_spec_file_outputs(
    params: ZipSpecFileParameters,
    execution: Execution,
) -> ZipSpecFileOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ZipSpecFileOutputs(
        root=execution.output_file("."),
    )
    return ret


def zip_spec_file_execute(
    params: ZipSpecFileParameters,
    execution: Execution,
) -> ZipSpecFileOutputs:
    """
    Zip a spec file and its data files.
    
    If zip-file already exists, it will be overwritten. If -base-dir is not
    specified, the directory containing the spec file is used for the base
    directory. The spec file must contain only relative paths, and no data files
    may be outside the base directory. Scene files inside spec files are not
    checked for what files they reference, ensure that all data files referenced
    by the scene files are also referenced by the spec file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ZipSpecFileOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = zip_spec_file_cargs(params, execution)
    ret = zip_spec_file_outputs(params, execution)
    execution.run(cargs)
    return ret


def zip_spec_file(
    spec_file: str,
    extract_folder: str,
    zip_file: str,
    opt_base_dir_directory: str | None = None,
    opt_skip_missing: bool = False,
    runner: Runner | None = None,
) -> ZipSpecFileOutputs:
    """
    Zip a spec file and its data files.
    
    If zip-file already exists, it will be overwritten. If -base-dir is not
    specified, the directory containing the spec file is used for the base
    directory. The spec file must contain only relative paths, and no data files
    may be outside the base directory. Scene files inside spec files are not
    checked for what files they reference, ensure that all data files referenced
    by the scene files are also referenced by the spec file.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        spec_file: the specification file to add to zip file.
        extract_folder: the name of the folder created when the zip file is\
            unzipped.
        zip_file: out - the zip file that will be created.
        opt_base_dir_directory: specify a directory that all data files are\
            somewhere within, this will become the root of the zipfile's directory\
            structure: the directory.
        opt_skip_missing: any missing files will generate only warnings, and\
            the zip file will be created anyway.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ZipSpecFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ZIP_SPEC_FILE_METADATA)
    params = zip_spec_file_params(spec_file=spec_file, extract_folder=extract_folder, zip_file=zip_file, opt_base_dir_directory=opt_base_dir_directory, opt_skip_missing=opt_skip_missing)
    return zip_spec_file_execute(params, execution)


__all__ = [
    "ZIP_SPEC_FILE_METADATA",
    "zip_spec_file",
    "zip_spec_file_params",
]
