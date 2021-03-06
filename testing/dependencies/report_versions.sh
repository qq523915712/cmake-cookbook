#!/usr/bin/env bash

echo "Report versions of whole tool stack"

for tool in cmake make ninja g++ gcc gfortran; do
    echo ""
    echo "Checking version of $tool:"
    $tool --version 2> /dev/null || echo "$tool not available"
done
