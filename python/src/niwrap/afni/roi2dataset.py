# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

ROI2DATASET_METADATA = Metadata(
    id="5ce644f007ce2ecc979c958450e6f9ce7de594be.boutiques",
    name="ROI2dataset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
Roi2datasetParameters = typing.TypedDict('Roi2datasetParameters', {
    "__STYX_TYPE__": typing.Literal["ROI2dataset"],
    "prefix": str,
    "input_rois": list[InputPathType],
    "keep_separate": bool,
    "nodelist": typing.NotRequired[str | None],
    "nodelist_nodups": typing.NotRequired[str | None],
    "nodelist_with_roival": bool,
    "label_dset": typing.NotRequired[str | None],
    "output_format": typing.NotRequired[str | None],
    "domain_parent_id": typing.NotRequired[str | None],
    "pad_to_node": typing.NotRequired[float | None],
    "pad_label": typing.NotRequired[float | None],
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "ROI2dataset": roi2dataset_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
    }.get(t)


class Roi2datasetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `roi2dataset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def roi2dataset_params(
    prefix: str,
    input_rois: list[InputPathType],
    keep_separate: bool = False,
    nodelist: str | None = None,
    nodelist_nodups: str | None = None,
    nodelist_with_roival: bool = False,
    label_dset: str | None = None,
    output_format: str | None = None,
    domain_parent_id: str | None = None,
    pad_to_node: float | None = None,
    pad_label: float | None = None,
) -> Roi2datasetParameters:
    """
    Build parameters.
    
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
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ROI2dataset",
        "prefix": prefix,
        "input_rois": input_rois,
        "keep_separate": keep_separate,
        "nodelist_with_roival": nodelist_with_roival,
    }
    if nodelist is not None:
        params["nodelist"] = nodelist
    if nodelist_nodups is not None:
        params["nodelist_nodups"] = nodelist_nodups
    if label_dset is not None:
        params["label_dset"] = label_dset
    if output_format is not None:
        params["output_format"] = output_format
    if domain_parent_id is not None:
        params["domain_parent_id"] = domain_parent_id
    if pad_to_node is not None:
        params["pad_to_node"] = pad_to_node
    if pad_label is not None:
        params["pad_label"] = pad_label
    return params


def roi2dataset_cargs(
    params: Roi2datasetParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("ROI2dataset")
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    cargs.extend([execution.input_file(f) for f in params.get("input_rois")])
    if params.get("keep_separate"):
        cargs.append("-keep_separate")
    if params.get("nodelist") is not None:
        cargs.extend([
            "-nodelist",
            params.get("nodelist")
        ])
    if params.get("nodelist_nodups") is not None:
        cargs.extend([
            "-nodelist.nodups",
            params.get("nodelist_nodups")
        ])
    if params.get("nodelist_with_roival"):
        cargs.append("-nodelist_with_ROIval")
    if params.get("label_dset") is not None:
        cargs.extend([
            "-label_dset",
            params.get("label_dset")
        ])
    if params.get("output_format") is not None:
        cargs.extend([
            "-of",
            params.get("output_format")
        ])
    if params.get("domain_parent_id") is not None:
        cargs.extend([
            "-dom_par_id",
            params.get("domain_parent_id")
        ])
    if params.get("pad_to_node") is not None:
        cargs.extend([
            "-pad_to_node",
            str(params.get("pad_to_node"))
        ])
    if params.get("pad_label") is not None:
        cargs.extend([
            "-pad_label",
            str(params.get("pad_label"))
        ])
    return cargs


def roi2dataset_outputs(
    params: Roi2datasetParameters,
    execution: Execution,
) -> Roi2datasetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Roi2datasetOutputs(
        root=execution.output_file("."),
    )
    return ret


def roi2dataset_execute(
    params: Roi2datasetParameters,
    execution: Execution,
) -> Roi2datasetOutputs:
    """
    Transforms a series of ROI files to a node dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Roi2datasetOutputs`).
    """
    params = execution.params(params)
    cargs = roi2dataset_cargs(params, execution)
    ret = roi2dataset_outputs(params, execution)
    execution.run(cargs)
    return ret


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
    pad_to_node: float | None = None,
    pad_label: float | None = None,
    runner: Runner | None = None,
) -> Roi2datasetOutputs:
    """
    Transforms a series of ROI files to a node dataset.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
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
    params = roi2dataset_params(prefix=prefix, input_rois=input_rois, keep_separate=keep_separate, nodelist=nodelist, nodelist_nodups=nodelist_nodups, nodelist_with_roival=nodelist_with_roival, label_dset=label_dset, output_format=output_format, domain_parent_id=domain_parent_id, pad_to_node=pad_to_node, pad_label=pad_label)
    return roi2dataset_execute(params, execution)


__all__ = [
    "ROI2DATASET_METADATA",
    "Roi2datasetOutputs",
    "Roi2datasetParameters",
    "roi2dataset",
    "roi2dataset_params",
]
