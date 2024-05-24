# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRHISTMATCH_METADATA = Metadata(
    id="e4897e06ec33ae448ea49aa022df30a84be3ecd8",
    name="mrhistmatch",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrhistmatchConfig:
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


class MrhistmatchOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrhistmatch(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image"""


def mrhistmatch(
    type_: typing.Literal["type"],
    input_: InputPathType,
    target: InputPathType,
    output: InputPathType,
    mask_input: InputPathType | None = None,
    mask_target: InputPathType | None = None,
    bins: int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrhistmatchConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrhistmatchOutputs:
    """
    mrhistmatch by Robert E. Smith (robert.smith@florey.edu.au).
    
    Modify the intensities of one image to match the histogram of another.
    
    
    
    References:
    
    * If using inverse contrast normalization for inter-modal (DWI - T1)
    registration:
    Bhushan, C.; Haldar, J. P.; Choi, S.; Joshi, A. A.; Shattuck, D. W. & Leahy,
    R. M. Co-registration and distortion correction of diffusion and anatomical
    images based on inverse contrast normalization. NeuroImage, 2015, 115,
    269-280.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrhistmatch.html
    
    Args:
        type_: type of histogram matching to perform; options are:
            scale,linear,nonlinear
        input_: the input image to be modified
        target: the input image from which to derive the target histogram
        output: the output image
        mask_input: only generate input histogram based on a specified binary
            mask image
        mask_target: only generate target histogram based on a specified binary
            mask image
        bins: the number of bins to use to generate the histograms
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
        NamedTuple of outputs (described in `MrhistmatchOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRHISTMATCH_METADATA)
    cargs = []
    cargs.append("mrhistmatch")
    if mask_input is not None:
        cargs.extend(["-mask_input", execution.input_file(mask_input)])
    if mask_target is not None:
        cargs.extend(["-mask_target", execution.input_file(mask_target)])
    if bins is not None:
        cargs.extend(["-bins", str(bins)])
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
    cargs.extend(["", type_])
    cargs.extend(["", execution.input_file(input_)])
    cargs.extend(["", execution.input_file(target)])
    cargs.extend(["", execution.input_file(output)])
    ret = MrhistmatchOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRHISTMATCH_METADATA",
    "MrhistmatchConfig",
    "MrhistmatchOutputs",
    "mrhistmatch",
]
