# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_HISTOGRAM_METADATA = Metadata(
    id="33a006d4e26ed5b8a4fc26f58a18e2eeb861abeb",
    name="fsl_histogram",
)


class FslHistogramOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_histogram(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    png_file: OutputPathType
    """Generated PNG file"""


def fsl_histogram(
    input_file: InputPathType,
    input_file_duplicate: InputPathType,
    output_file: str,
    output_file_duplicate: str,
    mask_file: InputPathType | None = None,
    mask_file_duplicate: InputPathType | None = None,
    gmmfit_file: InputPathType | None = None,
    gmmfit_file_duplicate: InputPathType | None = None,
    plot_title: str | None = None,
    plot_title_duplicate: str | None = None,
    legend_file: InputPathType | None = None,
    legend_file_duplicate: InputPathType | None = None,
    xlabel: str | None = None,
    xlabel_duplicate: str | None = None,
    ylabel: str | None = None,
    ylabel_duplicate: str | None = None,
    plot_height: float | int | None = None,
    plot_height_duplicate: float | int | None = None,
    plot_width: float | int | None = None,
    plot_width_duplicate: float | int | None = None,
    num_bins: float | int | None = None,
    num_bins_duplicate: float | int | None = None,
    zoom_factor: float | int | None = None,
    zoom_factor_duplicate: float | int | None = None,
    use_gmm_flag: bool = False,
    runner: Runner | None = None,
) -> FslHistogramOutputs:
    """
    fsl_histogram by University of Oxford.
    
    Histogram plotting tool for FSL.
    
    Args:
        input_file: Input file name.
        input_file_duplicate: Input file name.
        output_file: Output filename for the PNG file.
        output_file_duplicate: Output filename for the PNG file.
        mask_file: Mask file name.
        mask_file_duplicate: Mask file name.
        gmmfit_file: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        gmmfit_file_duplicate: File name of matrix with parameter estimates of\
            Gaussian/Gamma mixture model (means, variances and proportions per row).
        plot_title: Plot title.
        plot_title_duplicate: Plot title.
        legend_file: File name of ASCII text file, one row per legend entry.
        legend_file_duplicate: File name of ASCII text file, one row per legend\
            entry.
        xlabel: X-axis label.
        xlabel_duplicate: X-axis label.
        ylabel: Y-axis label.
        ylabel_duplicate: Y-axis label.
        plot_height: Plot height in pixels (default 400).
        plot_height_duplicate: Plot height in pixels (default 400).
        plot_width: Plot width in pixels (default 600).
        plot_width_duplicate: Plot width in pixels (default 600).
        num_bins: Number of histogram bins.
        num_bins_duplicate: Number of histogram bins.
        zoom_factor: Zoom factor for y-range (e.g. 2.0).
        zoom_factor_duplicate: Zoom factor for y-range (e.g. 2.0).
        use_gmm_flag: Use Gaussian mixture model instead of Gaussian/Gamma\
            mixture model.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslHistogramOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_HISTOGRAM_METADATA)
    cargs = []
    cargs.append("fsl_histogram")
    cargs.extend(["--in", execution.input_file(input_file_duplicate)])
    cargs.extend(["--out", output_file_duplicate])
    if mask_file_duplicate is not None:
        cargs.extend(["--mask", execution.input_file(mask_file_duplicate)])
    if gmmfit_file_duplicate is not None:
        cargs.extend(["--gmmfit", execution.input_file(gmmfit_file_duplicate)])
    if plot_title_duplicate is not None:
        cargs.extend(["--title", plot_title_duplicate])
    if legend_file_duplicate is not None:
        cargs.extend(["--legend", execution.input_file(legend_file_duplicate)])
    if xlabel_duplicate is not None:
        cargs.extend(["--xlabel", xlabel_duplicate])
    if ylabel_duplicate is not None:
        cargs.extend(["--ylabel", ylabel_duplicate])
    if plot_height_duplicate is not None:
        cargs.extend(["--height", str(plot_height_duplicate)])
    if plot_width_duplicate is not None:
        cargs.extend(["--width", str(plot_width_duplicate)])
    if num_bins_duplicate is not None:
        cargs.extend(["--bins", str(num_bins_duplicate)])
    if zoom_factor_duplicate is not None:
        cargs.extend(["--detail", str(zoom_factor_duplicate)])
    if use_gmm_flag:
        cargs.append("--gmm")
    ret = FslHistogramOutputs(
        root=execution.output_file("."),
        png_file=execution.output_file(f"{output_file}", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_HISTOGRAM_METADATA",
    "FslHistogramOutputs",
    "fsl_histogram",
]