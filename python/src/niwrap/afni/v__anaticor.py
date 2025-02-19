# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

V__ANATICOR_METADATA = Metadata(
    id="48ef68fd2da1d36a9c97f8ae28f53b818a2fe8ee.boutiques",
    name="@ANATICOR",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
VAnaticorParameters = typing.TypedDict('VAnaticorParameters', {
    "__STYX_TYPE__": typing.Literal["@ANATICOR"],
    "ts": InputPathType,
    "polort": str,
    "motion": InputPathType,
    "aseg": InputPathType,
    "prefix": str,
    "radius": typing.NotRequired[float | None],
    "view": typing.NotRequired[str | None],
    "nuisance": typing.NotRequired[InputPathType | None],
    "no_ventricles": bool,
    "Rsq_WMe": bool,
    "coverage": bool,
    "verb": bool,
    "dirty": bool,
    "echo": bool,
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
        "@ANATICOR": v__anaticor_cargs,
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
        "@ANATICOR": v__anaticor_outputs,
    }.get(t)


class VAnaticorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__anaticor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files with the prefix specified by the -prefix option."""


def v__anaticor_params(
    ts: InputPathType,
    polort: str,
    motion: InputPathType,
    aseg: InputPathType,
    prefix: str,
    radius: float | None = None,
    view: str | None = None,
    nuisance: InputPathType | None = None,
    no_ventricles: bool = False,
    rsq_wme: bool = False,
    coverage: bool = False,
    verb: bool = False,
    dirty: bool = False,
    echo: bool = False,
) -> VAnaticorParameters:
    """
    Build parameters.
    
    Args:
        ts: Time series volume which should have already undergone\
            preprocessing steps such as despiking, RetroIcor, RVT correction, time\
            shifting, and volume registration.
        polort: Polynomial for linear trend removal. Use the same order as for\
            afni_proc.py.
        motion: Head motion parameters from 3dvolreg, also created by\
            afni_proc.py.
        aseg: Aseg file from FreeSurfer's segmentation. This aseg volume must\
            be in register with the EPI time series.
        prefix: Use output (residual time series) for a prefix.
        radius: The radius of a local sphere mask in mm. Default is 15 mm for\
            high resolution 1.7x1.7x3mm data.
        view: Set the view of the output data. Default is +orig. Choose from\
            +orig, +acpc, or +tlrc.
        nuisance: Other nuisance regressors. Each regressor is a column in .1D\
            file.
        no_ventricles: Do not include LVe regressor.
        rsq_wme: Produce an explained variance map for WMeLOCAL regressor.
        coverage: Produce a spatial coverage map of WMeLOCAL regressor.
        verb: Verbose flag.
        dirty: Keep temporary files.
        echo: Echo each script command for debugging.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "@ANATICOR",
        "ts": ts,
        "polort": polort,
        "motion": motion,
        "aseg": aseg,
        "prefix": prefix,
        "no_ventricles": no_ventricles,
        "Rsq_WMe": rsq_wme,
        "coverage": coverage,
        "verb": verb,
        "dirty": dirty,
        "echo": echo,
    }
    if radius is not None:
        params["radius"] = radius
    if view is not None:
        params["view"] = view
    if nuisance is not None:
        params["nuisance"] = nuisance
    return params


def v__anaticor_cargs(
    params: VAnaticorParameters,
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
    cargs.append("@ANATICOR")
    cargs.extend([
        "-ts",
        execution.input_file(params.get("ts"))
    ])
    cargs.extend([
        "-polort",
        params.get("polort")
    ])
    cargs.extend([
        "-motion",
        execution.input_file(params.get("motion"))
    ])
    cargs.append(execution.input_file(params.get("aseg")))
    cargs.extend([
        "-prefix",
        params.get("prefix")
    ])
    if params.get("radius") is not None:
        cargs.extend([
            "-radius",
            str(params.get("radius"))
        ])
    if params.get("view") is not None:
        cargs.append(params.get("view"))
    if params.get("nuisance") is not None:
        cargs.extend([
            "-nuisance",
            execution.input_file(params.get("nuisance"))
        ])
    if params.get("no_ventricles"):
        cargs.append("-no_ventricles")
    if params.get("Rsq_WMe"):
        cargs.append("-Rsq_WMe")
    if params.get("coverage"):
        cargs.append("-coverage")
    if params.get("verb"):
        cargs.append("-verb")
    if params.get("dirty"):
        cargs.append("-dirty")
    if params.get("echo"):
        cargs.append("-echo")
    return cargs


def v__anaticor_outputs(
    params: VAnaticorParameters,
    execution: Execution,
) -> VAnaticorOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = VAnaticorOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(params.get("prefix")),
    )
    return ret


def v__anaticor_execute(
    params: VAnaticorParameters,
    execution: Execution,
) -> VAnaticorOutputs:
    """
    Script to produce a residual time series cleaned by ANATICOR model.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `VAnaticorOutputs`).
    """
    params = execution.params(params)
    cargs = v__anaticor_cargs(params, execution)
    ret = v__anaticor_outputs(params, execution)
    execution.run(cargs)
    return ret


def v__anaticor(
    ts: InputPathType,
    polort: str,
    motion: InputPathType,
    aseg: InputPathType,
    prefix: str,
    radius: float | None = None,
    view: str | None = None,
    nuisance: InputPathType | None = None,
    no_ventricles: bool = False,
    rsq_wme: bool = False,
    coverage: bool = False,
    verb: bool = False,
    dirty: bool = False,
    echo: bool = False,
    runner: Runner | None = None,
) -> VAnaticorOutputs:
    """
    Script to produce a residual time series cleaned by ANATICOR model.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        ts: Time series volume which should have already undergone\
            preprocessing steps such as despiking, RetroIcor, RVT correction, time\
            shifting, and volume registration.
        polort: Polynomial for linear trend removal. Use the same order as for\
            afni_proc.py.
        motion: Head motion parameters from 3dvolreg, also created by\
            afni_proc.py.
        aseg: Aseg file from FreeSurfer's segmentation. This aseg volume must\
            be in register with the EPI time series.
        prefix: Use output (residual time series) for a prefix.
        radius: The radius of a local sphere mask in mm. Default is 15 mm for\
            high resolution 1.7x1.7x3mm data.
        view: Set the view of the output data. Default is +orig. Choose from\
            +orig, +acpc, or +tlrc.
        nuisance: Other nuisance regressors. Each regressor is a column in .1D\
            file.
        no_ventricles: Do not include LVe regressor.
        rsq_wme: Produce an explained variance map for WMeLOCAL regressor.
        coverage: Produce a spatial coverage map of WMeLOCAL regressor.
        verb: Verbose flag.
        dirty: Keep temporary files.
        echo: Echo each script command for debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VAnaticorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ANATICOR_METADATA)
    params = v__anaticor_params(ts=ts, polort=polort, motion=motion, aseg=aseg, prefix=prefix, radius=radius, view=view, nuisance=nuisance, no_ventricles=no_ventricles, rsq_wme=rsq_wme, coverage=coverage, verb=verb, dirty=dirty, echo=echo)
    return v__anaticor_execute(params, execution)


__all__ = [
    "VAnaticorOutputs",
    "VAnaticorParameters",
    "V__ANATICOR_METADATA",
    "v__anaticor",
    "v__anaticor_params",
]
