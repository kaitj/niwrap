# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_DWITO_DT_METADATA = Metadata(
    id="28357e5c4de61ec6831cc8a882edb42b7e95b2c7",
    name="3dDWItoDT",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dDwitoDtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dwito_dt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dataset: OutputPathType
    """Output dataset"""


def v_3d_dwito_dt(
    gradient_file: InputPathType,
    dataset: InputPathType,
    prefix: str | None = None,
    automask: bool = False,
    mask: InputPathType | None = None,
    bmatrix_nz: InputPathType | None = None,
    bmatrix_z: InputPathType | None = None,
    bmatrix_full: InputPathType | None = None,
    scale_out_1000: bool = False,
    bmax_ref: float | int | None = None,
    nonlinear: bool = False,
    linear: bool = False,
    reweight: bool = False,
    max_iter: int | None = None,
    max_iter_rw: int | None = None,
    eigs: bool = False,
    debug_briks: bool = False,
    cumulative_wts: bool = False,
    verbose: int | None = None,
    drive_afni: int | None = None,
    sep_dsets: bool = False,
    csf_val: float | int | None = None,
    min_bad_md: int | None = None,
    csf_fa: float | int | None = None,
    opt: str | None = None,
    mean_b0: bool = False,
    runner: Runner | None = None,
) -> V3dDwitoDtOutputs:
    """
    3dDWItoDT by AFNI Team.
    
    Computes 6 principal direction tensors from multiple gradient vectors and
    corresponding DTI image volumes.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dDWItoDT.html
    
    Args:
        gradient_file: A 1D file of the gradient vectors with lines of ASCII\
            floats (Gxi, Gyi, Gzi) or a 1D file of b-matrix elements.
        dataset: A 3D bucket dataset with Np+1 sub-briks where the first\
            sub-brik is the volume acquired with no diffusion weighting.
        prefix: Output dataset prefix name. Default is 'DT'.
        automask: Mask dataset so that tensors are computed only for\
            high-intensity (presumably brain) voxels.
        mask: Use this dataset as mask to include/exclude voxels.
        bmatrix_nz: Input dataset is b-matrix, not gradient directions, and\
            there is no row of zeros at the top of the file.
        bmatrix_z: Similar to '-bmatrix_NZ' but first row of the file is all\
            zeros.
        bmatrix_full: Same as '-bmatrix_Z' but with a more intuitive name.
        scale_out_1000: Increase output parameters with physical units by\
            multiplying them by 1000.
        bmax_ref: Flag the reference b-value if it is greater than zero.
        nonlinear: Compute iterative solution to avoid negative eigenvalues.\
            This is the default method.
        linear: Compute simple linear solution.
        reweight: Recompute weight factors at end of iterations and restart.
        max_iter: Maximum number of iterations for convergence. Default is 10.
        max_iter_rw: Max number of iterations after reweighting. Default is 5.
        eigs: Compute eigenvalues, eigenvectors, fractional anisotropy, and\
            mean diffusivity in sub-briks 6-19.
        debug_briks: Add sub-briks with error functional, original error,\
            number of steps to convergence, and modeled B0 volume.
        cumulative_wts: Show overall weight factors for each gradient level.
        verbose: Print convergence steps every nnnnn voxels.
        drive_afni: Show convergence graphs every nnnnn voxels. AFNI must have\
            NIML communications on.
        sep_dsets: Save tensor, eigenvalues, vectors, FA, MD in separate\
            datasets.
        csf_val: Assign diffusivity value to DWI data where the mean values for\
            b=0 volumes is less than the mean of the remaining volumes at each\
            voxel.
        min_bad_md: Change the min MD value used as a 'badness check' for\
            tensor fits.
        csf_fa: Assign a specific FA value to CSF voxels.
        opt: Optimization method: 'powell', 'gradient', or 'hybrid'.
        mean_b0: Use mean of all b=0 volumes for linear computation and initial\
            linear for nonlinear method.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDwitoDtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DWITO_DT_METADATA)
    cargs = []
    cargs.append("3dDWItoDT")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(gradient_file))
    cargs.append(execution.input_file(dataset))
    ret = V3dDwitoDtOutputs(
        root=execution.output_file("."),
        output_dataset=execution.output_file(f"<PREFIX>.*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDwitoDtOutputs",
    "V_3D_DWITO_DT_METADATA",
    "v_3d_dwito_dt",
]