# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3DTTEST___METADATA = Metadata(
    id="9816ba0be883f397c48e16a5a699629ad3d438ae.boutiques",
    name="3dttest++",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V3dttestParameters = typing.TypedDict('V3dttestParameters', {
    "__STYX_TYPE__": typing.Literal["3dttest++"],
    "setA": list[str],
    "setB": typing.NotRequired[list[str] | None],
    "setA_long": typing.NotRequired[list[str] | None],
    "setB_long": typing.NotRequired[list[str] | None],
    "covariates": typing.NotRequired[InputPathType | None],
    "labelA": typing.NotRequired[str | None],
    "labelB": typing.NotRequired[str | None],
    "setweightA": typing.NotRequired[InputPathType | None],
    "setweightB": typing.NotRequired[InputPathType | None],
    "prefix": typing.NotRequired[str | None],
    "resid": typing.NotRequired[str | None],
    "paired": bool,
    "unpooled": bool,
    "mask": typing.NotRequired[InputPathType | None],
    "exblur": typing.NotRequired[int | None],
    "randomsign": bool,
    "permute": bool,
    "ETAC": bool,
    "ETAC_blur": typing.NotRequired[list[float] | None],
    "ETAC_opt": typing.NotRequired[list[str] | None],
    "seed": typing.NotRequired[float | None],
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
        "3dttest++": v_3dttest___cargs,
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
        "3dttest++": v_3dttest___outputs,
    }
    return vt.get(t)


class V3dttestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dttest__(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Main output dataset"""
    residuals: OutputPathType | None
    """Output residuals dataset"""


def v_3dttest___params(
    set_a: list[str],
    set_b: list[str] | None = None,
    set_a_long: list[str] | None = None,
    set_b_long: list[str] | None = None,
    covariates: InputPathType | None = None,
    label_a: str | None = None,
    label_b: str | None = None,
    setweight_a: InputPathType | None = None,
    setweight_b: InputPathType | None = None,
    prefix: str | None = None,
    resid: str | None = None,
    paired: bool = False,
    unpooled: bool = False,
    mask: InputPathType | None = None,
    exblur: int | None = None,
    randomsign: bool = False,
    permute: bool = False,
    etac: bool = False,
    etac_blur: list[float] | None = None,
    etac_opt: list[str] | None = None,
    seed: float | None = None,
) -> V3dttestParameters:
    """
    Build parameters.
    
    Args:
        set_a: Set A in short form, e.g., 'a+tlrc[3]' b+tlrc[3] ...'.
        set_b: Set B in short form, e.g., 'x+tlrc[3]' y+tlrc[3] ...'.
        set_a_long: Specify an overall name for the set of datasets (Long\
            form). Example: -setA Green sub001 a+tlrc[3] sub002 b+tlrc[3] ...
        set_b_long: Specify an overall name for the set of datasets (Long\
            form). Example: -setB Blue sub001 x+tlrc[3] sub002 y+tlrc[3] ...
        covariates: File containing covariates.
        label_a: Label for the set (for Set A). Limited to 12 characters.
        label_b: Label for the set (for Set B). Limited to 12 characters.
        setweight_a: File with voxel-wise weights for -setA datasets.
        setweight_b: File with voxel-wise weights for -setB datasets.
        prefix: Output the prefix name of the dataset result. For surface-based\
            datasets, use -prefix p.niml.dset or -prefix p.gii.dset.
        resid: Residuals will be output into a dataset with the given prefix.
        paired: Specify to use a paired-sample t-test to compare setA and setB.\
            Both sets must have the same cardinality.
        unpooled: Specify separate variance estimates for setA and setB (not\
            pooled together).
        mask: Set mask for dataset analysis.
        exblur: Add extra Gaussian blurring kernel FWHM (mm). Example: -exblur\
            6.
        randomsign: Randomize signs of datasets. Used with output from -resid\
            to generate null hypothesis statistics.
        permute: With -randomsign, adds inter-set permutation to randomization\
            when both sets are used.
        etac: Apply the Equitable Thresholding And Clustering (ETAC) method for\
            thresholding results.
        etac_blur: List of multiple levels of spatial blurring for ETAC.\
            Example: -ETAC_blur 4 6.
        etac_opt: Specify options for ETAC. Example: -ETAC_opt\
            NN=2:sid=2:hpow=0,2:pthr=0.01,0.005,0.002,0.01:name=Fred.
        seed: Random number seed for -randomsign and -permute/ETAC.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "3dttest++",
        "setA": set_a,
        "paired": paired,
        "unpooled": unpooled,
        "randomsign": randomsign,
        "permute": permute,
        "ETAC": etac,
    }
    if set_b is not None:
        params["setB"] = set_b
    if set_a_long is not None:
        params["setA_long"] = set_a_long
    if set_b_long is not None:
        params["setB_long"] = set_b_long
    if covariates is not None:
        params["covariates"] = covariates
    if label_a is not None:
        params["labelA"] = label_a
    if label_b is not None:
        params["labelB"] = label_b
    if setweight_a is not None:
        params["setweightA"] = setweight_a
    if setweight_b is not None:
        params["setweightB"] = setweight_b
    if prefix is not None:
        params["prefix"] = prefix
    if resid is not None:
        params["resid"] = resid
    if mask is not None:
        params["mask"] = mask
    if exblur is not None:
        params["exblur"] = exblur
    if etac_blur is not None:
        params["ETAC_blur"] = etac_blur
    if etac_opt is not None:
        params["ETAC_opt"] = etac_opt
    if seed is not None:
        params["seed"] = seed
    return params


def v_3dttest___cargs(
    params: V3dttestParameters,
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
    cargs.append("3dttest++")
    cargs.extend([
        "-setA",
        *params.get("setA")
    ])
    if params.get("setB") is not None:
        cargs.extend([
            "-setB",
            *params.get("setB")
        ])
    if params.get("setA_long") is not None:
        cargs.extend([
            "-setA",
            *params.get("setA_long")
        ])
    if params.get("setB_long") is not None:
        cargs.extend([
            "-setB",
            *params.get("setB_long")
        ])
    if params.get("covariates") is not None:
        cargs.extend([
            "-covariates",
            execution.input_file(params.get("covariates"))
        ])
    if params.get("labelA") is not None:
        cargs.extend([
            "-labelA",
            params.get("labelA")
        ])
    if params.get("labelB") is not None:
        cargs.extend([
            "-labelB",
            params.get("labelB")
        ])
    if params.get("setweightA") is not None:
        cargs.extend([
            "-setweightA",
            execution.input_file(params.get("setweightA"))
        ])
    if params.get("setweightB") is not None:
        cargs.extend([
            "-setweightB",
            execution.input_file(params.get("setweightB"))
        ])
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("resid") is not None:
        cargs.extend([
            "-resid",
            params.get("resid")
        ])
    if params.get("paired"):
        cargs.append("-paired")
    if params.get("unpooled"):
        cargs.append("-unpooled")
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("exblur") is not None:
        cargs.extend([
            "-exblur",
            str(params.get("exblur"))
        ])
    if params.get("randomsign"):
        cargs.append("-randomsign")
    if params.get("permute"):
        cargs.append("-permute")
    if params.get("ETAC"):
        cargs.append("-ETAC")
    if params.get("ETAC_blur") is not None:
        cargs.extend([
            "-ETAC_blur",
            *map(str, params.get("ETAC_blur"))
        ])
    if params.get("ETAC_opt") is not None:
        cargs.extend([
            "-ETAC_opt",
            *params.get("ETAC_opt")
        ])
    if params.get("seed") is not None:
        cargs.extend([
            "-seed",
            str(params.get("seed"))
        ])
    return cargs


def v_3dttest___outputs(
    params: V3dttestParameters,
    execution: Execution,
) -> V3dttestOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V3dttestOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(params.get("prefix") + ".nii.gz") if (params.get("prefix") is not None) else None,
        residuals=execution.output_file(params.get("resid") + ".nii.gz") if (params.get("resid") is not None) else None,
    )
    return ret


def v_3dttest___execute(
    params: V3dttestParameters,
    execution: Execution,
) -> V3dttestOutputs:
    """
    Gosset (Student) t-test of sets of 3D datasets in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V3dttestOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_3dttest___cargs(params, execution)
    ret = v_3dttest___outputs(params, execution)
    execution.run(cargs)
    return ret


def v_3dttest__(
    set_a: list[str],
    set_b: list[str] | None = None,
    set_a_long: list[str] | None = None,
    set_b_long: list[str] | None = None,
    covariates: InputPathType | None = None,
    label_a: str | None = None,
    label_b: str | None = None,
    setweight_a: InputPathType | None = None,
    setweight_b: InputPathType | None = None,
    prefix: str | None = None,
    resid: str | None = None,
    paired: bool = False,
    unpooled: bool = False,
    mask: InputPathType | None = None,
    exblur: int | None = None,
    randomsign: bool = False,
    permute: bool = False,
    etac: bool = False,
    etac_blur: list[float] | None = None,
    etac_opt: list[str] | None = None,
    seed: float | None = None,
    runner: Runner | None = None,
) -> V3dttestOutputs:
    """
    Gosset (Student) t-test of sets of 3D datasets in AFNI.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        set_a: Set A in short form, e.g., 'a+tlrc[3]' b+tlrc[3] ...'.
        set_b: Set B in short form, e.g., 'x+tlrc[3]' y+tlrc[3] ...'.
        set_a_long: Specify an overall name for the set of datasets (Long\
            form). Example: -setA Green sub001 a+tlrc[3] sub002 b+tlrc[3] ...
        set_b_long: Specify an overall name for the set of datasets (Long\
            form). Example: -setB Blue sub001 x+tlrc[3] sub002 y+tlrc[3] ...
        covariates: File containing covariates.
        label_a: Label for the set (for Set A). Limited to 12 characters.
        label_b: Label for the set (for Set B). Limited to 12 characters.
        setweight_a: File with voxel-wise weights for -setA datasets.
        setweight_b: File with voxel-wise weights for -setB datasets.
        prefix: Output the prefix name of the dataset result. For surface-based\
            datasets, use -prefix p.niml.dset or -prefix p.gii.dset.
        resid: Residuals will be output into a dataset with the given prefix.
        paired: Specify to use a paired-sample t-test to compare setA and setB.\
            Both sets must have the same cardinality.
        unpooled: Specify separate variance estimates for setA and setB (not\
            pooled together).
        mask: Set mask for dataset analysis.
        exblur: Add extra Gaussian blurring kernel FWHM (mm). Example: -exblur\
            6.
        randomsign: Randomize signs of datasets. Used with output from -resid\
            to generate null hypothesis statistics.
        permute: With -randomsign, adds inter-set permutation to randomization\
            when both sets are used.
        etac: Apply the Equitable Thresholding And Clustering (ETAC) method for\
            thresholding results.
        etac_blur: List of multiple levels of spatial blurring for ETAC.\
            Example: -ETAC_blur 4 6.
        etac_opt: Specify options for ETAC. Example: -ETAC_opt\
            NN=2:sid=2:hpow=0,2:pthr=0.01,0.005,0.002,0.01:name=Fred.
        seed: Random number seed for -randomsign and -permute/ETAC.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dttestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DTTEST___METADATA)
    params = v_3dttest___params(set_a=set_a, set_b=set_b, set_a_long=set_a_long, set_b_long=set_b_long, covariates=covariates, label_a=label_a, label_b=label_b, setweight_a=setweight_a, setweight_b=setweight_b, prefix=prefix, resid=resid, paired=paired, unpooled=unpooled, mask=mask, exblur=exblur, randomsign=randomsign, permute=permute, etac=etac, etac_blur=etac_blur, etac_opt=etac_opt, seed=seed)
    return v_3dttest___execute(params, execution)


__all__ = [
    "V3dttestOutputs",
    "V_3DTTEST___METADATA",
    "v_3dttest__",
    "v_3dttest___params",
]
