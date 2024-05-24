# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


MRMATH_METADATA = Metadata(
    id="e9cd8fb2a78037bf3a831231e693bdea958f5847",
    name="mrmath",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrmathConfig:
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


class MrmathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrmath(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output image."""


def mrmath(
    input_: list[InputPathType],
    operation: typing.Literal["operation"],
    output: InputPathType,
    axis: int | None = None,
    keep_unary_axes: bool = False,
    datatype: typing.Literal["spec"] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrmathConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MrmathOutputs:
    """
    mrmath by J-Donald Tournier (jdtournier@gmail.com).
    
    Compute summary statistic on image intensities either across images, or
    along a specified axis of a single image.
    
    Supported operations are:
    
    mean, median, sum, product, rms (root-mean-square value), norm (vector
    2-norm), var (unbiased variance), std (unbiased standard deviation), min,
    max, absmax (maximum absolute value), magmax (value with maximum absolute
    value, preserving its sign).
    
    This command is used to traverse either along an image axis, or across a set
    of input images, calculating some statistic from the values along each
    traversal. If you are seeking to instead perform mathematical calculations
    that are done independently for each voxel, pleaase see the 'mrcalc'
    command.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mrmath.html
    
    Args:
        input_: the input image(s).
        operation: the operation to apply, one of: mean, median, sum, product,
            rms, norm, var, std, min, max, absmax, magmax.
        output: the output image.
        axis: perform operation along a specified axis of a single input image
        keep_unary_axes: Keep unary axes in input images prior to calculating
            the stats. The default is to wipe axes with single elements.
        datatype: specify output image data type. Valid choices are: float32,
            float32le, float32be, float64, float64le, float64be, int64, uint64,
            int64le, uint64le, int64be, uint64be, int32, uint32, int32le, uint32le,
            int32be, uint32be, int16, uint16, int16le, uint16le, int16be, uint16be,
            cfloat32, cfloat32le, cfloat32be, cfloat64, cfloat64le, cfloat64be,
            int8, uint8, bit.
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
        NamedTuple of outputs (described in `MrmathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRMATH_METADATA)
    cargs = []
    cargs.append("mrmath")
    if axis is not None:
        cargs.extend(["-axis", str(axis)])
    if keep_unary_axes:
        cargs.append("-keep_unary_axes")
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
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
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend([execution.input_file(f) for f in input_])
    cargs.append(operation)
    cargs.append(execution.input_file(output))
    ret = MrmathOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRMATH_METADATA",
    "MrmathConfig",
    "MrmathOutputs",
    "mrmath",
]
