# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CLUST_EXP_STAT_PARSE_PY_METADATA = Metadata(
    id="0ee922f117a5e881955bf4f23aba845f4aef47bb.boutiques",
    name="ClustExp_StatParse.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
ClustExpStatParsePyParameters = typing.TypedDict('ClustExpStatParsePyParameters', {
    "__STYX_TYPE__": typing.Literal["ClustExp_StatParse.py"],
    "statdset": InputPathType,
    "meanbrik": float,
    "threshbrik": float,
    "subjdset": InputPathType,
    "subjtable": InputPathType,
    "master": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "pval": typing.NotRequired[float | None],
    "minvox": typing.NotRequired[float | None],
    "atlas": typing.NotRequired[str | None],
    "session": typing.NotRequired[str | None],
    "noshiny": bool,
    "overwrite": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "ClustExp_StatParse.py": clust_exp_stat_parse_py_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "ClustExp_StatParse.py": clust_exp_stat_parse_py_outputs,
    }
    return vt.get(t)


class ClustExpStatParsePyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `clust_exp_stat_parse_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    table_mean: OutputPathType | None
    """Table with all data extracted from all subjects."""
    group_table: OutputPathType | None
    """Table with information parsed from the statistics data set history."""
    v_3dclust_output: OutputPathType | None
    """Output directly from 3dclust."""
    clusters_output: OutputPathType | None
    """Cleaned up version of the whereami output."""
    statinfo_output: OutputPathType | None
    """Summary info for the shiny app."""
    thresholded_dataset: OutputPathType | None
    """A new data set from input statistics, thresholded at uncorrected p
    value."""
    thresholded_mask_dataset: OutputPathType | None
    """Integer labeled mask of the thresholded image with cluster sizes at least
    as big as the -MinVox."""
    master_copy: OutputPathType | None
    """A NIfTI copy of the master file provided that may have been resampled."""


def clust_exp_stat_parse_py_params(
    statdset: InputPathType,
    meanbrik: float,
    threshbrik: float,
    subjdset: InputPathType,
    subjtable: InputPathType,
    master: InputPathType,
    prefix: str | None = None,
    pval: float | None = None,
    minvox: float | None = None,
    atlas: str | None = None,
    session: str | None = None,
    noshiny: bool = False,
    overwrite: bool = False,
) -> ClustExpStatParsePyParameters:
    """
    Build parameters.
    
    Args:
        statdset: Statistics dataset.
        meanbrik: Mean subbrik (integer >= 0).
        threshbrik: Threshold subbrik. Might be the same as MeanBrik (integer\
            >= 0).
        subjdset: Labeled dataset with all subjects (from @ClustExp_CatLab).
        subjtable: Table with subject labels and input datasets.
        master: Master data set for underlay.
        prefix: Name for output (no path).
        pval: Uncorrected p value for thresholding.
        minvox: Minimum voxels in cluster.
        atlas: Atlas name for lookup (list at: whereami -help).
        session: Output parent folder if you don't want the current working\
            directory.
        noshiny: Do not create shiny app.
        overwrite: Remove previous folder with same PREFIX.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ClustExp_StatParse.py",
        "statdset": statdset,
        "meanbrik": meanbrik,
        "threshbrik": threshbrik,
        "subjdset": subjdset,
        "subjtable": subjtable,
        "master": master,
        "noshiny": noshiny,
        "overwrite": overwrite,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if pval is not None:
        params["pval"] = pval
    if minvox is not None:
        params["minvox"] = minvox
    if atlas is not None:
        params["atlas"] = atlas
    if session is not None:
        params["session"] = session
    return params


def clust_exp_stat_parse_py_cargs(
    params: ClustExpStatParsePyParameters,
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
    cargs.append("ClustExp_StatParse.py")
    cargs.extend([
        "-StatDSET",
        execution.input_file(params.get("statdset"))
    ])
    cargs.extend([
        "-MeanBrik",
        str(params.get("meanbrik"))
    ])
    cargs.extend([
        "-ThreshBrik",
        str(params.get("threshbrik"))
    ])
    cargs.extend([
        "-SubjDSET",
        execution.input_file(params.get("subjdset"))
    ])
    cargs.extend([
        "-SubjTable",
        execution.input_file(params.get("subjtable"))
    ])
    cargs.extend([
        "-master",
        execution.input_file(params.get("master"))
    ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("pval") is not None:
        cargs.extend([
            "-p",
            str(params.get("pval"))
        ])
    if params.get("minvox") is not None:
        cargs.extend([
            "-MinVox",
            str(params.get("minvox"))
        ])
    if params.get("atlas") is not None:
        cargs.extend([
            "-atlas",
            params.get("atlas")
        ])
    if params.get("session") is not None:
        cargs.extend([
            "-session",
            params.get("session")
        ])
    if params.get("noshiny"):
        cargs.append("-NoShiny")
    if params.get("overwrite"):
        cargs.append("-overwrite")
    return cargs


def clust_exp_stat_parse_py_outputs(
    params: ClustExpStatParsePyParameters,
    execution: Execution,
) -> ClustExpStatParsePyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ClustExpStatParsePyOutputs(
        root=execution.output_file("."),
        table_mean=execution.output_file(params.get("prefix") + "_p_uncor_" + str(params.get("pval")) + "_mean.csv") if (params.get("prefix") is not None and params.get("pval") is not None) else None,
        group_table=execution.output_file(params.get("prefix") + "_GroupTable.csv") if (params.get("prefix") is not None) else None,
        v_3dclust_output=execution.output_file(params.get("prefix") + "_p_uncor_" + str(params.get("pval")) + "_3dclust.1D") if (params.get("prefix") is not None and params.get("pval") is not None) else None,
        clusters_output=execution.output_file(params.get("prefix") + "_p_uncor_" + str(params.get("pval")) + "_clusters.csv") if (params.get("prefix") is not None and params.get("pval") is not None) else None,
        statinfo_output=execution.output_file(params.get("prefix") + "_StatInfo.csv") if (params.get("prefix") is not None) else None,
        thresholded_dataset=execution.output_file(params.get("prefix") + "_p_uncor_" + str(params.get("pval")) + ".nii.gz") if (params.get("prefix") is not None and params.get("pval") is not None) else None,
        thresholded_mask_dataset=execution.output_file(params.get("prefix") + "_p_uncor_" + str(params.get("pval")) + "_mask.nii.gz") if (params.get("prefix") is not None and params.get("pval") is not None) else None,
        master_copy=execution.output_file(params.get("prefix") + "_master.nii.gz") if (params.get("prefix") is not None) else None,
    )
    return ret


def clust_exp_stat_parse_py_execute(
    params: ClustExpStatParsePyParameters,
    execution: Execution,
) -> ClustExpStatParsePyOutputs:
    """
    Parser for statistical data sets and subject data sets, generating several
    outputs for further analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ClustExpStatParsePyOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = clust_exp_stat_parse_py_cargs(params, execution)
    ret = clust_exp_stat_parse_py_outputs(params, execution)
    execution.run(cargs)
    return ret


def clust_exp_stat_parse_py(
    statdset: InputPathType,
    meanbrik: float,
    threshbrik: float,
    subjdset: InputPathType,
    subjtable: InputPathType,
    master: InputPathType,
    prefix: str | None = None,
    pval: float | None = None,
    minvox: float | None = None,
    atlas: str | None = None,
    session: str | None = None,
    noshiny: bool = False,
    overwrite: bool = False,
    runner: Runner | None = None,
) -> ClustExpStatParsePyOutputs:
    """
    Parser for statistical data sets and subject data sets, generating several
    outputs for further analysis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        statdset: Statistics dataset.
        meanbrik: Mean subbrik (integer >= 0).
        threshbrik: Threshold subbrik. Might be the same as MeanBrik (integer\
            >= 0).
        subjdset: Labeled dataset with all subjects (from @ClustExp_CatLab).
        subjtable: Table with subject labels and input datasets.
        master: Master data set for underlay.
        prefix: Name for output (no path).
        pval: Uncorrected p value for thresholding.
        minvox: Minimum voxels in cluster.
        atlas: Atlas name for lookup (list at: whereami -help).
        session: Output parent folder if you don't want the current working\
            directory.
        noshiny: Do not create shiny app.
        overwrite: Remove previous folder with same PREFIX.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ClustExpStatParsePyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CLUST_EXP_STAT_PARSE_PY_METADATA)
    params = clust_exp_stat_parse_py_params(statdset=statdset, meanbrik=meanbrik, threshbrik=threshbrik, subjdset=subjdset, subjtable=subjtable, master=master, prefix=prefix, pval=pval, minvox=minvox, atlas=atlas, session=session, noshiny=noshiny, overwrite=overwrite)
    return clust_exp_stat_parse_py_execute(params, execution)


__all__ = [
    "CLUST_EXP_STAT_PARSE_PY_METADATA",
    "ClustExpStatParsePyOutputs",
    "clust_exp_stat_parse_py",
    "clust_exp_stat_parse_py_params",
]
