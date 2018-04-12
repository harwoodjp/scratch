## What is this?

This is a simple CLI tool to create/keep single-file code experiments.

## How do I use it?

Alias this script to `scratch` or whatever you'd like. Change the hard-coded variables in the file to suit your current system.

The basic commands are:

`scratch [js, py, html, ...]`

Creates and opens a file in your scratch path with the inputted extension. Saves to the filesystem as `/scratch/path/[todays-date]/[timestamp].[js, py, html, ...]`.

`scratch`

Open today's scratch directory in your specified editor.

## Why?

I made this because I frequently create files like `app.js` or `app.py` on my desktop to run experiments. I generally just delete them when I'm satisfied. This tool gives these "scratch" files persistence and makes them a bit less transient. 

