## SLURM

![test](http://hpc-uit.readthedocs.io/en/latest/_images/slurm.jpg)



### Basic SLURM commands
|Command                | Description                                     |
|-----------------------|-------------------------------------------------|
|sbatch <run_script.sh>         | Add new job into the queue                      |
|squeue                     | List all jobs, running [R] and pending [PD]     |
|scancel <job-id>           | Cancel job |
|scontrol show job <job-id> | show more details |

### Practical tips
- To see a real-time status of running and pending jobs, type this:  
```watch -n0.3 squeue```
- To start a new job, type this:  
```sbatch run_script.sh```
- Slurm runs scheduled jobs in the backround, so it will not display its output to stdout. 
  Luckily it writes all outputs into a log file. 
  To observe this log file while your process is running type this:  
```tail -f slurm-<job-id>.out```  

### Example config
This is an example `run_script.sh`:
```
#!/bin/bash
#SBATCH --time=0-12:00:00
#SBATCH -c1
#SBATCH --gres=gpu:1
#SBATCH --mail-type=ALL
#SBATCH --mail-user=some_user@gmail.com
python train.py --log_dir log_0018 --batch_size 64
```
