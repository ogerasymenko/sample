#!/bin/bash
exim -bpu | grep frozen | awk {'print $3'} | xargs exim -Mrm

