# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


MERGE_METADATA = Metadata(
    id="f2741a6793083f114232e821972234f922edfe01",
    name="Merge",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class MergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Merged output file."""


def merge(
    runner: Runner,
    in_files: list[InputPathType],
    merged_file: str,
    dimension: typing.Literal["t", "x", "y", "z", "a"] | None = None,
    dimension_tr: bool = False,
    tr: float | int | None = None,
    volume_number: int | None = None,
) -> MergeOutputs:
    """
    Concatenate image files into a single output. This concatenation can be in time,
    or in X, Y or Z. All image dimensions (except for the one being concatenated
    over) must be the same in all input images. For example, this can be used to
    take multiple 3D files (eg as output by SPM) and create a single 4D image file.
    
    Args:
        runner: Command runner
        in_files: A list of images to merge together.
        merged_file: Merged output file.
        dimension: 't' or 'x' or 'y' or 'z' or 'a'. Dimension along which to
            merge, optionally set tr input when dimension is t.
        dimension_tr: Concatenate images in time and set out image tr to final
            option value
        tr: Use to specify tr in seconds (default is 1.00 sec), overrides
            dimension and sets it to tr.
        volume_number: Only use volume <N> from each input file (first volume is
            0 and not 1).
    Returns:
        NamedTuple of outputs (described in `MergeOutputs`).
    """
    if not (
        dimension_tr ==
        (tr is not None)
    ):
        raise ValueError(
            "All or none of the following arguments must be specified:\n"
            "dimension_tr,\n"
            "tr"
        )
    if (
        (dimension is not None) +
        dimension_tr
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "dimension,\n"
            "dimension_tr"
        )
    if not (
        (dimension is not None) or
        dimension_tr
    ):
        raise ValueError(
            "One of the following arguments must be specified:\n"
            "- dimension\n"
            "- dimension_tr"
        )
    execution = runner.start_execution(MERGE_METADATA)
    cargs = []
    cargs.append("fslmerge")
    if dimension is not None:
        cargs.append(("-" + dimension))
    if dimension_tr:
        cargs.append("-tr")
    cargs.append(merged_file)
    cargs.extend([execution.input_file(f) for f in in_files])
    if tr is not None:
        cargs.append(str(tr))
    if volume_number is not None:
        cargs.extend(["-n", str(volume_number)])
    ret = MergeOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{merged_file}", optional=True),
    )
    execution.run(cargs)
    return ret
