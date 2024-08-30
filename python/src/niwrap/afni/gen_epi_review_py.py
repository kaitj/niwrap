# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

GEN_EPI_REVIEW_METADATA = Metadata(
    id="2f62502bf3ac29e0f478fa955db07cf611d2a72f",
    name="gen_epi_review",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class GenEpiReviewOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gen_epi_review(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def gen_epi_review(
    datasets: list[str],
    script_name: str | None = None,
    verbosity: float | int | None = None,
    windows: list[str] | None = None,
    image_size: list[float | int] | None = None,
    image_xoffset: float | int | None = None,
    image_yoffset: float | int | None = None,
    graph_size: list[float | int] | None = None,
    graph_xoffset: float | int | None = None,
    graph_yoffset: float | int | None = None,
    runner: Runner | None = None,
) -> GenEpiReviewOutputs:
    """
    gen_epi_review by AFNI Team.
    
    Generate an AFNI processing script to review EPI data.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/gen_epi_review.py.html
    
    Args:
        datasets: Specify input datasets for processing.
        script_name: Specify the name of the generated script.
        verbosity: Specify a verbosity level.
        windows: Specify the image windows to open.
        image_size: Set image dimensions, in pixels.
        image_xoffset: Set the X-offset for the image, in pixels.
        image_yoffset: Set the Y-offset for the image, in pixels.
        graph_size: Set graph dimensions, in pixels.
        graph_xoffset: Set the X-offset for the graph, in pixels.
        graph_yoffset: Set the Y-offset for the graph, in pixels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GenEpiReviewOutputs`).
    """
    runner = runner or get_global_runner()
    if image_size is not None and (len(image_size) != 2): 
        raise ValueError(f"Length of 'image_size' must be 2 but was {len(image_size)}")
    if graph_size is not None and (len(graph_size) != 2): 
        raise ValueError(f"Length of 'graph_size' must be 2 but was {len(graph_size)}")
    execution = runner.start_execution(GEN_EPI_REVIEW_METADATA)
    cargs = []
    cargs.append("gen_epi_review.py")
    cargs.extend(["-dsets", *datasets])
    if script_name is not None:
        cargs.extend(["-script", script_name])
    if windows is not None:
        cargs.extend(["-windows", *windows])
    if verbosity is not None:
        cargs.extend(["-verb", str(verbosity)])
    if image_size is not None:
        cargs.extend(["-im_size", *map(str, image_size)])
    if image_xoffset is not None:
        cargs.extend(["-im_xoff", str(image_xoffset)])
    if image_yoffset is not None:
        cargs.extend(["-im_yoff", str(image_yoffset)])
    if graph_size is not None:
        cargs.extend(["-gr_size", *map(str, graph_size)])
    if graph_xoffset is not None:
        cargs.extend(["-gr_xoff", str(graph_xoffset)])
    if graph_yoffset is not None:
        cargs.extend(["-gr_yoff", str(graph_yoffset)])
    ret = GenEpiReviewOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GEN_EPI_REVIEW_METADATA",
    "GenEpiReviewOutputs",
    "gen_epi_review",
]