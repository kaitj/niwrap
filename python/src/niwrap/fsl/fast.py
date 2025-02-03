# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAST_METADATA = Metadata(
    id="042321f76ec57a5cbf517c2d9669a0a520259d5c.boutiques",
    name="fast",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)
FastParameters = typing.TypedDict('FastParameters', {
    "__STYX_TYPE__": typing.Literal["fast"],
    "number_classes": typing.NotRequired[int | None],
    "bias_iters": typing.NotRequired[int | None],
    "bias_lowpass": typing.NotRequired[float | None],
    "img_type": typing.NotRequired[typing.Literal[1, 2, 3] | None],
    "init_seg_smooth": typing.NotRequired[float | None],
    "segments": bool,
    "init_transform": typing.NotRequired[InputPathType | None],
    "other_priors": typing.NotRequired[list[InputPathType] | None],
    "output_biasfield": bool,
    "output_biascorrected": bool,
    "no_bias": bool,
    "channels": typing.NotRequired[int | None],
    "out_basename": typing.NotRequired[str | None],
    "use_priors": bool,
    "no_pve": bool,
    "segment_iters": typing.NotRequired[int | None],
    "mixel_smooth": typing.NotRequired[float | None],
    "hyper": typing.NotRequired[float | None],
    "verbose": bool,
    "manual_seg": typing.NotRequired[InputPathType | None],
    "iters_afterbias": typing.NotRequired[int | None],
    "in_files": list[InputPathType],
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
        "fast": fast_cargs,
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
        "fast": fast_outputs,
    }
    return vt.get(t)


class FastOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fast(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mixeltype: OutputPathType | None
    """Path/name of mixeltype volume file _mixeltype."""
    bias_field: OutputPathType | None
    """No description provided."""
    partial_volume_map: OutputPathType | None
    """Path/name of partial volume file _pveseg."""
    restored_image: OutputPathType | None
    """No description provided."""
    tissue_class_map: OutputPathType | None
    """Path/name of binary segmented volume file one val for each class _seg."""


def fast_params(
    in_files: list[InputPathType],
    number_classes: int | None = None,
    bias_iters: int | None = None,
    bias_lowpass: float | None = None,
    img_type: typing.Literal[1, 2, 3] | None = None,
    init_seg_smooth: float | None = None,
    segments: bool = False,
    init_transform: InputPathType | None = None,
    other_priors: list[InputPathType] | None = None,
    output_biasfield: bool = False,
    output_biascorrected: bool = False,
    no_bias: bool = False,
    channels: int | None = None,
    out_basename: str | None = "fast_out",
    use_priors: bool = False,
    no_pve: bool = False,
    segment_iters: int | None = None,
    mixel_smooth: float | None = None,
    hyper: float | None = None,
    verbose: bool = False,
    manual_seg: InputPathType | None = None,
    iters_afterbias: int | None = None,
) -> FastParameters:
    """
    Build parameters.
    
    Args:
        in_files: Image, or multi-channel set of images, to be segmented.
        number_classes: number of tissue-type classes; default=3.
        bias_iters: number of main-loop iterations during bias-field removal;\
            default=4.
        bias_lowpass: bias field smoothing extent (FWHM) in mm; default=20.
        img_type: type of image 1=T1, 2=T2, 3=PD; default=T1.
        init_seg_smooth: initial segmentation spatial smoothness (during bias\
            field estimation); default=0.02.
        segments: outputs a separate binary image for each tissue type.
        init_transform: initialise using priors; you must supply a FLIRT\
            transform.
        other_priors: Alternative prior images.
        output_biasfield: Output estimated bias field.
        output_biascorrected: Output restored image (bias-corrected image).
        no_bias: Do not remove bias field.
        channels: number of input images (channels); default 1.
        out_basename: Base name of output files.
        use_priors: Use priors throughout.
        no_pve: Turn off pve (partial volume estimation).
        segment_iters: number of segmentation-initialisation iterations;\
            default=15.
        mixel_smooth: spatial smoothness for mixeltype; default=0.3.
        hyper: 0.0 <= a floating point number <= 1.0. segmentation spatial\
            smoothness; default=0.1.
        verbose: Switch on diagnostic messages.
        manual_seg: Filename containing intensities.
        iters_afterbias: number of main-loop iterations after bias-field\
            removal; default=4.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "fast",
        "segments": segments,
        "output_biasfield": output_biasfield,
        "output_biascorrected": output_biascorrected,
        "no_bias": no_bias,
        "use_priors": use_priors,
        "no_pve": no_pve,
        "verbose": verbose,
        "in_files": in_files,
    }
    if number_classes is not None:
        params["number_classes"] = number_classes
    if bias_iters is not None:
        params["bias_iters"] = bias_iters
    if bias_lowpass is not None:
        params["bias_lowpass"] = bias_lowpass
    if img_type is not None:
        params["img_type"] = img_type
    if init_seg_smooth is not None:
        params["init_seg_smooth"] = init_seg_smooth
    if init_transform is not None:
        params["init_transform"] = init_transform
    if other_priors is not None:
        params["other_priors"] = other_priors
    if channels is not None:
        params["channels"] = channels
    if out_basename is not None:
        params["out_basename"] = out_basename
    if segment_iters is not None:
        params["segment_iters"] = segment_iters
    if mixel_smooth is not None:
        params["mixel_smooth"] = mixel_smooth
    if hyper is not None:
        params["hyper"] = hyper
    if manual_seg is not None:
        params["manual_seg"] = manual_seg
    if iters_afterbias is not None:
        params["iters_afterbias"] = iters_afterbias
    return params


def fast_cargs(
    params: FastParameters,
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
    cargs.append("fast")
    if params.get("number_classes") is not None:
        cargs.extend([
            "-n",
            str(params.get("number_classes"))
        ])
    if params.get("bias_iters") is not None:
        cargs.extend([
            "-I",
            str(params.get("bias_iters"))
        ])
    if params.get("bias_lowpass") is not None:
        cargs.extend([
            "-l",
            str(params.get("bias_lowpass"))
        ])
    if params.get("img_type") is not None:
        cargs.extend([
            "-t",
            str(params.get("img_type"))
        ])
    if params.get("init_seg_smooth") is not None:
        cargs.extend([
            "-f",
            str(params.get("init_seg_smooth"))
        ])
    if params.get("segments"):
        cargs.append("-g")
    if params.get("init_transform") is not None:
        cargs.extend([
            "-a",
            execution.input_file(params.get("init_transform"))
        ])
    if params.get("other_priors") is not None:
        cargs.extend([
            "-A",
            *[execution.input_file(f) for f in params.get("other_priors")]
        ])
    if params.get("output_biasfield"):
        cargs.append("-b")
    if params.get("output_biascorrected"):
        cargs.append("-B")
    if params.get("no_bias"):
        cargs.append("-N")
    if params.get("channels") is not None:
        cargs.extend([
            "-S",
            str(params.get("channels"))
        ])
    if params.get("out_basename") is not None:
        cargs.extend([
            "-o",
            params.get("out_basename")
        ])
    if params.get("use_priors"):
        cargs.append("-P")
    if params.get("no_pve"):
        cargs.append("--nopve")
    if params.get("segment_iters") is not None:
        cargs.extend([
            "-W",
            str(params.get("segment_iters"))
        ])
    if params.get("mixel_smooth") is not None:
        cargs.extend([
            "-R",
            str(params.get("mixel_smooth"))
        ])
    if params.get("hyper") is not None:
        cargs.extend([
            "-H",
            str(params.get("hyper"))
        ])
    if params.get("verbose"):
        cargs.append("-v")
    if params.get("manual_seg") is not None:
        cargs.extend([
            "-s",
            execution.input_file(params.get("manual_seg"))
        ])
    if params.get("iters_afterbias") is not None:
        cargs.extend([
            "-O",
            str(params.get("iters_afterbias"))
        ])
    cargs.extend([execution.input_file(f) for f in params.get("in_files")])
    return cargs


def fast_outputs(
    params: FastParameters,
    execution: Execution,
) -> FastOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = FastOutputs(
        root=execution.output_file("."),
        mixeltype=execution.output_file(params.get("out_basename") + "_mixeltype.nii.gz") if (params.get("out_basename") is not None) else None,
        bias_field=execution.output_file(params.get("out_basename") + "_bias.nii.gz") if (params.get("out_basename") is not None) else None,
        partial_volume_map=execution.output_file(params.get("out_basename") + "_pveseg.nii.gz") if (params.get("out_basename") is not None) else None,
        restored_image=execution.output_file(params.get("out_basename") + "_restore.nii.gz") if (params.get("out_basename") is not None) else None,
        tissue_class_map=execution.output_file(params.get("out_basename") + "_seg.nii.gz") if (params.get("out_basename") is not None) else None,
    )
    return ret


def fast_execute(
    params: FastParameters,
    execution: Execution,
) -> FastOutputs:
    """
    FAST (FMRIB's Automated Segmentation Tool) segments a 3D image of the brain into
    different tissue types (Grey Matter, White Matter, CSF, etc.), whilst also
    correcting for spatial intensity variations (also known as bias field or RF
    inhomogeneities). The underlying method is based on a hidden Markov random field
    model and an associated Expectation-Maximization algorithm. The whole process is
    fully automated and can also produce a bias field-corrected input image and a
    probabilistic and/or partial volume tissue segmentation. It is robust and
    reliable, compared to most finite mixture model-based methods, which are
    sensitive to noise.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `FastOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = fast_cargs(params, execution)
    ret = fast_outputs(params, execution)
    execution.run(cargs)
    return ret


def fast(
    in_files: list[InputPathType],
    number_classes: int | None = None,
    bias_iters: int | None = None,
    bias_lowpass: float | None = None,
    img_type: typing.Literal[1, 2, 3] | None = None,
    init_seg_smooth: float | None = None,
    segments: bool = False,
    init_transform: InputPathType | None = None,
    other_priors: list[InputPathType] | None = None,
    output_biasfield: bool = False,
    output_biascorrected: bool = False,
    no_bias: bool = False,
    channels: int | None = None,
    out_basename: str | None = "fast_out",
    use_priors: bool = False,
    no_pve: bool = False,
    segment_iters: int | None = None,
    mixel_smooth: float | None = None,
    hyper: float | None = None,
    verbose: bool = False,
    manual_seg: InputPathType | None = None,
    iters_afterbias: int | None = None,
    runner: Runner | None = None,
) -> FastOutputs:
    """
    FAST (FMRIB's Automated Segmentation Tool) segments a 3D image of the brain into
    different tissue types (Grey Matter, White Matter, CSF, etc.), whilst also
    correcting for spatial intensity variations (also known as bias field or RF
    inhomogeneities). The underlying method is based on a hidden Markov random field
    model and an associated Expectation-Maximization algorithm. The whole process is
    fully automated and can also produce a bias field-corrected input image and a
    probabilistic and/or partial volume tissue segmentation. It is robust and
    reliable, compared to most finite mixture model-based methods, which are
    sensitive to noise.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        in_files: Image, or multi-channel set of images, to be segmented.
        number_classes: number of tissue-type classes; default=3.
        bias_iters: number of main-loop iterations during bias-field removal;\
            default=4.
        bias_lowpass: bias field smoothing extent (FWHM) in mm; default=20.
        img_type: type of image 1=T1, 2=T2, 3=PD; default=T1.
        init_seg_smooth: initial segmentation spatial smoothness (during bias\
            field estimation); default=0.02.
        segments: outputs a separate binary image for each tissue type.
        init_transform: initialise using priors; you must supply a FLIRT\
            transform.
        other_priors: Alternative prior images.
        output_biasfield: Output estimated bias field.
        output_biascorrected: Output restored image (bias-corrected image).
        no_bias: Do not remove bias field.
        channels: number of input images (channels); default 1.
        out_basename: Base name of output files.
        use_priors: Use priors throughout.
        no_pve: Turn off pve (partial volume estimation).
        segment_iters: number of segmentation-initialisation iterations;\
            default=15.
        mixel_smooth: spatial smoothness for mixeltype; default=0.3.
        hyper: 0.0 <= a floating point number <= 1.0. segmentation spatial\
            smoothness; default=0.1.
        verbose: Switch on diagnostic messages.
        manual_seg: Filename containing intensities.
        iters_afterbias: number of main-loop iterations after bias-field\
            removal; default=4.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FastOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAST_METADATA)
    params = fast_params(number_classes=number_classes, bias_iters=bias_iters, bias_lowpass=bias_lowpass, img_type=img_type, init_seg_smooth=init_seg_smooth, segments=segments, init_transform=init_transform, other_priors=other_priors, output_biasfield=output_biasfield, output_biascorrected=output_biascorrected, no_bias=no_bias, channels=channels, out_basename=out_basename, use_priors=use_priors, no_pve=no_pve, segment_iters=segment_iters, mixel_smooth=mixel_smooth, hyper=hyper, verbose=verbose, manual_seg=manual_seg, iters_afterbias=iters_afterbias, in_files=in_files)
    return fast_execute(params, execution)


__all__ = [
    "FAST_METADATA",
    "FastOutputs",
    "fast",
    "fast_params",
]
