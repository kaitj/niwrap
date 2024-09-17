# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_MAT_SEL_PY_METADATA = Metadata(
    id="7d57915d94e233ae332e06d9062f43d9600ec66d.boutiques",
    name="fat_mat_sel.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatMatSelPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat_sel_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    individual_images: OutputPathType
    """Individual images of matrix plots."""
    matrix_grids: OutputPathType
    """Output matrix grid files."""
    v_1_d_dsets: OutputPathType
    """Output 1D dataset files."""


def fat_mat_sel_py(
    runner: Runner | None = None,
) -> FatMatSelPyOutputs:
    """
    Perform simple matrix plotting operations from outputs of FATCAT programs
    3dNetCorr and 3dTrackID.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/fat_mat_sel.py.html
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMatSelPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MAT_SEL_PY_METADATA)
    cargs = []
    cargs.append("fat_mat_sel.py")
    cargs.append("[--Pars=Pars]")
    cargs.append("[--matr_in=MATR_FILES]")
    cargs.append("[--list_match=LIST]")
    cargs.append("[--out_ind_matr]")
    cargs.append("[--Out_ind_1ddset]")
    cargs.append("[--Hold_image]")
    cargs.append("[--ExternLabsNo]")
    cargs.append("[--type_file=TYPE]")
    cargs.append("[--dpi_file=DPI]")
    cargs.append("[--xlen_file=LX]")
    cargs.append("[--ylen_file=LY]")
    cargs.append("[--Tight_layout_on]")
    cargs.append("[--Fig_off]")
    cargs.append("[--Size_font=S]")
    cargs.append("[--Lab_size_font=S]")
    cargs.append("[--A_plotmin=MIN]")
    cargs.append("[--B_plotmax=MAX]")
    cargs.append("[--Cbar_off]")
    cargs.append("[--Map_of_colors=MAP]")
    cargs.append("[--cbar_int_num=N]")
    cargs.append("[--width_cbar_perc=W]")
    cargs.append("[--specifier=STR]")
    cargs.append("[--Xtick_lab_off]")
    ret = FatMatSelPyOutputs(
        root=execution.output_file("."),
        individual_images=execution.output_file("individual_images/*"),
        matrix_grids=execution.output_file("matrix_grids/*"),
        v_1_d_dsets=execution.output_file("1D_dsets/*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_MAT_SEL_PY_METADATA",
    "FatMatSelPyOutputs",
    "fat_mat_sel_py",
]