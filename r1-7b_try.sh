PYTHONPATH=/home/fuzhizhang.fzz/open-r1/src:$PYTHONPATH CUDA_VISIBLE_DEVICES=4,5 accelerate launch --main_process_port 29501\
    --config_file recipes/accelerate_configs/zero3.yaml src/open_r1/grpo.py \
    --config recipes/Qwen2.5-3B/grpo/config_demo.yaml \
    --wandb_entity fuzhizhang-fzz-westlake-university --wandb_project try_openr1_qwen2.5_3b --run_name Qwen2.5-3B-GRPO --vllm_mode colocate
    