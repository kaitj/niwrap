# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


DWIDENOISE_METADATA = Metadata(
    id="90468f4b55fd2315ebf673258aa3f5c3e3153ed2",
    name="dwidenoise",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class DwidenoiseConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.extend(["", self.key])
        cargs.extend(["", self.value])
        return cargs


class DwidenoiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dwidenoise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output denoised DWI image."""
    noise: OutputPathType | None
    """The output noise map, i.e., the estimated noise level 'sigma' in the data. Note that on complex input data, this will be the total noise level across real and imaginary channels, so a scale factor sqrt(2) applies. """


def dwidenoise(
    dwi: InputPathType,
    out: InputPathType,
    mask: InputPathType | None = None,
    extent: list[int] = None,
    noise: InputPathType | None = None,
    datatype: typing.Literal["float32", "float64"] | None = None,
    estimator: typing.Literal["Exp1", "Exp2"] | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[DwidenoiseConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> DwidenoiseOutputs:
    """
    dwidenoise by Daan Christiaens (daan.christiaens@kcl.ac.uk) & Jelle Veraart
    (jelle.veraart@nyumc.org) & J-Donald Tournier (jdtournier@gmail.com).
    
    dMRI noise level estimation and denoising using Marchenko-Pastur PCA.
    
    DWI data denoising and noise map estimation by exploiting data redundancy in
    the PCA domain using the prior knowledge that the eigenspectrum of random
    covariance matrices is described by the universal Marchenko-Pastur (MP)
    distribution. Fitting the MP distribution to the spectrum of patch-wise
    signal matrices hence provides an estimator of the noise level 'sigma', as
    was first shown in Veraart et al. (2016) and later improved in
    Cordero-Grande et al. (2019). This noise level estimate then determines the
    optimal cut-off for PCA denoising.
    
    Important note: image denoising must be performed as the first step of the
    image processing pipeline. The routine will fail if interpolation or
    smoothing has been applied to the data prior to denoising.
    
    Note that this function does not correct for non-Gaussian noise biases
    present in magnitude-reconstructed MRI images. If available, including the
    MRI phase data can reduce such non-Gaussian biases, and the command now
    supports complex input data.
    
    References:
    
    Veraart, J.; Novikov, D.S.; Christiaens, D.; Ades-aron, B.; Sijbers, J. &
    Fieremans, E. Denoising of diffusion MRI using random matrix theory.
    NeuroImage, 2016, 142, 394-406, doi: 10.1016/j.neuroimage.2016.08.016
    
    Veraart, J.; Fieremans, E. & Novikov, D.S. Diffusion MRI noise mapping using
    random matrix theory. Magn. Res. Med., 2016, 76(5), 1582-1593, doi:
    10.1002/mrm.26059
    
    Cordero-Grande, L.; Christiaens, D.; Hutter, J.; Price, A.N.; Hajnal, J.V.
    Complex diffusion-weighted image estimation via matrix recovery under
    general noise models. NeuroImage, 2019, 200, 391-404, doi:
    10.1016/j.neuroimage.2019.06.039.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/dwidenoise.html
    
    Args:
        dwi: the input diffusion-weighted image.
        out: the output denoised DWI image.
        mask: Only process voxels within the specified binary brain mask image.
        extent: Set the patch size of the denoising filter. By default, the
            command will select the smallest isotropic patch size that exceeds the
            number of DW images in the input data, e.g., 5x5x5 for data with <= 125
            DWI volumes, 7x7x7 for data with <= 343 DWI volumes, etc.
        noise: The output noise map, i.e., the estimated noise level 'sigma' in
            the data. Note that on complex input data, this will be the total noise
            level across real and imaginary channels, so a scale factor sqrt(2)
            applies.
        datatype: Datatype for the eigenvalue decomposition (single or double
            precision). For complex input data, this will select complex float32 or
            complex float64 datatypes.
        estimator: Select the noise level estimator (default = Exp2), either:
            * Exp1: the original estimator used in Veraart et al.
            (2016), or
            * Exp2: the improved estimator introduced in
            Cordero-Grande et al. (2019).
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `DwidenoiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DWIDENOISE_METADATA)
    cargs = []
    cargs.append("dwidenoise")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if extent is not None:
        cargs.extend(["-extent", *map(str, extent)])
    if noise is not None:
        cargs.extend(["-noise", execution.input_file(noise)])
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
    if estimator is not None:
        cargs.extend(["-estimator", estimator])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(dwi))
    cargs.append(execution.input_file(out))
    ret = DwidenoiseOutputs(
        root=execution.output_file("."),
        out=execution.output_file(f"{pathlib.Path(out).stem}"),
        noise=execution.output_file(f"{pathlib.Path(noise).stem}") if noise is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DWIDENOISE_METADATA",
    "DwidenoiseConfig",
    "DwidenoiseOutputs",
    "dwidenoise",
]