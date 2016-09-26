# watch_random
Execute a program repeatedly with random intervals. This script resembles the Linux command line 'watch' but allows for random intervals. 

## Syntax
`./watch_random.py <command> <min_interval> <max_interval>`
## Description
**watch_random** executes command repeatedly and displays the output, until Ctrl+C is pressed. 
## Input Arguments
### command
The command to be executed. If the command contains its own arguments, put everything in quotation marks.
### min_interval
Minimum interval between subsequent runs.
### max_interval
Maximum interval between subsequent runs.
