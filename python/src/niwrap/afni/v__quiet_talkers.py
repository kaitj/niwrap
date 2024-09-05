# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__QUIET_TALKERS_METADATA = Metadata(
    id="4e4b2854af68f2789084a083c9af42a086ef0ff6",
    name="@Quiet_Talkers",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VQuietTalkersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__quiet_talkers(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__quiet_talkers(
    sudo: bool = False,
    prog: list[str] | None = None,
    npb_val: list[float | int] | None = None,
    npb_range: list[float | int] | None = None,
    pif_key: str | None = None,
    no_npb: bool = False,
    list_: bool = False,
    quiet: bool = False,
    runner: Runner | None = None,
) -> VQuietTalkersOutputs:
    """
    @Quiet_Talkers by AFNI Team.
    
    A script to find and kill AFNI processes.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Quiet_Talkers.html
    
    Args:
        sudo: Invoke higher powers to kill processes that you do not own.
        prog: Instead of the default program list, only kill the specified\
            program. You can use multiple -prog options.
        npb_val: Kill those programs using NIML port block NV.
        npb_range: Kill those using NIML port blocks between NV0 and NV1.
        pif_key: Kill those programs that have a string matching KEY_STRING in\
            their commandline.
        no_npb: Kill any program in the list regardless of -npb options or -pif.
        list_: Just list process numbers, don't run kill command.
        quiet: Do it quietly.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VQuietTalkersOutputs`).
    """
    runner = runner or get_global_runner()
    if npb_range is not None and (len(npb_range) != 2): 
        raise ValueError(f"Length of 'npb_range' must be 2 but was {len(npb_range)}")
    execution = runner.start_execution(V__QUIET_TALKERS_METADATA)
    cargs = []
    cargs.append("@Quiet_Talkers")
    if sudo:
        cargs.append("-sudo")
    if prog is not None:
        cargs.extend(["-prog", *prog])
    if npb_val is not None:
        cargs.extend(["-npb_val", *map(str, npb_val)])
    if npb_range is not None:
        cargs.extend(["-npb_range", *map(str, npb_range)])
    if pif_key is not None:
        cargs.extend(["-pif", pif_key])
    if no_npb:
        cargs.append("-no_npb")
    if list_:
        cargs.append("-list")
    if quiet:
        cargs.append("-quiet")
    ret = VQuietTalkersOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VQuietTalkersOutputs",
    "V__QUIET_TALKERS_METADATA",
    "v__quiet_talkers",
]