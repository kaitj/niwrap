# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


PEAKS2AMP_METADATA = Metadata(
    id="6195b5016f6d674a5bc6010e961ebe0378c1626d",
    name="peaks2amp",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Peaks2ampConfig:
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


class Peaks2ampOutputs(typing.NamedTuple):
    """
    Output object returned when calling `peaks2amp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    amplitudes: OutputPathType
    """the output amplitudes image."""


def peaks2amp(
    directions: InputPathType,
    amplitudes: InputPathType,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Peaks2ampConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Peaks2ampOutputs:
    """
    peaks2amp by J-Donald Tournier (jdtournier@gmail.com).
    
    Extract amplitudes from a peak directions image.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/peaks2amp.html
    
    Args:
        directions: the input directions image. Each volume corresponds to the
            x, y & z component of each direction vector in turn.
        amplitudes: the output amplitudes image.
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
        NamedTuple of outputs (described in `Peaks2ampOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PEAKS2AMP_METADATA)
    cargs = []
    cargs.append("peaks2amp")
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
    cargs.extend(["", execution.input_file(directions)])
    cargs.extend(["", execution.input_file(amplitudes)])
    ret = Peaks2ampOutputs(
        root=execution.output_file("."),
        amplitudes=execution.output_file(f"{pathlib.Path(amplitudes).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PEAKS2AMP_METADATA",
    "Peaks2ampConfig",
    "Peaks2ampOutputs",
    "peaks2amp",
]
