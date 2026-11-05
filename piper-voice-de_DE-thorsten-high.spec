Name:		piper-voice-de_DE-thorsten-high
Version:	1.0.0
Release:	1
Summary:	German male voice for the Piper TTS system
URL:		https://huggingface.co/rhasspy/piper-voices/tree/main/de/de_DE/thorsten/medium
License:	MIT
BuildArch:	noarch
Group:		System/Multimedia
Provides:	piper-voice
Provides:	piper-voice-de
Provides:	piper-voice-de_DE

%sourcelist
https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/de/de_DE/thorsten/high/de_DE-thorsten-high.onnx
https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/de/de_DE/thorsten/high/de_DE-thorsten-high.onnx.json

%description
%{summary}

%install
mkdir -p %{buildroot}%{_datadir}/piper/voices
install -c -m 644 %{S:0} %{S:1} %{buildroot}%{_datadir}/piper/voices/

%files
%{_datadir}/piper/voices/*
