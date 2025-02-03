# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKGLOBAL_METADATA = Metadata(
    id="83ed2ed5059d206686d68bca5253e7191f588b5d.boutiques",
    name="tckglobal",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
TckglobalRisoParameters = typing.TypedDict('TckglobalRisoParameters', {
    "__STYX_TYPE__": typing.Literal["riso"],
    "response": InputPathType,
})
TckglobalConfigParameters = typing.TypedDict('TckglobalConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
TckglobalParameters = typing.TypedDict('TckglobalParameters', {
    "__STYX_TYPE__": typing.Literal["tckglobal"],
    "grad": typing.NotRequired[InputPathType | None],
    "mask": typing.NotRequired[InputPathType | None],
    "riso": typing.NotRequired[list[TckglobalRisoParameters] | None],
    "lmax": typing.NotRequired[int | None],
    "length": typing.NotRequired[float | None],
    "weight": typing.NotRequired[float | None],
    "ppot": typing.NotRequired[float | None],
    "cpot": typing.NotRequired[float | None],
    "t0": typing.NotRequired[float | None],
    "t1": typing.NotRequired[float | None],
    "niter": typing.NotRequired[int | None],
    "fod": typing.NotRequired[str | None],
    "noapo": bool,
    "fiso": typing.NotRequired[str | None],
    "eext": typing.NotRequired[str | None],
    "etrend": typing.NotRequired[str | None],
    "balance": typing.NotRequired[float | None],
    "density": typing.NotRequired[float | None],
    "prob": typing.NotRequired[list[float] | None],
    "beta": typing.NotRequired[float | None],
    "lambda": typing.NotRequired[float | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TckglobalConfigParameters] | None],
    "help": bool,
    "version": bool,
    "source": InputPathType,
    "response": InputPathType,
    "tracks": str,
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
        "tckglobal": tckglobal_cargs,
        "riso": tckglobal_riso_cargs,
        "config": tckglobal_config_cargs,
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
        "tckglobal": tckglobal_outputs,
    }
    return vt.get(t)


def tckglobal_riso_params(
    response: InputPathType,
) -> TckglobalRisoParameters:
    """
    Build parameters.
    
    Args:
        response: set one or more isotropic response functions. (multiple\
            allowed).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "riso",
        "response": response,
    }
    return params


def tckglobal_riso_cargs(
    params: TckglobalRisoParameters,
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
    cargs.append("-riso")
    cargs.append(execution.input_file(params.get("response")))
    return cargs


def tckglobal_config_params(
    key: str,
    value: str,
) -> TckglobalConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def tckglobal_config_cargs(
    params: TckglobalConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class TckglobalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckglobal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    tracks: OutputPathType
    """the output file containing the tracks generated."""
    fod: OutputPathType | None
    """Predicted fibre orientation distribution function (fODF).
    This fODF is estimated as part of the global track optimization, and
    therefore incorporates the spatial regularization that it imposes.
    Internally, the fODF is represented as a discrete sum of apodized point
    spread functions (aPSF) oriented along the directions of all particles in
    the voxel, used to predict the DWI signal from the particle configuration.
    """
    fiso: OutputPathType | None
    """Predicted isotropic fractions of the tissues for which response functions
    were provided with -riso. Typically, these are CSF and GM. """
    eext: OutputPathType | None
    """Residual external energy in every voxel. """
    etrend: OutputPathType | None
    """internal and external energy trend and cooling statistics. """


def tckglobal_params(
    source: InputPathType,
    response: InputPathType,
    tracks: str,
    grad: InputPathType | None = None,
    mask: InputPathType | None = None,
    riso: list[TckglobalRisoParameters] | None = None,
    lmax: int | None = None,
    length: float | None = None,
    weight: float | None = None,
    ppot: float | None = None,
    cpot: float | None = None,
    t0: float | None = None,
    t1: float | None = None,
    niter: int | None = None,
    fod: str | None = None,
    noapo: bool = False,
    fiso: str | None = None,
    eext: str | None = None,
    etrend: str | None = None,
    balance: float | None = None,
    density: float | None = None,
    prob: list[float] | None = None,
    beta: float | None = None,
    lambda_: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckglobalConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TckglobalParameters:
    """
    Build parameters.
    
    Args:
        source: the image containing the raw DWI data.
        response: the response of a track segment on the DWI signal.
        tracks: the output file containing the tracks generated.
        grad: specify the diffusion encoding scheme (required if not supplied\
            in the header).
        mask: only reconstruct the tractogram within the specified brain mask\
            image.
        riso: set one or more isotropic response functions. (multiple allowed).
        lmax: set the maximum harmonic order for the output series. (default =\
            8).
        length: set the length of the particles (fibre segments). (default =\
            1mm).
        weight: set the weight by which particles contribute to the model.\
            (default = 0.1).
        ppot: set the particle potential, i.e., the cost of adding one segment,\
            relative to the particle weight. (default = 0.05).
        cpot: set the connection potential, i.e., the energy term that drives\
            two segments together. (default = 0.5).
        t0: set the initial temperature of the metropolis hastings optimizer.\
            (default = 0.1).
        t1: set the final temperature of the metropolis hastings optimizer.\
            (default = 0.001).
        niter: set the number of iterations of the metropolis hastings\
            optimizer. (default = 10M).
        fod: Predicted fibre orientation distribution function (fODF).\
            This fODF is estimated as part of the global track optimization,\
            and therefore incorporates the spatial regularization that it\
            imposes. Internally, the fODF is represented as a discrete sum of\
            apodized point spread functions (aPSF) oriented along the\
            directions of all particles in the voxel, used to predict the DWI\
            signal from the particle configuration.
        noapo: disable spherical convolution of fODF with apodized PSF, to\
            output a sum of delta functions rather than a sum of aPSFs.
        fiso: Predicted isotropic fractions of the tissues for which response\
            functions were provided with -riso. Typically, these are CSF and GM.
        eext: Residual external energy in every voxel.
        etrend: internal and external energy trend and cooling statistics.
        balance: balance internal and external energy. (default = 0)\
            Negative values give more weight to the internal energy, positive\
            to the external energy.
        density: set the desired density of the free Poisson process. (default\
            = 1).
        prob: set the probabilities of generating birth, death, randshift,\
            optshift and connect proposals respectively. (default =\
            0.25,0.05,0.25,0.1,0.35).
        beta: set the width of the Hanning interpolation window. (in [0, 1],\
            default = 0)\
            If used, a mask is required, and this mask must keep at least one\
            voxel distance to the image bounding box.
        lambda_: set the weight of the internal energy directly. (default = 1)\
            If provided, any value of -balance will be ignored.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tckglobal",
        "noapo": noapo,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "source": source,
        "response": response,
        "tracks": tracks,
    }
    if grad is not None:
        params["grad"] = grad
    if mask is not None:
        params["mask"] = mask
    if riso is not None:
        params["riso"] = riso
    if lmax is not None:
        params["lmax"] = lmax
    if length is not None:
        params["length"] = length
    if weight is not None:
        params["weight"] = weight
    if ppot is not None:
        params["ppot"] = ppot
    if cpot is not None:
        params["cpot"] = cpot
    if t0 is not None:
        params["t0"] = t0
    if t1 is not None:
        params["t1"] = t1
    if niter is not None:
        params["niter"] = niter
    if fod is not None:
        params["fod"] = fod
    if fiso is not None:
        params["fiso"] = fiso
    if eext is not None:
        params["eext"] = eext
    if etrend is not None:
        params["etrend"] = etrend
    if balance is not None:
        params["balance"] = balance
    if density is not None:
        params["density"] = density
    if prob is not None:
        params["prob"] = prob
    if beta is not None:
        params["beta"] = beta
    if lambda_ is not None:
        params["lambda"] = lambda_
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tckglobal_cargs(
    params: TckglobalParameters,
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
    cargs.append("tckglobal")
    if params.get("grad") is not None:
        cargs.extend([
            "-grad",
            execution.input_file(params.get("grad"))
        ])
    if params.get("mask") is not None:
        cargs.extend([
            "-mask",
            execution.input_file(params.get("mask"))
        ])
    if params.get("riso") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("riso")] for a in c])
    if params.get("lmax") is not None:
        cargs.extend([
            "-lmax",
            str(params.get("lmax"))
        ])
    if params.get("length") is not None:
        cargs.extend([
            "-length",
            str(params.get("length"))
        ])
    if params.get("weight") is not None:
        cargs.extend([
            "-weight",
            str(params.get("weight"))
        ])
    if params.get("ppot") is not None:
        cargs.extend([
            "-ppot",
            str(params.get("ppot"))
        ])
    if params.get("cpot") is not None:
        cargs.extend([
            "-cpot",
            str(params.get("cpot"))
        ])
    if params.get("t0") is not None:
        cargs.extend([
            "-t0",
            str(params.get("t0"))
        ])
    if params.get("t1") is not None:
        cargs.extend([
            "-t1",
            str(params.get("t1"))
        ])
    if params.get("niter") is not None:
        cargs.extend([
            "-niter",
            str(params.get("niter"))
        ])
    if params.get("fod") is not None:
        cargs.extend([
            "-fod",
            params.get("fod")
        ])
    if params.get("noapo"):
        cargs.append("-noapo")
    if params.get("fiso") is not None:
        cargs.extend([
            "-fiso",
            params.get("fiso")
        ])
    if params.get("eext") is not None:
        cargs.extend([
            "-eext",
            params.get("eext")
        ])
    if params.get("etrend") is not None:
        cargs.extend([
            "-etrend",
            params.get("etrend")
        ])
    if params.get("balance") is not None:
        cargs.extend([
            "-balance",
            str(params.get("balance"))
        ])
    if params.get("density") is not None:
        cargs.extend([
            "-density",
            str(params.get("density"))
        ])
    if params.get("prob") is not None:
        cargs.extend([
            "-prob",
            *map(str, params.get("prob"))
        ])
    if params.get("beta") is not None:
        cargs.extend([
            "-beta",
            str(params.get("beta"))
        ])
    if params.get("lambda") is not None:
        cargs.extend([
            "-lambda",
            str(params.get("lambda"))
        ])
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("source")))
    cargs.append(execution.input_file(params.get("response")))
    cargs.append(params.get("tracks"))
    return cargs


