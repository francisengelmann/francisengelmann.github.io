## SLURM

### Basic SLURM commands
|Command                | Description                                     |
|-----------------------|-------------------------------------------------|
|sbatch <script.sh>         | Add new job into the queue                      |
|squeue                     | List all jobs, running [R] and pending [PD]     |
|scancel <job-id>           | Cancel job |
|scontrol show job <job-id> | show more details |

### Practical tips
- Slurm runs scheduled jobs in the backround, so it will not display its output to stdout. 
  Luckily it writes all outputs into a log file. 
  To observe this log file while your process is running type this:  
```tail -f slurm-<job-id>.out```  
- To see a real-time status of running and pending jobs, type thos:
```watch -n0.3 squeue```

### Example config
This is an example config:
