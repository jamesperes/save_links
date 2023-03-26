
from core_save import save_link
from chalice import Chalice, Rate

app = Chalice(app_name="save_link")

# Automatically runs every 5 minutes
@app.schedule(Rate(1, unit=Rate.MINUTES))
def periodic_task(event):
    save_link()
    return {"hello": "world"}
