# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


TSFINFO_METADATA = Metadata(
    id="ceba2a22604b0d92193f70c37430f3acedbf849c",
    name="tsfinfo",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TsfinfoConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class TsfinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsfinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tsfinfo(
    tracks: list[InputPathType],
    count: bool = False,
    ascii_: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfinfoConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TsfinfoOutputs:
    """
    tsfinfo by David Raffelt (david.raffelt@florey.edu.au).
    
    Print out information about a track scalar file.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tsfinfo.html
    
    Args:
        tracks: the input track scalar file.
        count: count number of tracks in file explicitly, ignoring the header
        ascii_: save values of each track scalar file in individual ascii files,
            with the specified prefix.
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `TsfinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TSFINFO_METADATA)
    cargs = []
    cargs.append("tsfinfo")
    if count:
        cargs.append("-count")
    if ascii_ is not None:
        cargs.extend(["-ascii", ascii_])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend(["-config", *[a for c in [s.run(execution) for s in config] for a in c]])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(["", *[execution.input_file(f) for f in tracks]])
    ret = TsfinfoOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TSFINFO_METADATA",
    "TsfinfoConfig",
    "TsfinfoOutputs",
    "tsfinfo",
]
