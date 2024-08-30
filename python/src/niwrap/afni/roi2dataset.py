# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ROI2DATASET_METADATA = Metadata(
    id="79f509dbae00db9dd651a0181347643e79e51931",
    name="ROI2dataset",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class Roi2datasetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `roi2dataset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def roi2dataset(
    prefix: str,
    input_rois: list[InputPathType],
    keep_separate: bool = False,
    nodelist: str | None = None,
    nodelist_nodups: str | None = None,
    nodelist_with_roival: bool = False,
    label_dset: str | None = None,
    output_format: str | None = None,
    domain_parent_id: str | None = None,
    pad_to_node: float | int | None = None,
    pad_label: float | int | None = None,
    runner: Runner | None = None,
) -> Roi2datasetOutputs:
    """
    ROI2dataset by AFNI Team.
    
    Transforms a series of ROI files to a node dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/ROI2dataset.html
    
    Args:
        prefix: Prefix of output dataset.
        input_rois: ROI files to turn into a data set (space-separated list).\
            This parameter MUST be the last one on command line.
        keep_separate: Output one column (sub-brick) for each ROI value.
        nodelist: Prefix for a set of .1D files that contain a list of node\
            indices in the order they appear in an ROI.
        nodelist_nodups: Prefix for a set of .1D files that contain a list of\
            node indices in the order they appear in an ROI, with duplicate nodes\
            removed.
        nodelist_with_roival: Also add the ROI value as a second column in .1D\
            files output by -nodelist.
        label_dset: Write a label dataset instead of a simple dataset. Sets\
            output format to NIML.
        output_format: Output format of dataset. One of: ni_bi, ni_as, 1D.
        domain_parent_id: Idcode of domain parent. Only ROIs with the same\
            domain parent are included in the output.
        pad_to_node: Output a full dataset from node 0 to node max_index (total\
            of max_index + 1 nodes).
        pad_label: Use padding_label (an integer) to label nodes not part of\
            any ROI. Default is 0.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Roi2datasetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ROI2DATASET_METADATA)
    cargs = []
    cargs.append("ROI2dataset")
    cargs.append("-prefix")
    cargs.append(prefix)
    cargs.extend([execution.input_file(f) for f in input_rois])
    if keep_separate:
        cargs.append("-keep_separate")
    if nodelist is not None:
        cargs.extend(["-nodelist", nodelist])
    if nodelist_nodups is not None:
        cargs.extend(["-nodelist.nodups", nodelist_nodups])
    if nodelist_with_roival:
        cargs.append("-nodelist_with_ROIval")
    if label_dset is not None:
        cargs.extend(["-label_dset", label_dset])
    if output_format is not None:
        cargs.extend(["-of", output_format])
    if domain_parent_id is not None:
        cargs.extend(["-dom_par_id", domain_parent_id])
    if pad_to_node is not None:
        cargs.extend(["-pad_to_node", str(pad_to_node)])
    if pad_label is not None:
        cargs.extend(["-pad_label", str(pad_label)])
    ret = Roi2datasetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ROI2DATASET_METADATA",
    "Roi2datasetOutputs",
    "roi2dataset",
]