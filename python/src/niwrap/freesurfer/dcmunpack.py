# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DCMUNPACK_METADATA = Metadata(
    id="01d871981fcfe7211d8f4250bbd352a2a097e2e7.boutiques",
    name="dcmunpack",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)
DcmunpackParameters = typing.TypedDict('DcmunpackParameters', {
    "__STYX_TYPE__": typing.Literal["dcmunpack"],
    "src": str,
    "targ": typing.NotRequired[str | None],
    "run": typing.NotRequired[str | None],
    "auto_runseq": typing.NotRequired[str | None],
    "keep_scouts": bool,
    "scanonly": typing.NotRequired[str | None],
    "one_per_dir": bool,
    "ext": typing.NotRequired[str | None],
    "pre": typing.NotRequired[str | None],
    "pat": typing.NotRequired[str | None],
    "no_infodump": bool,
    "generic": bool,
    "copy_only": bool,
    "no_convert": bool,
    "force_update": bool,
    "max": bool,
    "base": bool,
    "key_string": typing.NotRequired[str | None],
    "index_out": typing.NotRequired[str | None],
    "index_in": typing.NotRequired[str | None],
    "it_dicom": bool,
    "no_exit_on_error": bool,
    "run_skip": typing.NotRequired[str | None],
    "no_rescale_dicom": bool,
    "rescale_dicom": bool,
    "no_dwi": bool,
    "iid": typing.NotRequired[list[float] | None],
    "ijd": typing.NotRequired[list[float] | None],
    "ikd": typing.NotRequired[list[float] | None],
    "extra_info": bool,
    "first_dicom": bool,
    "no_dcm2niix": bool,
    "phase": bool,
    "fips": typing.NotRequired[str | None],
    "fips_run": typing.NotRequired[str | None],
    "xml_only": bool,
    "log": typing.NotRequired[str | None],
    "debug": bool,
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
        "dcmunpack": dcmunpack_cargs,
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


def dcmunpack_params(
    src: str,
    targ: str | None = None,
    run: str | None = None,
    auto_runseq: str | None = None,
    keep_scouts: bool = False,
    scanonly: str | None = None,
    one_per_dir: bool = False,
    ext: str | None = None,
    pre: str | None = None,
    pat: str | None = None,
    no_infodump: bool = False,
    generic: bool = False,
    copy_only: bool = False,
    no_convert: bool = False,
    force_update: bool = False,
    max_: bool = False,
    base: bool = False,
    key_string: str | None = None,
    index_out: str | None = None,
    index_in: str | None = None,
    it_dicom: bool = False,
    no_exit_on_error: bool = False,
    run_skip: str | None = None,
    no_rescale_dicom: bool = False,
    rescale_dicom: bool = False,
    no_dwi: bool = False,
    iid: list[float] | None = None,
    ijd: list[float] | None = None,
    ikd: list[float] | None = None,
    extra_info: bool = False,
    first_dicom: bool = False,
    no_dcm2niix: bool = False,
    phase: bool = False,
    fips: str | None = None,
    fips_run: str | None = None,
    xml_only: bool = False,
    log: str | None = None,
    debug: bool = False,
) -> DcmunpackParameters:
    """
    Build parameters.
    
    Args:
        src: Dicom source directory. You can specify more than one.
        targ: Output directory. Do not need to include when just getting\
            information about what is in the directory.
        run: Specify unpacking rules for a given run (series). Eg, "-run 3 bold\
            nii f.nii".
        auto_runseq: Save all scans in the targetdir as runo.seqname.format.
        keep_scouts: Unpack series with 'scout' or 'setter' in the name.
        scanonly: Only scan the directory and put result in file.
        one_per_dir: Assume that there is only one dicom series in each subdir.
        ext: Input extension (eg, dcm).
        pre: Input prefix (i.e., input file name init string).
        pat: Input pattern (i.e., string that occurs in the middle of file\
            name).
        no_infodump: Do not create the fname-infodump.dat file.
        generic: Do not use FSFAST hierarchy.
        copy_only: Only copy dicom files to output directory (implies\
            -no-convert).
        no_convert: Do not convert to output format.
        force_update: Convert even if output is newer than the input dicom.
        max_: Print out max in given dicom file.
        base: Report filename without path.
        key_string: Put keystring before each run line (good for searching).
        index_out: Save index of files to index.out.dat (for re-use).
        index_in: Read index of files (can make things much faster on 2nd run).
        it_dicom: Add -it dicom to mri_convert cmd line.
        no_exit_on_error: Continue to unpack data even if there is an error in\
            conversion.
        run_skip: Skip a given run (good when using -auto-runseq).
        no_rescale_dicom: Turn off DICOM rescaling based on tags (0028,1052)\
            (0028,1053).
        rescale_dicom: Turn DICOM rescaling on.
        no_dwi: Turn off trying to read DWI parameters.
        iid: Set -iid to mri_convert.
        ijd: Set -ijd to mri_convert.
        ikd: Set -ikd to mri_convert.
        extra_info: Add session info to each line of the info file (pat, date,\
            man, scan, field, serno).
        first_dicom: Copy first dicom file into output folder.
        no_dcm2niix: Turn off dcm2niix conversion.
        phase: Add the string _phase to volumes that are phase images based on\
            ImageType.
        fips: Fips parameters: project, site, birnid, visit.
        fips_run: Fips-run parameters: run paradigm.
        xml_only: For fips, only create xml file, do not convert to output.
        log: Log output to a file.
        debug: Enable debug mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "dcmunpack",
        "src": src,
        "keep_scouts": keep_scouts,
        "one_per_dir": one_per_dir,
        "no_infodump": no_infodump,
        "generic": generic,
        "copy_only": copy_only,
        "no_convert": no_convert,
        "force_update": force_update,
        "max": max_,
        "base": base,
        "it_dicom": it_dicom,
        "no_exit_on_error": no_exit_on_error,
        "no_rescale_dicom": no_rescale_dicom,
        "rescale_dicom": rescale_dicom,
        "no_dwi": no_dwi,
        "extra_info": extra_info,
        "first_dicom": first_dicom,
        "no_dcm2niix": no_dcm2niix,
        "phase": phase,
        "xml_only": xml_only,
        "debug": debug,
    }
    if targ is not None:
        params["targ"] = targ
    if run is not None:
        params["run"] = run
    if auto_runseq is not None:
        params["auto_runseq"] = auto_runseq
    if scanonly is not None:
        params["scanonly"] = scanonly
    if ext is not None:
        params["ext"] = ext
    if pre is not None:
        params["pre"] = pre
    if pat is not None:
        params["pat"] = pat
    if key_string is not None:
        params["key_string"] = key_string
    if index_out is not None:
        params["index_out"] = index_out
    if index_in is not None:
        params["index_in"] = index_in
    if run_skip is not None:
        params["run_skip"] = run_skip
    if iid is not None:
        params["iid"] = iid
    if ijd is not None:
        params["ijd"] = ijd
    if ikd is not None:
        params["ikd"] = ikd
    if fips is not None:
        params["fips"] = fips
    if fips_run is not None:
        params["fips_run"] = fips_run
    if log is not None:
        params["log"] = log
    return params


def dcmunpack_cargs(
    params: DcmunpackParameters,
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
    cargs.append("dcmunpack")
    cargs.extend([
        "-src",
        params.get("src")
    ])
    if params.get("targ") is not None:
        cargs.extend([
            "-targ",
            params.get("targ")
        ])
    if params.get("run") is not None:
        cargs.extend([
            "-run",
            params.get("run")
        ])
    if params.get("auto_runseq") is not None:
        cargs.extend([
            "-auto-runseq",
            params.get("auto_runseq")
        ])
    if params.get("keep_scouts"):
        cargs.append("-keep-scouts")
    if params.get("scanonly") is not None:
        cargs.extend([
            "-scanonly",
            params.get("scanonly")
        ])
    if params.get("one_per_dir"):
        cargs.append("-one-per-dir")
    if params.get("ext") is not None:
        cargs.extend([
            "-ext",
            params.get("ext")
        ])
    if params.get("pre") is not None:
        cargs.extend([
            "-pre",
            params.get("pre")
        ])
    if params.get("pat") is not None:
        cargs.extend([
            "-pat",
            params.get("pat")
        ])
    if params.get("no_infodump"):
        cargs.append("-no-infodump")
    if params.get("generic"):
        cargs.append("-generic")
    if params.get("copy_only"):
        cargs.append("-copy-only")
    if params.get("no_convert"):
        cargs.append("-no-convert")
    if params.get("force_update"):
        cargs.append("-force-update")
    if params.get("max"):
        cargs.append("-max")
    if params.get("base"):
        cargs.append("-base")
    if params.get("key_string") is not None:
        cargs.extend([
            "-key",
            params.get("key_string")
        ])
    if params.get("index_out") is not None:
        cargs.extend([
            "-index-out",
            params.get("index_out")
        ])
    if params.get("index_in") is not None:
        cargs.extend([
            "-index-in",
            params.get("index_in")
        ])
    if params.get("it_dicom"):
        cargs.append("-itdicom")
    if params.get("no_exit_on_error"):
        cargs.append("-no-exit-on-error")
    if params.get("run_skip") is not None:
        cargs.extend([
            "-run-skip",
            params.get("run_skip")
        ])
    if params.get("no_rescale_dicom"):
        cargs.append("-no-rescale-dicom")
    if params.get("rescale_dicom"):
        cargs.append("-rescale-dicom")
    if params.get("no_dwi"):
        cargs.append("-no-dwi")
    if params.get("iid") is not None:
        cargs.extend([
            "-iid",
            *map(str, params.get("iid"))
        ])
    if params.get("ijd") is not None:
        cargs.extend([
            "-ijd",
            *map(str, params.get("ijd"))
        ])
    if params.get("ikd") is not None:
        cargs.extend([
            "-ikd",
            *map(str, params.get("ikd"))
        ])
    if params.get("extra_info"):
        cargs.append("-extra-info")
    if params.get("first_dicom"):
        cargs.append("-first-dicom")
    if params.get("no_dcm2niix"):
        cargs.append("-no-dcm2niix")
    if params.get("phase"):
        cargs.append("-phase")
    if params.get("fips") is not None:
        cargs.extend([
            "-fips",
            params.get("fips")
        ])
    if params.get("fips_run") is not None:
        cargs.extend([
            "-fips-run",
            params.get("fips_run")
        ])
    if params.get("xml_only"):
        cargs.append("-xml-only")
    if params.get("log") is not None:
        cargs.extend([
            "-log",
            params.get("log")
        ])
    if params.get("debug"):
        cargs.append("-debug")
    return cargs


def dcmunpack_outputs(
    params: DcmunpackParameters,
    execution: Execution,
) -> DcmunpackOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = DcmunpackOutputs(
        root=execution.output_file("."),
    )
    return ret


def dcmunpack_execute(
    params: DcmunpackParameters,
    execution: Execution,
) -> DcmunpackOutputs:
    """
    Sorts and converts a directory of DICOM files (Siemens, GE, Philips) into an
    output hierarchy with nifti (nii), mgh, mgz, or analyze output formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `DcmunpackOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = dcmunpack_cargs(params, execution)
    ret = dcmunpack_outputs(params, execution)
    execution.run(cargs)
    return ret


def dcmunpack(
    src: str,
    targ: str | None = None,
    run: str | None = None,
    auto_runseq: str | None = None,
    keep_scouts: bool = False,
    scanonly: str | None = None,
    one_per_dir: bool = False,
    ext: str | None = None,
    pre: str | None = None,
    pat: str | None = None,
    no_infodump: bool = False,
    generic: bool = False,
    copy_only: bool = False,
    no_convert: bool = False,
    force_update: bool = False,
    max_: bool = False,
    base: bool = False,
    key_string: str | None = None,
    index_out: str | None = None,
    index_in: str | None = None,
    it_dicom: bool = False,
    no_exit_on_error: bool = False,
    run_skip: str | None = None,
    no_rescale_dicom: bool = False,
    rescale_dicom: bool = False,
    no_dwi: bool = False,
    iid: list[float] | None = None,
    ijd: list[float] | None = None,
    ikd: list[float] | None = None,
    extra_info: bool = False,
    first_dicom: bool = False,
    no_dcm2niix: bool = False,
    phase: bool = False,
    fips: str | None = None,
    fips_run: str | None = None,
    xml_only: bool = False,
    log: str | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> DcmunpackOutputs:
    """
    Sorts and converts a directory of DICOM files (Siemens, GE, Philips) into an
    output hierarchy with nifti (nii), mgh, mgz, or analyze output formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src: Dicom source directory. You can specify more than one.
        targ: Output directory. Do not need to include when just getting\
            information about what is in the directory.
        run: Specify unpacking rules for a given run (series). Eg, "-run 3 bold\
            nii f.nii".
        auto_runseq: Save all scans in the targetdir as runo.seqname.format.
        keep_scouts: Unpack series with 'scout' or 'setter' in the name.
        scanonly: Only scan the directory and put result in file.
        one_per_dir: Assume that there is only one dicom series in each subdir.
        ext: Input extension (eg, dcm).
        pre: Input prefix (i.e., input file name init string).
        pat: Input pattern (i.e., string that occurs in the middle of file\
            name).
        no_infodump: Do not create the fname-infodump.dat file.
        generic: Do not use FSFAST hierarchy.
        copy_only: Only copy dicom files to output directory (implies\
            -no-convert).
        no_convert: Do not convert to output format.
        force_update: Convert even if output is newer than the input dicom.
        max_: Print out max in given dicom file.
        base: Report filename without path.
        key_string: Put keystring before each run line (good for searching).
        index_out: Save index of files to index.out.dat (for re-use).
        index_in: Read index of files (can make things much faster on 2nd run).
        it_dicom: Add -it dicom to mri_convert cmd line.
        no_exit_on_error: Continue to unpack data even if there is an error in\
            conversion.
        run_skip: Skip a given run (good when using -auto-runseq).
        no_rescale_dicom: Turn off DICOM rescaling based on tags (0028,1052)\
            (0028,1053).
        rescale_dicom: Turn DICOM rescaling on.
        no_dwi: Turn off trying to read DWI parameters.
        iid: Set -iid to mri_convert.
        ijd: Set -ijd to mri_convert.
        ikd: Set -ikd to mri_convert.
        extra_info: Add session info to each line of the info file (pat, date,\
            man, scan, field, serno).
        first_dicom: Copy first dicom file into output folder.
        no_dcm2niix: Turn off dcm2niix conversion.
        phase: Add the string _phase to volumes that are phase images based on\
            ImageType.
        fips: Fips parameters: project, site, birnid, visit.
        fips_run: Fips-run parameters: run paradigm.
        xml_only: For fips, only create xml file, do not convert to output.
        log: Log output to a file.
        debug: Enable debug mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DcmunpackOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DCMUNPACK_METADATA)
    params = dcmunpack_params(src=src, targ=targ, run=run, auto_runseq=auto_runseq, keep_scouts=keep_scouts, scanonly=scanonly, one_per_dir=one_per_dir, ext=ext, pre=pre, pat=pat, no_infodump=no_infodump, generic=generic, copy_only=copy_only, no_convert=no_convert, force_update=force_update, max_=max_, base=base, key_string=key_string, index_out=index_out, index_in=index_in, it_dicom=it_dicom, no_exit_on_error=no_exit_on_error, run_skip=run_skip, no_rescale_dicom=no_rescale_dicom, rescale_dicom=rescale_dicom, no_dwi=no_dwi, iid=iid, ijd=ijd, ikd=ikd, extra_info=extra_info, first_dicom=first_dicom, no_dcm2niix=no_dcm2niix, phase=phase, fips=fips, fips_run=fips_run, xml_only=xml_only, log=log, debug=debug)
    return dcmunpack_execute(params, execution)


__all__ = [
    "DCMUNPACK_METADATA",
    "dcmunpack",
    "dcmunpack_params",
]
