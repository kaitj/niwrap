# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_ZEROPAD_METADATA = Metadata(
    id="89b57cae1500d60d81ab1eb191c2415cbf411ff1",
    name="3dZeropad",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dZeropadOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zeropad(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset_brik: OutputPathType | None
    """Output dataset (BRIK format)"""
    output_dataset_head: OutputPathType | None
    """Output dataset (HEAD format)"""


def v_3d_zeropad(
    dataset: InputPathType,
    i: float | int | None = None,
    s: float | int | None = None,
    a: float | int | None = None,
    p: float | int | None = None,
    l: float | int | None = None,
    r: float | int | None = None,
    z: float | int | None = None,
    rl: float | int | None = None,
    ap: float | int | None = None,
    is_: float | int | None = None,
    pad2even: bool = False,
    mm_flag: bool = False,
    master_dataset: InputPathType | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dZeropadOutputs:
    """
    3dZeropad by AFNI Team.
    
    Adds planes of zeros to a dataset (i.e., pads it out). Negative 'add' count
    means to cut a dataset down in size.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dZeropad.html
    
    Args:
        dataset: Input dataset.
        i: Adds 'n' planes of zero at the Inferior edge.
        s: Adds 'n' planes of zero at the Superior edge.
        a: Adds 'n' planes of zero at the Anterior edge.
        p: Adds 'n' planes of zero at the Posterior edge.
        l: Adds 'n' planes of zero at the Left edge.
        r: Adds 'n' planes of zero at the Right edge.
        z: Adds 'n' planes of zeros on EACH of the dataset z-axis\
            (slice-direction) faces.
        rl: Add/cut planes symmetrically to make the resulting volume have 'a'\
            slices in the Right/Left direction.
        ap: Add/cut planes symmetrically to make the resulting volume have 'b'\
            slices in the Anterior/Posterior direction.
        is_: Add/cut planes symmetrically to make the resulting volume have 'c'\
            slices in the Inferior/Superior direction.
        pad2even: Add 0 or 1 plane in each of the R/A/S directions, giving each\
            axis an even number of slices.
        mm_flag: Pad counts 'n' are in mm instead of slices.
        master_dataset: Match the volume described in dataset 'mset'. 'mset'\
            must have the same orientation and grid spacing as dataset to be\
            padded.
        prefix: Write result into dataset with prefix 'ppp'. Default is\
            'zeropad'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZeropadOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZEROPAD_METADATA)
    cargs = []
    cargs.append("3dZeropad")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dataset))
    ret = V3dZeropadOutputs(
        root=execution.output_file("."),
        output_dataset_brik=execution.output_file(f"{prefix}+orig.BRIK") if prefix is not None else None,
        output_dataset_head=execution.output_file(f"{prefix}+orig.HEAD") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dZeropadOutputs",
    "V_3D_ZEROPAD_METADATA",
    "v_3d_zeropad",
]