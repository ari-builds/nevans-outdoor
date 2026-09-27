from PIL import Image
from pathlib import Path
root=Path(__file__).parent/'dist'/'assets'
temp=Path('C:/Users/Arian/AppData/Local/Temp')
files={'lawn':('b824f8db-078a-4c37-b038-a3c361d44dc3',1600),'cleanout-before':('5743a2b3-d7c2-48fe-a576-cfbf5f9ef63e',1100),'cleanout-after':('201740dc-f09c-4fa3-aaa4-047febde4c44',1100),'hauling':('0499209a-ff91-4ece-851c-16f2ebb13ff2',1400),'yard':('31de62e2-6eaf-48cf-9681-b25d62946f65',1000)}
for name,(key,w) in files.items():
    im=Image.open(temp/f'codex-clipboard-{key}.png').convert('RGB')
    im.thumbnail((w,w*2),Image.Resampling.LANCZOS)
    im.save(root/f'{name}.webp',quality=85,method=6)
logo=Image.open(temp/'codex-clipboard-02be9f3d-2f53-4719-9a6f-2f07af6ec13b.png').convert('RGB')
logo.save(root/'brand.jpg',quality=95)
card=Image.new('RGB',(1200,630),'white')
logo.thumbnail((860,570),Image.Resampling.LANCZOS)
card.paste(logo,((1200-logo.width)//2,(630-logo.height)//2))
card.save(root/'og.jpg',quality=93)
print('Optimized supplied photographs:', [(p.name,p.stat().st_size) for p in root.iterdir()])
