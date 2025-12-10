#!/bin/bash

#Linux
MAC=$(ip a 2>/dev/null | awk '/ether/ {print $2; exit}')

#Mac
if [ -z "$MAC" ]; then
    MAC=$(ifconfig 2>/dev/null | awk '/ether/ {print $2; exit}')
fi

#Windows (GitBASH)
if [ -z "$MAC" ]; then
    MAC=$(getmac 2>/dev/null | awk 'NR==4 {print $1}')
fi

#Error
if [ -z "$MAC" ]; then
    MAC="MAC no disponible"
fi

# Sistema operativo
SO=$(uname -s)

# Hostname y usuario
HOST=$(hostname)
USER=$(whoami)

echo "Usuario: $USER | Equipo: $HOST | SO: $SO | MAC: $MAC"
