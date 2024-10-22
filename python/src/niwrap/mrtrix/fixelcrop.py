# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIXELCROP_METADATA = Metadata(
    id="df585f30c2a7738dc8886c2e7c7172b7e6cdc09c.boutiques",
    name="fixelcrop",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class FixelcropConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class FixelcropOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelcrop(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_fixel_directory: OutputPathType
    """the output directory to store the cropped directions and data files"""


def fixelcrop(
    input_fixel_directory: InputPathType,
    input_fixel_mask: InputPathType,
    output_fixel_directory: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelcropConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelcropOutputs:
    """
    Crop/remove fixels from sparse fixel image using a binary fixel mask.
    
    The mask must be input as a fixel data file the same dimensions as the fixel
    data file(s) to be cropped.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        input_fixel_directory: input fixel directory, all data files and\
            directions file will be cropped and saved in the output fixel directory.
        input_fixel_mask: the input fixel data file defining which fixels to\
            crop. Fixels with zero values will be removed.
        output_fixel_directory: the output directory to store the cropped\
            directions and data files.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FixelcropOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCROP_METADATA)
    cargs = []
    cargs.append("fixelcrop")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(input_fixel_directory))
    cargs.append(execution.input_file(input_fixel_mask))
    cargs.append(output_fixel_directory)
    ret = FixelcropOutputs(
        root=execution.output_file("."),
        output_fixel_directory=execution.output_file(output_fixel_directory),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXELCROP_METADATA",
    "FixelcropConfig",
    "FixelcropOutputs",
    "fixelcrop",
]
