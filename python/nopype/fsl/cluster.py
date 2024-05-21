# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CLUSTER_METADATA = Metadata(
    id="e7684e1f87a871bd106b15aa007a39ffbebfffb6",
    name="Cluster",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ClusterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cluster(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    index_file: OutputPathType
    """Output of cluster index (in size order)."""
    localmax_txt_file: OutputPathType
    """Local maxima text file."""
    localmax_vol_file: OutputPathType
    """Output of local maxima volume."""
    max_file: OutputPathType
    """Filename for output of max image."""
    mean_file: OutputPathType
    """Filename for output of mean image."""
    pval_file: OutputPathType
    """Filename for image output of log pvals."""
    size_file: OutputPathType
    """Filename for output of size image."""
    threshold_file: OutputPathType
    """Thresholded image."""


def cluster(
    runner: Runner,
    in_file: InputPathType,
    threshold: float | int,
    connectivity: int | None = None,
    cope_file: InputPathType | None = None,
    dlh: float | int | None = None,
    find_min: bool = False,
    fractional: bool = False,
    minclustersize: bool = False,
    no_table: bool = False,
    num_maxima: int | None = None,
    out_index_file: bool = False,
    out_index_file_2: InputPathType | None = None,
    out_localmax_txt_file: bool = False,
    out_localmax_txt_file_2: InputPathType | None = None,
    out_localmax_vol_file: bool = False,
    out_localmax_vol_file_2: InputPathType | None = None,
    out_max_file: bool = False,
    out_max_file_2: InputPathType | None = None,
    out_mean_file: bool = False,
    out_mean_file_2: InputPathType | None = None,
    out_pval_file: bool = False,
    out_pval_file_2: InputPathType | None = None,
    out_size_file: bool = False,
    out_size_file_2: InputPathType | None = None,
    out_threshold_file: bool = False,
    out_threshold_file_2: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    peak_distance: float | int | None = None,
    pthreshold: float | int | None = None,
    std_space_file: InputPathType | None = None,
    use_mm: bool = False,
    volume: int | None = None,
    warpfield_file: InputPathType | None = None,
    xfm_file: InputPathType | None = None,
) -> ClusterOutputs:
    """
    Uses FSL cluster to perform clustering on statistical output
    
    Args:
        runner: Command runner
        in_file: Input volume.
        threshold: Threshold for input volume.
        connectivity: The connectivity of voxels (default 26).
        cope_file: Cope volume.
        dlh: Smoothness estimate = sqrt(det(lambda)).
        find_min: Find minima instead of maxima.
        fractional: Interprets the threshold as a fraction of the robust range.
        minclustersize: Prints out minimum significant cluster size.
        no_table: Suppresses printing of the table info.
        num_maxima: No of local maxima to report.
        out_index_file: A boolean or file. Output of cluster index (in size
            order).
        out_index_file_2: A boolean or file. Output of cluster index (in size
            order).
        out_localmax_txt_file: A boolean or file. Local maxima text file.
        out_localmax_txt_file_2: A boolean or file. Local maxima text file.
        out_localmax_vol_file: A boolean or file. Output of local maxima volume.
        out_localmax_vol_file_2: A boolean or file. Output of local maxima
            volume.
        out_max_file: A boolean or file. Filename for output of max image.
        out_max_file_2: A boolean or file. Filename for output of max image.
        out_mean_file: A boolean or file. Filename for output of mean image.
        out_mean_file_2: A boolean or file. Filename for output of mean image.
        out_pval_file: A boolean or file. Filename for image output of log
            pvals.
        out_pval_file_2: A boolean or file. Filename for image output of log
            pvals.
        out_size_file: A boolean or file. Filename for output of size image.
        out_size_file_2: A boolean or file. Filename for output of size image.
        out_threshold_file: A boolean or file. Thresholded image.
        out_threshold_file_2: A boolean or file. Thresholded image.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.
            Fsl output type.
        peak_distance: Minimum distance between local maxima/minima, in mm
            (default 0).
        pthreshold: P-threshold for clusters.
        std_space_file: Filename for standard-space volume.
        use_mm: Use mm, not voxel, coordinates.
        volume: Number of voxels in the mask.
        warpfield_file: File containing warpfield.
        xfm_file: Filename for linear: input->standard-space transform.
            non-linear: input->highres transform.
    Returns:
        NamedTuple of outputs (described in `ClusterOutputs`).
    """
    if (
        out_index_file +
        (out_index_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_index_file,\n"
            "out_index_file_2"
        )
    if (
        out_localmax_txt_file +
        (out_localmax_txt_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_localmax_txt_file,\n"
            "out_localmax_txt_file_2"
        )
    if (
        out_localmax_vol_file +
        (out_localmax_vol_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_localmax_vol_file,\n"
            "out_localmax_vol_file_2"
        )
    if (
        out_max_file +
        (out_max_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_max_file,\n"
            "out_max_file_2"
        )
    if (
        out_mean_file +
        (out_mean_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_mean_file,\n"
            "out_mean_file_2"
        )
    if (
        out_pval_file +
        (out_pval_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_pval_file,\n"
            "out_pval_file_2"
        )
    if (
        out_size_file +
        (out_size_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_size_file,\n"
            "out_size_file_2"
        )
    if (
        out_threshold_file +
        (out_threshold_file_2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "out_threshold_file,\n"
            "out_threshold_file_2"
        )
    execution = runner.start_execution(CLUSTER_METADATA)
    cargs = []
    cargs.append("Cluster")
    if connectivity is not None:
        cargs.append(("--connectivity=" + str(connectivity)))
    if cope_file is not None:
        cargs.append(("--cope=" + execution.input_file(cope_file)))
    if dlh is not None:
        cargs.append(("--dlh=" + str(dlh)))
    if find_min:
        cargs.append("--min")
    if fractional:
        cargs.append("--fractional")
    cargs.append(("--in=" + execution.input_file(in_file)))
    if minclustersize:
        cargs.append("--minclustersize")
    if no_table:
        cargs.append("--no_table")
    if num_maxima is not None:
        cargs.append(("--num=" + str(num_maxima)))
    if out_index_file_2 is not None:
        cargs.append(("--oindex=" + execution.input_file(out_index_file_2)))
    if out_localmax_txt_file_2 is not None:
        cargs.append(("--olmax=" + execution.input_file(out_localmax_txt_file_2)))
    if out_localmax_vol_file_2 is not None:
        cargs.append(("--olmaxim=" + execution.input_file(out_localmax_vol_file_2)))
    if out_max_file_2 is not None:
        cargs.append(("--omax=" + execution.input_file(out_max_file_2)))
    if out_mean_file_2 is not None:
        cargs.append(("--omean=" + execution.input_file(out_mean_file_2)))
    if out_pval_file_2 is not None:
        cargs.append(("--opvals=" + execution.input_file(out_pval_file_2)))
    if out_size_file_2 is not None:
        cargs.append(("--osize=" + execution.input_file(out_size_file_2)))
    if out_threshold_file_2 is not None:
        cargs.append(("--othresh=" + execution.input_file(out_threshold_file_2)))
    if output_type is not None:
        cargs.append(output_type)
    if peak_distance is not None:
        cargs.append(("--peakdist=" + str(peak_distance)))
    if pthreshold is not None:
        cargs.append(("--pthresh=" + str(pthreshold)))
    if std_space_file is not None:
        cargs.append(("--stdvol=" + execution.input_file(std_space_file)))
    cargs.append(("--thresh=" + str(threshold)))
    if use_mm:
        cargs.append("--mm")
    if volume is not None:
        cargs.append(("--volume=" + str(volume)))
    if warpfield_file is not None:
        cargs.append(("--warpvol=" + execution.input_file(warpfield_file)))
    if xfm_file is not None:
        cargs.append(("--xfm=" + execution.input_file(xfm_file)))
    ret = ClusterOutputs(
        root=execution.output_file("."),
        index_file=execution.output_file(f"index_file", optional=True),
        localmax_txt_file=execution.output_file(f"localmax_txt_file", optional=True),
        localmax_vol_file=execution.output_file(f"localmax_vol_file", optional=True),
        max_file=execution.output_file(f"max_file", optional=True),
        mean_file=execution.output_file(f"mean_file", optional=True),
        pval_file=execution.output_file(f"pval_file", optional=True),
        size_file=execution.output_file(f"size_file", optional=True),
        threshold_file=execution.output_file(f"threshold_file", optional=True),
    )
    execution.run(cargs)
    return ret
