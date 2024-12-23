# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ZEROPAD_METADATA = Metadata(
    id="69b80943bdd6b997541b13be76f096b8bce260d4.boutiques",
    name="3dZeropad",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
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
    i: float | None = None,
    s: float | None = None,
    a: float | None = None,
    p: float | None = None,
    l: float | None = None,
    r: float | None = None,
    z: float | None = None,
    rl: float | None = None,
    ap: float | None = None,
    is_: float | None = None,
    pad2even: bool = False,
    mm_flag: bool = False,
    master_dataset: InputPathType | None = None,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dZeropadOutputs:
    """
    Adds planes of zeros to a dataset (i.e., pads it out). Negative 'add' count
    means to cut a dataset down in size.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
    cargs.append(execution.input_file(dataset))
    if i is not None:
        cargs.extend([
            "-I",
            str(i)
        ])
    if s is not None:
        cargs.extend([
            "-S",
            str(s)
        ])
    if a is not None:
        cargs.extend([
            "-A",
            str(a)
        ])
    if p is not None:
        cargs.extend([
            "-P",
            str(p)
        ])
    if l is not None:
        cargs.extend([
            "-L",
            str(l)
        ])
    if r is not None:
        cargs.extend([
            "-R",
            str(r)
        ])
    if z is not None:
        cargs.extend([
            "-z",
            str(z)
        ])
    if rl is not None:
        cargs.extend([
            "-RL",
            str(rl)
        ])
    if ap is not None:
        cargs.extend([
            "-AP",
            str(ap)
        ])
    if is_ is not None:
        cargs.extend([
            "-IS",
            str(is_)
        ])
    if pad2even:
        cargs.append("-pad2evens")
    if mm_flag:
        cargs.append("-mm")
    if master_dataset is not None:
        cargs.extend([
            "-master",
            execution.input_file(master_dataset)
        ])
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    ret = V3dZeropadOutputs(
        root=execution.output_file("."),
        output_dataset_brik=execution.output_file(prefix + "+orig.BRIK") if (prefix is not None) else None,
        output_dataset_head=execution.output_file(prefix + "+orig.HEAD") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dZeropadOutputs",
    "V_3D_ZEROPAD_METADATA",
    "v_3d_zeropad",
]
