# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

OXFORD_ASL_METADATA = Metadata(
    id="15f5db12a26405139618faef826afabb82fef564",
    name="oxford_asl",
)


class OxfordAslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `oxford_asl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir: OutputPathType
    """Directory containing the output files"""


def oxford_asl(
    asl_data: InputPathType,
    output_dir_name: str,
    mask: InputPathType | None = None,
    spatial_smoothing: bool = False,
    white_paper_analysis: bool = False,
    motion_correction: bool = False,
    input_asl_format: str | None = None,
    input_block_format: str | None = None,
    inversion_times: str | None = None,
    ti_image: InputPathType | None = None,
    casl: bool = False,
    arterial_suppression: bool = False,
    bolus_duration: float | int | None = None,
    bat: float | int | None = None,
    tissue_t1: float | int | None = None,
    blood_t1: float | int | None = None,
    slice_timing_difference: float | int | None = None,
    slice_band: float | int | None = None,
    flip_angle: float | int | None = None,
    fsl_anat_dir: str | None = None,
    structural_image: InputPathType | None = None,
    bet_structural_image: InputPathType | None = None,
    fast_segmentation_images: str | None = None,
    sensitivity_correction: bool = False,
    precomputed_m0_value: float | int | None = None,
    inversion_efficiency: float | int | None = None,
    calibration_image: InputPathType | None = None,
    tr_calibration_data: float | int | None = None,
    calibration_method: str | None = None,
    runner: Runner = None,
) -> OxfordAslOutputs:
    """
    oxford_asl by FMRIB Centre, University of Oxford.
    
    Calculate perfusion maps from ASL data.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/oxford_asl
    
    Args:
        asl_data: Input ASL data
        output_dir_name: Output directory name
        mask: Mask in native space of ASL data
        spatial_smoothing: Use adaptive spatial smoothing on perfusion
        white_paper_analysis: Analysis that conforms to the 'white paper' (Alsop
            et al. 2014)
        motion_correction: Apply motion correction using mcflirt
        input_asl_format: Input ASL format: diff, tc, ct
        input_block_format: Input block format (for multi-TI): rpt, tis
        inversion_times: Comma separated list of inversion times
        ti_image: 4D image containing voxelwise TI values
        casl: ASL acquisition is pseudo cASL (pcASL) rather than pASL
        arterial_suppression: Arterial suppression (vascular crushing) was used
        bolus_duration: Bolus duration
        bat: Bolus arrival time
        tissue_t1: Tissue T1 value
        blood_t1: Blood T1 value
        slice_timing_difference: Timing difference between slices
        slice_band: Number of slices per band in a multi-band setup
        flip_angle: Flip angle for Look-Locker readout correction
        fsl_anat_dir: An fsl_anat directory from structural image
        structural_image: Structural image (whole head)
        bet_structural_image: Structural image (already BETed)
        fast_segmentation_images: Images from a FAST segmentation
        sensitivity_correction: Use bias field (from segmentation) for
            sensitivity correction
        precomputed_m0_value: Single precomputed M0 value
        inversion_efficiency: Inversion efficiency
        calibration_image: M0 calibration image (proton density or mean control
            image)
        tr_calibration_data: TR of calibration data
        calibration_method: Calibration method: single or voxel
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `OxfordAslOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(OXFORD_ASL_METADATA)
    cargs = []
    cargs.append("oxford_asl")
    cargs.append("-i")
    cargs.append(execution.input_file(asl_data))
    cargs.append("-o")
    cargs.append(output_dir_name)
    cargs.append("[options]")
    ret = OxfordAslOutputs(
        root=execution.output_file("."),
        output_dir=execution.output_file(f"{output_dir_name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "OXFORD_ASL_METADATA",
    "OxfordAslOutputs",
    "oxford_asl",
]