def tckglobal_outputs(
    params: TckglobalParameters,
    execution: Execution,
) -> TckglobalOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TckglobalOutputs(
        root=execution.output_file("."),
        tracks=execution.output_file(params.get("tracks")),
        fod=execution.output_file(params.get("fod")) if (params.get("fod") is not None) else None,
        fiso=execution.output_file(params.get("fiso")) if (params.get("fiso") is not None) else None,
        eext=execution.output_file(params.get("eext")) if (params.get("eext") is not None) else None,
        etrend=execution.output_file(params.get("etrend")) if (params.get("etrend") is not None) else None,
    )
    return ret


def tckglobal_execute(
    params: TckglobalParameters,
    execution: Execution,
) -> TckglobalOutputs:
    """
    Multi-Shell Multi-Tissue Global Tractography.
    
    This command will reconstruct the global white matter fibre tractogram that
    best explains the input DWI data, using a multi-tissue spherical convolution
    model.
    
    Example use:
    
    $ tckglobal dwi.mif wmr.txt -riso csfr.txt -riso gmr.txt -mask mask.mif
    -niter 1e9 -fod fod.mif -fiso fiso.mif tracks.tck
    
    in which dwi.mif is the input image, wmr.txt is an anisotropic, multi-shell
    response function for WM, and csfr.txt and gmr.txt are isotropic response
    functions for CSF and GM. The output tractogram is saved to tracks.tck.
    Optional output images fod.mif and fiso.mif contain the predicted WM fODF
    and isotropic tissue fractions of CSF and GM respectively, estimated as part
    of the global optimization and thus affected by spatial regularization.
    
    References:
    
    Christiaens, D.; Reisert, M.; Dhollander, T.; Sunaert, S.; Suetens, P. &
    Maes, F. Global tractography of multi-shell diffusion-weighted imaging data
    using a multi-tissue model. NeuroImage, 2015, 123, 89-101.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TckglobalOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tckglobal_cargs(params, execution)
    ret = tckglobal_outputs(params, execution)
    execution.run(cargs)
    return ret


def tckglobal(
    source: InputPathType,
    response: InputPathType,
    tracks: str,
    grad: InputPathType | None = None,
    mask: InputPathType | None = None,
    riso: list[TckglobalRisoParameters] | None = None,
    lmax: int | None = None,
    length: float | None = None,
    weight: float | None = None,
    ppot: float | None = None,
    cpot: float | None = None,
    t0: float | None = None,
    t1: float | None = None,
    niter: int | None = None,
    fod: str | None = None,
    noapo: bool = False,
    fiso: str | None = None,
    eext: str | None = None,
    etrend: str | None = None,
    balance: float | None = None,
    density: float | None = None,
    prob: list[float] | None = None,
    beta: float | None = None,
    lambda_: float | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckglobalConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckglobalOutputs:
    """
    Multi-Shell Multi-Tissue Global Tractography.
    
    This command will reconstruct the global white matter fibre tractogram that
    best explains the input DWI data, using a multi-tissue spherical convolution
    model.
    
    Example use:
    
    $ tckglobal dwi.mif wmr.txt -riso csfr.txt -riso gmr.txt -mask mask.mif
    -niter 1e9 -fod fod.mif -fiso fiso.mif tracks.tck
    
    in which dwi.mif is the input image, wmr.txt is an anisotropic, multi-shell
    response function for WM, and csfr.txt and gmr.txt are isotropic response
    functions for CSF and GM. The output tractogram is saved to tracks.tck.
    Optional output images fod.mif and fiso.mif contain the predicted WM fODF
    and isotropic tissue fractions of CSF and GM respectively, estimated as part
    of the global optimization and thus affected by spatial regularization.
    
    References:
    
    Christiaens, D.; Reisert, M.; Dhollander, T.; Sunaert, S.; Suetens, P. &
    Maes, F. Global tractography of multi-shell diffusion-weighted imaging data
    using a multi-tissue model. NeuroImage, 2015, 123, 89-101.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        source: the image containing the raw DWI data.
        response: the response of a track segment on the DWI signal.
        tracks: the output file containing the tracks generated.
        grad: specify the diffusion encoding scheme (required if not supplied\
            in the header).
        mask: only reconstruct the tractogram within the specified brain mask\
            image.
        riso: set one or more isotropic response functions. (multiple allowed).
        lmax: set the maximum harmonic order for the output series. (default =\
            8).
        length: set the length of the particles (fibre segments). (default =\
            1mm).
        weight: set the weight by which particles contribute to the model.\
            (default = 0.1).
        ppot: set the particle potential, i.e., the cost of adding one segment,\
            relative to the particle weight. (default = 0.05).
        cpot: set the connection potential, i.e., the energy term that drives\
            two segments together. (default = 0.5).
        t0: set the initial temperature of the metropolis hastings optimizer.\
            (default = 0.1).
        t1: set the final temperature of the metropolis hastings optimizer.\
            (default = 0.001).
        niter: set the number of iterations of the metropolis hastings\
            optimizer. (default = 10M).
        fod: Predicted fibre orientation distribution function (fODF).\
            This fODF is estimated as part of the global track optimization,\
            and therefore incorporates the spatial regularization that it\
            imposes. Internally, the fODF is represented as a discrete sum of\
            apodized point spread functions (aPSF) oriented along the\
            directions of all particles in the voxel, used to predict the DWI\
            signal from the particle configuration.
        noapo: disable spherical convolution of fODF with apodized PSF, to\
            output a sum of delta functions rather than a sum of aPSFs.
        fiso: Predicted isotropic fractions of the tissues for which response\
            functions were provided with -riso. Typically, these are CSF and GM.
        eext: Residual external energy in every voxel.
        etrend: internal and external energy trend and cooling statistics.
        balance: balance internal and external energy. (default = 0)\
            Negative values give more weight to the internal energy, positive\
            to the external energy.
        density: set the desired density of the free Poisson process. (default\
            = 1).
        prob: set the probabilities of generating birth, death, randshift,\
            optshift and connect proposals respectively. (default =\
            0.25,0.05,0.25,0.1,0.35).
        beta: set the width of the Hanning interpolation window. (in [0, 1],\
            default = 0)\
            If used, a mask is required, and this mask must keep at least one\
            voxel distance to the image bounding box.
        lambda_: set the weight of the internal energy directly. (default = 1)\
            If provided, any value of -balance will be ignored.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TckglobalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKGLOBAL_METADATA)
    params = tckglobal_params(grad=grad, mask=mask, riso=riso, lmax=lmax, length=length, weight=weight, ppot=ppot, cpot=cpot, t0=t0, t1=t1, niter=niter, fod=fod, noapo=noapo, fiso=fiso, eext=eext, etrend=etrend, balance=balance, density=density, prob=prob, beta=beta, lambda_=lambda_, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, source=source, response=response, tracks=tracks)
    return tckglobal_execute(params, execution)


__all__ = [
    "TCKGLOBAL_METADATA",
    "TckglobalOutputs",
    "tckglobal",
    "tckglobal_config_params",
    "tckglobal_params",
    "tckglobal_riso_params",
]
