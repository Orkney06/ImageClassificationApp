#!/bin/zsh

tmux split-window -v
tmux select-pane -t 1
tmux split-window -h
tmux resize-pane -D 15
tmux select-pane -t 1

nvim app.py
