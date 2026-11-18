from PIL import Image
from io import BytesIO
from pathlib import Path
import base64
p = Path(__file__).with_name('index.html')
im = Image.open(r'C:\Users\user\Downloads\SCHOLASTIC SCIENCE ACADEMY.png')
im.thumbnail((192,192))
b = BytesIO()
im.save(b, format='PNG', optimize=True)
s = p.read_text(encoding='utf-8')
s = s.replace('<span class="logo" aria-hidden="true">S</span>', '<img class="logo" src="data:image/png;base64,' + base64.b64encode(b.getvalue()).decode() + '" alt="Scholastic Science Academy logo">')
s = s.replace('</style>', '.logo{object-fit:contain;background:#fff;box-shadow:none}</style>', 1)
p.write_text(s, encoding='utf-8')
print('Prepared logo in local page')
