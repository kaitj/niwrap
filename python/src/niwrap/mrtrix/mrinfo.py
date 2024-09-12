# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRINFO_METADATA = Metadata(
    id="1a85852eaad4b28e7ec279a82e8e478eaa7037b1.boutiques",
    name="mrinfo",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MrinfoProperty:
    """
    any text properties embedded in the image header under the specified key
    (use 'all' to list all keys found).
    """
    key: str
    """any text properties embedded in the image header under the specified key
    (use 'all' to list all keys found)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-property")
        cargs.append(self.key)
        return cargs


@dataclasses.dataclass
class MrinfoFslgrad:
    """
    Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used.
    """
    bvecs: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    bvals: InputPathType
    """Provide the diffusion-weighted gradient scheme used in the acquisition in
    FSL bvecs/bvals format files. If a diffusion gradient scheme is present in
    the input image header, the data provided with this option will be instead
    used."""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-fslgrad")
        cargs.append(execution.input_file(self.bvecs))
        cargs.append(execution.input_file(self.bvals))
        return cargs


class MrinfoExportGradFslOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MrinfoExportGradFsl | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    bvecs_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: OutputPathType
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""


@dataclasses.dataclass
class MrinfoExportGradFsl:
    """
    export the diffusion-weighted gradient table to files in FSL (bvecs / bvals)
    format.
    """
    bvecs_path: str
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    bvals_path: str
    """export the diffusion-weighted gradient table to files in FSL (bvecs /
    bvals) format"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-export_grad_fsl")
        cargs.append(self.bvecs_path)
        cargs.append(self.bvals_path)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MrinfoExportGradFslOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MrinfoExportGradFslOutputs`).
        """
        ret = MrinfoExportGradFslOutputs(
            root=execution.output_file("."),
            bvecs_path=execution.output_file(self.bvecs_path),
            bvals_path=execution.output_file(self.bvals_path),
        )
        return ret


class MrinfoExportPeEddyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `MrinfoExportPeEddy | None(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    config: OutputPathType
    """export phase-encoding information to an EDDY-style config / index file
    pair"""
    indices: OutputPathType
    """export phase-encoding information to an EDDY-style config / index file
    pair"""


@dataclasses.dataclass
class MrinfoExportPeEddy:
    """
    export phase-encoding information to an EDDY-style config / index file pair.
    """
    config: str
    """export phase-encoding information to an EDDY-style config / index file
    pair"""
    indices: str
    """export phase-encoding information to an EDDY-style config / index file
    pair"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-export_pe_eddy")
        cargs.append(self.config)
        cargs.append(self.indices)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> MrinfoExportPeEddyOutputs:
        """
        Collect output file paths.
        
        Args:
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `MrinfoExportPeEddyOutputs`).
        """
        ret = MrinfoExportPeEddyOutputs(
            root=execution.output_file("."),
            config=execution.output_file(self.config),
            indices=execution.output_file(self.indices),
        )
        return ret


@dataclasses.dataclass
class MrinfoConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class MrinfoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mrinfo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    json_keyval: OutputPathType | None
    """export header key/value entries to a JSON file """
    json_all: OutputPathType | None
    """export all header contents to a JSON file """
    export_grad_mrtrix: OutputPathType | None
    """export the diffusion-weighted gradient table to file in MRtrix format """
    export_pe_table: OutputPathType | None
    """export phase-encoding table to file """
    export_grad_fsl: MrinfoExportGradFslOutputs | None
    """Outputs from `MrinfoExportGradFsl`."""
    export_pe_eddy: MrinfoExportPeEddyOutputs | None
    """Outputs from `MrinfoExportPeEddy`."""


def mrinfo(
    image: list[InputPathType],
    all_: bool = False,
    name: bool = False,
    format_: bool = False,
    ndim: bool = False,
    size: bool = False,
    spacing: bool = False,
    datatype: bool = False,
    strides: bool = False,
    offset: bool = False,
    multiplier: bool = False,
    transform: bool = False,
    property_: list[MrinfoProperty] | None = None,
    json_keyval: str | None = None,
    json_all: str | None = None,
    grad: InputPathType | None = None,
    fslgrad: MrinfoFslgrad | None = None,
    bvalue_scaling: str | None = None,
    export_grad_mrtrix: str | None = None,
    export_grad_fsl: MrinfoExportGradFsl | None = None,
    dwgrad: bool = False,
    shell_bvalues: bool = False,
    shell_sizes: bool = False,
    shell_indices: bool = False,
    export_pe_table: str | None = None,
    export_pe_eddy: MrinfoExportPeEddy | None = None,
    petable: bool = False,
    nodelete: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MrinfoConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrinfoOutputs:
    """
    Display image header information, or extract specific information from the
    header.
    
    By default, all information contained in each image header will be printed
    to the console in a reader-friendly format.
    
    Alternatively, command-line options may be used to extract specific details
    from the header(s); these are printed to the console in a format more
    appropriate for scripting purposes or piping to file. If multiple options
    and/or images are provided, the requested header fields will be printed in
    the order in which they appear in the help page, with all requested details
    from each input image in sequence printed before the next image is
    processed.
    
    The command can also write the diffusion gradient table from a single input
    image to file; either in the MRtrix or FSL format (bvecs/bvals file pair;
    includes appropriate diffusion gradient vector reorientation)
    
    The -dwgrad, -export_* and -shell_* options provide (information about) the
    diffusion weighting gradient table after it has been processed by the
    MRtrix3 back-end (vectors normalised, b-values scaled by the square of the
    vector norm, depending on the -bvalue_scaling option). To see the raw
    gradient table information as stored in the image header, i.e. without
    MRtrix3 back-end processing, use "-property dw_scheme".
    
    The -bvalue_scaling option controls an aspect of the import of diffusion
    gradient tables. When the input diffusion-weighting direction vectors have
    norms that differ substantially from unity, the b-values will be scaled by
    the square of their corresponding vector norm (this is how multi-shell
    acquisitions are frequently achieved on scanner platforms). However in some
    rare instances, the b-values may be correct, despite the vectors not being
    of unit norm (or conversely, the b-values may need to be rescaled even
    though the vectors are close to unit norm). This option allows the user to
    control this operation and override MRrtix3's automatic detection.
    
    References:
    
    .
    
    Author: J-Donald Tournier (jdtournier@gmail.com) and Robert E. Smith
    (robert.smith@florey.edu.au)
    
    URL: https://mrtrix.readthedocs.io/en/latest/reference/commands/mrinfo.html
    
    Args:
        image: the input image(s).
        all_: print all properties, rather than the first and last 2 of each.
        name: print the file system path of the image.
        format_: image file format.
        ndim: number of image dimensions.
        size: image size along each axis.
        spacing: voxel spacing along each image dimension.
        datatype: data type used for image data storage.
        strides: data strides i.e. order and direction of axes data layout.
        offset: image intensity offset.
        multiplier: image intensity multiplier.
        transform: the transformation from image coordinates [mm] to scanner /\
            real world coordinates [mm].
        property_: any text properties embedded in the image header under the\
            specified key (use 'all' to list all keys found).
        json_keyval: export header key/value entries to a JSON file.
        json_all: export all header contents to a JSON file.
        grad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in a text file. This should be supplied as a 4xN text file\
            with each line is in the format [ X Y Z b ], where [ X Y Z ] describe\
            the direction of the applied gradient, and b gives the b-value in units\
            of s/mm^2. If a diffusion gradient scheme is present in the input image\
            header, the data provided with this option will be instead used.
        fslgrad: Provide the diffusion-weighted gradient scheme used in the\
            acquisition in FSL bvecs/bvals format files. If a diffusion gradient\
            scheme is present in the input image header, the data provided with\
            this option will be instead used.
        bvalue_scaling: enable or disable scaling of diffusion b-values by the\
            square of the corresponding DW gradient norm (see Desciption). Valid\
            choices are yes/no, true/false, 0/1 (default: automatic).
        export_grad_mrtrix: export the diffusion-weighted gradient table to\
            file in MRtrix format.
        export_grad_fsl: export the diffusion-weighted gradient table to files\
            in FSL (bvecs / bvals) format.
        dwgrad: the diffusion-weighting gradient table, as interpreted by\
            MRtrix3.
        shell_bvalues: list the average b-value of each shell.
        shell_sizes: list the number of volumes in each shell.
        shell_indices: list the image volumes attributed to each b-value shell.
        export_pe_table: export phase-encoding table to file.
        export_pe_eddy: export phase-encoding information to an EDDY-style\
            config / index file pair.
        petable: print the phase encoding table.
        nodelete: don't delete temporary images or images passed to mrinfo via\
            Unix pipes.
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
        NamedTuple of outputs (described in `MrinfoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRINFO_METADATA)
    cargs = []
    cargs.append("mrinfo")
    if all_:
        cargs.append("-all")
    if name:
        cargs.append("-name")
    if format_:
        cargs.append("-format")
    if ndim:
        cargs.append("-ndim")
    if size:
        cargs.append("-size")
    if spacing:
        cargs.append("-spacing")
    if datatype:
        cargs.append("-datatype")
    if strides:
        cargs.append("-strides")
    if offset:
        cargs.append("-offset")
    if multiplier:
        cargs.append("-multiplier")
    if transform:
        cargs.append("-transform")
    if property_ is not None:
        cargs.extend([a for c in [s.run(execution) for s in property_] for a in c])
    if json_keyval is not None:
        cargs.extend([
            "-json_keyval",
            json_keyval
        ])
    if json_all is not None:
        cargs.extend([
            "-json_all",
            json_all
        ])
    if grad is not None:
        cargs.extend([
            "-grad",
            execution.input_file(grad)
        ])
    if fslgrad is not None:
        cargs.extend(fslgrad.run(execution))
    if bvalue_scaling is not None:
        cargs.extend([
            "-bvalue_scaling",
            bvalue_scaling
        ])
    if export_grad_mrtrix is not None:
        cargs.extend([
            "-export_grad_mrtrix",
            export_grad_mrtrix
        ])
    if export_grad_fsl is not None:
        cargs.extend(export_grad_fsl.run(execution))
    if dwgrad:
        cargs.append("-dwgrad")
    if shell_bvalues:
        cargs.append("-shell_bvalues")
    if shell_sizes:
        cargs.append("-shell_sizes")
    if shell_indices:
        cargs.append("-shell_indices")
    if export_pe_table is not None:
        cargs.extend([
            "-export_pe_table",
            export_pe_table
        ])
    if export_pe_eddy is not None:
        cargs.extend(export_pe_eddy.run(execution))
    if petable:
        cargs.append("-petable")
    if nodelete:
        cargs.append("-nodelete")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend([execution.input_file(f) for f in image])
    ret = MrinfoOutputs(
        root=execution.output_file("."),
        json_keyval=execution.output_file(json_keyval) if (json_keyval is not None) else None,
        json_all=execution.output_file(json_all) if (json_all is not None) else None,
        export_grad_mrtrix=execution.output_file(export_grad_mrtrix) if (export_grad_mrtrix is not None) else None,
        export_pe_table=execution.output_file(export_pe_table) if (export_pe_table is not None) else None,
        export_grad_fsl=export_grad_fsl.outputs(execution) if export_grad_fsl else None,
        export_pe_eddy=export_pe_eddy.outputs(execution) if export_pe_eddy else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRINFO_METADATA",
    "MrinfoConfig",
    "MrinfoExportGradFsl",
    "MrinfoExportGradFslOutputs",
    "MrinfoExportPeEddy",
    "MrinfoExportPeEddyOutputs",
    "MrinfoFslgrad",
    "MrinfoOutputs",
    "MrinfoProperty",
    "mrinfo",
]
