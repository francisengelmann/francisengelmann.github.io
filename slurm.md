## SLURM


### Basic SLURM commands
|Command                | Description                                     |
|-----------------------|-------------------------------------------------|
|sbatch <script.sh>     | add new job                                     |
|squeue                 | list all jobs, running [R] and pending [PD]     |
|scancel                | cancel job |
|scontrol show job <id> | show more details |

### Pracical tips
- Slurm runs scheduled jobs in the backround, so it will not display its output to stdout. 
  Luckily it writes all outputs into a log file. 
  To observe this log file while your process is running type this: 
```tail -f slurm-<job-id>.out``` 

### Example config
