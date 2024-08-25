import torch
from diffusers import DiffusionPipeline, AutoencoderKL
device = 'cuda' if torch.cuda.is_available() else 'cpu'


class ImageGenerationService:
    def __init__(self, revision: str) -> None:
        vae = AutoencoderKL.from_pretrained("madebyollin/sdxl-vae-fp16-fix", torch_dtype=torch.float16)
        self.pipe = DiffusionPipeline.from_pretrained(
            "cagliostrolab/animagine-xl-3.0",
            vae=vae,
            torch_dtype=torch.float16,
            # use_safetensors=True
        )
        repo_id = "truong-xuan-linh/busai_LoRA"
        self.pipe.load_lora_weights(repo_id, revision=revision)
        self.pipe.to(device)

    def run(self, prompt: str):
        prompt = f"a photo of TOK panda, {prompt}"

        image = self.pipe(prompt=prompt, num_inference_steps=25).images[0]
        return image