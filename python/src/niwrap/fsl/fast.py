# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAST_METADATA = Metadata(
    id="ea3782de983ce088a9fbd87043027a7111fd16cd.boutiques",
    name="fast",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


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
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FAST
    
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
    if number_classes is not None and not (1 <= number_classes): 
        raise ValueError(f"'number_classes' must be greater than 1 <= x but was {number_classes}")
    if bias_iters is not None and not (1 <= bias_iters): 
        raise ValueError(f"'bias_iters' must be greater than 1 <= x but was {bias_iters}")
    if bias_lowpass is not None and not (0 <= bias_lowpass): 
        raise ValueError(f"'bias_lowpass' must be greater than 0 <= x but was {bias_lowpass}")
    if segment_iters is not None and not (1 <= segment_iters): 
        raise ValueError(f"'segment_iters' must be greater than 1 <= x but was {segment_iters}")
    if hyper is not None and not (0.0 <= hyper <= 1.0): 
        raise ValueError(f"'hyper' must be between 0.0 <= x <= 1.0 but was {hyper}")
    if iters_afterbias is not None and not (1 <= iters_afterbias): 
        raise ValueError(f"'iters_afterbias' must be greater than 1 <= x but was {iters_afterbias}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAST_METADATA)
    cargs = []
    cargs.append("fast")
    if number_classes is not None:
        cargs.extend([
            "-n",
            str(number_classes)
        ])
    if bias_iters is not None:
        cargs.extend([
            "-I",
            str(bias_iters)
        ])
    if bias_lowpass is not None:
        cargs.extend([
            "-l",
            str(bias_lowpass)
        ])
    if img_type is not None:
        cargs.extend([
            "-t",
            str(img_type)
        ])
    if init_seg_smooth is not None:
        cargs.extend([
            "-f",
            str(init_seg_smooth)
        ])
    if segments:
        cargs.append("-g")
    if init_transform is not None:
        cargs.extend([
            "-a",
            execution.input_file(init_transform)
        ])
    if other_priors is not None:
        cargs.extend([
            "-A",
            *[execution.input_file(f) for f in other_priors]
        ])
    if output_biasfield:
        cargs.append("-b")
    if output_biascorrected:
        cargs.append("-B")
    if no_bias:
        cargs.append("-N")
    if channels is not None:
        cargs.extend([
            "-S",
            str(channels)
        ])
    if out_basename is not None:
        cargs.extend([
            "-o",
            out_basename
        ])
    if use_priors:
        cargs.append("-P")
    if no_pve:
        cargs.append("--nopve")
    if segment_iters is not None:
        cargs.extend([
            "-W",
            str(segment_iters)
        ])
    if mixel_smooth is not None:
        cargs.extend([
            "-R",
            str(mixel_smooth)
        ])
    if hyper is not None:
        cargs.extend([
            "-H",
            str(hyper)
        ])
    if verbose:
        cargs.append("-v")
    if manual_seg is not None:
        cargs.extend([
            "-s",
            execution.input_file(manual_seg)
        ])
    if iters_afterbias is not None:
        cargs.extend([
            "-O",
            str(iters_afterbias)
        ])
    cargs.extend([execution.input_file(f) for f in in_files])
    ret = FastOutputs(
        root=execution.output_file("."),
        mixeltype=execution.output_file(out_basename + "_mixeltype.nii.gz") if (out_basename is not None) else None,
        bias_field=execution.output_file(out_basename + "_bias.nii.gz") if (out_basename is not None) else None,
        partial_volume_map=execution.output_file(out_basename + "_pveseg.nii.gz") if (out_basename is not None) else None,
        restored_image=execution.output_file(out_basename + "_restore.nii.gz") if (out_basename is not None) else None,
        tissue_class_map=execution.output_file(out_basename + "_seg.nii.gz") if (out_basename is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAST_METADATA",
    "FastOutputs",
    "fast",
]
