# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURF_SMOOTH_METADATA = Metadata(
    id="ff78abe6a6fbceb953687fc929f58909c68d6499.boutiques",
    name="SurfSmooth",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class SurfSmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_smooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Name of the output file."""


def surf_smooth(
    surface: str,
    method: str,
    input_data: InputPathType | None = None,
    target_fwhm: float | None = None,
    fwhm: float | None = None,
    number_iterations: float | None = None,
    output_file: InputPathType | None = None,
    band_pass_frequency: float | None = None,
    lambda_mu: str | None = None,
    interp_weights: str | None = None,
    node_mask: InputPathType | None = None,
    surface_output: InputPathType | None = None,
    dbg_node: float | None = None,
    use_neighbors_outside_mask: bool = False,
    talk_suma: bool = False,
    refresh_rate: float | None = None,
    runner: Runner | None = None,
) -> SurfSmoothOutputs:
    """
    Tool for smoothing data on surfaces using various methods.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfSmooth.html
    
    Args:
        surface: Option for specifying the surface to smooth or the domain over\
            which DSET is defined.
        method: Name of smoothing method to use. Choose from: HEAT_07, HEAT_05,\
            LM, NN_geom.
        input_data: File containing data (in 1D or NIML format). Required for\
            HEAT_05 and HEAT_07 methods.
        target_fwhm: Blur so that the final FWHM of the data is TF mm. Only for\
            HEAT_07 method.
        fwhm: Effective Full Width at Half Maximum for smoothing. Required for\
            HEAT_05 and optional for HEAT_07 methods.
        number_iterations: Number of smoothing iterations (default is 100 for\
            LM and NN_geom, -1 for HEAT methods).
        output_file: Name of output file. Default based on method being used.
        band_pass_frequency: Bandpass frequency for LM method (0 < k < 10).
        lambda_mu: Lambda and Mu parameters for LM method. Sample values are:\
            0.6307 and -0.6732.
        interp_weights: Set interpolation weights for LM method. Options:\
            Equal, Fujiwara, Desbrun.
        node_mask: Apply operations only to nodes listed in the given mask.
        surface_output: Writes the surface with smoothed coordinates to disk.\
            For LM and NN_geom methods.
        dbg_node: Output debug information for node 'node'.
        use_neighbors_outside_mask: Allow value from a node neighboring node n\
            to contribute to the value at n even if the neighbor is not in the\
            mask.
        talk_suma: Send progress with each iteration to SUMA for real-time\
            visualization.
        refresh_rate: Maximum number of updates to SUMA per second.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfSmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_SMOOTH_METADATA)
    cargs = []
    cargs.append("SurfSmooth")
    cargs.extend([
        "-SURF_1",
        surface
    ])
    cargs.extend([
        "-met",
        method
    ])
    if input_data is not None:
        cargs.extend([
            "-input",
            execution.input_file(input_data)
        ])
    if target_fwhm is not None:
        cargs.extend([
            "-target_fwhm",
            str(target_fwhm)
        ])
    if fwhm is not None:
        cargs.extend([
            "-fwhm",
            str(fwhm)
        ])
    if number_iterations is not None:
        cargs.extend([
            "-Niter",
            str(number_iterations)
        ])
    if output_file is not None:
        cargs.extend([
            "-output",
            execution.input_file(output_file)
        ])
    if band_pass_frequency is not None:
        cargs.extend([
            "-kpb",
            str(band_pass_frequency)
        ])
    if lambda_mu is not None:
        cargs.extend([
            "-lm",
            lambda_mu
        ])
    if interp_weights is not None:
        cargs.extend([
            "-iw",
            interp_weights
        ])
    if node_mask is not None:
        cargs.extend([
            "-MASK",
            execution.input_file(node_mask)
        ])
    if surface_output is not None:
        cargs.extend([
            "-surf_out",
            execution.input_file(surface_output)
        ])
    if dbg_node is not None:
        cargs.extend([
            "-dbg_n",
            str(dbg_node)
        ])
    if use_neighbors_outside_mask:
        cargs.append("-use_neighbors_outside_mask")
    if talk_suma:
        cargs.append("-talk_suma")
    if refresh_rate is not None:
        cargs.extend([
            "-refresh_rate",
            str(refresh_rate)
        ])
    ret = SurfSmoothOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(pathlib.Path(output_file).name) if (output_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURF_SMOOTH_METADATA",
    "SurfSmoothOutputs",
    "surf_smooth",
]
