# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKMAP_METADATA = Metadata(
    id="20fc0eb1cf1e5881a0131f8a9755f1e2d22946f9.boutiques",
    name="tckmap",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)
TckmapVariousStringParameters = typing.TypedDict('TckmapVariousStringParameters', {
    "__STYX_TYPE__": typing.Literal["VariousString"],
    "obj": str,
})
TckmapVariousFileParameters = typing.TypedDict('TckmapVariousFileParameters', {
    "__STYX_TYPE__": typing.Literal["VariousFile"],
    "obj": InputPathType,
})
TckmapConfigParameters = typing.TypedDict('TckmapConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})
TckmapParameters = typing.TypedDict('TckmapParameters', {
    "__STYX_TYPE__": typing.Literal["tckmap"],
    "template": typing.NotRequired[InputPathType | None],
    "vox": typing.NotRequired[list[float] | None],
    "datatype": typing.NotRequired[str | None],
    "dec": bool,
    "dixel": typing.NotRequired[typing.Union[TckmapVariousStringParameters, TckmapVariousFileParameters] | None],
    "tod": typing.NotRequired[int | None],
    "contrast": typing.NotRequired[str | None],
    "image": typing.NotRequired[InputPathType | None],
    "vector_file": typing.NotRequired[InputPathType | None],
    "stat_vox": typing.NotRequired[str | None],
    "stat_tck": typing.NotRequired[str | None],
    "fwhm_tck": typing.NotRequired[float | None],
    "map_zero": bool,
    "backtrack": bool,
    "upsample": typing.NotRequired[int | None],
    "precise": bool,
    "ends_only": bool,
    "tck_weights_in": typing.NotRequired[InputPathType | None],
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[TckmapConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks": InputPathType,
    "output": str,
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
        "tckmap": tckmap_cargs,
        "VariousString": tckmap_various_string_cargs,
        "VariousFile": tckmap_various_file_cargs,
        "config": tckmap_config_cargs,
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
        "tckmap": tckmap_outputs,
    }
    return vt.get(t)


def tckmap_various_string_params(
    obj: str,
) -> TckmapVariousStringParameters:
    """
    Build parameters.
    
    Args:
        obj: String object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousString",
        "obj": obj,
    }
    return params


def tckmap_various_string_cargs(
    params: TckmapVariousStringParameters,
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
    cargs.append(params.get("obj"))
    return cargs


def tckmap_various_file_params(
    obj: InputPathType,
) -> TckmapVariousFileParameters:
    """
    Build parameters.
    
    Args:
        obj: File object.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "VariousFile",
        "obj": obj,
    }
    return params


def tckmap_various_file_cargs(
    params: TckmapVariousFileParameters,
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
    cargs.append(execution.input_file(params.get("obj")))
    return cargs


def tckmap_config_params(
    key: str,
    value: str,
) -> TckmapConfigParameters:
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


def tckmap_config_cargs(
    params: TckmapConfigParameters,
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


class TckmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track-weighted image"""


def tckmap_params(
    tracks: InputPathType,
    output: str,
    template: InputPathType | None = None,
    vox: list[float] | None = None,
    datatype: str | None = None,
    dec: bool = False,
    dixel: typing.Union[TckmapVariousStringParameters, TckmapVariousFileParameters] | None = None,
    tod: int | None = None,
    contrast: str | None = None,
    image: InputPathType | None = None,
    vector_file: InputPathType | None = None,
    stat_vox: str | None = None,
    stat_tck: str | None = None,
    fwhm_tck: float | None = None,
    map_zero: bool = False,
    backtrack: bool = False,
    upsample: int | None = None,
    precise: bool = False,
    ends_only: bool = False,
    tck_weights_in: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckmapConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> TckmapParameters:
    """
    Build parameters.
    
    Args:
        tracks: the input track file.
        output: the output track-weighted image.
        template: an image file to be used as a template for the output (the\
            output image will have the same transform and field of view).
        vox: provide either an isotropic voxel size (in mm), or comma-separated\
            list of 3 voxel dimensions.
        datatype: specify output image data type.
        dec: perform track mapping in directionally-encoded colour (DEC) space.
        dixel: map streamlines to dixels within each voxel; requires either a\
            number of dixels (references an internal direction set), or a path to a\
            text file containing a set of directions stored as azimuth/elevation\
            pairs.
        tod: generate a Track Orientation Distribution (TOD) in each voxel;\
            need to specify the maximum spherical harmonic degree lmax to use when\
            generating Apodised Point Spread Functions.
        contrast: define the desired form of contrast for the output image\
            Options are: tdi, length, invlength, scalar_map, scalar_map_count,\
            fod_amp, curvature, vector_file (default: tdi).
        image: provide the scalar image map for generating images with\
            'scalar_map' / 'scalar_map_count' contrast, or the spherical harmonics\
            image for 'fod_amp' contrast.
        vector_file: provide the vector data file for generating images with\
            'vector_file' contrast.
        stat_vox: define the statistic for choosing the final voxel intensities\
            for a given contrast type given the individual values from the tracks\
            passing through each voxel.\
            Options are: sum, min, mean, max (default: sum).
        stat_tck: define the statistic for choosing the contribution to be made\
            by each streamline as a function of the samples taken along their\
            lengths.\
            Only has an effect for 'scalar_map', 'fod_amp' and 'curvature'\
            contrast types.\
            Options are: sum, min, mean, max, median, mean_nonzero, gaussian,\
            ends_min, ends_mean, ends_max, ends_prod (default: mean).
        fwhm_tck: when using gaussian-smoothed per-track statistic, specify the\
            desired full-width half-maximum of the Gaussian smoothing kernel (in\
            mm).
        map_zero: if a streamline has zero contribution based on the contrast &\
            statistic, typically it is not mapped; use this option to still\
            contribute to the map even if this is the case (these non-contributing\
            voxels can then influence the mean value in each voxel of the map).
        backtrack: when using -stat_tck ends_*, if the streamline endpoint is\
            outside the FoV, backtrack along the streamline trajectory until an\
            appropriate point is found.
        upsample: upsample the tracks by some ratio using Hermite interpolation\
            before mappping\
            (If omitted, an appropriate ratio will be determined automatically).
        precise: use a more precise streamline mapping strategy, that\
            accurately quantifies the length through each voxel (these lengths are\
            then taken into account during TWI calculation).
        ends_only: only map the streamline endpoints to the image.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
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
        "__STYXTYPE__": "tckmap",
        "dec": dec,
        "map_zero": map_zero,
        "backtrack": backtrack,
        "precise": precise,
        "ends_only": ends_only,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks": tracks,
        "output": output,
    }
    if template is not None:
        params["template"] = template
    if vox is not None:
        params["vox"] = vox
    if datatype is not None:
        params["datatype"] = datatype
    if dixel is not None:
        params["dixel"] = dixel
    if tod is not None:
        params["tod"] = tod
    if contrast is not None:
        params["contrast"] = contrast
    if image is not None:
        params["image"] = image
    if vector_file is not None:
        params["vector_file"] = vector_file
    if stat_vox is not None:
        params["stat_vox"] = stat_vox
    if stat_tck is not None:
        params["stat_tck"] = stat_tck
    if fwhm_tck is not None:
        params["fwhm_tck"] = fwhm_tck
    if upsample is not None:
        params["upsample"] = upsample
    if tck_weights_in is not None:
        params["tck_weights_in"] = tck_weights_in
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tckmap_cargs(
    params: TckmapParameters,
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
    cargs.append("tckmap")
    if params.get("template") is not None:
        cargs.extend([
            "-template",
            execution.input_file(params.get("template"))
        ])
    if params.get("vox") is not None:
        cargs.extend([
            "-vox",
            ",".join(map(str, params.get("vox")))
        ])
    if params.get("datatype") is not None:
        cargs.extend([
            "-datatype",
            params.get("datatype")
        ])
    if params.get("dec"):
        cargs.append("-dec")
    if params.get("dixel") is not None:
        cargs.extend([
            "-dixel",
            *dyn_cargs(params.get("dixel")["__STYXTYPE__"])(params.get("dixel"), execution)
        ])
    if params.get("tod") is not None:
        cargs.extend([
            "-tod",
            str(params.get("tod"))
        ])
    if params.get("contrast") is not None:
        cargs.extend([
            "-contrast",
            params.get("contrast")
        ])
    if params.get("image") is not None:
        cargs.extend([
            "-image",
            execution.input_file(params.get("image"))
        ])
    if params.get("vector_file") is not None:
        cargs.extend([
            "-vector_file",
            execution.input_file(params.get("vector_file"))
        ])
    if params.get("stat_vox") is not None:
        cargs.extend([
            "-stat_vox",
            params.get("stat_vox")
        ])
    if params.get("stat_tck") is not None:
        cargs.extend([
            "-stat_tck",
            params.get("stat_tck")
        ])
    if params.get("fwhm_tck") is not None:
        cargs.extend([
            "-fwhm_tck",
            str(params.get("fwhm_tck"))
        ])
    if params.get("map_zero"):
        cargs.append("-map_zero")
    if params.get("backtrack"):
        cargs.append("-backtrack")
    if params.get("upsample") is not None:
        cargs.extend([
            "-upsample",
            str(params.get("upsample"))
        ])
    if params.get("precise"):
        cargs.append("-precise")
    if params.get("ends_only"):
        cargs.append("-ends_only")
    if params.get("tck_weights_in") is not None:
        cargs.extend([
            "-tck_weights_in",
            execution.input_file(params.get("tck_weights_in"))
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
    cargs.append(execution.input_file(params.get("tracks")))
    cargs.append(params.get("output"))
    return cargs


def tckmap_outputs(
    params: TckmapParameters,
    execution: Execution,
) -> TckmapOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = TckmapOutputs(
        root=execution.output_file("."),
        output=execution.output_file(params.get("output")),
    )
    return ret


def tckmap_execute(
    params: TckmapParameters,
    execution: Execution,
) -> TckmapOutputs:
    """
    Use track data as a form of contrast for producing a high-resolution image.
    
    Note: if you run into limitations with RAM usage, make sure you output the
    results to a .mif file or .mih / .dat file pair - this will avoid the
    allocation of an additional buffer to store the output for write-out.
    
    References:
    
    * For TDI or DEC TDI:
    Calamante, F.; Tournier, J.-D.; Jackson, G. D. & Connelly, A. Track-density
    imaging (TDI): Super-resolution white matter imaging using whole-brain
    track-density mapping. NeuroImage, 2010, 53, 1233-1243
    
    * If using -contrast length and -stat_vox mean:
    Pannek, K.; Mathias, J. L.; Bigler, E. D.; Brown, G.; Taylor, J. D. & Rose,
    S. E. The average pathlength map: A diffusion MRI tractography-derived index
    for studying brain pathology. NeuroImage, 2011, 55, 133-141
    
    * If using -dixel option with TDI contrast only:
    Smith, R.E., Tournier, J-D., Calamante, F., Connelly, A. A novel paradigm
    for automated segmentation of very large whole-brain probabilistic
    tractography data sets. In proc. ISMRM, 2011, 19, 673
    
    * If using -dixel option with any other contrast:
    Pannek, K., Raffelt, D., Salvado, O., Rose, S. Incorporating directional
    information in diffusion tractography derived maps: angular track imaging
    (ATI). In Proc. ISMRM, 2012, 20, 1912
    
    * If using -tod option:
    Dhollander, T., Emsell, L., Van Hecke, W., Maes, F., Sunaert, S., Suetens,
    P. Track Orientation Density Imaging (TODI) and Track Orientation
    Distribution (TOD) based tractography. NeuroImage, 2014, 94, 312-336
    
    * If using other contrasts / statistics:
    Calamante, F.; Tournier, J.-D.; Smith, R. E. & Connelly, A. A generalised
    framework for super-resolution track-weighted imaging. NeuroImage, 2012, 59,
    2494-2503
    
    * If using -precise mapping option:
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT:
    Spherical-deconvolution informed filtering of tractograms. NeuroImage, 2013,
    67, 298-312 (Appendix 3).
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `TckmapOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = tckmap_cargs(params, execution)
    ret = tckmap_outputs(params, execution)
    execution.run(cargs)
    return ret


def tckmap(
    tracks: InputPathType,
    output: str,
    template: InputPathType | None = None,
    vox: list[float] | None = None,
    datatype: str | None = None,
    dec: bool = False,
    dixel: typing.Union[TckmapVariousStringParameters, TckmapVariousFileParameters] | None = None,
    tod: int | None = None,
    contrast: str | None = None,
    image: InputPathType | None = None,
    vector_file: InputPathType | None = None,
    stat_vox: str | None = None,
    stat_tck: str | None = None,
    fwhm_tck: float | None = None,
    map_zero: bool = False,
    backtrack: bool = False,
    upsample: int | None = None,
    precise: bool = False,
    ends_only: bool = False,
    tck_weights_in: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckmapConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckmapOutputs:
    """
    Use track data as a form of contrast for producing a high-resolution image.
    
    Note: if you run into limitations with RAM usage, make sure you output the
    results to a .mif file or .mih / .dat file pair - this will avoid the
    allocation of an additional buffer to store the output for write-out.
    
    References:
    
    * For TDI or DEC TDI:
    Calamante, F.; Tournier, J.-D.; Jackson, G. D. & Connelly, A. Track-density
    imaging (TDI): Super-resolution white matter imaging using whole-brain
    track-density mapping. NeuroImage, 2010, 53, 1233-1243
    
    * If using -contrast length and -stat_vox mean:
    Pannek, K.; Mathias, J. L.; Bigler, E. D.; Brown, G.; Taylor, J. D. & Rose,
    S. E. The average pathlength map: A diffusion MRI tractography-derived index
    for studying brain pathology. NeuroImage, 2011, 55, 133-141
    
    * If using -dixel option with TDI contrast only:
    Smith, R.E., Tournier, J-D., Calamante, F., Connelly, A. A novel paradigm
    for automated segmentation of very large whole-brain probabilistic
    tractography data sets. In proc. ISMRM, 2011, 19, 673
    
    * If using -dixel option with any other contrast:
    Pannek, K., Raffelt, D., Salvado, O., Rose, S. Incorporating directional
    information in diffusion tractography derived maps: angular track imaging
    (ATI). In Proc. ISMRM, 2012, 20, 1912
    
    * If using -tod option:
    Dhollander, T., Emsell, L., Van Hecke, W., Maes, F., Sunaert, S., Suetens,
    P. Track Orientation Density Imaging (TODI) and Track Orientation
    Distribution (TOD) based tractography. NeuroImage, 2014, 94, 312-336
    
    * If using other contrasts / statistics:
    Calamante, F.; Tournier, J.-D.; Smith, R. E. & Connelly, A. A generalised
    framework for super-resolution track-weighted imaging. NeuroImage, 2012, 59,
    2494-2503
    
    * If using -precise mapping option:
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT:
    Spherical-deconvolution informed filtering of tractograms. NeuroImage, 2013,
    67, 298-312 (Appendix 3).
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks: the input track file.
        output: the output track-weighted image.
        template: an image file to be used as a template for the output (the\
            output image will have the same transform and field of view).
        vox: provide either an isotropic voxel size (in mm), or comma-separated\
            list of 3 voxel dimensions.
        datatype: specify output image data type.
        dec: perform track mapping in directionally-encoded colour (DEC) space.
        dixel: map streamlines to dixels within each voxel; requires either a\
            number of dixels (references an internal direction set), or a path to a\
            text file containing a set of directions stored as azimuth/elevation\
            pairs.
        tod: generate a Track Orientation Distribution (TOD) in each voxel;\
            need to specify the maximum spherical harmonic degree lmax to use when\
            generating Apodised Point Spread Functions.
        contrast: define the desired form of contrast for the output image\
            Options are: tdi, length, invlength, scalar_map, scalar_map_count,\
            fod_amp, curvature, vector_file (default: tdi).
        image: provide the scalar image map for generating images with\
            'scalar_map' / 'scalar_map_count' contrast, or the spherical harmonics\
            image for 'fod_amp' contrast.
        vector_file: provide the vector data file for generating images with\
            'vector_file' contrast.
        stat_vox: define the statistic for choosing the final voxel intensities\
            for a given contrast type given the individual values from the tracks\
            passing through each voxel.\
            Options are: sum, min, mean, max (default: sum).
        stat_tck: define the statistic for choosing the contribution to be made\
            by each streamline as a function of the samples taken along their\
            lengths.\
            Only has an effect for 'scalar_map', 'fod_amp' and 'curvature'\
            contrast types.\
            Options are: sum, min, mean, max, median, mean_nonzero, gaussian,\
            ends_min, ends_mean, ends_max, ends_prod (default: mean).
        fwhm_tck: when using gaussian-smoothed per-track statistic, specify the\
            desired full-width half-maximum of the Gaussian smoothing kernel (in\
            mm).
        map_zero: if a streamline has zero contribution based on the contrast &\
            statistic, typically it is not mapped; use this option to still\
            contribute to the map even if this is the case (these non-contributing\
            voxels can then influence the mean value in each voxel of the map).
        backtrack: when using -stat_tck ends_*, if the streamline endpoint is\
            outside the FoV, backtrack along the streamline trajectory until an\
            appropriate point is found.
        upsample: upsample the tracks by some ratio using Hermite interpolation\
            before mappping\
            (If omitted, an appropriate ratio will be determined automatically).
        precise: use a more precise streamline mapping strategy, that\
            accurately quantifies the length through each voxel (these lengths are\
            then taken into account during TWI calculation).
        ends_only: only map the streamline endpoints to the image.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
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
        NamedTuple of outputs (described in `TckmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKMAP_METADATA)
    params = tckmap_params(template=template, vox=vox, datatype=datatype, dec=dec, dixel=dixel, tod=tod, contrast=contrast, image=image, vector_file=vector_file, stat_vox=stat_vox, stat_tck=stat_tck, fwhm_tck=fwhm_tck, map_zero=map_zero, backtrack=backtrack, upsample=upsample, precise=precise, ends_only=ends_only, tck_weights_in=tck_weights_in, info=info, quiet=quiet, debug=debug, force=force, nthreads=nthreads, config=config, help_=help_, version=version, tracks=tracks, output=output)
    return tckmap_execute(params, execution)


__all__ = [
    "TCKMAP_METADATA",
    "TckmapOutputs",
    "tckmap",
    "tckmap_config_params",
    "tckmap_params",
    "tckmap_various_file_params",
    "tckmap_various_string_params",
]
