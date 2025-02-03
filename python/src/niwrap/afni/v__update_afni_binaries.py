# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__UPDATE_AFNI_BINARIES_METADATA = Metadata(
    id="893694dbbccc046a97eb3b039a42a123a05bfc8f.boutiques",
    name="@update.afni.binaries",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VUpdateAfniBinariesParameters = typing.TypedDict('VUpdateAfniBinariesParameters', {
    "__STYX_TYPE__": typing.Literal["@update.afni.binaries"],
    "defaults_flag": bool,
    "help_flag": bool,
    "help_sys_progs_flag": bool,
    "apsearch": typing.NotRequired[str | None],
    "bindir": typing.NotRequired[str | None],
    "curl_flag": bool,
    "do_dotfiles_flag": bool,
    "do_extras_flag": bool,
    "echo_flag": bool,
    "make_backup": typing.NotRequired[str | None],
    "no_cert_verify_flag": bool,
    "no_recur_flag": bool,
    "proto": typing.NotRequired[str | None],
    "quick_flag": bool,
    "show_obsoletes_flag": bool,
    "show_obsoletes_grep_flag": bool,
    "show_system_progs_flag": bool,
    "sys_ok_flag": bool,
    "test_flag": bool,
    "test_protos_flag": bool,
    "revert_flag": bool,
    "local_package": typing.NotRequired[str | None],
    "prog_list": typing.NotRequired[list[str] | None],
    "package": typing.NotRequired[str | None],
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
        "@update.afni.binaries": v__update_afni_binaries_cargs,
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


def v__update_afni_binaries_params(
    defaults_flag: bool = False,
    help_flag: bool = False,
    help_sys_progs_flag: bool = False,
    apsearch: str | None = None,
    bindir: str | None = None,
    curl_flag: bool = False,
    do_dotfiles_flag: bool = False,
    do_extras_flag: bool = False,
    echo_flag: bool = False,
    make_backup: str | None = None,
    no_cert_verify_flag: bool = False,
    no_recur_flag: bool = False,
    proto: str | None = None,
    quick_flag: bool = False,
    show_obsoletes_flag: bool = False,
    show_obsoletes_grep_flag: bool = False,
    show_system_progs_flag: bool = False,
    sys_ok_flag: bool = False,
    test_flag: bool = False,
    test_protos_flag: bool = False,
    revert_flag: bool = False,
    local_package: str | None = None,
    prog_list: list[str] | None = None,
    package: str | None = None,
) -> VUpdateAfniBinariesParameters:
    """
    Build parameters.
    
    Args:
        defaults_flag: Install current package into abin.
        help_flag: Show this help.
        help_sys_progs_flag: List system programs that block update.
        apsearch: Specify getting apsearch updates.
        bindir: Set AFNI binary directory to ABIN.
        curl_flag: Default to curl instead of wget.
        do_dotfiles_flag: Try to initialize dot files if needed.
        do_extras_flag: Do extra niceties (beyond simple install).
        echo_flag: Turn on shell command echo.
        make_backup: Make a backup of binaries before replacing.
        no_cert_verify_flag: Do not verify the server CA certificate.
        no_recur_flag: Do not download and run new @uab script.
        proto: Access afni host via specified PROTOCOL.
        quick_flag: Quick mode, no fancies.
        show_obsoletes_flag: List any obsolete packages.
        show_obsoletes_grep_flag: List any obsolete packages (easy to grep).
        show_system_progs_flag: Show system programs that do not belong in\
            abin.
        sys_ok_flag: OK to update, even if system progs found.
        test_flag: Just attempt the download and quit.
        test_protos_flag: Test download protocols and exit.
        revert_flag: Revert binaries to previous version.
        local_package: Install local PACKAGE.tgz package.
        prog_list: Install given programs, not whole PACKAGE.
        package: Install distribution package PACKAGE.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@update.afni.binaries",
        "defaults_flag": defaults_flag,
        "help_flag": help_flag,
        "help_sys_progs_flag": help_sys_progs_flag,
        "curl_flag": curl_flag,
        "do_dotfiles_flag": do_dotfiles_flag,
        "do_extras_flag": do_extras_flag,
        "echo_flag": echo_flag,
        "no_cert_verify_flag": no_cert_verify_flag,
        "no_recur_flag": no_recur_flag,
        "quick_flag": quick_flag,
        "show_obsoletes_flag": show_obsoletes_flag,
        "show_obsoletes_grep_flag": show_obsoletes_grep_flag,
        "show_system_progs_flag": show_system_progs_flag,
        "sys_ok_flag": sys_ok_flag,
        "test_flag": test_flag,
        "test_protos_flag": test_protos_flag,
        "revert_flag": revert_flag,
    }
    if apsearch is not None:
        params["apsearch"] = apsearch
    if bindir is not None:
        params["bindir"] = bindir
    if make_backup is not None:
        params["make_backup"] = make_backup
    if proto is not None:
        params["proto"] = proto
    if local_package is not None:
        params["local_package"] = local_package
    if prog_list is not None:
        params["prog_list"] = prog_list
    if package is not None:
        params["package"] = package
    return params


def v__update_afni_binaries_cargs(
    params: VUpdateAfniBinariesParameters,
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
    cargs.append("@update.afni.binaries")
    if params.get("defaults_flag"):
        cargs.append("-defaults")
    if params.get("help_flag"):
        cargs.append("-help")
    if params.get("help_sys_progs_flag"):
        cargs.append("-help_sys_progs")
    if params.get("apsearch") is not None:
        cargs.extend([
            "-apsearch",
            params.get("apsearch")
        ])
    if params.get("bindir") is not None:
        cargs.extend([
            "-bindir",
            params.get("bindir")
        ])
    if params.get("curl_flag"):
        cargs.append("-curl")
    if params.get("do_dotfiles_flag"):
        cargs.append("-do_dotfiles")
    if params.get("do_extras_flag"):
        cargs.append("-do_extras")
    if params.get("echo_flag"):
        cargs.append("-echo")
    if params.get("make_backup") is not None:
        cargs.extend([
            "-make_backup",
            params.get("make_backup")
        ])
    if params.get("no_cert_verify_flag"):
        cargs.append("-no_cert_verify")
    if params.get("no_recur_flag"):
        cargs.append("-no_recur")
    if params.get("proto") is not None:
        cargs.extend([
            "-proto",
            params.get("proto")
        ])
    if params.get("quick_flag"):
        cargs.append("-quick")
    if params.get("show_obsoletes_flag"):
        cargs.append("-show_obsoletes")
    if params.get("show_obsoletes_grep_flag"):
        cargs.append("-show_obsoletes_grep")
    if params.get("show_system_progs_flag"):
        cargs.append("-show_system_progs")
    if params.get("sys_ok_flag"):
        cargs.append("-sys_ok")
    if params.get("test_flag"):
        cargs.append("-test")
    if params.get("test_protos_flag"):
        cargs.append("-test_protos")
    if params.get("revert_flag"):
        cargs.append("-revert")
    if params.get("local_package") is not None:
        cargs.extend([
            "-local_package",
            params.get("local_package")
        ])
    if params.get("prog_list") is not None:
        cargs.extend([
            "-prog_list",
            *params.get("prog_list")
        ])
    if params.get("package") is not None:
        cargs.extend([
            "-package",
            params.get("package")
        ])
    return cargs


def v__update_afni_binaries_outputs(
    params: VUpdateAfniBinariesParameters,
    execution: Execution,
) -> VUpdateAfniBinariesOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VUpdateAfniBinariesOutputs(
        root=execution.output_file("."),
    )
    return ret


def v__update_afni_binaries_execute(
    params: VUpdateAfniBinariesParameters,
    execution: Execution,
) -> VUpdateAfniBinariesOutputs:
    """
    Install or update AFNI binaries.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VUpdateAfniBinariesOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v__update_afni_binaries_cargs(params, execution)
    ret = v__update_afni_binaries_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__update_afni_binaries(
    defaults_flag: bool = False,
    help_flag: bool = False,
    help_sys_progs_flag: bool = False,
    apsearch: str | None = None,
    bindir: str | None = None,
    curl_flag: bool = False,
    do_dotfiles_flag: bool = False,
    do_extras_flag: bool = False,
    echo_flag: bool = False,
    make_backup: str | None = None,
    no_cert_verify_flag: bool = False,
    no_recur_flag: bool = False,
    proto: str | None = None,
    quick_flag: bool = False,
    show_obsoletes_flag: bool = False,
    show_obsoletes_grep_flag: bool = False,
    show_system_progs_flag: bool = False,
    sys_ok_flag: bool = False,
    test_flag: bool = False,
    test_protos_flag: bool = False,
    revert_flag: bool = False,
    local_package: str | None = None,
    prog_list: list[str] | None = None,
    package: str | None = None,
    runner: Runner | None = None,
) -> VUpdateAfniBinariesOutputs:
    """
    Install or update AFNI binaries.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        defaults_flag: Install current package into abin.
        help_flag: Show this help.
        help_sys_progs_flag: List system programs that block update.
        apsearch: Specify getting apsearch updates.
        bindir: Set AFNI binary directory to ABIN.
        curl_flag: Default to curl instead of wget.
        do_dotfiles_flag: Try to initialize dot files if needed.
        do_extras_flag: Do extra niceties (beyond simple install).
        echo_flag: Turn on shell command echo.
        make_backup: Make a backup of binaries before replacing.
        no_cert_verify_flag: Do not verify the server CA certificate.
        no_recur_flag: Do not download and run new @uab script.
        proto: Access afni host via specified PROTOCOL.
        quick_flag: Quick mode, no fancies.
        show_obsoletes_flag: List any obsolete packages.
        show_obsoletes_grep_flag: List any obsolete packages (easy to grep).
        show_system_progs_flag: Show system programs that do not belong in\
            abin.
        sys_ok_flag: OK to update, even if system progs found.
        test_flag: Just attempt the download and quit.
        test_protos_flag: Test download protocols and exit.
        revert_flag: Revert binaries to previous version.
        local_package: Install local PACKAGE.tgz package.
        prog_list: Install given programs, not whole PACKAGE.
        package: Install distribution package PACKAGE.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VUpdateAfniBinariesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__UPDATE_AFNI_BINARIES_METADATA)
    params = v__update_afni_binaries_params(defaults_flag=defaults_flag, help_flag=help_flag, help_sys_progs_flag=help_sys_progs_flag, apsearch=apsearch, bindir=bindir, curl_flag=curl_flag, do_dotfiles_flag=do_dotfiles_flag, do_extras_flag=do_extras_flag, echo_flag=echo_flag, make_backup=make_backup, no_cert_verify_flag=no_cert_verify_flag, no_recur_flag=no_recur_flag, proto=proto, quick_flag=quick_flag, show_obsoletes_flag=show_obsoletes_flag, show_obsoletes_grep_flag=show_obsoletes_grep_flag, show_system_progs_flag=show_system_progs_flag, sys_ok_flag=sys_ok_flag, test_flag=test_flag, test_protos_flag=test_protos_flag, revert_flag=revert_flag, local_package=local_package, prog_list=prog_list, package=package)
    return v__update_afni_binaries_execute(params, execution)


__all__ = [
    "V__UPDATE_AFNI_BINARIES_METADATA",
    "v__update_afni_binaries",
    "v__update_afni_binaries_params",
]
