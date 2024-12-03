# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

LONG_SUBMIT_JOBS_METADATA = Metadata(
    id="d9fdcdcc044b4b6a583cb8d7681940ebbb389e10.boutiques",
    name="long_submit_jobs",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class LongSubmitJobsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `long_submit_jobs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def long_submit_jobs(
    qdec: InputPathType,
    cdir: str,
    bdir: str | None = None,
    ldir: str | None = None,
    scriptsdir: str | None = None,
    cross: bool = False,
    base: bool = False,
    long: bool = False,
    cflags: str | None = None,
    bflags: str | None = None,
    lflags: str | None = None,
    affine: bool = False,
    force: bool = False,
    simulate: bool = False,
    simfiles: bool = False,
    check: bool = False,
    pause: float | None = None,
    max_: float | None = None,
    queue_: str | None = None,
    cmem: float | None = None,
    bmem: float | None = None,
    lmem: float | None = None,
    cnodes: float | None = None,
    bnodes: float | None = None,
    lnodes: float | None = None,
    runner: Runner | None = None,
) -> LongSubmitJobsOutputs:
    """
    Submits longitudinal processing jobs to the NMR cluster (seychelles or
    launchpad).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        qdec: QDEC table file specifying the subjects and time points.
        cdir: Directory for cross-sectional subjects (inherited by base and\
            long).
        bdir: Directory for base runs (default: inherit from cross).
        ldir: Directory for longitudinal runs (default: inherit from base).
        scriptsdir: Location to save submitted scripts (default:\
            <cdir,bdir,ldir>/scripts_submitted).
        cross: Process cross-sectional streams.
        base: Process base streams.
        long: Process longitudinal streams.
        cflags: Manual flags for cross processing (e.g., '-all -cw256').
        bflags: Manual flags for base processing (default: '-all').
        lflags: Manual flags for long processing (default: '-all').
        affine: Use affine registration for base.
        force: Force reprocessing of jobs even if marked as done.
        simulate: Simulate submission only, without executing.
        simfiles: Simulate command file creation only, without executing.
        check: Check if all longitudinal processing is complete.
        pause: Pause duration (in seconds) between submissions (default: 13).
        max_: Maximum number of jobs per user (default: 100).
        queue_: Queue to submit jobs.
        cmem: RAM (in GB) requested for cross (default: 7).
        bmem: RAM (in GB) requested for base (default: 7).
        lmem: RAM (in GB) requested for long (default: 7).
        cnodes: Number of nodes for cross runs (default: 1).
        bnodes: Number of nodes for base runs (default: 1).
        lnodes: Number of nodes for long runs (default: 1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `LongSubmitJobsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LONG_SUBMIT_JOBS_METADATA)
    cargs = []
    cargs.append("long_submit_jobs")
    cargs.extend([
        "--qdec",
        execution.input_file(qdec)
    ])
    cargs.extend([
        "--cdir",
        cdir
    ])
    if bdir is not None:
        cargs.extend([
            "--bdir",
            bdir
        ])
    if ldir is not None:
        cargs.extend([
            "--ldir",
            ldir
        ])
    if scriptsdir is not None:
        cargs.extend([
            "--scriptsdir",
            scriptsdir
        ])
    if cross:
        cargs.append("--cross")
    if base:
        cargs.append("--base")
    if long:
        cargs.append("--long")
    if cflags is not None:
        cargs.extend([
            "--cflags",
            cflags
        ])
    if bflags is not None:
        cargs.extend([
            "--bflags",
            bflags
        ])
    if lflags is not None:
        cargs.extend([
            "--lflags",
            lflags
        ])
    if affine:
        cargs.append("--affine")
    if force:
        cargs.append("--force")
    if simulate:
        cargs.append("--simulate")
    if simfiles:
        cargs.append("--simfiles")
    cargs.append("[--skip]")
    cargs.append("[--skiperror]")
    if check:
        cargs.append("--check")
    cargs.append("[--update-recon-all]")
    cargs.append("[--use-recon-all]")
    if pause is not None:
        cargs.extend([
            "--pause",
            str(pause)
        ])
    if max_ is not None:
        cargs.extend([
            "--max",
            str(max_)
        ])
    if queue_ is not None:
        cargs.extend([
            "--queue",
            queue_
        ])
    if cmem is not None:
        cargs.extend([
            "--cmem",
            str(cmem)
        ])
    if bmem is not None:
        cargs.extend([
            "--bmem",
            str(bmem)
        ])
    if lmem is not None:
        cargs.extend([
            "--lmem",
            str(lmem)
        ])
    if cnodes is not None:
        cargs.extend([
            "--cnodes",
            str(cnodes)
        ])
    if bnodes is not None:
        cargs.extend([
            "--bnodes",
            str(bnodes)
        ])
    if lnodes is not None:
        cargs.extend([
            "--lnodes",
            str(lnodes)
        ])
    ret = LongSubmitJobsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LONG_SUBMIT_JOBS_METADATA",
    "LongSubmitJobsOutputs",
    "long_submit_jobs",
]