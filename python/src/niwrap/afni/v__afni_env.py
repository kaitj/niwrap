# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__AFNI_ENV_METADATA = Metadata(
    id="16f129198419674aa6c4039e01dd5d599fafb94f.boutiques",
    name="@AfniEnv",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VAfniEnvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__afni_env(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__afni_env(
    set_flag: list[str] | None = None,
    unset_flag: str | None = None,
    get_flag: str | None = None,
    help_flag: bool = False,
    help_web_flag_alias: bool = False,
    help_view_flag_alias: bool = False,
    all_opts_flag: bool = False,
    help_find_flag: str | None = None,
    runner: Runner | None = None,
) -> VAfniEnvOutputs:
    """
    Script to set or unset an AFNI environment variable in your .afnirc file.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        set_flag: Set environment variable NAME to value VALUE.
        unset_flag: Unset environment variable NAME.
        get_flag: Get the value of environment variable NAME.
        help_flag: Display the help message for @AfniEnv script.
        help_web_flag_alias: Same as -h_web.
        help_view_flag_alias: Same as -h_view.
        all_opts_flag: List all of the options for this script.
        help_find_flag: Search for lines containing WORD in -help output.\
            Search is approximate.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAfniEnvOutputs`).
    """
    if set_flag is not None and (len(set_flag) != 2): 
        raise ValueError(f"Length of 'set_flag' must be 2 but was {len(set_flag)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__AFNI_ENV_METADATA)
    cargs = []
    cargs.append("@AfniEnv")
    if set_flag is not None:
        cargs.extend([
            "-set",
            *set_flag
        ])
    if unset_flag is not None:
        cargs.extend([
            "-unset",
            unset_flag
        ])
    if get_flag is not None:
        cargs.extend([
            "-get",
            get_flag
        ])
    if help_flag:
        cargs.append("-help")
    if help_web_flag_alias:
        cargs.append("-hweb")
    if help_view_flag_alias:
        cargs.append("-hview")
    if all_opts_flag:
        cargs.append("-all_opts")
    if help_find_flag is not None:
        cargs.extend([
            "-h_find",
            help_find_flag
        ])
    ret = VAfniEnvOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VAfniEnvOutputs",
    "V__AFNI_ENV_METADATA",
    "v__afni_env",
]
