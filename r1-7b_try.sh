CUDA_VISIBLE_DEVICES=0,1 accelerate launch --config_file recipes/accelerate_configs/zero3.yaml src/open_r3/grpo.py \
    --config recipes/DeepSeek-R1-Distill-Qwen-7B/grpo/config_demo.yaml \
    --main_process_port 0
