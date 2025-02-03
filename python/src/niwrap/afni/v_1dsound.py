# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1DSOUND_METADATA = Metadata(
    id="27afe9539a9fa717bc8a3162d9645362879cc57c.boutiques",
    name="1dsound",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)
V1dsoundParameters = typing.TypedDict('V1dsoundParameters', {
    "__STYX_TYPE__": typing.Literal["1dsound"],
    "tsfile": InputPathType,
    "prefix": typing.NotRequired[str | None],
    "encoding_16PCM": bool,
    "encoding_8PCM": bool,
    "encoding_8ulaw": bool,
    "tper_option": typing.NotRequired[float | None],
    "fm_option": bool,
    "notes_option": bool,
    "notewave_option": typing.NotRequired[str | None],
    "despike_option": bool,
    "play_option": bool,
})


def dyn_cargs(
    t: str,
) -> None:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    vt = {
        "1dsound": v_1dsound_cargs,
    }
    return vt.get(t)


def dyn_outputs(
    t: str,
) -> None:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    vt = {
        "1dsound": v_1dsound_outputs,
    }
    return vt.get(t)


class V1dsoundOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1dsound(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType | None
    """The output audio file."""


def v_1dsound_params(
    tsfile: InputPathType,
    prefix: str | None = None,
    encoding_16_pcm: bool = False,
    encoding_8_pcm: bool = False,
    encoding_8ulaw: bool = False,
    tper_option: float | None = None,
    fm_option: bool = False,
    notes_option: bool = False,
    notewave_option: str | None = None,
    despike_option: bool = False,
    play_option: bool = False,
) -> V1dsoundParameters:
    """
    Build parameters.
    
    Args:
        tsfile: The input 1D time series file containing the data to transform\
            into sound.
        prefix: Prefix for the output filename, which will have '.au'\
            extension.
        encoding_16_pcm: Output in 16-bit linear PCM encoding (uncompressed).
        encoding_8_pcm: Output in 8-bit linear PCM encoding.
        encoding_8ulaw: Output in 8-bit mu-law encoding.
        tper_option: Time in seconds per time point in 'tsfile'. Allowed range\
            is 0.01 to 1.0 (inclusive). [default is 0.2s].
        fm_option: Output sound is frequency modulated between 110 and 1760 Hz\
            from min to max in the input 1D file.
        notes_option: Output sound is a sequence of notes, low to high pitch\
            based on min to max in the input 1D file. Uses pentatonic scale.
        notewave_option: Shape of the notes used. Select from [sine, sqsine,\
            square, triangle].
        despike_option: Apply a simple despiking algorithm to avoid artifacts\
            from large/small values in the input.
        play_option: Plays the sound file after it is written.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "1dsound",
        "tsfile": tsfile,
        "encoding_16PCM": encoding_16_pcm,
        "encoding_8PCM": encoding_8_pcm,
        "encoding_8ulaw": encoding_8ulaw,
        "fm_option": fm_option,
        "notes_option": notes_option,
        "despike_option": despike_option,
        "play_option": play_option,
    }
    if prefix is not None:
        params["prefix"] = prefix
    if tper_option is not None:
        params["tper_option"] = tper_option
    if notewave_option is not None:
        params["notewave_option"] = notewave_option
    return params


def v_1dsound_cargs(
    params: V1dsoundParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("1dsound")
    cargs.append(execution.input_file(params.get("tsfile")))
    if params.get("prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("prefix")
        ])
    if params.get("encoding_16PCM"):
        cargs.append("-16PCM")
    if params.get("encoding_8PCM"):
        cargs.append("-8PCM")
    if params.get("encoding_8ulaw"):
        cargs.append("-8ulaw")
    if params.get("tper_option") is not None:
        cargs.extend([
            "-tper",
            str(params.get("tper_option"))
        ])
    if params.get("fm_option"):
        cargs.append("-FM")
    if params.get("notes_option"):
        cargs.append("-notes")
    if params.get("notewave_option") is not None:
        cargs.extend([
            "-notewave",
            params.get("notewave_option")
        ])
    if params.get("despike_option"):
        cargs.append("-despike")
    if params.get("play_option"):
        cargs.append("-play")
    return cargs


def v_1dsound_outputs(
    params: V1dsoundParameters,
    execution: Execution,
) -> V1dsoundOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = V1dsoundOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("prefix") + ".au") if (params.get("prefix") is not None) else None,
    )
    return ret


def v_1dsound_execute(
    params: V1dsoundParameters,
    execution: Execution,
) -> V1dsoundOutputs:
    """
    Program to create a sound file from a 1D file (column of numbers).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `V1dsoundOutputs`).
    """
    # validate constraint checks (or after middlewares?)
    cargs = v_1dsound_cargs(params, execution)
    ret = v_1dsound_outputs(params, execution)
    execution.run(cargs)
    return ret


def v_1dsound(
    tsfile: InputPathType,
    prefix: str | None = None,
    encoding_16_pcm: bool = False,
    encoding_8_pcm: bool = False,
    encoding_8ulaw: bool = False,
    tper_option: float | None = None,
    fm_option: bool = False,
    notes_option: bool = False,
    notewave_option: str | None = None,
    despike_option: bool = False,
    play_option: bool = False,
    runner: Runner | None = None,
) -> V1dsoundOutputs:
    """
    Program to create a sound file from a 1D file (column of numbers).
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        tsfile: The input 1D time series file containing the data to transform\
            into sound.
        prefix: Prefix for the output filename, which will have '.au'\
            extension.
        encoding_16_pcm: Output in 16-bit linear PCM encoding (uncompressed).
        encoding_8_pcm: Output in 8-bit linear PCM encoding.
        encoding_8ulaw: Output in 8-bit mu-law encoding.
        tper_option: Time in seconds per time point in 'tsfile'. Allowed range\
            is 0.01 to 1.0 (inclusive). [default is 0.2s].
        fm_option: Output sound is frequency modulated between 110 and 1760 Hz\
            from min to max in the input 1D file.
        notes_option: Output sound is a sequence of notes, low to high pitch\
            based on min to max in the input 1D file. Uses pentatonic scale.
        notewave_option: Shape of the notes used. Select from [sine, sqsine,\
            square, triangle].
        despike_option: Apply a simple despiking algorithm to avoid artifacts\
            from large/small values in the input.
        play_option: Plays the sound file after it is written.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dsoundOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1DSOUND_METADATA)
    params = v_1dsound_params(tsfile=tsfile, prefix=prefix, encoding_16_pcm=encoding_16_pcm, encoding_8_pcm=encoding_8_pcm, encoding_8ulaw=encoding_8ulaw, tper_option=tper_option, fm_option=fm_option, notes_option=notes_option, notewave_option=notewave_option, despike_option=despike_option, play_option=play_option)
    return v_1dsound_execute(params, execution)


__all__ = [
    "V1dsoundOutputs",
    "V_1DSOUND_METADATA",
    "v_1dsound",
    "v_1dsound_params",
]
