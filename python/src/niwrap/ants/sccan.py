# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCCAN_METADATA = Metadata(
    id="26f604003de4aee5a1d0df471af2893515e5b091.boutiques",
    name="sccan",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)
SccanParameters = typing.TypedDict('SccanParameters', {
    "__STYX_TYPE__": typing.Literal["sccan"],
    "output": typing.NotRequired[str | None],
    "n_permutations": typing.NotRequired[int | None],
    "smoother": typing.NotRequired[int | None],
    "row_sparseness": typing.NotRequired[int | None],
    "iterations": typing.NotRequired[int | None],
    "n_eigenvectors": typing.NotRequired[int | None],
    "robustify": typing.NotRequired[int | None],
    "covering": typing.NotRequired[int | None],
    "uselong": typing.NotRequired[int | None],
    "l1": typing.NotRequired[float | None],
    "pclusterthresh": typing.NotRequired[float | None],
    "qclusterthresh": typing.NotRequired[float | None],
    "ridge_cca": typing.NotRequired[float | None],
    "initialization": typing.NotRequired[str | None],
    "initialization2": typing.NotRequired[str | None],
    "mask": typing.NotRequired[InputPathType | None],
    "mask2": typing.NotRequired[InputPathType | None],
    "partial_scca_option": typing.NotRequired[str | None],
    "prior_weight": typing.NotRequired[float | None],
    "get_small": typing.NotRequired[float | None],
    "verbose": typing.NotRequired[float | None],
    "imageset_to_matrix": typing.NotRequired[str | None],
    "timeseriesimage_to_matrix": typing.NotRequired[str | None],
    "vector_to_image": typing.NotRequired[str | None],
    "imageset_to_projections": typing.NotRequired[str | None],
    "scca": typing.NotRequired[str | None],
    "svd": typing.NotRequired[str | None],
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
        "sccan": sccan_cargs,
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
    vt = {}
    return vt.get(t)


def sccan_params(
    output: str | None = None,
    n_permutations: int | None = None,
    smoother: int | None = None,
    row_sparseness: int | None = None,
    iterations: int | None = None,
    n_eigenvectors: int | None = None,
    robustify: int | None = None,
    covering: int | None = None,
    uselong: int | None = None,
    l1: float | None = None,
    pclusterthresh: float | None = None,
    qclusterthresh: float | None = None,
    ridge_cca: float | None = None,
    initialization: str | None = None,
    initialization2: str | None = None,
    mask: InputPathType | None = None,
    mask2: InputPathType | None = None,
    partial_scca_option: str | None = None,
    prior_weight: float | None = None,
    get_small: float | None = None,
    verbose: float | None = None,
    imageset_to_matrix: str | None = None,
    timeseriesimage_to_matrix: str | None = None,
    vector_to_image: str | None = None,
    imageset_to_projections: str | None = None,
    scca: str | None = None,
    svd: str | None = None,
) -> SccanParameters:
    """
    Build parameters.
    
    Args:
        output: Output dependent on which option is called.
        n_permutations: Number of permutations to use in scca.
        smoother: Smoothing function for variates.
        row_sparseness: Row sparseness - if (+) then keep values (+) otherwise\
            allow +/- values --- always L1.
        iterations: Max iterations for scca optimization (min 20).
        n_eigenvectors: Number of eigenvectors to compute in scca/spca.
        robustify: Rank-based scca.
        covering: Try to make the decomposition cover the whole domain, if\
            possible.
        uselong: Use longitudinal formulation (> 0) or not (<= 0).
        l1: Use l1 (> 0) or l0 (< 0) penalty, also sets gradient step size.
        pclusterthresh: Cluster threshold on view P.
        qclusterthresh: Cluster threshold on view Q.
        ridge_cca: Ridge cca.
        initialization: Initialization file list for Eigenanatomy - must also\
            pass mask option.
        initialization2: Initialization file list for SCCAN-Eigenanatomy - must\
            also pass mask option.
        mask: Mask file for Eigenanatomy initialization.
        mask2: Mask file for Eigenanatomy initialization 2.
        partial_scca_option: Choices for pscca: PQ, PminusRQ, PQminusR,\
            PminusRQminusR.
        prior_weight: Scalar value weight on prior between 0 (prior is weak)\
            and 1 (prior is strong). Only engaged if initialization is used.
        get_small: Find smallest eigenvectors.
        verbose: Set whether output is verbose.
        imageset_to_matrix: Takes a list of image files names (one per line)\
            and converts it to a 2D matrix/image in binary or csv format.
        timeseriesimage_to_matrix: Takes a timeseries (4D) image and converts\
            it to a 2D matrix csv format.
        vector_to_image: Converts the 1st column vector in a csv file back to\
            an image.
        imageset_to_projections: Takes a list of image and projection files\
            names and writes them to a csv file.
        scca: Matrix-based scca operations for 2 and 3 views.
        svd: A sparse SVD implementation.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "sccan",
    }
    if output is not None:
        params["output"] = output
    if n_permutations is not None:
        params["n_permutations"] = n_permutations
    if smoother is not None:
        params["smoother"] = smoother
    if row_sparseness is not None:
        params["row_sparseness"] = row_sparseness
    if iterations is not None:
        params["iterations"] = iterations
    if n_eigenvectors is not None:
        params["n_eigenvectors"] = n_eigenvectors
    if robustify is not None:
        params["robustify"] = robustify
    if covering is not None:
        params["covering"] = covering
    if uselong is not None:
        params["uselong"] = uselong
    if l1 is not None:
        params["l1"] = l1
    if pclusterthresh is not None:
        params["pclusterthresh"] = pclusterthresh
    if qclusterthresh is not None:
        params["qclusterthresh"] = qclusterthresh
    if ridge_cca is not None:
        params["ridge_cca"] = ridge_cca
    if initialization is not None:
        params["initialization"] = initialization
    if initialization2 is not None:
        params["initialization2"] = initialization2
    if mask is not None:
        params["mask"] = mask
    if mask2 is not None:
        params["mask2"] = mask2
    if partial_scca_option is not None:
        params["partial_scca_option"] = partial_scca_option
    if prior_weight is not None:
        params["prior_weight"] = prior_weight
    if get_small is not None:
        params["get_small"] = get_small
    if verbose is not None:
        params["verbose"] = verbose
    if imageset_to_matrix is not None:
        params["imageset_to_matrix"] = imageset_to_matrix
    if timeseriesimage_to_matrix is not None:
        params["timeseriesimage_to_matrix"] = timeseriesimage_to_matrix
    if vector_to_image is not None:
        params["vector_to_image"] = vector_to_image
    if imageset_to_projections is not None:
        params["imageset_to_projections"] = imageset_to_projections
    if scca is not None:
        params["scca"] = scca
    if svd is not None:
        params["svd"] = svd
    return params


def sccan_cargs(
    params: SccanParameters,
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
    cargs.append("sccan")
    if params.get("output") is not None:
        cargs.extend([
            "-o",
            params.get("output")
        ])
    if params.get("n_permutations") is not None:
        cargs.extend([
            "-p",
            str(params.get("n_permutations"))
        ])
    if params.get("smoother") is not None:
        cargs.extend([
            "-s",
            str(params.get("smoother"))
        ])
    if params.get("row_sparseness") is not None:
        cargs.extend([
            "-z",
            str(params.get("row_sparseness"))
        ])
    if params.get("iterations") is not None:
        cargs.extend([
            "-i",
            str(params.get("iterations"))
        ])
    if params.get("n_eigenvectors") is not None:
        cargs.extend([
            "-n",
            str(params.get("n_eigenvectors"))
        ])
    if params.get("robustify") is not None:
        cargs.extend([
            "-r",
            str(params.get("robustify"))
        ])
    if params.get("covering") is not None:
        cargs.extend([
            "-c",
            str(params.get("covering"))
        ])
    if params.get("uselong") is not None:
        cargs.extend([
            "-g",
            str(params.get("uselong"))
        ])
    if params.get("l1") is not None:
        cargs.extend([
            "-l",
            str(params.get("l1"))
        ])
    if params.get("pclusterthresh") is not None:
        cargs.extend([
            "--PClusterThresh",
            str(params.get("pclusterthresh"))
        ])
    if params.get("qclusterthresh") is not None:
        cargs.extend([
            "--QClusterThresh",
            str(params.get("qclusterthresh"))
        ])
    if params.get("ridge_cca") is not None:
        cargs.extend([
            "-e",
            str(params.get("ridge_cca"))
        ])
    if params.get("initialization") is not None:
        cargs.extend([
            "--initialization",
            params.get("initialization")
        ])
    if params.get("initialization2") is not None:
        cargs.extend([
            "--initialization2",
            params.get("initialization2")
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "--mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("mask2") is not None:
        cargs.extend([
            "--mask2",
            execution.input_file(params.get("mask2"))
        ])
    if params.get("partial_scca_option") is not None:
        cargs.extend([
            "--partial-scca-option",
            params.get("partial_scca_option")
        ])
    if params.get("prior_weight") is not None:
        cargs.extend([
            "--prior-weight",
            str(params.get("prior_weight"))
        ])
    if params.get("get_small") is not None:
        cargs.extend([
            "--get-small",
            str(params.get("get_small"))
        ])
    if params.get("verbose") is not None:
        cargs.extend([
            "-v",
            str(params.get("verbose"))
        ])
    if params.get("imageset_to_matrix") is not None:
        cargs.extend([
            "--imageset-to-matrix",
            params.get("imageset_to_matrix")
        ])
    if params.get("timeseriesimage_to_matrix") is not None:
        cargs.extend([
            "--timeseriesimage-to-matrix",
            params.get("timeseriesimage_to_matrix")
        ])
    if params.get("vector_to_image") is not None:
        cargs.extend([
            "--vector-to-image",
            params.get("vector_to_image")
        ])
    if params.get("imageset_to_projections") is not None:
        cargs.extend([
            "--imageset-to-projections",
            params.get("imageset_to_projections")
        ])
    if params.get("scca") is not None:
        cargs.extend([
            "--scca",
            params.get("scca")
        ])
    if params.get("svd") is not None:
        cargs.extend([
            "--svd",
            params.get("svd")
        ])
    return cargs


def sccan_outputs(
    params: SccanParameters,
    execution: Execution,
) -> SccanOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SccanOutputs(
        root=execution.output_file("."),
    )
    return ret


def sccan_execute(
    params: SccanParameters,
    execution: Execution,
) -> SccanOutputs:
    """
    A tool for sparse statistical analysis on images : scca, pscca (with options),
    mscca. Can also convert an imagelist/mask pair to a binary matrix image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SccanOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = sccan_cargs(params, execution)
    ret = sccan_outputs(params, execution)
    execution.run(cargs)
    return ret


def sccan(
    output: str | None = None,
    n_permutations: int | None = None,
    smoother: int | None = None,
    row_sparseness: int | None = None,
    iterations: int | None = None,
    n_eigenvectors: int | None = None,
    robustify: int | None = None,
    covering: int | None = None,
    uselong: int | None = None,
    l1: float | None = None,
    pclusterthresh: float | None = None,
    qclusterthresh: float | None = None,
    ridge_cca: float | None = None,
    initialization: str | None = None,
    initialization2: str | None = None,
    mask: InputPathType | None = None,
    mask2: InputPathType | None = None,
    partial_scca_option: str | None = None,
    prior_weight: float | None = None,
    get_small: float | None = None,
    verbose: float | None = None,
    imageset_to_matrix: str | None = None,
    timeseriesimage_to_matrix: str | None = None,
    vector_to_image: str | None = None,
    imageset_to_projections: str | None = None,
    scca: str | None = None,
    svd: str | None = None,
    runner: Runner | None = None,
) -> SccanOutputs:
    """
    A tool for sparse statistical analysis on images : scca, pscca (with options),
    mscca. Can also convert an imagelist/mask pair to a binary matrix image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        output: Output dependent on which option is called.
        n_permutations: Number of permutations to use in scca.
        smoother: Smoothing function for variates.
        row_sparseness: Row sparseness - if (+) then keep values (+) otherwise\
            allow +/- values --- always L1.
        iterations: Max iterations for scca optimization (min 20).
        n_eigenvectors: Number of eigenvectors to compute in scca/spca.
        robustify: Rank-based scca.
        covering: Try to make the decomposition cover the whole domain, if\
            possible.
        uselong: Use longitudinal formulation (> 0) or not (<= 0).
        l1: Use l1 (> 0) or l0 (< 0) penalty, also sets gradient step size.
        pclusterthresh: Cluster threshold on view P.
        qclusterthresh: Cluster threshold on view Q.
        ridge_cca: Ridge cca.
        initialization: Initialization file list for Eigenanatomy - must also\
            pass mask option.
        initialization2: Initialization file list for SCCAN-Eigenanatomy - must\
            also pass mask option.
        mask: Mask file for Eigenanatomy initialization.
        mask2: Mask file for Eigenanatomy initialization 2.
        partial_scca_option: Choices for pscca: PQ, PminusRQ, PQminusR,\
            PminusRQminusR.
        prior_weight: Scalar value weight on prior between 0 (prior is weak)\
            and 1 (prior is strong). Only engaged if initialization is used.
        get_small: Find smallest eigenvectors.
        verbose: Set whether output is verbose.
        imageset_to_matrix: Takes a list of image files names (one per line)\
            and converts it to a 2D matrix/image in binary or csv format.
        timeseriesimage_to_matrix: Takes a timeseries (4D) image and converts\
            it to a 2D matrix csv format.
        vector_to_image: Converts the 1st column vector in a csv file back to\
            an image.
        imageset_to_projections: Takes a list of image and projection files\
            names and writes them to a csv file.
        scca: Matrix-based scca operations for 2 and 3 views.
        svd: A sparse SVD implementation.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SccanOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCCAN_METADATA)
    params = sccan_params(output=output, n_permutations=n_permutations, smoother=smoother, row_sparseness=row_sparseness, iterations=iterations, n_eigenvectors=n_eigenvectors, robustify=robustify, covering=covering, uselong=uselong, l1=l1, pclusterthresh=pclusterthresh, qclusterthresh=qclusterthresh, ridge_cca=ridge_cca, initialization=initialization, initialization2=initialization2, mask=mask, mask2=mask2, partial_scca_option=partial_scca_option, prior_weight=prior_weight, get_small=get_small, verbose=verbose, imageset_to_matrix=imageset_to_matrix, timeseriesimage_to_matrix=timeseriesimage_to_matrix, vector_to_image=vector_to_image, imageset_to_projections=imageset_to_projections, scca=scca, svd=svd)
    return sccan_execute(params, execution)


__all__ = [
    "SCCAN_METADATA",
    "sccan",
    "sccan_params",
]
