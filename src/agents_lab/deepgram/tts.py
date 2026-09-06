"""Deepgram Flux TTS non-streamed REST helpers."""

from __future__ import annotations

from enum import StrEnum
import os
from pathlib import Path
from typing import Any

import httpx2
from pydantic import TypeAdapter

URL = "https://api.deepgram.com/v2/speak"


# https://developers.deepgram.com/docs/flux-tts/voices
class FluxVoice(StrEnum):
    # Featured voices
    ALEXIS = "flux-alexis-en"
    BROOKE = "flux-brooke-en"
    CLIFF = "flux-cliff-en"
    COLE = "flux-cole-en"
    COLIN = "flux-colin-en"
    GEMMA = "flux-gemma-en"
    HALEY = "flux-haley-en"
    HANNAH = "flux-hannah-en"
    HEATHER = "flux-heather-en"
    KIT = "flux-kit-en"
    MILES = "flux-miles-en"
    SEAN = "flux-sean-en"
    SIENNA = "flux-sienna-en"
    # More voices
    BREE = "flux-bree-en"
    BRITTANY = "flux-brittany-en"
    BRUCE = "flux-bruce-en"
    CONOR = "flux-conor-en"
    DONOVAN = "flux-donovan-en"
    DREW = "flux-drew-en"
    ELISE = "flux-elise-en"
    JACK = "flux-jack-en"
    KAI = "flux-kai-en"
    KELSEY = "flux-kelsey-en"
    MAEVE = "flux-maeve-en"
    MARCELO = "flux-marcelo-en"
    MARCUS = "flux-marcus-en"
    MEENA = "flux-meena-en"
    MEGHAN = "flux-meghan-en"
    NAVEEN = "flux-naveen-en"
    PAIGE = "flux-paige-en"
    PRIYA = "flux-priya-en"
    RUFUS = "flux-rufus-en"
    SHARON = "flux-sharon-en"
    TANNER = "flux-tanner-en"
    WADE = "flux-wade-en"
    WES = "flux-wes-en"


_voice_adapter = TypeAdapter(FluxVoice)


def _raise_for_status(res: httpx2.Response) -> None:
    if res.is_error:
        detail = res.headers.get("dg-error") or res.text
        raise httpx2.HTTPStatusError(
            f"{res.status_code} {res.reason_phrase}: {detail}",
            request=res.request,
            response=res,
        )


def speak(
    text: str,
    *,
    model: FluxVoice | str = FluxVoice.HALEY,
    output: str | Path | None = None,
    api_key: str | None = None,
    timeout: float = 30.0,
    **params: Any,
) -> bytes:
    """Synthesize text using Deepgram Flux TTS REST API."""
    voice = _voice_adapter.validate_python(model)
    res = httpx2.post(
        URL,
        params={"model": str(voice), **params},
        headers={"Authorization": f"Token {api_key or os.environ['DEEPGRAM_KEY']}"},
        json={"text": text},
        timeout=timeout,
    )
    _raise_for_status(res)
    if output:
        Path(output).write_bytes(res.content)
    return res.content


async def aspeak(
    text: str,
    *,
    model: FluxVoice | str = FluxVoice.HALEY,
    output: str | Path | None = None,
    api_key: str | None = None,
    timeout: float = 30.0,
    **params: Any,
) -> bytes:
    """Synthesize text asynchronously using Deepgram Flux TTS REST API."""
    voice = _voice_adapter.validate_python(model)
    async with httpx2.AsyncClient(timeout=timeout) as client:
        res = await client.post(
            URL,
            params={"model": str(voice), **params},
            headers={"Authorization": f"Token {api_key or os.environ['DEEPGRAM_KEY']}"},
            json={"text": text},
        )
    _raise_for_status(res)
    if output:
        Path(output).write_bytes(res.content)
    return res.content

