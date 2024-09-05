# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1DGRAYPLOT_METADATA = Metadata(
    id="c9c54b4f4c955678553f1bde775145e0b7ebb3bb",
    name="1dgrayplot",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dgrayplotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dgrayplot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1dgrayplot(
    tsfile: InputPathType,
    install: bool = False,
    ignore: float | int | None = None,
    flip: bool = False,
    sep: bool = False,
    use: float | int | None = None,
    ps: bool = False,
    runner: Runner | None = None,
) -> V1dgrayplotOutputs:
    """
    1dgrayplot by AFNI Team.
    
    Graphs the columns of a *.1D type time series file to the screen in
    grayscale.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dgrayplot.html
    
    Args:
        tsfile: Input time series file (*.1D format).
        install: Install a new X11 colormap (for X11 PseudoColor).
        ignore: Skip first 'nn' rows in the input file [default = 0].
        flip: Plot x and y axes interchanged [default: data columns plotted\
            DOWN the screen].
        sep: Separate scales for each column.
        use: Plot 'mm' points [default: all of them].
        ps: Don't draw plot in a window; write it to stdout in PostScript\
            format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dgrayplotOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DGRAYPLOT_METADATA)
    cargs = []
    cargs.append("1dgrayplot")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(tsfile))
    ret = V1dgrayplotOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dgrayplotOutputs",
    "V_1DGRAYPLOT_METADATA",
    "v_1dgrayplot",
]